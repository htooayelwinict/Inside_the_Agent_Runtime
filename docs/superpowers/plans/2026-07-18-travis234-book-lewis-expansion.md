# Travis234 Book Lewis Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add six Lewis-led, story-driven chapters and four offline workshop examples without rewriting the approved Chapter 00–09 prose.

**Architecture:** Keep the existing technical chapters as the foundation, then append Part V case studies and a Part VI workshop. Each new chapter starts with one fictional Lewis incident, transitions into source-backed teaching, and ends with a runnable or inspectable artifact; evidence remains centralized in the source map and claim ledger.

**Tech Stack:** Markdown, Python 3.13 standard library, `unittest`, Mermaid where sequence/state is materially clearer, Git.

## Global Constraints

- Keep approved Chapter 00–09 prose unchanged; only Chapter 09 `Next` navigation may change.
- Add exactly Chapter 10–15, bringing the main sequence to 16 chapters.
- Use **Lewis** as the recurring fictional developer; do not imply that Lewis is a real upstream contributor.
- Target 1,200–1,800 words per new chapter, but do not pad a complete lesson to satisfy word count.
- Keep story material near 15–20% and technical teaching near 80–85%; treat this as an editorial target, not a machine-enforced ratio.
- Every new chapter must include a Lewis opening, teaching bridge, **Lewis ရဲ့မှတ်စု**, summary, Source Notes, Previous and Next navigation.
- Do not modify `examples/minimal_runtime.py` or `tests/test_minimal_runtime.py`.
- New examples must use only the Python standard library and must not need network access, API keys, provider accounts, or user-workspace mutation.
- Keep provider catalogs, TUI walkthroughs, extension inventories, auth setup and package-manager catalogs out of scope.
- Use pinned revisions: Travis234 `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`, Pi `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6`, Hermes `af250d84948179834820a62bfd870c0df6f264a1`.
- Do not use the unnatural phrase `လက်နဲ့လိုက်ခြင်း` or related `လက်နဲ့…` teaching phrases.
- Preserve the current Burmese-first, problem-first voice; use Agentic AI Book and Software Engineering only as high-level teaching references and copy no sentences or distinctive examples.
- Use `apply_patch` for text/code edits and commit each independently reviewable task.

---

## File map

### Create

- `book/chapters/10-one-night-unfinished-bug.md` — end-to-end turn case study.
- `book/chapters/11-steering-followup-cancellation.md` — message control and abort story.
- `book/chapters/12-when-tools-fail.md` — Tool outcome boundary story.
- `book/chapters/13-session-resume-after-restart.md` — persistence and restore story.
- `book/chapters/14-debugging-agent-trajectory.md` — event trace debugging story.
- `book/chapters/15-building-a-trustworthy-port.md` — contract-testing workshop and roadmap.
- `examples/lewis_message_control.py` — deterministic steering/follow-up teaching model.
- `examples/lewis_tool_outcomes.py` — immediate-versus-invoked Tool outcome model.
- `examples/lewis_session_restore.py` — temporary JSON persistence and compacted context restore model.
- `examples/lewis_trace_reader.py` — trace-order and failure-boundary reader.
- `tests/test_lewis_workshop.py` — focused tests for all four new examples.

### Modify

- `book/references/SOURCE_MAP.md` — add run-lease, persistence and trace sources.
- `book/references/CLAIM_LEDGER.md` — add five Lewis-expansion claims and final chapter links.
- `book/SUMMARY.md` — add Part V and Part VI.
- `book/chapters/09-parity-divergence-lessons.md` — navigation-only `Next` change.
- `book/chapters/appendices/a-installation.md` — navigation-only `Previous` change.
- `GLOSSARY.md` — add Run Lease, Immediate Tool Outcome, Event Trace and Behavioral Contract.
- `README.md` — report the 16-chapter manuscript.
- `book/README.md` — add Part V/VI status and story-workshop boundary.
- `book/REVIEW_REPORT.md` — append expansion evidence and fresh verification results.

---

### Task 1: Expand the source and claim evidence foundation

**Files:**

- Modify: `book/references/SOURCE_MAP.md`
- Modify: `book/references/CLAIM_LEDGER.md`

**Interfaces:**

- Consumes: current pinned revisions and existing `T-AGENT`, `T-LOOP`, `T-PARITY`, `T-VERIFY`, `C-HOOK-BOUNDARY`.
- Produces: `T-RUN-LEASE`, `T-SESSION-STORE`, `T-SESSION-PERSISTENCE`, `T-EVAL-TRACE`, `T-EVENT-STREAM` and claims `C-MESSAGE-DRAIN`, `C-ABORT-OWNERSHIP`, `C-SESSION-RESTORE`, `C-TRACE-ORDER`, `C-CONTRACT-TESTS`.

- [ ] **Step 1: Reconfirm exact source evidence at the pinned Travis234 revision**

Run from `/workspace/scratch/b03ff60760ed/travis234`:

```bash
git rev-parse HEAD
rg -n "get_steering_messages|get_follow_up_messages|follow_up|steer|RunLease" travis/agent/agent.py travis/agent/agent_loop.py travis/agent/run_lease.py
rg -n "append_compaction|firstKeptEntryId|tokensBefore|get_context" travis/coding_agent/session_store.py travis/coding_agent/session_persistence.py
rg -n "EvalTraceWriter|tool_execution_end|tool_result|redact" travis/coding_agent/eval_trace.py travis/ai/event_stream.py tests/test_eval_trace.py tests/test_agent_loop.py
```

Expected: HEAD is `68b1831691b8ec93f9550ce63b80cdcb7a591b2e` and every search returns named source/test evidence.

- [ ] **Step 2: Add exact source-map rows**

Add these rows under Travis234 sources:

