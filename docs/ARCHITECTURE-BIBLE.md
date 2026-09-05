# Architecture Bible

## Baseline purpose

This document indexes the governed architecture. Detailed specifications are added only after reconciliation and approval.

## Current architectural principles

- Offline-first.
- Pedagogical authority outside the LLM.
- Adaptive Pedagogical Engine (APE) as intended pedagogical orchestrator.
- Student Digital Twin (SDT) as intended learner-state representation.
- Formal Domain Model (FDM) as domain boundary.
- Local governed RAG.
- LLM replaceability.
- Rust + Kotlin separation, with exact boundaries pending specification.
- Evidence-driven CPU/RAM/NPU/GPU optimization.
- Task-routed AI context.
- Linguistic & Pedagogical Harness (LPH) as the proposed model-independent control boundary between authoritative pedagogical/linguistic logic and probabilistic generation.

## Specifications / status

- PRD — **NOT FOUND on inspected branch at expected path**; requirements remain governed by baseline artifacts until formalized.
- PAD — **PROPOSED / DRAFT v0.1**, newly formalized; not approved.
- CLM — **PROPOSED / DRAFT v0.1**, newly formalized; not approved.
- APE — **PROPOSED / DRAFT v0.1**, newly formalized; not approved.
- FDM — **PROPOSED / DRAFT v0.1**, newly formalized; not approved.
- LPH-SPEC — **PROPOSED / DRAFT v0.1**, implementation not authorized by this document alone.
- SDT standalone specification — **NOT FOUND on inspected branch at expected path**; required for CLM/APE contract closure.
- SRA — pending; must consume approved upstream contracts rather than redefine them during implementation.
- LLM/inference architecture — pending; expected artifact not found on inspected branch.
- RAG architecture — pending; expected artifact not found on inspected branch.
- Audio architecture — pending.
- Data architecture — pending.
- Benchmark plan — pending.

## Formalization and reconciliation status

The four upstream documents now exist as draft artifacts, but they have **not** yet been mutually approved. Cross-document reconciliation identified P1 ambiguities and missing supporting contracts.

Current reconciliation artifacts:

- `docs/architecture/CONTRADICTION-MATRIX-v0.1.md`
- `docs/architecture/CONTRACT-MATRIX-v0.1.md`
- `docs/architecture/MISSING-ARTIFACTS-REGISTER-v0.1.md`

**Current gate: BLOCKED / NOT READY FOR LPH v1.0 or SRA.**

## LPH architectural role

The LPH specification defines the proposed boundary for:

- separating authoritative pedagogical state and progression from LLM generation;
- keeping the concrete LLM replaceable;
- constraining and validating generated outputs;
- representing linguistic/error assessment as structured evidence;
- integrating APE, FDM, CLM, SDT, RAG, and mastery/progression policies without making any one LLM the system authority.

Reference: `docs/architecture/LINGUISTIC-PEDAGOGICAL-HARNESS-SPEC.md`.

The LPH specification intentionally leaves final model, runtime, NPU/GPU strategy, STT/TTS, pronunciation/prosody assessment, persistence, budgets, and other technology choices unresolved until evidence-backed ADRs/specifications exist.

## Authority

This index does not silently resolve unresolved technical choices. Pending items remain pending until an approved specification or ADR provides evidence and a decision.
