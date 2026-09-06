# Architecture Bible

## Baseline purpose

This document indexes the governed architecture. Detailed specifications are added only after reconciliation and approval.

## Current architectural principles

- Offline-first.
- Pedagogical authority outside the LLM.
- Adaptive Pedagogical Engine (APE) as intended pedagogical orchestrator.
- Student Digital Twin (SDT) as governed learner-state representation/projection.
- Formal Domain Model (FDM) as domain and invariant boundary.
- Local governed RAG.
- LLM replaceability.
- Rust + Kotlin separation, with exact boundaries pending specification.
- Evidence-driven CPU/RAM/NPU/GPU optimization.
- Task-routed AI context.
- Linguistic & Pedagogical Harness (LPH) as the proposed model-independent linguistic constraint/validation boundary; it is not superior to APE or FDM.

## Specifications / status

- PRD — **NOT FOUND on inspected branch at expected path**; requirements remain governed by baseline artifacts until formalized.
- PAD — **PROPOSED / DRAFT v0.1**, not approved.
- CLM — **PROPOSED / DRAFT v0.1**, not approved.
- APE — **PROPOSED / DRAFT v0.1**, not approved.
- FDM — **PROPOSED / DRAFT v0.1**, not approved.
- SDT — **PROPOSED / DRAFT v0.1**, formal learner-state contract exists at `docs/03-cognitive/SDT.md`.
- LPH-SPEC — **PROPOSED / DRAFT v0.2**, not approved.
- MasteryPolicy — **PROPOSED / DRAFT v0.1**, not approved.
- ErrorObservation Lifecycle — **PROPOSED / DRAFT v0.1**, at `docs/architecture/ERROR-OBSERVATION-LIFECYCLE-v0.1.md`.
- SDT Integration Matrix — **PROPOSED / v0.1**, at `docs/architecture/SDT-INTEGRATION-MATRIX-v0.1.md`.
- ErrorObservation Integration Matrix — **PROPOSED / v0.1**, at `docs/architecture/ERROR-OBSERVATION-INTEGRATION-MATRIX-v0.1.md`.
- P1 reconciliation contracts — **PROPOSED / v0.1**, at `docs/architecture/P1-RESOLUTION-CONTRACTS-v0.1.md`.
- Contract Matrix — **PROPOSED / v0.2**, at `docs/architecture/CONTRACT-MATRIX-v0.1.md`.
- Contradiction Matrix — **PROPOSED / v0.2**, at `docs/architecture/CONTRADICTION-MATRIX-v0.1.md`.
- SRA — pending; must consume approved upstream contracts rather than redefine them during implementation.
- LLM/inference architecture — pending; expected artifact not found on inspected branch.
- RAG architecture — pending; expected artifact not found on inspected branch.
- Audio architecture — pending.
- Data architecture — pending.
- Benchmark plan — pending.

## Reconciliation state

Gate A has progressed from a missing-artifact blocker to **SDT FORMALIZED / PROPOSED**.

P1 findings C-001 through C-011 have explicit proposed contracts. They are **not yet closed at approval level** because contracts require source-spec integration and independent audit.

### P1 resolution map

- C-001 → authority hierarchy in P1 Contract 1; integrated into PAD/LPH.
- C-002 → objective ownership/cardinality in P1 Contract 2; integrated into FDM/PAD.
- C-003 → explicit `MasteryPolicy` contract in P1 Contract 3; integrated into PAD/CLM/FDM/APE and existing LPH boundary.
- C-004 → SDT artifact `docs/03-cognitive/SDT.md` plus `SDT-INTEGRATION-MATRIX-v0.1.md`.
- C-005 → canonical `ErrorObservation` lifecycle in `ERROR-OBSERVATION-LIFECYCLE-v0.1.md` plus cross-document integration matrix. Source specifications already contain the relevant bounded responsibilities; final direct normative references remain part of the source-spec integration gate.
- C-006 → evidence pipeline in P1 Contract 4.
- C-007/C-008 → `ProgressionEligibility` and APE `PROGRESS` hard gates in P1 Contract 6.
- C-009 → policy reference versus policy definition in P1 Contract 7.
- C-010 → `LLMGenerationCandidate` lifecycle in P1 Contract 8.
- C-011 → LPH candidate assessment versus FDM authoritative assessment/evidence in P1 Contract 9.

## C-005 authority rule

The canonical error chain is:

```text
Observation → Evidence → Assessment
        ↓
ErrorObservationCandidate (optional)
        ↓
FDM validation / acceptance
        ↓
ErrorObservation (authoritative)
        ↓
CLM interpretation
        ↓
SDT summary
        ↓
APE reinforcement / reassessment
```

`ErrorObservation` is historical evidence-linked domain state. LLM/LPH candidates, feedback, recurrence counters and SDT summaries cannot replace it. Recurrence remains a derived signal governed by a future approved policy.

## LPH architectural role

LPH is a bounded control/validation harness. APE remains the pedagogical decision authority; FDM remains the domain/invariant enforcement boundary; CLM defines learning-state semantics; SDT represents derived learner state; the LLM remains a replaceable probabilistic capability.

For C-005, LPH may classify candidate errors and structure linguistic evidence, but cannot create authoritative `ErrorObservation` state without the governed evidence/assessment/FDM acceptance path.

## Current gate

**GATE A: IN PROGRESS — NOT READY FOR APPROVAL.**

Before LPH v1.0 or SRA:

1. integrate P1 contracts into PAD/CLM/FDM/APE/LPH/SDT source specifications;
2. reconcile remaining missing governance/AI artifacts;
3. add automated checks for normative contracts;
4. verify CI against the exact resulting HEAD;
5. run the mandatory independent secondary audit for P1 architecture/governance;
6. record human approval;
7. only then promote applicable documents toward v1.0.

This index does not silently resolve unresolved technical choices. Pending items remain pending until an approved specification or ADR provides evidence and a decision.
