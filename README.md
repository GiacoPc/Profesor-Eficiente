# Profesor Eficiente

**Governed offline-first Android pedagogical tutor for American English.**

This repository is the versioned project source of truth for approved requirements, specifications, architecture, implementation, tests, and evidence.

## Current phase

`PGKI-1.0 BASELINE`

Production implementation has **not** started. The project is establishing governance and architecture before runtime implementation.

## Bootstrap for AI/IDE agents

Read, in order:

1. `PROJECT-STATE.yaml`
2. `PROJECT-CONSTITUTION.md`
3. `AI-GOVERNANCE.md`
4. `CONTEXT-MANIFEST.yaml`
5. `DECISION-LEDGER.yaml`
6. `docs/ARCHITECTURE-BIBLE.md`
7. Task-specific specifications and ADRs
8. Relevant tests/evidence

If information is missing, use `UNKNOWN`; do not invent decisions.

## Architecture direction

The product is intended to remain offline-first, modular, evidence-driven and independent of a single LLM. The pedagogical authority is external to the generative model; the LLM is a capability component, not the sole source of curriculum or progression rules.
