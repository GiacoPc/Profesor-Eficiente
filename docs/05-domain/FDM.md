# Formal Domain Model (FDM)

**Document ID:** FDM
**Version:** 0.1-draft
**Status:** PROPOSED / NOT YET APPROVED
**Scope:** Formal domain semantics and invariants for Profesor-Eficiente
**Implementation status:** NONE — specification only

## 0. Governance status

FDM formalizes the domain boundaries required by the project without selecting persistence technology, Android framework details, Rust implementation details, or a specific LLM.

This document deliberately distinguishes proposed domain contracts from approved project directions. Unresolved information remains `PENDING`, `UNKNOWN`, or `TBD`.

## 1. Purpose

FDM defines the authoritative domain vocabulary, entities, relationships, states, events, invariants, and command/result boundaries needed for PAD, CLM, APE, LPH, and later SRA to interoperate without inventing semantics during implementation.

## 2. Domain authority principles

1. Curriculum truth is governed data, not LLM-generated content.
2. Learner evidence is distinct from learner-state interpretation.
3. Mastery is a governed domain decision.
4. Progression is a governed domain decision.
5. LLM outputs are non-authoritative candidates.
6. Domain invariants must be enforceable independently of probabilistic generation.
7. Every authoritative mutation must be attributable to a command/policy and evidence where applicable.

## 3. Bounded contexts

FDM proposes these bounded contexts:

```text
+-------------------+
| Curriculum        |
+-------------------+
          |
          v
+-------------------+       +-------------------+
| Learning          |<----->| Student / SDT     |
+-------------------+       +-------------------+
          ^                           ^
          |                           |
+-------------------+       +-------------------+
| Evaluation        |------>| Evidence          |
+-------------------+       +-------------------+
          ^
          |
+-------------------+
| Conversation/Audio|
+-------------------+
          ^
          |
+-------------------+
| AI / Generation   |
+-------------------+
          |
          v
+-------------------+
| Pedagogical APE   |
+-------------------+
```

These are architectural boundaries, not necessarily separate processes or packages.

## 4. Core domain entities

### 4.1 Curriculum

Represents governed educational content and structure.

Conceptual attributes:

- `curriculum_id`;
- `version`;
- `authority_reference`;
- `levels`;
- `units`;
- `lessons`;
- `competencies`;
- `objectives`;
- `prerequisites`.

### 4.2 Lesson

Represents a governed instructional unit.

Conceptual attributes:

- `lesson_id`;
- `curriculum_id`;
- `level_id`;
- `objective_ids`;
- `competency_ids`;
- `prerequisite_ids`;
- `activity_policy_reference`;
- `mastery_policy_reference`.

### 4.3 Competency

Represents an assessable learning capability.

Conceptual attributes:

- `competency_id`;
- `domain`;
- `objective_reference`;
- `target_criteria`;
- `required_evidence_types`.

Exact taxonomy is `PENDING`.

### 4.4 Objective

Represents an intended learning outcome associated with curriculum authority.

An objective is immutable at runtime by the LLM or ordinary dialogue generation.

### 4.5 Prerequisite

Represents a condition required before a lesson/competency can become eligible.

The exact prerequisite expression language is `TBD`.

### 4.6 Learner

Represents the domain identity of the learner.

### 4.7 Student Digital Twin (SDT)

Represents the governed derived learner-learning state used for pedagogical adaptation.

SDT is not the raw event log. It is a projection/representation derived from authoritative evidence and policies.

### 4.8 Evidence

Represents an observation or assessment input that can support a learning-state update.

Minimum conceptual properties:

- stable `evidence_id`;
- learner reference;
- competency/lesson context where known;
- source type;
- timestamp;
- local data reference;
- assessment/provenance status.

### 4.9 Assessment

Represents an evaluation of evidence against an explicit target/criterion.

Assessment may be probabilistic, but its result must be represented separately from authoritative mastery state.

### 4.10 ErrorObservation

Represents a structured learner error derived from evidence.

Conceptual fields:

- `error_id`;
- `evidence_id`;
- `competency_id`;
- category;
- observed form;
- target form;
- severity;
- recurrence context;
- status.

### 4.11 MasteryRecord

Represents the governed mastery state/evidence for a competency.

It must reference the policy and evidence supporting the state.

### 4.12 ProgressionEligibility

