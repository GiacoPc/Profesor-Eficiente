# AI Governance

**Version:** 1.0
**Status:** APPROVED FOR BASELINE

## Mandatory rules

1. Never invent project decisions.
2. Never convert `PROPOSED`, `UNKNOWN` or `PENDING` into `APPROVED` without evidence/approval.
3. Conversation memory is not authoritative after repository activation.
4. Prefer repository artifacts and evidence over conversational memory.
5. If required information is absent, state `UNKNOWN`.
6. Detect contradictions before implementation.
7. Do not silently modify architectural invariants.
8. Significant architectural changes require an ADR.
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

## Evidence labels

- `FACT`
- `EVIDENCE`
- `INFERENCE`
- `PROPOSAL`
- `DECISION`
- `UNKNOWN`

## Conflict rule

If two authoritative artifacts conflict, stop and report `ARCHITECTURAL CONFLICT`. Do not silently choose one.
