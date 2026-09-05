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

- PRD — no formal repository document currently established on this branch; requirements remain governed by baseline artifacts until formalized.
- PAD — **PROPOSED / DRAFT v0.1**, newly formalized; not approved.
- CLM — **PROPOSED / DRAFT v0.1**, newly formalized; not approved.
- APE — **PROPOSED / DRAFT v0.1**, newly formalized; not approved.
- FDM — **PROPOSED / DRAFT v0.1**, newly formalized; not approved.
- LPH-SPEC — **PROPOSED / DRAFT v0.1**, implementation not authorized by this document alone.
- SRA — pending; must consume approved upstream contracts rather than redefine them during implementation.
- LLM/inference architecture — pending evidence-backed decisions.
- Audio architecture — pending.
- Data architecture — pending.
- Benchmark plan — pending.

## Formalization sequence

The current architecture work establishes the following dependency order:

```text
Requirements / governed baseline
          |
          +--> PAD  (how to teach)
          |
          +--> CLM  (how learning state is represented)
          |
          +--> FDM  (formal domain semantics and invariants)
          |
          +--> APE  (pedagogical decision authority)
          |
          +--> LPH  (linguistic/pedagogical control around generation)
          |
          +--> SRA  (implementation architecture)
```

These documents are currently **draft specifications**, not a claim that the contracts have already been mutually reconciled.

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
