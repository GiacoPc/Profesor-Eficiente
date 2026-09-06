# Architecture Bible

## Baseline purpose

This document indexes the governed architecture. Detailed specifications are added only after reconciliation and approval.

## Cross-P1 reconciliation status

C-001 through C-011 have now been compositionally reconciled at contract level. The dedicated transversal artifact is `docs/architecture/CROSS-P1-RECONCILIATION-v0.1.md`.

The resulting authority chain is:

```text
Curriculum / governed policy
          ↓
accepted Evidence → Assessment
          ↓
MasteryPolicy → MasteryRecord
          ↓
ProgressionEligibility
          ↓
APE → PedagogicalDecision
```

LLM, speech, linguistic-analysis and other capability outputs remain candidates until governed acceptance. SDT remains a projection. No lateral authority path is intentionally defined.

**Important:** this is a contract-level reconciliation result, not executable proof and not approval.

## Current architectural principles

- Offline-first.
- Pedagogical authority outside the LLM.
- APE as intended pedagogical orchestrator.
- SDT as governed learner-state representation/projection.
- FDM as domain and invariant boundary.
- Local governed RAG.
- LLM replaceability.
- Rust + Kotlin separation, with exact boundaries pending specification.
- Evidence-driven CPU/RAM/NPU/GPU optimization.
- Task-routed AI context.
- LPH as proposed model-independent linguistic constraint/validation boundary; it is not superior to APE or FDM.

## Specifications / status

- PRD — NOT FOUND on inspected branch at expected path; requirements remain governed by baseline artifacts until formalized.
- PAD — PROPOSED / DRAFT v0.1, not approved.
- CLM — PROPOSED / DRAFT v0.1, not approved.
- APE — PROPOSED / DRAFT v0.1, not approved.
- FDM — PROPOSED / DRAFT v0.1, not approved.
- SDT — PROPOSED / DRAFT v0.1, not approved.
- LPH-SPEC — PROPOSED / DRAFT v0.3, not approved.
- MasteryPolicy — PROPOSED / DRAFT v0.1, not approved.
- ErrorObservation Lifecycle — PROPOSED / DRAFT v0.1.
- Speech Evidence/Assessment Contract — PROPOSED / DRAFT v0.1.
- Progression Eligibility Contract — PROPOSED / DRAFT v0.1.
- Mastery Policy Reference Boundary Matrix — PROPOSED / DRAFT v0.1.
- LLMGenerationCandidate Lifecycle — PROPOSED / DRAFT v0.1.
- LinguisticAssessmentCandidate Ownership — PROPOSED / DRAFT v0.1.
- Cross-P1 Reconciliation — PROPOSED / DRAFT v0.1.
- P1 reconciliation contracts — PROPOSED / v0.1.
- Contract Matrix — PROPOSED / DRAFT v0.3.
- Contradiction Matrix — PROPOSED / DRAFT v0.8.
- SRA — pending; must consume approved upstream contracts rather than redefine them during implementation.

## Gate status

**GATE A: IN PROGRESS — NOT READY FOR APPROVAL.**

Cross-P1 has passed conceptual/contract reconciliation only. Before P1 approval or LPH v1.0/SRA:

1. integrate normative references across PAD/CLM/FDM/APE/SDT/LPH;
2. resolve remaining schema/cardinality/command/event decisions;
3. implement automated invariant and compatibility checks;
4. verify CI against the exact resulting HEAD;
5. run mandatory independent secondary AI audit for P1 architecture/governance;
6. record human approval;
7. only then promote applicable specifications toward v1.0.

No implementation authorization is granted by this document.
