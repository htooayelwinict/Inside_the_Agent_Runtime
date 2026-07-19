"""Offline teaching model for reading Agent event traces."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TraceEvent:
    index: int
    kind: str
    call_id: str = ""
    is_error: bool = False


@dataclass(frozen=True)
class TraceReport:
    completion_order: tuple[str, ...]
    result_order: tuple[str, ...]
    first_failure: str | None


def analyze_trace(events: tuple[TraceEvent, ...]) -> TraceReport:
    ordered = sorted(events, key=lambda event: event.index)
    completion_order = tuple(
        event.call_id
        for event in ordered
        if event.kind == "tool_execution_end"
    )
    result_order = tuple(
        event.call_id
        for event in ordered
        if event.kind == "tool_result"
    )
    first_failure = next(
        (event.call_id for event in ordered if event.is_error),
        None,
    )
    return TraceReport(completion_order, result_order, first_failure)


if __name__ == "__main__":
    report = analyze_trace(
        (
            TraceEvent(1, "tool_execution_end", "fast"),
            TraceEvent(2, "tool_execution_end", "slow"),
            TraceEvent(3, "tool_result", "slow"),
            TraceEvent(4, "tool_result", "fast"),
            TraceEvent(5, "tool_execution_end", "test", is_error=True),
        )
    )
    print(f"completion_order:{','.join(report.completion_order)}")
    print(f"result_order:{','.join(report.result_order)}")
    print(f"first_failure:{report.first_failure}")
