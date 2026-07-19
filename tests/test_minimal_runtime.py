from __future__ import annotations

import asyncio
import unittest

from examples.minimal_runtime import AssistantTurn, ToolCall, run_agent_loop


class MinimalRuntimeTests(unittest.IsolatedAsyncioTestCase):
    async def test_parallel_results_keep_source_order(self) -> None:
        model_calls = 0
        completion_order: list[str] = []

        async def model(_messages):
            nonlocal model_calls
            model_calls += 1
            if model_calls == 1:
                return AssistantTurn(
                    text="",
                    tool_calls=(
                        ToolCall("call-slow", "slow", {}, parallel=True),
                        ToolCall("call-fast", "fast", {}, parallel=True),
                    ),
                )
            return AssistantTurn(text="done", tool_calls=())

        async def slow(_arguments):
            await asyncio.sleep(0.02)
            completion_order.append("slow")
            return "slow-result"

        async def fast(_arguments):
            await asyncio.sleep(0)
            completion_order.append("fast")
            return "fast-result"

        events = await run_agent_loop(
            model,
            {"slow": slow, "fast": fast},
            "compare both tools",
        )

        self.assertEqual(completion_order, ["fast", "slow"])
        self.assertEqual(
            [event.kind for event in events],
            [
                "assistant_start",
                "assistant_end",
                "tool_start",
                "tool_start",
                "tool_end",
                "tool_end",
                "assistant_start",
                "assistant_end",
            ],
        )
        self.assertEqual(
            [event.detail for event in events if event.kind == "tool_end"],
            ["slow:slow-result", "fast:fast-result"],
        )

    async def test_parallel_tools_respect_worker_limit(self) -> None:
        model_calls = 0
        active = 0
        peak = 0

        async def model(_messages):
            nonlocal model_calls
            model_calls += 1
            if model_calls == 1:
                return AssistantTurn(
                    text="",
                    tool_calls=tuple(
                        ToolCall(f"call-{index}", "worker", {}, parallel=True)
                        for index in range(5)
                    ),
                )
            return AssistantTurn(text="done", tool_calls=())

        async def worker(_arguments):
            nonlocal active, peak
            active += 1
            peak = max(peak, active)
            await asyncio.sleep(0.01)
            active -= 1
            return "ok"

        await run_agent_loop(
            model,
            {"worker": worker},
            "run the workers",
            max_parallel_tools=2,
        )

        self.assertEqual(peak, 2)

    async def test_unknown_tool_fails_with_clear_name(self) -> None:
        async def model(_messages):
            return AssistantTurn(
                text="",
                tool_calls=(
                    ToolCall("call-missing", "missing", {}, parallel=False),
                ),
            )

        with self.assertRaises(KeyError) as raised:
            await run_agent_loop(model, {}, "call a missing tool")

        self.assertEqual(raised.exception.args, ("unknown tool: missing",))

    async def test_iteration_limit_stops_endless_tool_loop(self) -> None:
        async def model(_messages):
            return AssistantTurn(
                text="",
                tool_calls=(
                    ToolCall("call-again", "again", {}, parallel=False),
                ),
            )

        async def again(_arguments):
            return "continue"

        with self.assertRaisesRegex(RuntimeError, "^iteration limit reached$"):
            await run_agent_loop(
                model,
                {"again": again},
                "never stop",
                max_iterations=2,
            )


if __name__ == "__main__":
    unittest.main()
