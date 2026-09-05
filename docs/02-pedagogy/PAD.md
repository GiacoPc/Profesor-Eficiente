# Pedagogical Architecture Document (PAD)

**Document ID:** PAD
**Version:** 0.1-draft
**Status:** PROPOSED / NOT YET APPROVED
**Scope:** Pedagogical architecture for Profesor-Eficiente
**Implementation status:** NONE — specification only

## 0. Governance status

This document formalizes the pedagogical architecture from zero using only requirements and architectural directions already established in the governed project baseline. It does **not** convert unresolved details into decisions.

Normative status vocabulary used here:

- `DECIDED`: explicitly established project requirement/direction.
- `PROPOSED`: formalization proposed by this document and requiring approval.
- `PENDING`: necessary decision not yet made.
- `UNKNOWN`: insufficient evidence or definition.
- `TBD`: value to be established later by evidence and/or pedagogical validation.

Source constraints include the Project Constitution and Decision Ledger. The Constitution requires approved pedagogical requirements not to be silently weakened, unknown information to remain unknown, and AI proposals not to become decisions automatically.

## 1. Purpose

PAD defines **how Profesor-Eficiente teaches** independently of any concrete LLM, Android implementation, inference runtime, database, STT engine, or TTS engine.

The pedagogical architecture must transform a learner's current evidenced state into an explicit instructional objective, activity, feedback/reinforcement policy, assessment requirement, and progression decision.

## 2. Product pedagogical contract

### 2.1 Established requirements

The product is intended to:

1. teach American English;
2. support a Latin-neutral Spanish-speaking learner;
3. begin from absolute zero;
4. use the MCER/CEFR as the governing proficiency framework;
5. represent the governed curriculum locally, including structured JSON or an equivalent governed representation;
6. operate offline-first after required local assets are provisioned;
7. provide spoken instruction and interactive practice;
8. correct relevant grammar, phonetics, pronunciation, rules, and prosody errors;
9. retain learner errors and weaknesses locally as evidence for reinforcement;
10. prevent progression when explicit mastery requirements have not been satisfied;
11. integrate shadowing, chunking, and Kaizen-style incremental learning as pedagogical mechanisms;
12. keep pedagogical authority outside the concrete LLM.

Items 1–12 are treated as inherited project requirements/directions, not newly invented requirements.

### 2.2 Explicitly unresolved

The following are not defined by PAD v0.1:

- exact CEFR curriculum source/version;
- exact lesson count;
- exact mastery thresholds;
- exact number of attempts required;
- exact forgetting/retention equations;
- exact spacing schedule;
- exact pronunciation/prosody scoring algorithm;
- exact STT/TTS implementation;
- exact remediation durations;
- exact assessment weighting.

## 3. Pedagogical authority model

The pedagogical control chain is:

```text
Curriculum authority
       |
       v
Learner evidenced state (CLM / SDT)
       |
       v
APE — pedagogical decision authority
       |
       v
Instructional task specification
       |
       +----> LPH linguistic/pedagogical constraint & validation boundary
       |
       v
LLM / other generation capability
       |
       v
Learner interaction
       |
       v
Evidence collection
       |
       +----> CLM / SDT update
       |
       +----> mastery assessment
       |
       v
APE next decision
```

The LLM may generate language and interaction content but does not become the authority for curriculum, mastery, or progression.

### 3.1 P1 C-001 authority contract

For cross-document reconciliation, the authority hierarchy is normative at the contract level:

```text
Curriculum Authority
        ↓
CLM learning-state semantics + FDM domain invariants
        ↓
SDT learner-state projection
        ↓
APE pedagogical decision authority
        ↓
LPH linguistic/interaction constraint + validation boundary
        ↓
LLM / bounded generation capability
        ↓
Learner interaction
        ↓
Evidence
```

The hierarchy above does not grant any lower layer authority over a higher layer. In particular:

- LPH may constrain and validate linguistic/interaction processing but cannot authorize pedagogical progression or mutate authoritative learner state.
- The LLM is a bounded generation/interpretation capability and cannot redefine curriculum, mastery, prerequisites, or progression.
- APE owns the pedagogical decision, but does not become the source of curriculum truth, learning-state semantics, or FDM domain invariants.
- SDT represents governed learner state and does not independently decide pedagogical actions.
- Evidence produced after learner interaction must enter the governed evidence/assessment pipeline before it can affect authoritative learning state.