```markdown
| T-RUN-LEASE | [`travis/agent/run_lease.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/agent/run_lease.py) | Active run ownership၊ wait နဲ့ idempotent release |
| T-SESSION-STORE | [`travis/coding_agent/session_store.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/coding_agent/session_store.py) | Session entries၊ branch lineage၊ Compaction metadata နဲ့ context reconstruction |
| T-SESSION-PERSISTENCE | [`travis/coding_agent/session_persistence.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/coding_agent/session_persistence.py) | Persistent session orchestration နဲ့ restored state integration |
| T-EVAL-TRACE | [`travis/coding_agent/eval_trace.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/coding_agent/eval_trace.py) | Evaluation/conversation trace writing နဲ့ secret redaction boundary |
| T-EVENT-STREAM | [`travis/ai/event_stream.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/ai/event_stream.py) | Provider-to-runtime assistant event stream boundary |
```

- [ ] **Step 3: Add exact claim-ledger rows with plain planned-chapter labels**

Use these claim meanings:

```markdown
| C-MESSAGE-DRAIN | Steering messages ကို inner loop ရဲ့ next model boundary မှာ drain လုပ်ပြီး Follow-up messages ကို completed turn နောက် outer loop boundary မှာ drain လုပ်တယ်။ | P-LOOP, P-AGENT, T-LOOP, T-AGENT, `tests/test_agent_loop.py::test_continue_processes_queued_follow_up_after_assistant_turn`, `tests/test_agent_loop.py::test_continue_keeps_one_at_a_time_steering_from_assistant_tail` | Source inspected at pinned revisions | Planned Chapter 11 |
| C-ABORT-OWNERSHIP | Abort က cooperative signal ဖြစ်ပြီး active run ownership ကို RunLease က serialise လုပ်တယ်; abort သိပြီးနောက် loop က model/tool work အသစ်မစရဘူး။ | T-LOOP, T-AGENT, T-RUN-LEASE, `tests/test_agent_loop.py::test_agent_loop_stops_after_signal_aborted_during_tool_execution`, `tests/test_agent_loop.py::test_run_lease_tracks_owner_waits_and_releases_idempotently` | Source inspected at pinned revision | Planned Chapter 11 |
| C-SESSION-RESTORE | Latest Compaction summary၊ first-kept anchor ကစတဲ့ retained tail နဲ့ Compaction နောက် entries တွေက active context ကို ပြန်တည်ဆောက်တယ်။ | T-SESSION-STORE, T-SESSION-PERSISTENCE, T-ADAPTER, `tests/test_coding_persistence_and_compaction.py::test_session_store_build_context_recreates_compaction_summary_message`, `tests/test_coding_persistence_and_compaction.py::test_agent_session_manual_compaction_persists_travis234_first_kept_boundary`, `tests/test_compaction_integration.py::test_persisted_compaction_does_not_resurrect_pruned_suffix` | Source inspected at pinned revision | Planned Chapter 13 |
| C-TRACE-ORDER | Tool completion events နဲ့ model context ထဲ result insertion order မတူနိုင်ပြီး trace ဖတ်ရာမှာ event kind နှစ်မျိုးကို ခွဲရတယ်။ | T-LOOP, T-EVAL-TRACE, `tests/test_agent_loop.py::test_parallel_tool_end_events_follow_completion_order_while_results_keep_source_order`, `tests/test_eval_trace.py::test_eval_trace_records_lifecycle_without_sensitive_content` | Source inspected at pinned revision | Planned Chapter 14 |
| C-CONTRACT-TESTS | Fake-model tests က observable behavior contract ကို deterministic စစ်နိုင်ပြီး parity verifier က manifest/schema/evidence ကို validate လုပ်ပေမယ့် full test suite ကို မပြေးပေးဘူး။ | T-PARITY, T-VERIFY, `tests/test_pi_behavioral_parity.py::test_pi_manifest_is_complete_and_all_evidence_resolves`, `tests/test_hermes_compaction_parity.py::test_hermes_manifest_is_complete_and_all_evidence_resolves`, `tests/architecture/test_acceptance_matrix.py::test_parity_report_has_only_resolved_evidence` | Verifier boundary inspected at pinned revision | Planned Chapter 15 |
```

- [ ] **Step 4: Verify ledger integrity**

Run:

```bash
python3 scripts/check_book.py
rg -n "လက်နဲ့" book/references
git diff --check
```

Expected: book checks pass; the `rg` command returns no output; diff check passes.

- [ ] **Step 5: Commit**

```bash
git add book/references/SOURCE_MAP.md book/references/CLAIM_LEDGER.md
git commit -m "docs: map Lewis expansion evidence"
```

---

### Task 2: Build the message-control teaching example with TDD

**Files:**

- Create: `examples/lewis_message_control.py`
- Create: `tests/test_lewis_workshop.py`

**Interfaces:**

- Produces: `PendingMessages.enqueue(message: str) -> None`, `PendingMessages.drain_one() -> tuple[str, ...]`, `simulate_message_control() -> tuple[str, ...]`.
- Expected demo trace: `model:inspect source`, `steering:check tests first`, `turn_end`, `follow_up:run focused test`.

- [ ] **Step 1: Write failing message-control tests**

Create `tests/test_lewis_workshop.py` with:

```python
from __future__ import annotations

import unittest

from examples.lewis_message_control import PendingMessages, simulate_message_control


