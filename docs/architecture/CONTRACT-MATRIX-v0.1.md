# Contract Matrix — PAD / CLM / FDM / APE / LPH

**Version:** 0.1
**Status:** PROPOSED / REQUIRES RESOLUTION
**Purpose:** Convert conceptual boundaries into implementation-preventing contracts without inventing unresolved decisions.

## 1. Authority contracts

| Contract | Producer | Consumer | Authoritative? | Required rule |
|---|---|---|---|---|
| CurriculumContext | Governed curriculum | PAD/APE/LPH | YES | Runtime generation cannot mutate it. |
| LearnerEvidence | Evidence pipeline/FDM | CLM/APE | YES after acceptance policy | Must contain provenance and assessment status. |
| LearnerState/SDT | CLM/FDM projection | APE | YES | Must be versioned; no direct LLM mutation. |
| MasteryPolicy | Governed policy | CLM/FDM/APE | YES | Thresholds/criteria are policy data, not LLM decisions. |
| ProgressionEligibility | FDM/mastery policy | APE | YES | Mandatory prerequisites and mastery gates must pass. |
| PedagogicalDecision | APE | LPH/FDM/execution layer | YES as decision record | Structured, versioned, traceable, policy-bound. |
| LinguisticTaskContract | APE/LPH | LLM Gateway | CONTROL CONTRACT | Specifies target, constraints, evidence needs and output schema. |
| GenerationCandidate | LLM Gateway | LPH/FDM | NO | Candidate only until validation/acceptance. |
| LinguisticAssessment | LPH/bounded assessment component | FDM/CLM | Candidate evidence | Must preserve uncertainty and provenance. |

## 2. Canonical data flow

```text
Governed Curriculum
        |
        v
Current Lesson/Objective
        |
        +--------------------+
        |                    |
        v                    v
   Learner State         Domain Rules
        |                    |
        +---------+----------+
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
                  v
          LPH validation
                  |
          +-------+-------+
          |               |
        reject           accept
          |               |
          v               v
       fallback       controlled delivery
                          |
                          v
                      observation
                          |
                          v
                       evidence
                          |
                          v
                      assessment
                          |
                          v
                    CLM / SDT update
                          |
                          v
                    mastery policy
                          |
                          v
                 progression eligibility
                          |
                          v
                         APE
```

## 3. Contract requirements

### CM-01 — No direct LLM authority

The LLM Gateway may return candidates only. It cannot invoke authoritative progression/mastery/state mutation commands.

### CM-02 — Evidence provenance

Every authoritative learning-state mutation must reference accepted evidence, applicable assessment, policy version and state version where relevant.

### CM-03 — Policy reference versus policy definition

APE and LPH may reference an approved policy; neither may invent or redefine its authoritative numerical content at runtime.

### CM-04 — State versioning

APE decisions must identify the learner-state version used to make the decision. Stale decisions must be rejected or explicitly reconciled by the domain layer.

### CM-05 — Candidate isolation

Generated content is not evidence merely because it was generated. Learner evidence begins with an observation of learner behavior/output or an explicitly defined assessment event.

### CM-06 — Uncertainty preservation

An uncertain assessment must remain uncertain/insufficient and cannot satisfy a mastery gate unless the approved policy explicitly defines how such evidence is handled.

### CM-07 — Progression gate

`PROGRESS` is executable only if all mandatory domain prerequisites and approved mastery/progression conditions are satisfied.

### CM-08 — Conflict handling

Conflicting authoritative inputs produce a controlled `CONFLICT` state; the system must not silently select a winner.

### CM-09 — Offline critical path

Curriculum access, authoritative learner state, prerequisite enforcement, mastery/progression gating and APE decision execution cannot require a remote service.

### CM-10 — Replaceability

The domain contracts cannot mention a concrete LLM model, tokenizer, inference runtime, vendor SDK or accelerator backend.

## 4. Contract objects that remain deliberately incomplete

The following require later approved specifications before implementation:

- exact curriculum schema;
- exact SDT schema;
- exact MasteryPolicy schema and thresholds;
- exact evidence acceptance policy;
- exact LinguisticTaskContract schema;
- exact GenerationCandidate schema;
- exact speech evidence schema;
- exact concurrency/version conflict policy;
- exact serialization/transport format;
- exact Rust/Kotlin ownership boundary.

## 5. Reconciliation decision

The conceptual interfaces are now sufficiently constrained to identify what SRA must not invent, but they are **not yet sufficiently complete for implementation** because the missing policy/schema contracts above are still unresolved.

**Status: PROPOSED / NOT READY FOR SRA.**
