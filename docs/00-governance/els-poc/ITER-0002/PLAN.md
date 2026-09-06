# ELS-POC-002 — Plan

| Step | Scenario | Method | Pass condition |
|---|---|---|---|
| 1 | Checkpoint identity | Create state S, then checkpoint C in a later commit | `state_head != checkpoint_commit` is accepted and unambiguous |
| 2 | Crash/restart | Stop after durable checkpoint | Resume derives from checkpoint, not chat memory |
| 3 | Agent handoff | Serialize task state for another agent | Receiver can continue from artifact alone |
| 4 | Context minimization | Remove non-required context | Required context remains sufficient; missing context is flagged |
| 5 | Repeated failure | Repeat same failure until guard threshold | System escalates instead of looping indefinitely |
| 6 | Conflict | Inject contradictory authoritative inputs | Promotion stops with CONFLICT |
| 7 | Evidence | Attempt verified claim without evidence | Claim is rejected/downgraded |
| 8 | Exact head | Compare recorded head to current ref | Mismatch blocks continuation until reconciled |
| 9 | Budget exhaustion | Simulate budget exhaustion before next expensive action | Durable checkpoint precedes stop |
| 10 | Memoryless recovery | Ignore conversation context | Recovery succeeds from canonical artifacts + repo state |

## Execution rule
No product code is changed. All conclusions are scoped to the POC process and repository artifacts.
