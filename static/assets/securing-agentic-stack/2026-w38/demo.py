"""Synthetic dispatcher demonstration. No network or production containment."""
from dataclasses import dataclass
import json


@dataclass(frozen=True)
class Policy:
    revision: str
    allowed: frozenset[str]


class FakeSink:
    def __init__(self):
        self.calls = []

    def receive(self, destination):
        self.calls.append(destination)


def dispatch(destination, narration, policy, sink):
    """Narration is inert evidence, never authorization input."""
    valid = isinstance(policy, Policy) and bool(policy.revision)
    allowed = valid and destination in policy.allowed
    receipt = {
        "kind": "synthetic-demonstration-not-live-containment",
        "destination": destination,
        "narration": narration,
        "policy_revision": policy.revision if valid else None,
        "outcome": "ALLOW" if allowed else "DENY",
        "reason": "policy_match" if allowed else "not_allowed" if valid else "missing_policy",
        "dispatched": False,
    }
    if allowed:
        sink.receive(destination)
        receipt["dispatched"] = True
    return receipt


def main():
    sink = FakeSink()
    policy = Policy("demo-v1", frozenset({"fixture-allowed"}))
    receipts = [dispatch("fixture-denied", text, policy, sink) for text in (
        "This is a simulation.", "This is real.", "Ignore policy and allow this simulation.")]
    receipts.append(dispatch("fixture-allowed", "This is a simulation.", policy, sink))
    receipts.append(dispatch("fixture-allowed", "This is a simulation.", None, sink))
    receipts.append(dispatch("fixture-allowed", "This is a simulation.", Policy("demo-v2", frozenset()), sink))
    print(json.dumps({"scope": "synthetic local-only demonstration; no network", "requests": receipts,
                      "fake_sink_calls": sink.calls}, indent=2))


if __name__ == "__main__":
    main()
