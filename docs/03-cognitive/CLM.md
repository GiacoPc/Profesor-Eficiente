# Cognitive Learning Model (CLM)

**Document ID:** CLM
**Version:** 0.1-draft
**Status:** PROPOSED / NOT YET APPROVED
**Scope:** Cognitive/learning-state model for Profesor-Eficiente
**Implementation status:** NONE — specification only

## 0. Governance status

CLM formalizes the learner-learning model from zero. It defines the semantics of learning state and evidence required by the pedagogical engine; it does not choose a database, ML model, numerical mastery algorithm, or Android implementation.

Unknown information remains `UNKNOWN`. Proposed formalizations are not decisions until approved.

## 1. Purpose

CLM defines how the system represents, updates, and reasons about learning progress without allowing a generative model to become the authoritative learner-state owner.

CLM is concerned with **learning state**, not merely application/session state.

## 2. Core concepts

The model distinguishes:

```text
Observation
   ↓
Evidence
   ↓
Assessment
   ↓
Learning-state interpretation
   ↓
Learner state / SDT
   ↓
Pedagogical decision by APE
```

A generated explanation or LLM opinion is not automatically an authoritative learning event.

## 3. Student Digital Twin relationship

The Student Digital Twin (SDT) is the intended runtime representation of the learner's relevant state.

CLM defines the **semantics** of that state; FDM defines its formal domain representation; APE consumes it to select pedagogical action.

CLM does not require the SDT to be a literal AI-generated clone of the learner. It is a governed, evidence-backed state representation.

## 4. Learning-state dimensions

CLM proposes the following dimensions:

### 4.1 Curriculum position

- current level/band;
- current unit/lesson;
- objective/competency targets;
- prerequisite status;
- progression eligibility.

### 4.2 Competency state

For each competency, the system may maintain:

- evidence history;
- current mastery estimate/state;
- confidence or evidence sufficiency;
- active weaknesses;
- recurring error patterns;
- reinforcement requirement;
- last meaningful assessment;
- temporal stability of performance.

### 4.3 Error state

An error is not simply text displayed to the learner. It is an evidence-linked learning event that can affect future pedagogy.

Conceptual categories include:

- grammar;
- lexical;
- phonetic/phonological;
- pronunciation;
- prosody;
- discourse/communicative;
- comprehension/production where applicable.

### 4.4 Strategy state

The learner may have evidence regarding which activity forms are currently useful or difficult, including:

- retrieval practice;
- shadowing;
- chunking;
- communicative practice;
- corrective repetition;
- delayed reassessment.

This does not mean the system should infer psychological traits without evidence.

### 4.5 Pace/adherence state

Session pace, repetition load, and adherence may be represented only when they have a justified pedagogical purpose. They must not become arbitrary behavioral surveillance.

## 5. Evidence model

Every authoritative state update should be traceable to evidence.

Conceptual evidence object:

```yaml
evidence_id: <stable-id>
learner_id: <stable-id>
session_id: <stable-id>
lesson_id: <stable-id>
competency_id: <stable-id>
source_type: <text|speech|comprehension|assessment|other>
observed_at: <timestamp>
raw_reference: <local-data-reference>
assessment_status: <accepted|rejected|uncertain|insufficient>
assessment_reference: <assessment-id>
```

This is conceptual and not the final persistence schema.

## 6. Observation versus interpretation

CLM requires strict separation between:

- **Observed:** directly captured data;
- **Assessed:** interpretation produced by an assessment component;
- **Inferred:** a derived learning-state interpretation;
- **Verified:** supported by the project's evidence standard;
- **Unknown:** insufficient evidence.

This follows the project's evidence-integrity principle.

## 7. Mastery representation

CLM does not define a single universal scalar as the authoritative definition of mastery.

A competency may require multiple evidence dimensions. Therefore the model supports a structured mastery state such as:

```text
NOT_ASSESSED
INSUFFICIENT_EVIDENCE
DEVELOPING
NEAR_MASTERY
MASTERED
REASSESSMENT_REQUIRED
```

These labels are `PROPOSED`; exact state names and transition rules require approval.

## 8. Mastery evidence

Mastery must be based on explicit evidence appropriate to the competency.

Conceptual relationship:

```text
Competency
   + target criterion
   + required evidence
   + observed performance
   + assessment result
   + policy
   → mastery evidence
```

A single conversational success may be insufficient when the competency requires stability, transfer, or multiple modalities.

Exact evidence counts, thresholds, confidence requirements, and temporal windows are `PENDING/TBD`.

## 9. Learning event model

CLM proposes these conceptual event classes:

- `LESSON_STARTED`;
- `ACTIVITY_STARTED`;
- `RESPONSE_OBSERVED`;
- `ASSESSMENT_COMPLETED`;
- `ERROR_OBSERVED`;
- `FEEDBACK_DELIVERED`;
- `REINFORCEMENT_ASSIGNED`;
- `REASSESSMENT_COMPLETED`;
- `MASTERY_EVIDENCE_UPDATED`;
- `PROGRESSION_ELIGIBILITY_UPDATED`.

Events should be immutable evidence records where feasible. Derived learner state can then be recomputed or repaired from authoritative history subject to the persistence architecture.

## 10. Error recurrence

Recurring errors are pedagogically important because they indicate a need for targeted reinforcement.

A recurrence metric must not be defined as a simple raw count without considering:

- exposure opportunities;
- evidence quality;
- temporal spacing;
- competency context;
- whether the target was explicitly practiced;
- uncertainty of the assessment.

Exact recurrence formula is `TBD`.

## 11. Forgetting and retention

The project intends to reinforce weaknesses until adequate mastery and should use learning-science-informed mechanisms.

CLM therefore reserves a retention dimension, but deliberately does not invent a mathematical forgetting curve, half-life, decay coefficient, or spacing algorithm.

Candidate mechanisms may include spaced retrieval and delayed reassessment, but their parameters require pedagogical validation and evidence.

## 12. Reinforcement state

A competency may enter reinforcement when evidence indicates insufficient mastery or a recurring weakness.

Conceptual flow:

```text
Insufficient / unstable evidence
          ↓
Reinforcement need
          ↓
APE selects intervention
          ↓
Practice
          ↓
New evidence
          ↓
Reassessment
```

Reinforcement should be targeted to the weakest relevant competency rather than globally restarting a lesson.

## 13. Transfer and generalization

Where a competency is intended to be communicative, mastery should eventually be evaluated beyond the exact surface form practiced.

The precise transfer criteria are `PENDING` and must be defined per competency/curriculum contract.

## 14. Cognitive techniques

### 14.1 Chunking

Learning units may be represented as meaningful reusable chunks. The learner should be able to recognize and produce them in context where the curriculum requires it.

### 14.2 Shadowing

Shadowing produces speech evidence that may contribute to pronunciation, phonology, timing, and prosody assessment. The speech pipeline must determine what can actually be measured.

### 14.3 Kaizen-style progression

The system should favor measurable incremental improvement and feedback loops without lowering mastery requirements.

These mechanisms are pedagogical directions; their exact scheduling and scoring remain `PENDING`.

## 15. Learner-state update policy

A proposed authoritative update pipeline is:

```text
Input
 ↓
Observation
 ↓
Evidence validation
 ↓
Assessment
 ↓
Evidence classification
 ↓
CLM state update
 ↓
SDT projection
 ↓
APE decision
```

The LLM can participate in observation interpretation or candidate feedback but cannot directly commit an authoritative learner-state mutation.

## 16. Uncertainty and insufficient evidence

CLM must support uncertainty explicitly.

If an assessment cannot distinguish between competing interpretations, the state must remain uncertain/insufficient rather than forcing a binary pass/fail conclusion.

This is especially important for:

- noisy speech;
- ambiguous learner answers;
- weak acoustic evidence;
- uncertain semantic interpretation;
- insufficient sample size.

## 17. Session versus longitudinal state

CLM distinguishes:

### Session state

Temporary information needed to run the current interaction.

### Longitudinal learning state

Evidence and derived state intended to influence future lessons.

Session context must not automatically become durable learner memory.

## 18. Memory boundaries

The model distinguishes at least:

- curriculum memory: governed external knowledge;
- session context: ephemeral interaction state;
- learner evidence: durable local evidence;
- learner derived state: computed learning interpretation;
- pedagogical history: decisions/interventions relevant to learning.

Exact persistence and retention policies are `PENDING`.

## 19. Adaptation signals

APE may use CLM-derived signals such as:

- mastery status;
- active error clusters;
- recurrence;
- recent performance;
- evidence sufficiency;
- reinforcement need;
- progression eligibility.

APE should not infer unsupported personal or psychological characteristics merely because they might improve personalization.

## 20. CLM invariants

The following are proposed normative invariants:

1. Authoritative learner state must be evidence-linked.
2. Observations and interpretations must remain distinguishable.
3. Uncertain assessments must not silently become verified mastery.
4. LLM output is not authoritative learner state.
5. Historical evidence must not be silently overwritten by generated text.
6. Mastery is competency-specific and policy-governed.
7. Reinforcement is triggered by evidence, not arbitrary repetition.
8. Learning-state transitions must be testable and attributable.
9. Session context must not automatically become longitudinal memory.
10. Privacy-sensitive learner data must remain within explicit data contracts.

## 21. Required reconciliation dependencies

CLM must be reconciled with:

- PAD: pedagogical objectives, competency model, mastery and reinforcement;
- FDM: entity/event representation and invariants;
- APE: decision inputs/outputs and state-transition authority;
- LPH: linguistic evidence, error taxonomy and assessment boundaries;
- data architecture: persistence, encryption, deletion and recovery.

## 22. Open decisions

- exact SDT schema;
- exact mastery state machine;
- mastery thresholds;
- confidence/evidence sufficiency policy;
- forgetting/retention model;
- spacing algorithm;
- recurrence calculation;
- transfer criteria;
- learner strategy inference policy;
- persistence representation;
- privacy/retention values.

## 23. Acceptance criteria for CLM v1.0

CLM cannot become `APPROVED` until:

- PAD competency/mastery requirements are reconciled;
- FDM entities and events are formally mapped;
- APE input/output contracts are defined;
- SDT is formally specified;
- mastery and uncertainty semantics are testable;
- evidence provenance is testable;
- privacy/data contracts are reconciled;
- required pedagogical validation is completed;
- independent review is completed for the applicable risk class.

## 24. Status

**PROPOSED / NOT YET APPROVED.**

CLM v0.1 establishes the learning-state semantics without inventing numerical mastery, forgetting, or retention algorithms.