Represents whether domain prerequisites and mastery requirements permit progression.

Eligibility is not identical to the APE's final pedagogical action; APE may choose reinforcement even when progression is technically allowed.

### 4.13 Activity

Represents a pedagogical interaction/exercise instance governed by an activity policy.

### 4.14 Session

Represents a bounded learner interaction context.

Session state is not automatically longitudinal learner memory.

### 4.15 PedagogicalDecision

Represents an APE decision selecting the next controlled pedagogical action.

It should reference the input state snapshot/version and applicable policy.

### 4.16 LLMGenerationCandidate

Represents non-authoritative generated content proposed by an LLM.

It may be accepted, rejected, repaired, or regenerated after validation.

## 5. Identity and provenance

All authoritative entities/events require stable identifiers suitable for traceability.

Proposed identifier classes:

```text
curriculum_id
lesson_id
competency_id
objective_id
learner_id
session_id
activity_id
evidence_id
assessment_id
error_id
mastery_id
decision_id
generation_id
```

Exact ID encoding is `TBD`.

## 6. Entity relationships

Conceptual cardinalities:

```text
Curriculum 1 ── * Level
Level      1 ── * Unit
Unit       1 ── * Lesson
Lesson     * ── * Competency
Competency 1 ── * Objective/criteria
Lesson     * ── * Prerequisite
Learner    1 ── 1 SDT
Learner    1 ── * Session
Session    1 ── * Activity
Activity   1 ── * Evidence
Evidence   * ── * Assessment
Evidence   1 ── * ErrorObservation
Competency 1 ── * MasteryRecord
APE        1 ── * PedagogicalDecision
Generation * ── 1 PedagogicalDecision/context
```

These cardinalities are proposed and require reconciliation with implementation and persistence requirements.

## 7. State machines

### 7.1 Lesson state

Proposed states:

```text
LOCKED → AVAILABLE → IN_PROGRESS → ASSESSMENT
                         ↑              |
                         |              v
                  REINFORCEMENT ←  MASTERY_EVALUATION
                                        |
                                        v
                                  MASTERED / ELIGIBLE
```

Exact state set and transition conditions are `PENDING`.

### 7.2 Evidence state

Proposed:

```text
CAPTURED → VALIDATED → ASSESSED → ACCEPTED
                         |            |
                         +→ UNCERTAIN  +→ REJECTED
```

### 7.3 Generation candidate state

```text
REQUESTED → GENERATED → VALIDATING
                         |       |
                         |       +→ REJECTED
                         v
                      ACCEPTED
```

Repair/regeneration may create a new candidate rather than mutating historical evidence.

## 8. Commands and authoritative mutations

Proposed command boundary:

```text
StartLesson
SubmitResponse
RecordEvidence
AssessEvidence
RecordError
RequestReinforcement
ReassessCompetency
EvaluateMastery
EvaluateProgressionEligibility
RequestPedagogicalDecision
AcceptGenerationCandidate
```

A command may fail if a domain invariant is violated.

The exact command API is for SRA and remains `PENDING`.

## 9. Domain events

Proposed events:

- `LessonStarted`;
- `ActivityStarted`;
- `ResponseObserved`;
- `EvidenceRecorded`;
- `AssessmentCompleted`;
- `ErrorObserved`;
- `FeedbackDelivered`;
- `ReinforcementAssigned`;
- `MasteryEvidenceUpdated`;
- `MasteryStateChanged`;
- `ProgressionEligibilityChanged`;
- `PedagogicalDecisionRecorded`;
- `GenerationCandidateRejected`;
- `GenerationCandidateAccepted`.

Events should preserve provenance and relevant policy/version references.

## 10. Critical invariants

The following are proposed normative domain invariants.

### FDM-I01 — Curriculum immutability at runtime

LLM output or learner interaction cannot mutate authoritative curriculum objectives, prerequisites, or competency definitions.

### FDM-I02 — Evidence provenance

An authoritative learner-state mutation must have a traceable cause. For learning judgments, that cause must include relevant evidence and assessment/policy provenance.

### FDM-I03 — LLM non-authority

An LLM cannot directly transition authoritative lesson/mastery/progression state.

### FDM-I04 — Prerequisite enforcement

A lesson cannot become progression-eligible when mandatory prerequisites are unsatisfied.