This section integrates **P1 Contract C-001** from `docs/architecture/P1-RESOLUTION-CONTRACTS-v0.1.md`. The contract remains `PROPOSED / REQUIRES APPROVAL`; this integration does not approve PAD or the contract.

## 4. Curriculum architecture

### 4.1 Curriculum authority

The curriculum is a governed structured artifact. The runtime may retrieve relevant curriculum content, but retrieval does not authorize mutation of curriculum truth.

### 4.2 Curriculum hierarchy

PAD proposes the following logical hierarchy, subject to reconciliation with the formal domain model:

```text
Curriculum
  └── Level / proficiency band
       └── Unit / module
            └── Lesson
                 └── Competency
                      └── Objective
                           └── Activity / assessment criterion
```

This hierarchy is a **PROPOSED formalization** until FDM and the curriculum schema are approved.

### 4.3 Lesson contract

Every executable lesson should expose, at minimum:

- stable lesson identifier;
- level/proficiency context;
- prerequisite identifiers;
- learning objectives;
- target competencies;
- target linguistic material;
- permitted activity types;
- required evidence;
- mastery criteria reference;
- remediation/reinforcement policy reference;
- progression destination(s).

Exact fields belong to FDM/curriculum schema and are `PENDING`.

## 5. Competency model

The pedagogical system must distinguish at least the following linguistic domains because the product explicitly requires correction across them:

- grammar;
- vocabulary/lexicon;
- phonology/phonetics;
- pronunciation;
- prosody;
- communicative/discourse function;
- comprehension;
- production.

A competency may have multiple observable evidence types. No single modality is assumed to be sufficient for every competency.

The exact competency taxonomy and CEFR mapping are `PENDING`.

## 6. Learning cycle

The canonical pedagogical cycle is:

```text
ORIENT
  ↓
MODEL / EXPLAIN
  ↓
GUIDED PRACTICE
  ↓
INDEPENDENT / COMMUNICATIVE PRACTICE
  ↓
OBSERVE
  ↓
ASSESS
  ↓
FEEDBACK
  ↓
REINFORCE or CONSOLIDATE
  ↓
MASTERY DECISION
  ↓
PROGRESS or REMEDIATE
```

This is a proposed control cycle; specific lesson methodology must be defined per curriculum/competency.

## 7. Error correction architecture

Correction is evidence-driven, not merely conversational.

```text
Learner output
   ↓
Observation evidence
   ↓
Assessment
   ↓
Error / strength classification
   ↓
Feedback
   ↓
Targeted practice
   ↓
Reassessment
```

Feedback may be generated naturally by the LLM, but the classification and pedagogical consequence must remain governed by the application policies.

The system must avoid converting uncertain model interpretations into authoritative learner-state changes without an evidence policy.

## 8. Mastery and progression

### 8.1 Principle

The learner must not advance solely because a generative model says that the learner is ready.

### 8.2 Required separation

```text
Evidence
  → Assessment
  → Mastery evidence
  → Mastery decision
  → Progression eligibility
  → APE decision
```

### 8.3 Mastery policy

The exact threshold, aggregation method, confidence policy, minimum evidence, temporal stability, and reassessment policy are `PENDING/TBD`.

PAD therefore defines the architectural requirement, not the numerical answer.

## 9. Reinforcement architecture

When a competency is insufficiently mastered, the system should select reinforcement based on the learner's evidenced weakness rather than simply repeat the same activity.

Potential reinforcement dimensions:

- repetition with controlled variation;
- retrieval practice;
- chunking;
- shadowing;
- targeted pronunciation practice;
- focused grammar practice;
- lexical retrieval;
- communicative reuse;
- delayed reassessment.

The selection policy is `PENDING` and belongs to APE/CLM policy contracts.

## 10. Shadowing, chunking and Kaizen

### Shadowing

A learner repeats target speech with timing and pronunciation/prosodic constraints. It is a pedagogical activity whose scoring pipeline is external to the LLM.

### Chunking

Target language is represented and practiced in meaningful reusable units rather than requiring word-by-word generation/translation as the default learning primitive.

### Kaizen-style learning

