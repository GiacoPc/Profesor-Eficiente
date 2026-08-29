# AGENTS.md — Profesor Eficiente

## Bootstrap

Before any change:
1. Read `PROJECT-STATE.yaml`.
2. Read `PROJECT-CONSTITUTION.md`.
3. Read `AI-GOVERNANCE.md`.
4. Read `CONTEXT-MANIFEST.yaml`.
5. Read `DECISION-LEDGER.yaml`.
6. Read `docs/ARCHITECTURE-BIBLE.md`.
7. Load `docs/00-governance/PGKI-1.1-EVIDENCE-CLAIM-INTEGRITY.md` for claims involving external/verifiable state.
8. Load only task-relevant specifications and ADRs.
9. Check relevant tests/evidence.

## Hard rules

- Do not invent requirements or decisions.
- Preserve `UNKNOWN`, `PENDING` and `PROPOSED` states.
- Repository artifacts and evidence outrank conversational memory.
- Report contradictions as `ARCHITECTURAL CONFLICT`.
- Report evidence disagreement as `EVIDENCE CONFLICT`.
- Significant architectural changes require an ADR.
- Do not claim target-device performance without measurements.
- Do not claim that an artifact was seen, reviewed, inspected or verified unless it was actually accessible in the current execution context.
- Critical externally verifiable claims require an evidence reference.
- Do not claim absence of failures without a defined audit scope and coverage statement.
- Keep requirements, specifications, code, tests and evidence traceable.
- Do not dump the entire repository into every AI task; use minimum sufficient context.
