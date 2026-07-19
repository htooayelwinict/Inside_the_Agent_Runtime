from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from examples.lewis_message_control import PendingMessages, simulate_message_control
from examples.lewis_session_restore import (
    SessionEntry,
    load_entries,
    restore_context,
    save_entries,
)
from examples.lewis_trace_reader import TraceEvent, analyze_trace
from examples.lewis_tool_outcomes import execute_tool_call


class MessageControlTests(unittest.TestCase):
    def test_steering_follows_turn_end_and_precedes_next_model_call(self) -> None:
        self.assertEqual(
            simulate_message_control(),
            (
                "model:inspect source",
                "turn_end",
                "steering:check tests first",
                "model:continue with steering",
                "turn_end",
                "follow_up:run focused test",
            ),
        )

    def test_one_at_a_time_queue_keeps_later_messages_pending(self) -> None:
        queue = PendingMessages()
        queue.enqueue("first")
        queue.enqueue("second")

        self.assertEqual(queue.drain_one(), ("first",))
        self.assertEqual(queue.drain_one(), ("second",))
        self.assertEqual(queue.drain_one(), ())


class ToolOutcomeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.after_calls: list[str] = []

    def after_hook(self, outcome) -> None:
        self.after_calls.append(outcome.reason)

    def test_immediate_outcomes_skip_after_hook(self) -> None:
        tools = {"read": lambda arguments: f"read:{arguments['path']}"}

        unknown = execute_tool_call("missing", {}, tools, after_hook=self.after_hook)
        invalid = execute_tool_call("read", {}, tools, after_hook=self.after_hook)
        blocked = execute_tool_call(
            "read",
            {"path": "notes.txt"},
            tools,
            before_allowed=False,
            after_hook=self.after_hook,
        )

        self.assertEqual(
            [(item.phase, item.reason) for item in (unknown, invalid, blocked)],
            [
                ("immediate", "unknown_tool"),
                ("immediate", "invalid_arguments"),
                ("immediate", "blocked"),
            ],
        )
        self.assertEqual(self.after_calls, [])

    def test_invoked_failure_runs_after_hook_once(self) -> None:
        def fail(_arguments):
            raise RuntimeError("disk unavailable")

        outcome = execute_tool_call(
            "read",
            {"path": "notes.txt"},
            {"read": fail},
            after_hook=self.after_hook,
        )

        self.assertEqual((outcome.phase, outcome.reason), ("invoked", "failure"))
        self.assertEqual(outcome.content, "RuntimeError: disk unavailable")
        self.assertTrue(outcome.after_hook_called)
        self.assertEqual(self.after_calls, ["failure"])

    def test_invoked_success_runs_after_hook_once(self) -> None:
        outcome = execute_tool_call(
            "read",
            {"path": "notes.txt"},
            {"read": lambda arguments: f"read:{arguments['path']}"},
            after_hook=self.after_hook,
        )

        self.assertEqual((outcome.phase, outcome.reason), ("invoked", "success"))
        self.assertEqual(outcome.content, "read:notes.txt")
        self.assertEqual(self.after_calls, ["success"])


class SessionRestoreTests(unittest.TestCase):
    def test_round_trip_restores_summary_retained_tail_and_later_messages(self) -> None:
        entries = (
            SessionEntry("m1", "message", content="Goal: fix ordering"),
            SessionEntry("m2", "message", content="Read agent loop"),
            SessionEntry("m3", "message", content="Fast tool finished first"),
            SessionEntry(
                "c1",
                "compaction",
                summary="Goal and ordering evidence retained",
                first_kept_entry_id="m3",
            ),
            SessionEntry("m4", "message", content="Focused test still fails"),
        )

        with TemporaryDirectory() as temp:
            path = Path(temp) / "session.json"
            save_entries(path, entries)
            restored = restore_context(load_entries(path))

        self.assertEqual(
            restored,
            (
                "summary:Goal and ordering evidence retained",
                "message:Fast tool finished first",
                "message:Focused test still fails",
            ),
        )

    def test_history_without_compaction_restores_all_messages(self) -> None:
        self.assertEqual(
            restore_context(
                (
                    SessionEntry("m1", "message", content="first"),
                    SessionEntry("m2", "message", content="second"),
                )
            ),
            ("message:first", "message:second"),
        )

    def test_latest_of_two_compactions_replaces_older_summary_and_tail(self) -> None:
        entries = (
            SessionEntry("m1", "message", content="Original goal"),
            SessionEntry("m2", "message", content="Old retained tail"),
            SessionEntry(
                "c1",
                "compaction",
                summary="Older summary",
                first_kept_entry_id="m2",
            ),
            SessionEntry("m3", "message", content="After first compaction"),
            SessionEntry("m4", "message", content="Latest retained tail"),
            SessionEntry(
                "c2",
                "compaction",
                summary="Latest summary",
                first_kept_entry_id="m4",
            ),
            SessionEntry("m5", "message", content="Later message"),
        )

        self.assertEqual(
            restore_context(entries),
            (
                "summary:Latest summary",
                "message:Latest retained tail",
                "message:Later message",
            ),
        )

    def test_missing_first_kept_anchor_is_rejected(self) -> None:
        entries = (
            SessionEntry("m1", "message", content="Original goal"),
            SessionEntry(
                "c1",
                "compaction",
                summary="Summary",
                first_kept_entry_id="missing",
            ),
        )

        with self.assertRaisesRegex(
            ValueError,
            "^first kept entry not found: missing$",
        ):
            restore_context(entries)

    def test_compaction_without_anchor_restores_no_pre_compaction_tail(self) -> None:
        entries = (
            SessionEntry("m1", "message", content="Pruned history"),
            SessionEntry("c1", "compaction", summary="Summary"),
            SessionEntry("m2", "message", content="Later message"),
        )

        self.assertEqual(
            restore_context(entries),
            ("summary:Summary", "message:Later message"),
        )


class TraceReaderTests(unittest.TestCase):
    def test_completion_and_result_order_are_reported_separately(self) -> None:
        report = analyze_trace(
            (
                TraceEvent(4, "tool_result", "fast"),
                TraceEvent(2, "tool_execution_end", "slow"),
                TraceEvent(1, "tool_execution_end", "fast"),
                TraceEvent(3, "tool_result", "slow"),
            )
        )

        self.assertEqual(report.completion_order, ("fast", "slow"))
        self.assertEqual(report.result_order, ("slow", "fast"))

    def test_first_error_marks_the_failure_boundary(self) -> None:
        report = analyze_trace(
            (
                TraceEvent(1, "tool_execution_end", "read"),
                TraceEvent(2, "tool_execution_end", "test", is_error=True),
                TraceEvent(3, "tool_result", "test", is_error=True),
                TraceEvent(4, "tool_execution_end", "deploy", is_error=True),
                TraceEvent(5, "tool_result", "deploy", is_error=True),
            )
        )

        self.assertEqual(report.first_failure, "test")


if __name__ == "__main__":
    unittest.main()
