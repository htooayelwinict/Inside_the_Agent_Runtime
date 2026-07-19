"""Offline teaching model for immediate and invoked Tool outcomes."""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Callable, Literal


Phase = Literal["immediate", "invoked"]
Reason = Literal[
    "unknown_tool",
    "invalid_arguments",
    "blocked",
    "success",
    "failure",
]
Tool = Callable[[dict[str, object]], str]


@dataclass(frozen=True)
class ToolOutcome:
    phase: Phase
    reason: Reason
    content: str
    after_hook_called: bool = False


def execute_tool_call(
    name: str,
    arguments: dict[str, object],
    tools: dict[str, Tool],
    *,
    before_allowed: bool = True,
    after_hook: Callable[[ToolOutcome], None] | None = None,
) -> ToolOutcome:
    tool = tools.get(name)
    if tool is None:
        return ToolOutcome("immediate", "unknown_tool", f"unknown tool: {name}")

    path = arguments.get("path")
    if not isinstance(path, str) or not path:
        return ToolOutcome("immediate", "invalid_arguments", "path is required")

    if not before_allowed:
        return ToolOutcome("immediate", "blocked", "blocked by before hook")

    try:
        outcome = ToolOutcome("invoked", "success", tool(arguments))
    except Exception as error:
        outcome = ToolOutcome(
            "invoked",
            "failure",
            f"{type(error).__name__}: {error}",
        )

    if after_hook is not None:
        after_hook(outcome)
        outcome = replace(outcome, after_hook_called=True)
    return outcome


if __name__ == "__main__":
    tools = {"read": lambda arguments: f"read:{arguments['path']}"}
    for result in (
        execute_tool_call("missing", {}, tools),
        execute_tool_call("read", {}, tools),
        execute_tool_call("read", {"path": "notes.txt"}, tools),
    ):
        print(f"{result.phase}:{result.reason}:{result.content}")
