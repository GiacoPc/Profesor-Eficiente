# Contract Matrix — PAD / CLM / FDM / APE / LPH

**Version:** 0.2
**Status:** PROPOSED / REQUIRES INTEGRATION + INDEPENDENT AUDIT
**Purpose:** Convert conceptual boundaries into explicit cross-document contracts without inventing unresolved decisions.

## 1. Authority contracts

| Contract | Producer | Consumer | Authority | Required rule |
|---|---|---|---|---|
| CurriculumContext | Governed curriculum | PAD/APE/LPH | YES | Runtime generation cannot mutate it. |
| LearnerEvidence | Evidence pipeline/FDM | CLM/SDT/APE | YES after acceptance policy | Provenance and assessment status required. |
| LearnerState/SDT | CLM/FDM projection | APE | YES as derived state | Versioned; no direct LLM mutation. |
| MasteryPolicy | Governed policy | CLM/FDM/APE | YES | Defines mastery; consumers reference it. |
| ProgressionEligibility | FDM/mastery policy | APE/SDT | YES | Mandatory prerequisites/mastery gates required. |
| PedagogicalDecision | APE | LPH/FDM/execution | YES as decision record | Structured, versioned, traceable, policy-bound. |
| LinguisticTaskContract | APE/LPH | LLM Gateway | CONTROL | Target, constraints, evidence needs, output schema. |
| GenerationCandidate | LLM Gateway | LPH/FDM | NO | Candidate until validation/acceptance. |
| LinguisticAssessmentCandidate | LPH/bounded assessment | FDM | NO | Candidate linguistic interpretation; uncertainty preserved. |
| Assessment | FDM/domain evaluation | CLM/SDT | YES as domain record | Evaluates accepted evidence against explicit criteria/policy. |
| ErrorObservation | FDM from accepted evidence | CLM/SDT/APE | YES as evidence-derived record | Canonical error term; historical record immutable. |

## 2. Canonical data flow

```text
Governed Curriculum
        |
        v
Current Lesson / Objective / Competency
        |
        +----------------------+
        |                      |
        v                      v
    SDT snapshot          Domain constraints
        |                      |
        +----------+-----------+
                   v
                  APE
                   |
                   v
         PedagogicalDecision
                   |
                   v
                  LPH
                   |
          LinguisticTaskContract
                   |
                   v
              LLM Gateway
                   |
                   v
         GenerationCandidate
                   |
             LPH validation
              /           \
           reject         pass
             |              |
          fallback     controlled delivery
                            |
                            v
                    learner observation
                            |
                            v
                         evidence
                            |
                     validation/acceptance
                            |
                            v
                       assessment
                            |
                            +----> ErrorObservation
                            |
                            v
                     CLM learning-state
                            |
                            v
                      SDT projection N+1
                            |
                            v
                     MasteryPolicy
                            |
                            v
                 ProgressionEligibility
                            |
                            v
                           APE
```

## 3. P1 contract bindings

The complete proposed P1 resolutions are defined in:

`docs/architecture/P1-RESOLUTION-CONTRACTS-v0.1.md`

Bindings:

- C-001 authority hierarchy → Contract 1.
- C-002 objective ownership/cardinality → Contract 2.
- C-003 MasteryPolicy → Contract 3.
- C-004 SDT artifact → `docs/03-cognitive/SDT.md`.
- C-005 ErrorObservation lifecycle → Contract 5.
- C-006 speech/evidence pipeline → Contract 4.
- C-007/C-008 progression eligibility and `PROGRESS` gates → Contract 6.
- C-009 policy reference boundary → Contract 7.
- C-010 generation candidate lifecycle → Contract 8.
- C-011 linguistic assessment ownership → Contract 9.

## 4. Normative cross-layer rules

### CM-01 — No direct LLM authority

The LLM Gateway may return candidates only. It cannot invoke authoritative progression/mastery/state mutation commands.

### CM-02 — Evidence provenance

Every authoritative learning-state mutation must reference accepted evidence, applicable assessment/policy and the relevant state version where required.

### CM-03 — Policy reference versus policy definition

APE and LPH may reference an approved `MasteryPolicy`; neither may redefine its authoritative criteria at runtime.

### CM-04 — State versioning

APE decisions identify the learner-state version used. Stale decisions must be rejected or explicitly revalidated by the domain layer.

### CM-05 — Candidate isolation

Generated content is not learner evidence merely because it was generated. Evidence begins with an observation/assessment event governed by the evidence contract.

### CM-06 — Uncertainty preservation

Uncertain or insufficient evidence cannot silently satisfy a mastery gate.

### CM-07 — Progression gate

APE `PROGRESS` is executable only when `ProgressionEligibility == ELIGIBLE` and all hard preconditions in P1 Contract 6 pass.

### CM-08 — Conflict handling

Conflicting authoritative inputs produce `CONFLICT`; no layer may silently choose a winner.

### CM-09 — Offline critical path

Curriculum access, authoritative learner state, prerequisite enforcement, mastery/progression gating and APE decision execution cannot require a remote service.

### CM-10 — Replaceability

Domain contracts cannot mention a concrete LLM model, tokenizer, inference runtime, vendor SDK or accelerator backend.

### CM-11 — Objective ownership

Objectives are curriculum-authority entities. Competency/objective relationships are explicit many-to-many mappings where the curriculum defines them; criteria are not silently promoted to objectives.

### CM-12 — Error terminology

`ErrorObservation` is the canonical domain record. Human-facing `error` is descriptive terminology only.

### CM-13 — SDT projection

SDT is derived learner state, not raw evidence history. Every authoritative state element is provenance-linked or policy/curriculum referenced.

### CM-14 — Assessment boundary

LPH may produce linguistic assessment candidates; FDM owns authoritative assessment/evidence semantics and mutation.

## 5. Deliberately unresolved contracts

The following remain `PENDING/TBD` and must not be invented during SRA:

- exact curriculum schema/source/version;
- exact SDT serialization/persistence schema;
- exact MasteryPolicy thresholds and evidence counts;
- exact evidence acceptance policy;
- exact speech/acoustic/prosody assessment implementation;
- exact LinguisticTaskContract serialization;
- exact GenerationCandidate schema;
- exact concurrency/transaction model;
- exact persistence technology;
- exact Rust/Kotlin boundary;
- final local LLM/runtime/NPU strategy.

## 6. Gate

The matrix now defines the proposed P1 contracts and the SDT artifact exists. It is **not** an implementation authorization.

**Status: PROPOSED / NOT READY FOR SRA.**

Promotion requires source-spec integration, automated checks, independent secondary audit, and human approval.
