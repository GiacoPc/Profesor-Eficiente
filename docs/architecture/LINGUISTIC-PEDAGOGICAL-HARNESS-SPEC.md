# Linguistic & Pedagogical Harness (LPH) — Specification

**Document ID:** LPH-SPEC
**Version:** 0.2-draft
**Status:** PROPOSED / NOT YET APPROVED
**Branch:** `architecture/pad-clm-fdm-ape-v1.0`
**Depends on:** PAD, CLM, FDM, APE, SDT, PGKI governance, Architecture Bible, P1 reconciliation contracts
**Implementation status:** NONE — specification only

> This document formalizes a model-independent boundary between pedagogical/linguistic control and probabilistic generation. It does not authorize implementation or promote unresolved policies to decisions.

## 1. Purpose

Define a stable, testable, model-independent boundary between Profesor-Eficiente's pedagogical/linguistic control plane and probabilistic generative models.

## 2. Non-goals

The LPH is not a replacement LLM, a new large neural network, a final SRA, or an authority for curriculum, mastery, progression, or authoritative learner state.

## 3. Normative authority boundary

The following ownership is normative for this draft:

```text
Curriculum authority
       ↓
CLM learning-state semantics + FDM domain invariants
       ↓
SDT learner-state projection
       ↓
APE pedagogical decision authority
       ↓
LPH linguistic/interaction constraint + validation boundary
       ↓
LLM Gateway / generation capability
       ↓
Learner interaction
       ↓
Evidence → Assessment → CLM/SDT update
```

LPH is **not** superior to APE, CLM or FDM. LPH may constrain, validate and structure linguistic processing, but it cannot:

- authorize progression;
- define or override mastery policy;
- mutate authoritative learner state;
- override curriculum or prerequisite authority;
- convert an LLM candidate directly into authoritative evidence/state.

APE remains the pedagogical decision authority; FDM remains the domain/invariant enforcement boundary.

## 4. High-level model

```text
             APE / FDM / CLM / SDT
                     |
                     v
                    LPH
          constraint + validation
                     |
                     v
               LLM Gateway
                     |
          Generation Candidate
                     |
              LPH validation
                /        \
             reject       pass
                |           |
             repair     controlled delivery
                            |
                            v
                         learner
                            |
                            v
                         evidence
                            |
                       assessment
                            |
                         CLM/SDT
```

The diagram is conceptual; concrete component placement belongs to SRA.

## 5. Control plane vs generation plane

### 5.1 Control plane — authoritative

Contains governed state and rules determining what the system is allowed to teach, assess, record, reinforce and advance:

- APE;
- curriculum/lesson state machine;
- FDM-backed domain knowledge/invariants;
- CLM learning-state semantics;
- SDT;
- mastery/progression policy contracts;
- evidence validation;
- governance/evidence hooks.

### 5.2 Generation plane — non-authoritative

Contains probabilistic capabilities such as dialogue generation, explanations, reformulations, controlled examples and candidate feedback wording.

## 6. LLM abstraction boundary

The application communicates with an LLM through a stable adapter contract. Model-specific APIs remain behind the gateway.

Conceptual input:

```text
system constraints
pedagogical task
retrieved knowledge
bounded learner context
linguistic constraints
output schema
```

Conceptual output:

```text
GenerationCandidate
  content
  structured metadata where supported
  uncertainty/refusal information where available
  provider/model metadata
```

A `GenerationCandidate` is non-authoritative until it passes applicable validation; passing validation does not grant it authority over curriculum, mastery or progression.

## 7. RAG boundary

RAG is retrieval, not authority.

```text
Governed structured knowledge
          ↓
       Retriever
          ↓
   Context / evidence pack
          ↓
      APE / LPH constraints
          ↓
      LLM generation
          ↓
     LPH validation
```

Retrieval cannot authorize curriculum mutation.

## 8. Linguistic control domains

LPH provides explicit interfaces/validation boundaries for grammar, vocabulary, phonology/phonetics, pronunciation, prosody, discourse/communicative function, comprehension/production constraints, and error classification.

LPH must distinguish authoritative linguistic facts from model-generated pedagogical language.

## 9. Speech pipeline boundary

```text
Microphone
   ↓
Audio Capture
   ↓
VAD / segmentation
   ↓
STT / acoustic analysis
   ├── transcript evidence
   ├── pronunciation evidence
   └── prosody evidence
            ↓
  LinguisticAssessmentCandidate
            ↓
      evidence contract
            ↓
     FDM authoritative record
            ↓
        CLM / SDT
```

