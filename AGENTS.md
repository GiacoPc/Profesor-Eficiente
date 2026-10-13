# AGENTS.md — Profesor Eficiente

## Bootstrap

Before any change:
1. Read `PROJECT-STATE.yaml`.
2. Read `PROJECT-CONSTITUTION.md`.
3. Read `AI-GOVERNANCE.md`.
4. Read `CONTEXT-MANIFEST.yaml`.
5. Read `DECISION-LEDGER.yaml`.
6. Read `docs/ARCHITECTURE-BIBLE.md`.
7. Load only task-relevant specifications and ADRs.
8. Check relevant tests/evidence.

## Hard rules

- Do not invent requirements or decisions.
- Preserve `UNKNOWN`, `PENDING` and `PROPOSED` states.
- Repository artifacts and evidence outrank conversational memory.
- Report contradictions as `ARCHITECTURAL CONFLICT`.
- Significant architectural changes require an ADR.
- Do not claim target-device performance without measurements.
- Keep requirements, specifications, code, tests and evidence traceable.
- Do not dump the entire repository into every AI task; use minimum sufficient context.
