"""Offline teaching model for a small agent loop.

This example is intentionally smaller than Travis234.  It demonstrates only
assistant boundaries, tool execution, source-ordered results and an iteration
ceiling.  It does not call a real model or mutate the network.
"""

from __future__ import annotations

import asyncio
from dataclasses import asdict, dataclass
from typing import Awaitable, Callable


@dataclass(frozen=True)
class ToolCall:
    id: str
    name: str
    arguments: dict[str, object]
    parallel: bool


@dataclass(frozen=True)
class AssistantTurn:
    text: str
    tool_calls: tuple[ToolCall, ...]


@dataclass(frozen=True)
class RuntimeEvent:
    kind: str
    detail: str


Model = Callable[[list[dict[str, object]]], Awaitable[AssistantTurn]]
Tool = Callable[[dict[str, object]], Awaitable[str]]


async def run_agent_loop(
    model: Model,
    tools: dict[str, Tool],
    user_input: str,
    *,
    max_iterations: int = 8,
    max_parallel_tools: int = 4,
) -> list[RuntimeEvent]:
    """Run a bounded educational model/tool loop and return its event trace.

    ``max_parallel_tools`` must be greater than zero.
    """

    if max_parallel_tools <= 0:
        raise ValueError("max_parallel_tools must be greater than zero")

    messages: list[dict[str, object]] = [
        {"role": "user", "content": user_input},
    ]
    events: list[RuntimeEvent] = []
    semaphore = asyncio.Semaphore(max_parallel_tools)

    async def invoke(call: ToolCall) -> str:
        tool = tools.get(call.name)
        if tool is None:
            raise KeyError(f"unknown tool: {call.name}")
        async with semaphore:
            return await tool(call.arguments)

    for iteration in range(1, max_iterations + 1):
        events.append(RuntimeEvent("assistant_start", str(iteration)))
        turn = await model(list(messages))
        events.append(RuntimeEvent("assistant_end", turn.text))
        messages.append(
            {
                "role": "assistant",
                "content": turn.text,
                "tool_calls": [asdict(call) for call in turn.tool_calls],
            }
        )

        if not turn.tool_calls:
            return events

        for call in turn.tool_calls:
            events.append(RuntimeEvent("tool_start", call.name))

        if all(call.parallel for call in turn.tool_calls):
            results = await asyncio.gather(*(invoke(call) for call in turn.tool_calls))
        else:
            results = [await invoke(call) for call in turn.tool_calls]

        for call, result in zip(turn.tool_calls, results, strict=True):
            events.append(RuntimeEvent("tool_end", f"{call.name}:{result}"))
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "name": call.name,
                    "content": result,
                }
            )

    raise RuntimeError("iteration limit reached")


async def _demo() -> None:
    model_calls = 0

    async def fake_model(_messages: list[dict[str, object]]) -> AssistantTurn:
        nonlocal model_calls
        model_calls += 1
        if model_calls == 1:
            return AssistantTurn(
                text="I will check both sources.",
                tool_calls=(
                    ToolCall("call-slow", "slow", {}, parallel=True),
                    ToolCall("call-fast", "fast", {}, parallel=True),
                ),
            )
        return AssistantTurn(text="Both results are ready.", tool_calls=())

    async def slow(_arguments: dict[str, object]) -> str:
        await asyncio.sleep(0.02)
        return "slow-result"

    async def fast(_arguments: dict[str, object]) -> str:
        await asyncio.sleep(0)
        return "fast-result"

    events = await run_agent_loop(
        fake_model,
        {"slow": slow, "fast": fast},
        "Compare both sources",
    )
    for event in events:
        print(f"{event.kind}: {event.detail}")


if __name__ == "__main__":
    asyncio.run(_demo())
