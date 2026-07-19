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
