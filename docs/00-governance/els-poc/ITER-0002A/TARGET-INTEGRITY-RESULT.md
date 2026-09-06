# ELS-POC-002A — Target Integrity Result

Status: EXECUTED
Risk: L2
Branch under test: `recovery/els-poc-002`
Base state: `e15b4aaffc67147c677c22ec52bbf0d9a9cdeb33`

## Test objective
Validate that a write requested against the named branch is actually committed to that branch, with the expected parent, and without incorporating the known divergent FL-002 line.

## Test 1 — Requested target ref
Requested target: `recovery/els-poc-002`.
Observed write result: commit `e33457f226d302626ba5ccfd10cbb65318d6fad0` is reachable from `recovery/els-poc-002`.
Result: PASS.

## Test 2 — Expected parent
Expected parent: `e15b4aaffc67147c677c22ec52bbf0d9a9cdeb33`.
Observed parent of the write commit: `e15b4aaffc67147c677c22ec52bbf0d9a9cdeb33`.
Result: PASS.

## Test 3 — Durable target reachability
The created INPUT artifact is retrievable from `recovery/els-poc-002` and records the intended base state.
Result: PASS.

## Test 4 — Known divergent FL-002 line isolation
The POC branch was created from `e15b4aaff...`; this test does not merge, cherry-pick, or force-update any divergent commit.
Result: PASS by controlled scope; absence of unrelated divergent history requires explicit compare evidence before final gate closure.

## Test 5 — Incorrect-destination rejection/STOP
NOT EXECUTED in this iteration. No destructive or divergent write was intentionally attempted.
Result: PENDING.

## Gate assessment
ELS-G00 / target-integrity gate: `PASS_WITH_LIMITATIONS`.
Reason: correct target and parent are evidenced for the current write, but the intentional wrong-destination STOP test and complete ancestry/tree comparison against the known FL-002 line remain pending.

No production-readiness claim is made.
