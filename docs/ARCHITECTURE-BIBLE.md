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
- LPH-SPEC — **PROPOSED / DRAFT v0.3**, not approved.
- MasteryPolicy — **PROPOSED / DRAFT v0.1**, not approved.
- ErrorObservation Lifecycle — **PROPOSED / DRAFT v0.1**, at `docs/architecture/ERROR-OBSERVATION-LIFECYCLE-v0.1.md`.
- SDT Integration Matrix — **PROPOSED / v0.1**, at `docs/architecture/SDT-INTEGRATION-MATRIX-v0.1.md`.
- ErrorObservation Integration Matrix — **PROPOSED / v0.1**, at `docs/architecture/ERROR-OBSERVATION-INTEGRATION-MATRIX-v0.1.md`.
- Speech Evidence/Assessment Contract — **PROPOSED / DRAFT v0.1**, at `docs/architecture/SPEECH-EVIDENCE-ASSESSMENT-CONTRACT-v0.1.md`.
- Speech Evidence Integration Matrix — **PROPOSED / v0.1**, at `docs/architecture/SPEECH-EVIDENCE-INTEGRATION-MATRIX-v0.1.md`.
- Progression Eligibility Contract — **PROPOSED / DRAFT v0.1**, at `docs/architecture/PROGRESSION-ELIGIBILITY-CONTRACT-v0.1.md`.
- Progression Eligibility Integration Matrix — **PROPOSED / v0.1**, at `docs/architecture/PROGRESSION-ELIGIBILITY-INTEGRATION-MATRIX-v0.1.md`.
- Mastery Policy Reference Boundary Integration Matrix — **PROPOSED / DRAFT v0.1**, at `docs/architecture/MASTERY-POLICY-REFERENCE-BOUNDARY-INTEGRATION-MATRIX-v0.1.md`.
- LLMGenerationCandidate Lifecycle — **PROPOSED / DRAFT v0.1**, at `docs/architecture/LLM-GENERATION-CANDIDATE-LIFECYCLE-v0.1.md`.
- LLMGenerationCandidate Integration Matrix — **PROPOSED / v0.1**, at `docs/architecture/LLM-GENERATION-CANDIDATE-INTEGRATION-MATRIX-v0.1.md`.
- LinguisticAssessmentCandidate Ownership — **PROPOSED / DRAFT v0.1**, at `docs/architecture/LINGUISTIC-ASSESSMENT-CANDIDATE-OWNERSHIP-v0.1.md`.
- LinguisticAssessment Integration Matrix — **PROPOSED / v0.1**, at `docs/architecture/LINGUISTIC-ASSESSMENT-INTEGRATION-MATRIX-v0.1.md`.
- P1 reconciliation contracts — **PROPOSED / v0.1**, at `docs/architecture/P1-RESOLUTION-CONTRACTS-v0.1.md`.
- Contract Matrix — **PROPOSED / v0.2**, at `docs/architecture/CONTRACT-MATRIX-v0.1.md`.
- Contradiction Matrix — **PROPOSED / v0.8**, at `docs/architecture/CONTRADICTION-MATRIX-v0.1.md`.
- SRA — pending; must consume approved upstream contracts rather than redefine them during implementation.
- LLM/inference architecture — pending; expected artifact not found on inspected branch.
- RAG architecture — pending; expected artifact not found on inspected branch.
- Audio architecture — pending.
- Data architecture — pending.
- Benchmark plan — pending.

## Reconciliation state

Gate A remains **IN PROGRESS / NOT READY FOR APPROVAL**.

P1 findings C-001 through C-011 have explicit proposed contracts. They are **not yet closed at approval level** because contracts require complete source-spec integration, executable checks, independent audit and human approval.

### P1 resolution map