### FDM-I05 — Mastery policy enforcement

A mastery state cannot be set by bypassing the currently applicable mastery policy.

### FDM-I06 — Uncertainty preservation

Insufficient or uncertain evidence cannot silently become verified evidence.

### FDM-I07 — Candidate isolation

Generated content remains non-authoritative until it passes applicable validation and acceptance policy.

### FDM-I08 — Historical integrity

Authoritative historical evidence cannot be rewritten merely to make a generated answer or current assessment appear consistent.

### FDM-I09 — Offline critical path

Critical domain decisions required for core learning/progression cannot require a remote service.

### FDM-I10 — Version traceability

Authoritative decisions should identify the relevant curriculum/policy/domain versions where needed for reproducibility.

## 11. APE boundary

APE is an application/pedagogical authority operating over FDM entities and CLM-derived state.

APE may request domain commands, but FDM/domain rules must still reject invalid mutations.

This creates defense in depth:

```text
APE policy decision
      ↓
Domain command
      ↓
FDM invariant enforcement
      ↓
Authoritative mutation
```

## 12. LPH boundary

LPH consumes and produces structured linguistic/evidence contracts around FDM entities.

LPH may:

- validate linguistic generation candidates;
- structure linguistic evidence;
- classify candidate errors;
- enforce output constraints.

LPH may not bypass FDM invariants or directly authorize progression.

## 13. LLM boundary

The LLM is represented as a capability provider, not a domain authority.

Conceptual interface:

```text
LLMRequest
  - task
  - constraints
  - context/evidence references
  - output schema

LLMResult
  - candidate content
  - structured fields where supported
  - uncertainty/error information
  - provider/model metadata
```

The exact schema belongs to LPH/SRA.

## 14. Audio and speech evidence

Speech-related domain data should enter FDM as evidence from bounded processing components.

The domain must distinguish:

- captured audio reference;
- transcript result;
- acoustic/prosodic measurements;
- pronunciation assessment;
- linguistic interpretation;
- pedagogical consequence.

No single speech component is assumed authoritative for all dimensions.

## 15. Persistence independence

FDM does not select Room, SQLite, Realm, custom Rust storage, or another technology.

The domain model must remain serializable/persistable through an adapter without changing domain semantics.

## 16. Deterministic core

The following should be deterministic wherever their rules are formally defined:

- identifiers;
- state transitions;
- prerequisite evaluation;
- policy application;
- evidence provenance;
- progression eligibility;
- invariant enforcement;
- event ordering/versioning where required.

## 17. Concurrency and consistency

Concurrent learner interactions must not cause:

- lost evidence;
- duplicate authoritative transitions;
- invalid progression;
- stale SDT updates overwriting newer state.

The exact consistency model, transaction boundaries, conflict policy, and event ordering are `PENDING`.

## 18. Security/privacy domain boundary

FDM must allow learner-sensitive data to be handled explicitly and separately from generic diagnostics.

No domain contract should require raw learner audio or sensitive learner data to be copied into logs by default.

Encryption, deletion, retention, and access-control details belong to the data/security architecture.

## 19. Testability

Every invariant must map to automated tests before implementation is considered complete.

Minimum categories:

- invariant tests;
- state-machine tests;
- property-based tests where useful;
- serialization compatibility tests;
- event/provenance tests;
- concurrency tests;
- offline-path tests;
- LLM candidate isolation tests.

## 20. Open decisions

- exact bounded-context/package boundaries;
- final entity schemas;
- identifier encoding;
- state names and transitions;
- event schema/versioning;
- transaction/consistency model;
- persistence mapping;
- exact curriculum schema;
- exact mastery policy representation;
- audio evidence schema;
- final LPH/FDM interface serialization;
- Rust/Kotlin boundary.

## 21. Acceptance criteria for FDM v1.0

FDM cannot become `APPROVED` until:

- PAD concepts map to explicit domain entities/contracts;
- CLM state/evidence semantics map to entities/events;
- APE commands/results are defined;
- LPH interfaces are reconciled;
- invariants are reviewed and testable;
- concurrency/persistence semantics are specified sufficiently for SRA;
- traceability is complete;
- independent architectural review is completed.

## 22. Status

**PROPOSED / NOT YET APPROVED.**

FDM v0.1 establishes a formal domain vocabulary and safety boundary without locking implementation technology.
