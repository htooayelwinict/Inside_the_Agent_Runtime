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