The system should use small measurable improvements, frequent feedback, and controlled progression. This is a pedagogical principle, not permission to lower mastery standards.

Exact operationalization remains `PENDING`.

## 11. Adaptivity

Adaptation may modify:

- exercise selection;
- difficulty within permitted bounds;
- repetition;
- feedback depth;
- pacing;
- modality;
- reinforcement priority;
- conversational context.

Adaptation must not silently modify:

- curriculum authority;
- required competencies;
- prerequisite rules;
- approved mastery policy;
- learner's authoritative historical evidence.

APE is the intended authority for these adaptations.

## 12. Learner state relationship

PAD does not own the complete learner model. It defines what pedagogical decisions require from the learner state.

The Student Digital Twin (SDT) is the intended learner-state representation. CLM defines the learning-state semantics; FDM defines persistent/domain entities; APE consumes the resulting state for decisions.

Minimum pedagogically relevant state categories include:

- current curriculum position;
- competency mastery evidence;
- active weaknesses;
- recurring errors;
- recent performance;
- reinforcement needs;
- prerequisites satisfied/unsatisfied;
- interaction/pace information where pedagogically justified.

Exact schema is `PENDING`.

## 13. Assessment architecture

Assessment should be competency-specific and evidence-based.

Evidence can include, depending on competency:

- selected/typed responses;
- free text production;
- speech transcript;
- acoustic/prosodic evidence;
- pronunciation evidence;
- comprehension responses;
- task completion;
- repeated performance over time.

The system must preserve the distinction between:

- observed evidence;
- model interpretation;
- pedagogical judgment;
- authoritative mastery state.

## 14. LLM role

The LLM is a bounded capability for language generation/interpretation and conversation.

It may:

- explain a concept;
- produce controlled examples;
- conduct dialogue;
- reformulate feedback;
- interpret natural-language responses;
- propose candidate classifications.

It may not:

- rewrite the curriculum;
- redefine lesson objectives;
- change mastery thresholds;
- authorize progression;
- directly mutate authoritative learner state;
- override prerequisites;
- bypass governance or validation.

## 15. Offline-first pedagogical guarantee

Pedagogically critical operation must remain possible without network access after required assets are installed.

The curriculum, learner state, evidence required for core progression, and critical pedagogical policies must not depend on a remote service.

## 16. Determinism and uncertainty

Where a pedagogical decision has a rule-based answer, the system should use deterministic policy execution.

Probabilistic components may provide candidate evidence or language, but uncertainty must remain explicit and bounded.

If evidence is insufficient, the pedagogical system must prefer `INSUFFICIENT_EVIDENCE` / equivalent controlled states over fabricated certainty.

## 17. Privacy and learner data

Learner audio, transcripts, errors, weaknesses, progress, and assessment evidence are local learner data.

PAD requires explicit policies for collection, retention, deletion, access, and diagnostic exposure. Exact implementation is owned by the data/security architecture and is `PENDING`.

## 18. Pedagogical invariants

The following are proposed normative invariants for approval:

1. Curriculum authority is external to the LLM.
2. Mastery authority is external to the LLM.
3. Progression authority is external to the LLM.
4. Approved prerequisites cannot be bypassed by generated dialogue.
5. Uncertain evidence cannot be silently promoted to verified mastery.
6. Reinforcement must be traceable to an evidenced learning need.
7. Pedagogical adaptation may vary execution but may not silently weaken approved learning objectives.
8. Core pedagogical operation must remain offline-first.
9. Learner-state mutation must be attributable to evidence and policy.
10. All normative pedagogical rules must be testable.

## 19. Acceptance criteria for PAD v1.0

PAD cannot become `APPROVED` until:

- the exact curriculum authority/source is defined;
- CEFR/MCER mapping is formally represented;
- competency taxonomy is approved;
- lesson contract is reconciled with FDM;
- mastery evidence policy is reconciled with CLM and APE;
- reinforcement policy is defined sufficiently for deterministic testing;
- assessment/evidence semantics are reconciled with FDM;
- contradiction review is completed;
- traceability IDs are assigned;
- independent review is completed for the required risk class.

## 20. Status

**PROPOSED / NOT YET APPROVED.**

PAD v0.1 establishes the pedagogical architecture without inventing unresolved thresholds, curriculum sources, algorithms, or implementation technologies.