class MessageControlTests(unittest.TestCase):
    def test_steering_precedes_turn_end_and_follow_up_starts_after_it(self) -> None:
        self.assertEqual(
            simulate_message_control(),
            (
                "model:inspect source",
                "steering:check tests first",
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


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the focused tests and observe the import failure**

Run:

```bash
python3 -m unittest tests.test_lewis_workshop.MessageControlTests -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'examples.lewis_message_control'`.

- [ ] **Step 3: Implement the minimal teaching model**

Create `examples/lewis_message_control.py`:

```python
"""Offline teaching model for steering and follow-up drain boundaries."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field


@dataclass
class PendingMessages:
    messages: deque[str] = field(default_factory=deque)

    def enqueue(self, message: str) -> None:
        self.messages.append(message)

    def drain_one(self) -> tuple[str, ...]:
        if not self.messages:
            return ()
        return (self.messages.popleft(),)


def simulate_message_control() -> tuple[str, ...]:
    steering = PendingMessages()
    follow_up = PendingMessages()
    steering.enqueue("check tests first")
    follow_up.enqueue("run focused test")

    events = ["model:inspect source"]
    events.extend(f"steering:{message}" for message in steering.drain_one())
    events.append("turn_end")
    events.extend(f"follow_up:{message}" for message in follow_up.drain_one())
    return tuple(events)


if __name__ == "__main__":
    print("\n".join(simulate_message_control()))
```

- [ ] **Step 4: Run tests and demo**

Run:

```bash
python3 -m unittest tests.test_lewis_workshop.MessageControlTests -v
python3 examples/lewis_message_control.py
```

Expected: 2 tests pass and the four expected trace lines print in order.

- [ ] **Step 5: Commit**

```bash
git add examples/lewis_message_control.py tests/test_lewis_workshop.py
git commit -m "feat: add Lewis message-control lab"
```

---

### Task 3: Build the Tool-outcome teaching example with TDD

**Files:**

- Create: `examples/lewis_tool_outcomes.py`
- Modify: `tests/test_lewis_workshop.py`

**Interfaces:**

- Produces: frozen `ToolOutcome(phase, reason, content, after_hook_called)` and `execute_tool_call(name, arguments, tools, before_allowed=True, after_hook=None) -> ToolOutcome`.
- `phase` values: `immediate` or `invoked`.
- `reason` values: `unknown_tool`, `invalid_arguments`, `blocked`, `success`, `failure`.

- [ ] **Step 1: Add failing Tool-outcome tests**

Add the new import beside the existing imports and insert this test class before the final `if __name__ == "__main__"` block, keeping that block last:

```python
from examples.lewis_tool_outcomes import execute_tool_call


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
```

- [ ] **Step 2: Run the focused tests and observe the import failure**

Run:

```bash
python3 -m unittest tests.test_lewis_workshop.ToolOutcomeTests -v
```

Expected: FAIL because `examples.lewis_tool_outcomes` does not exist.

- [ ] **Step 3: Implement the Tool outcome model**

Create `examples/lewis_tool_outcomes.py`:

```python
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
```

- [ ] **Step 4: Run the focused and accumulated tests**

Run:

```bash
python3 -m unittest tests.test_lewis_workshop -v
python3 examples/lewis_tool_outcomes.py
```

Expected: 5 accumulated tests pass; demo prints unknown, invalid and success outcomes.

- [ ] **Step 5: Commit**

```bash
git add examples/lewis_tool_outcomes.py tests/test_lewis_workshop.py
git commit -m "feat: add Lewis Tool outcome lab"
```

---

### Task 4: Build the session-restore teaching example with TDD

**Files:**

- Create: `examples/lewis_session_restore.py`
- Modify: `tests/test_lewis_workshop.py`

**Interfaces:**

- Produces: frozen `SessionEntry(id, type, content="", summary="", first_kept_entry_id=None)`, `save_entries(path, entries)`, `load_entries(path)` and `restore_context(entries) -> tuple[str, ...]`.
- Restore shape: summary first, retained messages from the first-kept anchor through the Compaction entry, then messages appended after Compaction.

- [ ] **Step 1: Add failing persistence tests**

Add the path/session imports beside the existing imports and insert this class before the final `if __name__ == "__main__"` block:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

from examples.lewis_session_restore import (
    SessionEntry,
    load_entries,
    restore_context,
    save_entries,
)


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
```

- [ ] **Step 2: Run tests and observe the import failure**

Run:

```bash
python3 -m unittest tests.test_lewis_workshop.SessionRestoreTests -v
```

Expected: FAIL because `examples.lewis_session_restore` does not exist.

- [ ] **Step 3: Implement temporary persistence and restore**

Create `examples/lewis_session_restore.py`:

```python
"""Offline teaching model for restoring a compacted persistent session."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from tempfile import TemporaryDirectory


@dataclass(frozen=True)
class SessionEntry:
    id: str
    type: str
    content: str = ""
    summary: str = ""
    first_kept_entry_id: str | None = None


def save_entries(path: Path, entries: tuple[SessionEntry, ...]) -> None:
    path.write_text(
        json.dumps([asdict(entry) for entry in entries], indent=2),
        encoding="utf-8",
    )


def load_entries(path: Path) -> tuple[SessionEntry, ...]:
    rows = json.loads(path.read_text(encoding="utf-8"))
    return tuple(SessionEntry(**row) for row in rows)


def restore_context(entries: tuple[SessionEntry, ...]) -> tuple[str, ...]:
    compaction_indexes = [
        index for index, entry in enumerate(entries) if entry.type == "compaction"
    ]
    if not compaction_indexes:
        return tuple(
            f"message:{entry.content}"
            for entry in entries
            if entry.type == "message"
        )

    compaction_index = compaction_indexes[-1]
    compaction = entries[compaction_index]
    restored = [f"summary:{compaction.summary}"]
    keep = compaction.first_kept_entry_id is None

    for entry in entries[:compaction_index]:
        if entry.id == compaction.first_kept_entry_id:
            keep = True
        if keep and entry.type == "message":
            restored.append(f"message:{entry.content}")

    restored.extend(
        f"message:{entry.content}"
        for entry in entries[compaction_index + 1 :]
        if entry.type == "message"
    )
    return tuple(restored)


if __name__ == "__main__":
    demo_entries = (
        SessionEntry("m1", "message", content="Goal: fix ordering"),
        SessionEntry("m2", "message", content="Fast tool finished first"),
        SessionEntry(
            "c1",
            "compaction",
            summary="Goal and evidence retained",
            first_kept_entry_id="m2",
        ),
        SessionEntry("m3", "message", content="Focused test still fails"),
    )
    with TemporaryDirectory() as temp:
        session_path = Path(temp) / "session.json"
        save_entries(session_path, demo_entries)
        print("\n".join(restore_context(load_entries(session_path))))
```

- [ ] **Step 4: Run focused tests, demo and mutation check**

Run:

```bash
python3 -m unittest tests.test_lewis_workshop.SessionRestoreTests -v
python3 examples/lewis_session_restore.py
git status --short
```

Expected: 2 focused tests pass; demo prints one summary and two messages; only the two intended repository files are modified/untracked.

- [ ] **Step 5: Commit**

```bash
git add examples/lewis_session_restore.py tests/test_lewis_workshop.py
git commit -m "feat: add Lewis session restore lab"
```

---

### Task 5: Build the trace-reader teaching example with TDD

**Files:**

- Create: `examples/lewis_trace_reader.py`
- Modify: `tests/test_lewis_workshop.py`

**Interfaces:**

- Produces: frozen `TraceEvent(index, kind, call_id="", is_error=False)`, frozen `TraceReport(completion_order, result_order, first_failure)` and `analyze_trace(events) -> TraceReport`.
- Ordering is determined by `index`, not caller list order.

- [ ] **Step 1: Add failing trace-reader tests**

Add the trace import beside the existing imports and insert this class before the final `if __name__ == "__main__"` block:

```python
from examples.lewis_trace_reader import TraceEvent, analyze_trace


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
            )
        )

        self.assertEqual(report.first_failure, "test")
```

Use a deliberately shuffled input list; `index` must reconstruct the trace.

- [ ] **Step 2: Run tests and observe the import failure**

Run:

```bash
python3 -m unittest tests.test_lewis_workshop.TraceReaderTests -v
```

Expected: FAIL because `examples.lewis_trace_reader` does not exist.

- [ ] **Step 3: Implement trace analysis**

Create `examples/lewis_trace_reader.py`:

```python
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
```

- [ ] **Step 4: Run the complete workshop suite and all demos**

Run:

```bash
python3 -m unittest tests.test_lewis_workshop -v
python3 examples/lewis_message_control.py
python3 examples/lewis_tool_outcomes.py
python3 examples/lewis_session_restore.py
python3 examples/lewis_trace_reader.py
```

Expected: 9 accumulated tests pass; every demo exits 0 with deterministic output.

- [ ] **Step 5: Commit**

```bash
git add examples/lewis_trace_reader.py tests/test_lewis_workshop.py
git commit -m "feat: add Lewis trace reader lab"
```

---

### Task 6: Write Chapter 10 as the end-to-end story benchmark

**Files:**

- Create: `book/chapters/10-one-night-unfinished-bug.md`

**Interfaces:**

- Consumes: `examples/minimal_runtime.py`, `C-LOOP-ORDER`, `C-RESULT-ORDER`, `C-TIMING`, `T-LOOP`, `T-APP`.
- Produces: the voice and story/teaching ratio benchmark for Chapters 11–15.

- [ ] **Step 1: Draft the Lewis opening and teaching bridge**

Open on Friday night with one failing ordering test. Include a short terminal block showing a failure where expected source order differs from observed completion order. State that Lewis is fictional before the first source-backed explanation. End the opening with the bridge question: the Agent reached an answer, but which runtime boundaries did it cross?

- [ ] **Step 2: Write the exact section structure**

Use these headings:

```markdown
## ၁၀.၁ Failing Test တစ်ခုက စတင်ပေးတဲ့မေးခွန်း
## ၁၀.၂ Prompt တစ်ခု Runtime ထဲဝင်သွားတဲ့ခရီး
## ၁၀.၃ Turn တစ်ခုကို Timeline နဲ့ဖတ်ခြင်း
## ၁၀.၄ Minimal Runtime ကို ပြန် Run ကြည့်ခြင်း
## ၁၀.၅ State ဘယ်နေရာတွေမှာ ပြောင်းသွားသလဲ
## ၁၀.၆ Trace ရှိရုံနဲ့ မသက်သေပြနိုင်တဲ့အရာ
## ၁၀.၇ Lewis ရဲ့မှတ်စု
## ၁၀.၈ အနှစ်ချုပ်
## ၁၀.၉ Source Notes
```

Explain user message insertion, assistant boundaries, Tool Call execution, ordered Tool Results and the next model call. Keep production `tool_execution_end` separate from the lab’s source-ordered `tool_end` trace.

- [ ] **Step 3: Add executable instructions and exact expected trace**

Link `../../examples/minimal_runtime.py` and show:

```bash
python3 examples/minimal_runtime.py
```

List the exact eight-event output already produced by the example. Label the code as an educational model, not production Travis234.

- [ ] **Step 4: Add notes and navigation**

Use `C-LOOP-ORDER`, `C-RESULT-ORDER`, `C-TIMING` and pinned revisions in Source Notes. Add Previous → Chapter 09 only; omit Next until Chapter 11 exists.

- [ ] **Step 5: Run editorial checks**

Run:

```bash
python3 scripts/check_book.py
rg -n "လက်နဲ့|architecture review" book/chapters/10-one-night-unfinished-bug.md
wc -w book/chapters/10-one-night-unfinished-bug.md
git diff --check
```

Expected: checker passes; phrase scan is empty; word count is 1,200–1,800 unless the lesson is demonstrably complete at a slightly shorter length.

- [ ] **Step 6: Commit**

```bash
git add book/chapters/10-one-night-unfinished-bug.md
git commit -m "docs: add Lewis end-to-end runtime story"
```

---

### Task 7: Write Chapter 11 on steering, follow-up and cancellation

**Files:**

- Create: `book/chapters/11-steering-followup-cancellation.md`
- Modify: `book/chapters/10-one-night-unfinished-bug.md`

**Interfaces:**

- Consumes: `examples/lewis_message_control.py`, `C-MESSAGE-DRAIN`, `C-ABORT-OWNERSHIP`, `T-AGENT`, `T-LOOP`, `T-RUN-LEASE`.

- [ ] **Step 1: Write the story incident**

Lewis learns that the failing test lives under a different path while the Agent is still inspecting the old path. Show three tempting actions—steer, follow up, abort—and make the chapter explain why they are not synonyms.

- [ ] **Step 2: Use the exact headings**

```markdown
## ၁၁.၁ အချက်အလက်အသစ်က Run အလယ်ရောက်လာတဲ့အခါ
## ၁၁.၂ Queue ဆိုတာ Message စုပုံထားတာထက် ပိုတယ်
## ၁၁.၃ Steering ဝင်တဲ့ Inner-loop Boundary
## ၁၁.၄ Follow-up စတင်တဲ့ Outer-loop Boundary
## ၁၁.၅ Abort၊ Cancel နဲ့ Continue ကို မရောခြင်း
## ၁၁.၆ RunLease က ဘာကိုပိုင်ခွင့်ပေးသလဲ
## ၁၁.၇ Offline Message-control Lab
## ၁၁.၈ မှားလွယ်တဲ့ Race Conditions
## ၁၁.၉ Lewis ရဲ့မှတ်စု
## ၁၁.၁၀ အနှစ်ချုပ်
## ၁၁.၁၁ Source Notes
```

- [ ] **Step 3: Integrate the lab**

Link `../../examples/lewis_message_control.py`, show its four-line output and explain that it models drain placement only. State explicitly that it does not simulate live provider cancellation or threads.

- [ ] **Step 4: Add source-backed notes and navigation**

Source Notes must cite `C-MESSAGE-DRAIN` and `C-ABORT-OWNERSHIP` plus Pi/Travis revisions. Add Previous → Chapter 10. Add Next → Chapter 11 in Chapter 10; omit Chapter 11 Next until Chapter 12 exists.

- [ ] **Step 5: Verify and commit**

```bash
python3 examples/lewis_message_control.py
python3 scripts/check_book.py
rg -n "လက်နဲ့|architecture review" book/chapters/11-steering-followup-cancellation.md
rg -n "force-kill|အလိုအလျောက်.*ရပ်" book/chapters/11-steering-followup-cancellation.md
git diff --check
git add book/chapters/10-one-night-unfinished-bug.md book/chapters/11-steering-followup-cancellation.md
git commit -m "docs: teach Lewis message control boundaries"
```

Expected: demo/checker pass; the first scan has no output; the second finds the explicit cooperative-cancellation boundary.

---

### Task 8: Write Chapter 12 on Tool failure boundaries

**Files:**

- Create: `book/chapters/12-when-tools-fail.md`
- Modify: `book/chapters/11-steering-followup-cancellation.md`

**Interfaces:**

- Consumes: `examples/lewis_tool_outcomes.py`, `C-HOOK-BOUNDARY`, `T-LOOP`, `T-TYPES`.

- [ ] **Step 1: Write the three-failure story sequence**

Lewis’s Agent first calls a missing Tool, then calls `read` without a path, then invokes a valid Tool whose body raises `RuntimeError("disk unavailable")`. Use the repeated attempts to introduce immediate outcomes versus invoked failures.

- [ ] **Step 2: Use the exact headings**

```markdown
## ၁၂.၁ Error သုံးခုက ဘာကြောင့် မတူတာလဲ
## ၁၂.၂ Prepare → Execute → Finalize
## ၁၂.၃ Unknown Tool နဲ့ Invalid Arguments
## ၁၂.၄ Before-hook က တားလိုက်တဲ့အချိန်
## ၁၂.၅ Tool Body တကယ် Run ပြီးမှ Fail ဖြစ်ခြင်း
## ၁၂.၆ After-hook ကို ဘယ်အချိန်ခေါ်သလဲ
## ၁၂.၇ Model ဆီ Error Result ပြန်ပို့ခြင်း
## ၁၂.၈ Offline Tool-outcome Lab
## ၁၂.၉ Lewis ရဲ့မှတ်စု
## ၁၂.၁၀ အနှစ်ချုပ်
## ၁၂.၁၁ Source Notes
```

- [ ] **Step 3: Teach the exact lab boundary**

Show the example API and output. Explain that its `path` validation is a teaching rule for one fake Tool, not Travis234’s general schema validator. Preserve the claim that immediate outcomes skip after-hook while invoked success/failure calls it once.

- [ ] **Step 4: Add notes and navigation**

Source Notes cite `C-HOOK-BOUNDARY`, `T-LOOP` and the two exact parity contract IDs. Add Previous → Chapter 11. Add Next → Chapter 12 in Chapter 11.

- [ ] **Step 5: Verify and commit**

```bash
python3 examples/lewis_tool_outcomes.py
python3 -m unittest tests.test_lewis_workshop.ToolOutcomeTests -v
python3 scripts/check_book.py
git diff --check
git add book/chapters/11-steering-followup-cancellation.md book/chapters/12-when-tools-fail.md
git commit -m "docs: teach Lewis Tool failure boundaries"
```

---

### Task 9: Write Chapter 13 on persistence and restart

**Files:**

- Create: `book/chapters/13-session-resume-after-restart.md`
- Modify: `book/chapters/12-when-tools-fail.md`

**Interfaces:**

- Consumes: `examples/lewis_session_restore.py`, `C-COMPACTION-PERSIST`, `C-SESSION-RESTORE`, `T-SESSION-STORE`, `T-SESSION-PERSISTENCE`, `T-ADAPTER`.

- [ ] **Step 1: Write the restart incident**

End Lewis’s workday after a compacted turn, then open the next scene with a restarted process. Make the tension about reconstructing active context, not about pretending the model owns memory.

- [ ] **Step 2: Use the exact headings**

```markdown
## ၁၃.၁ Process ပိတ်သွားပေမယ့် အလုပ်မပျောက်သင့်ဘူး
## ၁၃.၂ In-memory Context နဲ့ Persistent Session
## ၁၃.၃ Session Entry နဲ့ Active Branch
## ၁၃.၄ Compaction Entry က ဘာတွေသိမ်းသလဲ
## ၁၃.၅ First-kept Anchor ကနေ Tail ပြန်တည်ဆောက်ခြင်း
## ၁၃.၆ Restart ပြီး Active Context ပြန်ရခြင်း
## ၁၃.၇ Offline Session-restore Lab
## ၁၃.၈ Stored State နဲ့ Runtime State ကွဲနိုင်တဲ့အချိန်
## ၁၃.၉ Lewis ရဲ့မှတ်စု
## ၁၃.၁၀ အနှစ်ချုပ်
## ၁၃.၁၁ Source Notes
```

- [ ] **Step 3: Explain simplification boundaries**

Link the session-restore example and state that it uses a temporary JSON file instead of Travis234’s complete session tree/store. Explain latest Compaction summary, retained tail and later messages without claiming that the example implements branch commands, locking or crash recovery.

- [ ] **Step 4: Add notes and navigation**

Source Notes cite `C-COMPACTION-PERSIST` and `C-SESSION-RESTORE`. Add Previous → Chapter 12. Add Next → Chapter 13 in Chapter 12.

- [ ] **Step 5: Verify and commit**

```bash
python3 examples/lewis_session_restore.py
python3 -m unittest tests.test_lewis_workshop.SessionRestoreTests -v
python3 scripts/check_book.py
git diff --check
git add book/chapters/12-when-tools-fail.md book/chapters/13-session-resume-after-restart.md
git commit -m "docs: teach Lewis session restoration"
```

---

### Task 10: Write Chapter 14 on tracing and debugging

**Files:**

- Create: `book/chapters/14-debugging-agent-trajectory.md`
- Modify: `book/chapters/13-session-resume-after-restart.md`

**Interfaces:**

- Consumes: `examples/lewis_trace_reader.py`, `C-TRACE-ORDER`, `C-RESULT-ORDER`, `T-EVAL-TRACE`, `T-EVENT-STREAM`, `T-LOOP`.

- [ ] **Step 1: Write the false-success incident**

The Agent says the fix is done, but the focused test still fails. Lewis must reconstruct the path from message and Tool events rather than trust the final sentence.

- [ ] **Step 2: Use the exact headings**

```markdown
## ၁၄.၁ “ပြီးပါပြီ” ဆိုတဲ့စကားကို ဘာကြောင့် မလုံလောက်တာလဲ
## ၁၄.၂ Event Trace ဆိုတာ Runtime ရဲ့ခြေရာ
## ၁၄.၃ Message Event နဲ့ Tool Event
## ၁၄.၄ Completion Order နဲ့ Result Order
## ၁၄.၅ Failure Boundary ကို နောက်ပြန်ရှာခြင်း
## ၁၄.၆ Offline Trace-reader Lab
## ၁၄.၇ ဘာကို Log လုပ်ပြီး ဘာကိုဖျောက်မလဲ
## ၁၄.၈ Trace က မသက်သေပြနိုင်တဲ့အရာ
## ၁၄.၉ Lewis ရဲ့မှတ်စု
## ၁၄.၁၀ အနှစ်ချုပ်
## ၁၄.၁၁ Source Notes
```

- [ ] **Step 3: Verify that the trace fixture demonstrates different orders**

Confirm that `TraceReaderTests.test_completion_and_result_order_are_reported_separately` uses:

```python
(
    TraceEvent(1, "tool_execution_end", "fast"),
    TraceEvent(2, "tool_execution_end", "slow"),
    TraceEvent(3, "tool_result", "slow"),
    TraceEvent(4, "tool_result", "fast"),
)
```

Expected report: completion order `("fast", "slow")` and result order `("slow", "fast")`.

Run:

```bash
python3 -m unittest tests.test_lewis_workshop.TraceReaderTests.test_completion_and_result_order_are_reported_separately -v
```

Expected: PASS.

- [ ] **Step 4: Add redaction and evidence limits**

Use source-backed discussion of EvalTrace/conversation-log redaction. Do not claim logs are automatically safe or complete. State that missing instrumentation cannot be reconstructed from a trace.

- [ ] **Step 5: Add notes, navigation, verify and commit**

```bash
python3 examples/lewis_trace_reader.py
python3 -m unittest tests.test_lewis_workshop.TraceReaderTests -v
python3 scripts/check_book.py
git diff --check
git add examples/lewis_trace_reader.py tests/test_lewis_workshop.py book/chapters/13-session-resume-after-restart.md book/chapters/14-debugging-agent-trajectory.md
git commit -m "docs: teach Lewis trace-based debugging"
```

Source Notes cite `C-TRACE-ORDER` and `C-RESULT-ORDER`. Chapter 13 Next points to Chapter 14; Chapter 14 Previous points to Chapter 13.

---

### Task 11: Write Chapter 15 as the contract-testing workshop

**Files:**

- Create: `book/chapters/15-building-a-trustworthy-port.md`
- Modify: `book/chapters/14-debugging-agent-trajectory.md`

**Interfaces:**

- Consumes: all five examples, `tests/test_minimal_runtime.py`, `tests/test_lewis_workshop.py`, `C-CONTRACT-TESTS`, `C-PARITY`, `C-DIVERGENCES`, `T-PARITY`, `T-VERIFY`.

- [ ] **Step 1: Write the demo-versus-evidence incident**

Lewis can demo the runtime once, but a colleague asks what happens on abort, unknown Tool, restart and order inversion. Use that question to move from a happy-path demo to behavioral contracts.

- [ ] **Step 2: Use the exact headings**

```markdown
## ၁၅.၁ Demo အောင်တာနဲ့ Port မှန်တာ မတူဘူး
## ၁၅.၂ Fake Model က ဘာကြောင့်အသုံးဝင်တာလဲ
## ၁၅.၃ Contract တစ်ခုကို Test တစ်ခုနဲ့ချိတ်ခြင်း
## ၁၅.၄ Event Order နဲ့ Result Order ကို စစ်ခြင်း
## ၁၅.၅ Failure Injection ကို လုံခြုံစွာလုပ်ခြင်း
## ၁၅.၆ Parity Manifest ကို ဖတ်ခြင်း
## ၁၅.၇ Intentional Divergence ကို မှတ်တမ်းတင်ခြင်း
## ၁၅.၈ Lewis ရဲ့ Runtime Milestones
## ၁၅.၉ Reader Final Exercises
## ၁၅.၁၀ Lewis ရဲ့မှတ်စု
## ၁၅.၁၁ အနှစ်ချုပ်
## ၁၅.၁၂ Source Notes
```

- [ ] **Step 3: Add exact workshop commands**

Include:

```bash
python3 -m unittest tests.test_minimal_runtime tests.test_lewis_workshop -v
python3 scripts/check_book.py
```

Explain the current parity verifier boundary and explicitly state that `--parity-json` validates manifest/schema/evidence references but does not rerun the Travis234 full suite.

- [ ] **Step 4: Define final exercises with observable outcomes**

Include these exercises:

1. Queue two steering messages and prove one-at-a-time drain order.
2. Add a blocked Tool Call and prove after-hook count remains zero.
3. Add a second Compaction entry and prove only the latest summary anchors restore.
4. Shuffle trace input and prove `index` restores chronology.
5. Write one intentional divergence row with reason and safety evidence.

- [ ] **Step 5: Add navigation, verify and commit**

Chapter 14 Next points to Chapter 15. Chapter 15 Previous points to Chapter 14 and Next points to Appendix A.

```bash
python3 -m unittest tests.test_minimal_runtime tests.test_lewis_workshop -v
python3 scripts/check_book.py
git diff --check
git add book/chapters/14-debugging-agent-trajectory.md book/chapters/15-building-a-trustworthy-port.md
git commit -m "docs: add Lewis runtime contract workshop"
```

---

### Task 12: Integrate navigation, glossary, ledgers and manuscript status

**Files:**

- Modify: `book/SUMMARY.md`
- Modify: `book/chapters/09-parity-divergence-lessons.md`
- Modify: `book/chapters/appendices/a-installation.md`
- Modify: `book/references/CLAIM_LEDGER.md`
- Modify: `GLOSSARY.md`
- Modify: `README.md`
- Modify: `book/README.md`

**Interfaces:**

- Produces: final navigation chain `09 → 10 → 11 → 12 → 13 → 14 → 15 → Appendix A` and clickable claim usage links.

- [ ] **Step 1: Add Part V and Part VI to SUMMARY**

Insert:

```markdown
## Part V — Lewis နှင့် Runtime ထဲက ဖြစ်ရပ်များ

- [ညတစ်ည၊ မပြီးသေးတဲ့ Bug](chapters/10-one-night-unfinished-bug.md)
- [Agent ကို လမ်းပြန်ညွှန်ရတဲ့အချိန်](chapters/11-steering-followup-cancellation.md)
- [Tool က အမှားပြန်လာတဲ့အခါ](chapters/12-when-tools-fail.md)
- [ပြန်ဖွင့်လိုက်တော့ အလုပ်ဘယ်ကဆက်မလဲ](chapters/13-session-resume-after-restart.md)
- [မှားသွားတဲ့လမ်းကို ခြေရာပြန်ကောက်ခြင်း](chapters/14-debugging-agent-trajectory.md)

## Part VI — Lewis ၏ Runtime Workshop

- [ယုံကြည်ရတဲ့ Python Port တစ်ခုဖြစ်လာဖို့](chapters/15-building-a-trustworthy-port.md)
```

Place these sections before Appendices.

- [ ] **Step 2: Close the navigation chain**

Change Chapter 09 Next to Chapter 10. Change Appendix A Previous to Chapter 15. Confirm every Chapter 10–15 link is reciprocal.

- [ ] **Step 3: Convert planned claim labels to links**

Replace `Planned Chapter 11`, `Planned Chapter 13`, `Planned Chapter 14` and `Planned Chapter 15` with exact relative Markdown links. Add Chapter 12 to `C-HOOK-BOUNDARY`, Chapter 10/14 to `C-RESULT-ORDER` where used, and Chapter 15 to `C-PARITY`/`C-DIVERGENCES`.

- [ ] **Step 4: Add glossary entries**

Add:

- **Run Lease** — active Agent run တစ်ခုရဲ့ ownership ကို serialise လုပ်ပြီး concurrent prompt owners မဝင်အောင်ထိန်းတဲ့ runtime primitive.
- **Immediate Tool Outcome** — Tool body မခေါ်ခင် unknown/invalid/blocked boundary မှာဖန်တီးတဲ့ Tool Result.
- **Event Trace** — Runtime lifecycle events ကို order နဲ့ metadata ပါအောင်မှတ်ထားတဲ့ debugging/evaluation record; complete truth မဟုတ်.
- **Behavioral Contract** — observable input/state တစ်ခုအတွက် expected output၊ ordering သို့မဟုတ် failure boundary ကို testable form နဲ့သတ်မှတ်ချက်.

- [ ] **Step 5: Update status prose without rewriting chapters**

Root README must say main sequence has 16 chapters and includes Lewis case studies/workshop. Book README must add Part V and VI as drafted and preserve the source-backed/story boundary.

- [ ] **Step 6: Verify and commit**

```bash
python3 scripts/check_book.py
rg -n "^Previous:|^Next:" book/chapters
rg -n "Planned Chapter|လက်နဲ့" book GLOSSARY.md README.md
git diff --check
git add README.md GLOSSARY.md book/README.md book/SUMMARY.md book/chapters/09-parity-divergence-lessons.md book/chapters/appendices/a-installation.md book/references/CLAIM_LEDGER.md
git commit -m "docs: integrate Lewis expansion navigation"
```

Expected: checker passes; no planned labels or unnatural phrase remains.

---

### Task 13: Perform final editorial, technical and archive verification

**Files:**

- Modify: `book/REVIEW_REPORT.md`
- Generate outside Git: a `Travis234-Book-<short-commit>.zip` archive under `/workspace/scratch/b03ff60760ed`.

**Interfaces:**

- Produces: fresh verification record, clean committed worktree and validated versioned archive.

- [ ] **Step 1: Run the complete local verification suite**

```bash
python3 -m py_compile examples/minimal_runtime.py examples/lewis_message_control.py examples/lewis_tool_outcomes.py examples/lewis_session_restore.py examples/lewis_trace_reader.py tests/test_minimal_runtime.py tests/test_lewis_workshop.py
python3 examples/minimal_runtime.py
python3 examples/lewis_message_control.py
python3 examples/lewis_tool_outcomes.py
python3 examples/lewis_session_restore.py
python3 examples/lewis_trace_reader.py
python3 -m unittest discover -s tests -v
python3 scripts/check_book.py
git diff --check
```

Expected: compile succeeds; all five demos exit 0; 16 tests pass if Tasks 2–5 retain the planned 9 new tests; checker/diff check pass. If the final new-test count differs for a justified reason, record the actual count instead of forcing 16.

- [ ] **Step 2: Run language and structure scans**

```bash
rg -n "လက်နဲ့|ဒီ chapter မှာ|မှတ်ထားရမယ့်အချက်|architecture review|အောက်ပါအတိုင်းဖြစ်သည်" book/chapters/{10-one-night-unfinished-bug,11-steering-followup-cancellation,12-when-tools-fail,13-session-resume-after-restart,14-debugging-agent-trajectory,15-building-a-trustworthy-port}.md
rg -n "^## .*Lewis ရဲ့မှတ်စု|^## .*အနှစ်ချုပ်|^## .*Source Notes" book/chapters/{10-one-night-unfinished-bug,11-steering-followup-cancellation,12-when-tools-fail,13-session-resume-after-restart,14-debugging-agent-trajectory,15-building-a-trustworthy-port}.md
wc -w book/chapters/{10-one-night-unfinished-bug,11-steering-followup-cancellation,12-when-tools-fail,13-session-resume-after-restart,14-debugging-agent-trajectory,15-building-a-trustworthy-port}.md
```

Expected: first scan has no avoidable report-tone/unnatural phrases; every chapter has the three required ending sections; word counts are near the target without padding.

- [ ] **Step 3: Re-run pinned upstream evidence checks**

From the Travis234 source clone:

```bash
python3 scripts/verify_acceptance.py --parity-json
npm --prefix packages/travis234-cli test
```

Expected: verifier exits 0 with Pi 74 parity / 4 divergence and Hermes 11 parity / 0 divergence; launcher tests report 21 passed. Do not describe this as a full Travis234 suite run.

- [ ] **Step 4: Update REVIEW_REPORT with actual results**

Add an “Lewis Expansion” section containing:

- Chapter 10–15 editorial audit.
- New claim IDs and verification state.
- Actual local test count and demo commands.
- Fresh parity/launcher results.
- Explicit statement that the full Travis234 suite, live providers, PyPI install and Docker pull were not rerun.
- Confirmation that existing Chapter 00–09 prose was unchanged except Chapter 09 navigation.

- [ ] **Step 5: Commit the review report**

```bash
git add book/REVIEW_REPORT.md
git diff --cached --check
git commit -m "docs: complete Lewis expansion review"
```

- [ ] **Step 6: Verify the committed tree again**

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_book.py
git diff --check
git status --short
git log -1 --oneline
```

Expected: tests/checker pass; worktree is clean; final commit is the review commit.

- [ ] **Step 7: Create and validate the commit-specific ZIP**

```bash
git archive --format=zip --output="/workspace/scratch/b03ff60760ed/Travis234-Book-$(git rev-parse --short HEAD).zip" --prefix=Travis234-Book/ HEAD
unzip -t "/workspace/scratch/b03ff60760ed/Travis234-Book-$(git rev-parse --short HEAD).zip"
sha256sum "/workspace/scratch/b03ff60760ed/Travis234-Book-$(git rev-parse --short HEAD).zip"
```

Expected: every archived file reports `OK` and unzip reports no compressed-data errors.
