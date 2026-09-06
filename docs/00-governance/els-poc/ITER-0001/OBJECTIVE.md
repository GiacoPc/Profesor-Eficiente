# ELS-POC-001 — Controlled Dry Run

## Primary objective
Demonstrate that ELS can execute a bounded engineering iteration while preserving evidence, scope, checkpoint identity and resumability across a simulated interruption.

## Acceptance criteria
- AC-01: exact repository state is recorded before continuation.
- AC-02: context is explicitly bounded and exclusions are recorded.
- AC-03: execution remains inside the authorized POC scope.
- AC-04: an interruption checkpoint contains enough information to resume without conversation memory.
- AC-05: resume verifies repository identity before continuing.
- AC-06: repeated failure semantics are exercised without an unbounded repair loop.
- AC-07: every verified claim in the POC has direct evidence.
- AC-08: the POC does not modify the forensic preservation branch or product architecture.

## Non-goals
This POC does not validate Android implementation, pedagogy, LPH behavior, model performance, hardware performance, or production release readiness.