LPH may produce a linguistic assessment candidate. FDM owns authoritative evidence/assessment semantics and mutation.

## 10. Error model

The canonical domain record is `ErrorObservation`.

LPH may classify a candidate error, but an accepted authoritative error record must follow the evidence contract. `recurrence_count` is not authoritative by itself and must be policy-derived.

Conceptual candidate:

```yaml
error_observation_candidate:
  competency_id: <id>
  category: <grammar|lexical|phonetic|pronunciation|prosody|discourse>
  observed_form: <evidence>
  target_form: <target>
  uncertainty: <explicit>
  source_evidence: <evidence-id-or-candidate-reference>
```

## 11. Mastery and progression boundary

The authoritative sequence is:

```text
Observation
   ↓
Evidence
   ↓
Assessment
   ↓
MasteryPolicy
   ↓
MasteryRecord
   ↓
ProgressionEligibility
   ↓
APE action
```

LPH and APE **reference** the applicable `MasteryPolicy` by identifier/version. They do not redefine its thresholds or evidence requirements.

`ProgressionEligibility.status == ELIGIBLE` is a necessary condition for APE `PROGRESS`, subject to all other hard preconditions. LPH cannot create or override eligibility.

## 12. Pedagogical orchestration boundary

APE remains the director of the pedagogical process.

APE may supply LPH with:

- current lesson/objective/competency references;
- learner prerequisites;
- evidenced weaknesses;
- exercise mode;
- interaction/correction constraints;
- reinforcement policy reference;
- mastery-policy reference/version;
- required evidence;
- allowable next states.

LPH translates these into a bounded linguistic task contract. It cannot alter the governing values.

## 13. Lesson state machine

Conceptual flow:

```text
LOCKED → AVAILABLE → IN_PROGRESS → ASSESSMENT
                              ↓
                         REINFORCEMENT
                              ↓
                         REASSESSMENT
                              ↓
                           MASTERY
                              ↓
                    PROGRESSION ELIGIBILITY
```

Exact states and transitions belong to FDM/SRA. LPH cannot create unauthorized transitions.

## 14. Deterministic vs probabilistic responsibilities

Prefer deterministic mechanisms for state transitions, prerequisites, approved thresholds, schema validation, evidence identifiers, persistence integrity, policy enforcement, reproducible calculations and governance gates.

Permit ML/LLM for natural-language generation, bounded semantic interpretation, speech recognition/assessment where validated, and candidate feedback generation.

Every probabilistic component requires an explicit uncertainty/failure boundary.

## 15. Failure containment

Malformed, unsupported, hallucinated, constraint-violating or unauthorized LLM output remains a failed/non-authoritative candidate.

```text
LLM output
   ↓
Schema / policy / knowledge validation
   ├── FAIL → reject / repair / regenerate / fallback
   └── PASS → controlled delivery
```

No validation pass grants authority to bypass FDM/APE policy boundaries.

## 16. Offline-first constraint

LPH must operate without network access after required local assets are provisioned. No pedagogically critical decision may require a remote service.

## 17. Performance/resource boundary

Independent budgets for CPU, GPU, NPU, RAM, storage, audio buffers, model memory and caches are required later. No numerical budget is asserted without measurement.

## 18. Security/privacy boundary

Learner audio, transcripts, errors, weaknesses, progress and assessment evidence are local learner data. LPH must not implicitly embed sensitive learner state into prompts without a defined data contract.

## 19. Testability

Future tests must cover lesson transitions, mastery/progression gates, error classification, RAG contracts, LLM adapter contracts, malformed output, hallucination containment, offline operation, resource budgets, concurrency, audio pipeline and persistence/recovery.

## 20. Evidence requirements

No implementation, performance, model-superiority, pronunciation-reliability or hardware-utilization claim is verified without appropriate evidence.

## 21. Open decisions

Still unresolved: final LLM, quantization, inference runtime, NPU/GPU strategy, STT/TTS, pronunciation/prosody assessment, persistence, exact mastery thresholds, CEFR data model, resource budgets, concurrency model, and Rust/Kotlin boundary.

## 22. Acceptance criteria for LPH v1.0

LPH cannot be promoted until PAD/CLM/FDM/APE/SDT interfaces are reconciled, authoritative/generative boundaries are testable, speech boundaries are defined, failure containment is tested, offline guarantees are testable, required ADRs exist, and independent architectural review is complete.

## 23. Status

**PROPOSED / DRAFT v0.2.**

This revision integrates P1 authority/policy boundaries without promoting unresolved thresholds or implementation choices to decisions.
