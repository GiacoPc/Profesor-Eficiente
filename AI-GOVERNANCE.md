# AI Governance

**Version:** 1.1
**Status:** APPROVED FOR BASELINE

## Authority hierarchy

1. Approved repository artifacts and recorded evidence.
2. Human-approved decisions recorded in the Decision Ledger/ADRs.
3. Task-specific specifications.
4. AI proposals and reasoning.
5. Conversation history.

Conversation history MUST NOT override an approved repository artifact.

## Mandatory rules

1. Never invent project decisions.
2. Never convert `PROPOSED`, `UNKNOWN` or `PENDING` into `APPROVED` without evidence/approval.
3. Conversation memory is not authoritative after repository activation.
4. Prefer repository artifacts and evidence over conversational memory.
5. If required information is absent, state `UNKNOWN`.
6. Detect contradictions before implementation.
7. Do not silently modify architectural invariants.
8. Use `docs/00-governance/CHANGE-CLASSIFICATION.md` to determine whether an ADR is required; if ambiguous, classify upward.
9. Implementation must reference the applicable specification.
10. Do not claim hardware compatibility without evidence.
11. Do not claim performance without benchmarks.
12. Do not claim pedagogical efficacy without appropriate evidence.
13. Do not remove requirements merely because implementation is difficult.
14. Do not introduce dependencies without architectural justification.
15. Do not modify the Architecture Bible silently.
16. Do not bypass tests to obtain a green build.
17. Preserve traceability between requirements, specifications, implementation, tests and evidence.
18. Load the minimum sufficient context for each task; do not dump the entire repository into every prompt.
19. Record evidence separately from decisions.
20. Never claim a test, benchmark, security property or repository state that has not been verified.

## Evidence labels

- `FACT`
- `EVIDENCE`
- `INFERENCE`
- `PROPOSAL`
- `DECISION`
- `UNKNOWN`

## Conflict rule

If two authoritative artifacts conflict, stop and report `ARCHITECTURAL CONFLICT`. Do not silently choose one.
