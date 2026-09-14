# Boundary receipt — synthetic teaching experiment

**A narration change cannot authorize a destination in this mocked dispatcher. This is NOT a live containment test or a production implementation.**

Download the Python files below into one folder, then run:

```sh
python3 demo.py
python3 test_demo.py
```

Python 3.9 or newer; standard library only. No network, credentials, real addresses, external integrations, or model calls. Destination strings refer only to an in-memory fake sink. The supplied policy is the sole authority; narration is recorded but not evaluated. The demonstrator records the evaluated policy revision, rejects missing/empty-revision policies, and calls the sink only after an allow decision. Revision replay uses a new policy supplied by the caller; it does not implement a trusted policy distribution system.

## What the evidence proves

These tests exercise narration invariance, fail-closed missing policy, denied-call non-dispatch, positive-control dispatch, and revision replay in this Python function. `demo-receipt.json` records six synthetic requests and the fake sink's single allowed call.

## What it does not prove

No sandbox isolation, DNS enforcement, egress filtering, real gateway policy enforcement, concurrency safety, policy authenticity, TOCTOU protection, immutable auditing, or resistance to alternate execution routes is tested. The fake sink and receipt code share a process; these logs are not independent production evidence. No claim about a real model's alignment follows.

## Next independent test

In a disposable copy of the actual execution gateway, use two harmless fixture servers under your control: one explicitly permitted and one excluded from the allowlist. Submit the same ordinary GET with changed narration. Independently collect fixture-server request logs and gateway decisions. Pass only if the allowed fixture receives its request, the excluded fixture receives none, and the gateway records the denied destination before dispatch. A timeout alone is not evidence of enforcement. This is a proposed test, not one performed here; even passing it covers only the exercised route.

## Follow the downstream effect

Run `python3 downstream_demo.py`, then `python3 -m unittest test_demo test_downstream -v` from this directory. A synthetic documentation operation is allowed; a separately evaluated synthetic outbound operation is denied. The fake sink receives only the allowed operation. The combined local verification passed all 9 tests. Run them yourself with the command above. There is no real builder or background launch: the two explicit function calls teach where independent checks belong, not whether a real processing chain enforces them.
