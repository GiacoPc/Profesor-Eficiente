# AI Governance

**Version:** 1.2
**Status:** PROPOSED HARDENING — PENDING HUMAN APPROVAL
**Parent baseline:** PGKI-1.0 / AI Governance 1.1

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
21. Apply `docs/00-governance/PGKI-1.1-EVIDENCE-CLAIM-INTEGRITY.md` to all externally verifiable claims.
22. Establish evidence availability before asserting that an artifact was seen, reviewed, inspected or verified.
23. Never claim absence of prior failures without a defined audit scope and coverage statement.
24. Treat `NOT_AVAILABLE` and `UNKNOWN` as controlled states, not implicit success.
25. For high-impact gates, use independent secondary verification when defined by the applicable gate policy.

## Evidence labels

- `FACT`
- `EVIDENCE`
- `OBSERVED`
- `VERIFIED`
- `INFERENCE`
- `PROPOSAL`
- `DECISION`
- `UNKNOWN`
- `NOT_AVAILABLE`
- `CONFLICT`

## Conflict rule

If two authoritative artifacts conflict, stop and report `ARCHITECTURAL CONFLICT`. Do not silently choose one.

If evidence sources disagree, stop and report `EVIDENCE CONFLICT`. Resolve the evidence before proceeding.
