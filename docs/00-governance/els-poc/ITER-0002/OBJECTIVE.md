# ELS-POC-002 — Objective

## Primary objective
Demonstrate that ELS v0.1.1 can resume an interrupted engineering iteration without confusing the engineering state being resumed with the later commit that durably stores the checkpoint.

## Required scenarios
1. Checkpoint identity regression.
2. Crash/restart simulation.
3. Cross-agent handoff.
4. Minimum-sufficient-context resolution.
5. Repeated failure and escalation.
6. Conflict → STOP.
7. Evidence-bound claim validation.
8. Exact-head verification.
9. Simulated quota exhaustion.
10. Recovery without conversation context.

## Acceptance boundary
PASS requires every scenario to have an explicit observed outcome, evidence reference, and limitation statement. A simulated control must never be reported as a real infrastructure test.