- C-001 → authority hierarchy in P1 Contract 1; integrated into PAD/LPH.
- C-002 → objective ownership/cardinality in P1 Contract 2; integrated into FDM/PAD.
- C-003 → explicit `MasteryPolicy` contract in P1 Contract 3; integrated into PAD/CLM/FDM/APE and existing LPH boundary.
- C-004 → SDT artifact `docs/03-cognitive/SDT.md` plus `SDT-INTEGRATION-MATRIX-v0.1.md`.
- C-005 → canonical `ErrorObservation` lifecycle in `ERROR-OBSERVATION-LIFECYCLE-v0.1.md` plus cross-document integration matrix. Source specifications already contain the relevant bounded responsibilities; final direct normative references remain part of the source-spec integration gate.
- C-006 → `SPEECH-EVIDENCE-ASSESSMENT-CONTRACT-v0.1.md` plus `SPEECH-EVIDENCE-INTEGRATION-MATRIX-v0.1.md`; authoritative sequence is speech artifact → bounded processing → validated evidence → assessment → MasteryPolicy/CLM → governed state → SDT → APE.
- C-007/C-008 → `ProgressionEligibility` and APE `PROGRESS` hard gates in P1 Contract 6, plus dedicated progression contract/integration matrix.
- C-009 → policy reference versus policy definition in P1 Contract 7 plus `MASTERY-POLICY-REFERENCE-BOUNDARY-INTEGRATION-MATRIX-v0.1.md`; APE, CLM, FDM and LPH source specifications explicitly preserve the boundary.
- C-010 → `LLMGenerationCandidate` lifecycle in P1 Contract 8 plus `LLM-GENERATION-CANDIDATE-LIFECYCLE-v0.1.md` and `LLM-GENERATION-CANDIDATE-INTEGRATION-MATRIX-v0.1.md`.
- C-011 → linguistic assessment ownership in P1 Contract 9 plus `LINGUISTIC-ASSESSMENT-CANDIDATE-OWNERSHIP-v0.1.md` and `LINGUISTIC-ASSESSMENT-INTEGRATION-MATRIX-v0.1.md`; LPH §9–§10 explicitly marks the candidate as non-authoritative and FDM remains the authoritative Evidence/Assessment boundary.

## C-009 mastery policy reference rule

The normative distinction is:

```text
Governed MasteryPolicy definition
        ↓
policy reference (stable id + version)
        ↓
consumer use / enforcement
```

APE, CLM, FDM, SDT and LPH may consume or preserve a policy reference and governed constraint/evidence references. They cannot create an authoritative local definition of thresholds, evidence requirements, aggregation, stability, transfer or uncertainty semantics.

If policy resolution is undefined, unavailable, stale, malformed, out of scope or conflicting, the system must enter controlled policy-resolution/insufficient-evidence/conflict handling. No hard-coded, inferred, conversational or LLM-generated replacement is authoritative.

Every authoritative mastery evaluation must retain the exact `mastery_policy_id` and `mastery_policy_version` used for reproducibility. A policy revision creates governed new versioning and does not silently rewrite historical decisions.

## C-010 generation candidate rule

The normative distinction is:

```text
LLMRequest
   ↓
LLMGenerationCandidate
   ↓
validation
   ├── REJECTED → discard / repair / regenerate
   └── ACCEPTED_FOR_USE → scoped controlled delivery

candidate ≠ evidence
candidate ≠ assessment
candidate ≠ mastery
candidate ≠ progression eligibility
candidate ≠ SDT state
```

Acceptance is scoped to the declared use. A candidate accepted for learner-facing wording is not automatically authorized for assessment use. If a candidate contributes to an assessment workflow, a separate governed evidence/assessment record and provenance path is required.

LLM-generated claims about learner error, mastery or readiness cannot directly mutate authoritative state. Repair/regeneration creates a new candidate identity and preserves lineage where applicable. Replacing or removing the LLM cannot alter authoritative domain gates, and LLM unavailability must remain a controlled capability failure rather than learner-state failure.

## C-011 linguistic assessment ownership rule

The normative distinction is:

```text
LPH linguistic processing
        ↓
LinguisticAssessmentCandidate
        ↓
validation + provenance
        ↓
FDM authoritative Evidence / Assessment
        ↓
CLM / SDT
        ↓
APE decision
```

`LinguisticAssessmentCandidate` is a non-authoritative proposed interpretation. `Evidence` is an accepted provenance-bearing domain record. `Assessment` is an authoritative evaluation of accepted evidence against the applicable target/criterion.

LPH may produce or validate candidate results across grammar, lexicon, phonology, pronunciation, prosody and discourse, but cannot directly create authoritative Evidence, Assessment, MasteryRecord, ErrorObservation or ProgressionEligibility. This remains true for candidates originating from an LLM, STT system, acoustic analyzer, pronunciation model or ensemble.

Structured output, syntax validation, model confidence or provider reputation does not grant domain authority. Candidate acceptance is a governed FDM operation; uncertainty and conflict remain explicit rather than being silently converted into learner failure or mastery.

## Current gate

**GATE A: IN PROGRESS — NOT READY FOR APPROVAL.**

Before LPH v1.0 or SRA:

1. integrate P1 contracts into PAD/CLM/FDM/APE/LPH/SDT source specifications;
2. reconcile remaining missing governance/AI artifacts;
3. add automated checks for normative contracts, including C-009 identity/version/scope/no-fallback behavior, C-010 candidate-authority/validation/isolation behavior, and C-011 candidate/evidence/assessment ownership and provenance behavior;
4. verify CI against the exact resulting HEAD;
5. run the mandatory independent secondary audit for P1 architecture/governance;
6. record human approval;
7. only then promote applicable documents toward v1.0.

This index does not silently resolve unresolved technical choices. Pending items remain pending until an approved specification or ADR provides evidence and a decision.
