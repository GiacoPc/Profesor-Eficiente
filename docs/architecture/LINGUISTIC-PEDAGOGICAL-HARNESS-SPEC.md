# Linguistic & Pedagogical Harness (LPH) — Specification

**Document ID:** LPH-SPEC
**Version:** 0.1-draft
**Status:** PROPOSED / NOT YET APPROVED
**Branch:** `architecture/lph-spec-v1.0`
**Depends on:** PAD, CLM, FDM, APE direction, PGKI governance, Architecture Bible
**Implementation status:** NONE — specification only

> This document formalizes the architectural direction previously established for Professor Eficiente: pedagogical authority and critical linguistic control must remain outside the concrete LLM. The LLM is a replaceable generative capability behind an explicit adapter boundary. This specification is intentionally implementation-neutral and does not select a final model, runtime, STT, TTS, NPU backend, database, or performance target.

## 1. Purpose

Define a stable, testable, model-independent boundary between Professor Eficiente's pedagogical/linguistic control plane and probabilistic generative models.

The LPH exists to ensure that changing the local LLM does not require redesigning the pedagogical state machine, mastery policy, student model, curriculum representation, or linguistic validation contracts.

## 2. Non-goals

The LPH is **not**:

- a replacement LLM;
- a new large neural network;
- a claim that deterministic rules can solve all speech, pronunciation, prosody, or language understanding problems;
- the final SRA;
- a final selection of Gemma, Qwen, or another model;
- a final selection of inference runtime or NPU backend;
- a substitute for empirical validation.

Where machine-learning components are objectively useful (for example speech recognition or pronunciation assessment), they remain bounded components with explicit contracts and evidence requirements.

## 3. Core architectural invariant

**The LLM must not be the sovereign authority for pedagogical progression or mastery.**

The LLM may generate, explain, reformulate, converse, and propose candidate linguistic responses. It must not unilaterally:

- declare a lesson mastered;
- advance the learner to the next lesson;
- rewrite curriculum objectives;
- override prerequisite constraints;
- alter the learner's authoritative progress state;
- redefine assessment thresholds;
- bypass safety or governance gates.

Those decisions belong to governed application components and explicit policies.

## 4. High-level model

```text
                    PROFESSOR EFICIENTE
                           |
                           v
              +--------------------------+
              | LINGUISTIC & PEDAGOGICAL |
              | HARNESS (LPH)            |
              +------------+-------------+
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
        APE               FDM              CLM
   pedagogical       domain/linguistic   cognitive model
    authority           knowledge
          |                |                |
          +----------------+----------------+
                           |
                           v
                    Student Digital Twin
                           |
                           v
                    Mastery / Progression
                           |
                           v
                    LLM Abstraction Layer
                           |
              +------------+-------------+
              |            |             |
              v            v             v
           Model A      Model B       Future Model
              |            |             |
              +------------+-------------+
                           |
                           v
                    Candidate Generation
                           |
                           v
                     LPH Validation
                           |
                           v
                         User
```

The diagram is conceptual. Concrete component placement belongs to SRA.

## 5. Control-plane vs generation-plane

### 5.1 Control plane — authoritative

The control plane contains state and rules that determine what the system is allowed to teach, assess, record, reinforce, and advance.

Candidate components:

- APE — pedagogical orchestration and decision authority;
- curriculum/lesson state machine;
- FDM-backed linguistic and curriculum knowledge;
- CLM-backed learning strategy state;
- Student Digital Twin (SDT);
- error taxonomy and persistence;
- mastery engine;
- prerequisite and progression policy;
- validation and constraint engine;
- governance/evidence hooks.

### 5.2 Generation plane — non-authoritative

The generation plane contains probabilistic capabilities such as:

- conversational generation;
- explanations;
- controlled examples;
- reformulation;
- dialogue continuation;
- candidate feedback wording.

The generation plane operates under an explicit contract supplied by the control plane.

## 6. LLM abstraction boundary

The application must communicate with an LLM through a stable adapter contract rather than model-specific APIs leaking through the domain layer.

Conceptual contract:

```text
LLM Gateway
  input:
    system constraints
    pedagogical task
    retrieved knowledge
    learner context
    linguistic constraints
    output schema

  output:
    candidate response
    structured metadata where supported
    uncertainty / refusal information where available
```

The exact API and serialization are implementation decisions for SRA.

### 6.1 Model replaceability requirement

No domain or pedagogical component may depend directly on:

- a specific model name;
- a specific tokenizer implementation;
- a specific inference engine;
- a specific vendor SDK;
- a specific accelerator backend.

These belong behind adapters.

## 7. RAG boundary

RAG is a retrieval mechanism, not the final authority.

```text
Structured Knowledge
      |
      v
Retriever
      |
      v
Evidence / Context Pack
      |
      v
APE / LPH policy
      |
      v
LLM generation
      |
      v
LPH validation
```

The local JSON curriculum/MCER representation is treated as governed structured knowledge. Retrieval may expose relevant content; it does not authorize the LLM to modify curriculum truth.

## 8. Linguistic control domains

The LPH must provide explicit interfaces or validation boundaries for at least:

1. grammar;
2. vocabulary/lexical constraints;
3. phonology and phonetics;
4. pronunciation;
5. prosody;
6. discourse/communicative function;
7. comprehension/production task constraints;
8. error classification.

The LPH must distinguish **authoritative linguistic facts** from **model-generated pedagogical language**.

## 9. Speech pipeline boundary

Speech processing is treated as a pipeline of independently testable components rather than as an implicit LLM capability.

```text
Microphone
   |
   v
Audio Capture
   |
   v
VAD / segmentation
   |
   v
STT / acoustic analysis
   |
   +----> transcript evidence
   |
   +----> pronunciation evidence
   |
   +----> prosody evidence
   |
   v
Linguistic Assessment
   |
   v
Error Taxonomy
   |
   v
SDT + Mastery Engine
```

The exact models and DSP/ML implementations remain unresolved until evidence-driven SRA design and hardware benchmarking.

## 10. Error model

Errors must be represented as structured learner evidence rather than only natural-language text.

Conceptual record:

```yaml
error_id: <stable-id>
lesson_id: <lesson-id>
competency_id: <competency-id>
category: <grammar|lexical|phonetic|pronunciation|prosody|discourse>
observed_form: <evidence>
target_form: <target>
severity: <policy-defined>
recurrence_count: <integer>
last_observed: <timestamp>
status: <active|improving|mastered>
source_evidence: <evidence-id>
```

This is a domain contract, not a final persistence schema.

## 11. Mastery and progression

The LPH must separate:

```text
observation
   -> assessment
   -> mastery evidence
   -> mastery decision
   -> progression decision
```

A single LLM statement is insufficient evidence of mastery.

Progression must be determined by an explicit policy using measurable evidence appropriate to the competency. Thresholds are intentionally **TBD** until pedagogical and empirical validation establishes them.

## 12. Pedagogical orchestration

APE remains the director of the pedagogical process.

The LPH must permit APE to specify:

- current lesson and objective;
- learner prerequisites;
- current weaknesses;
- exercise mode;
- interaction constraints;
- correction policy;
- reinforcement policy;
- mastery requirements;
- allowable next states.

The LLM receives the task as a constrained generation problem rather than as an unconstrained lesson planner.

## 13. Lesson state machine

Conceptual state flow:

```text
LOCKED
  |
  v
AVAILABLE
  |
  v
IN_PROGRESS
  |
  +----> REINFORCEMENT <----+
  |                          |
  v                          |
ASSESSMENT ------------------+
  |
  v
MASTERED
  |
  v
ELIGIBLE_FOR_NEXT
```

The exact states and transitions belong to the formal domain model and SRA. The LLM cannot create an unauthorized transition.

## 14. Deterministic vs probabilistic responsibilities

### Prefer deterministic mechanisms for:

- state transitions;
- prerequisites;
- thresholds once formally defined;
- schema validation;
- curriculum identifiers;
- evidence IDs;
- persistence integrity;
- policy enforcement;
- reproducible calculations;
- governance gates.

### Permit ML/LLM mechanisms for:

- natural-language generation;
- semantic interpretation where deterministic methods are insufficient;
- conversational adaptation;
- speech recognition/assessment where validated models are required;
- candidate feedback generation.

Every probabilistic component must have an explicit uncertainty and failure boundary.

## 15. Failure containment

If the LLM:

- produces malformed output;
- violates requested constraints;
- hallucinates a linguistic fact;
- attempts an unauthorized state transition;
- gives an unsupported mastery judgment;
- conflicts with retrieved authoritative knowledge;

the LPH must treat the output as a failed candidate, not authoritative state.

Conceptually:

```text
LLM output
   |
   v
Schema / policy / knowledge validation
   |
   +---- FAIL ----> reject / repair / regenerate / fallback
   |
   +---- PASS ----> controlled delivery
```

The exact recovery policy is TBD and must be tested.

## 16. Offline-first constraint

The LPH must operate without network access after required local assets have been provisioned.

No pedagogically critical decision may require a remote LLM or cloud service.

Any optional remote capability, if introduced later, must be an explicitly bounded enhancement and must not become a hidden dependency.

## 17. Performance and resource boundary

The LPH architecture must permit independent resource budgeting for:

- CPU;
- GPU;
- NPU;
- RAM;
- storage;
- audio buffers;
- model memory;
- caches.

No specific budget is declared by this specification. Those values require device-specific measurements on the target hardware before being promoted to normative requirements.

Caching and prefetching must be policy-driven and bounded. They must never compromise learner state integrity or cause unbounded memory growth.

## 18. Security and privacy boundary

Learner audio, transcripts, errors, weaknesses, progress, and assessment evidence are local learner data.

The LPH must expose explicit boundaries for:

- storage;
- retention;
- deletion;
- encryption where required;
- model access;
- diagnostic logging.

No sensitive learner state should be implicitly embedded into prompts without a defined data contract.

## 19. Testability requirements

Every authoritative component must be independently testable.

Minimum future test categories:

- lesson state transition tests;
- mastery policy tests;
- prerequisite tests;
- error classification tests;
- RAG retrieval contract tests;
- LLM adapter contract tests;
- malformed-output tests;
- hallucination containment tests;
- offline tests;
- resource-budget tests;
- concurrency tests;
- audio pipeline tests;
- persistence/recovery tests.

The LPH specification is complete only when its normative contracts can be mapped to executable tests.

## 20. Evidence requirements

No claim that an implementation uses or optimally exploits CPU/GPU/NPU/RAM may be treated as verified without device-specific evidence.

No claim that a model is pedagogically superior may be treated as verified without an explicit evaluation protocol and evidence.

No claim that a pronunciation/prosody assessment is reliable may be treated as verified without validation evidence.

This preserves the project's Claim -> Evidence -> Verification governance model.

## 21. Open decisions intentionally deferred

The following remain unresolved and must not be guessed:

- final local LLM;
- quantization level;
- inference runtime;
- NPU execution strategy;
- GPU delegation strategy;
- STT implementation;
- TTS implementation;
- pronunciation-assessment model;
- prosody-assessment method;
- database/persistence technology;
- exact mastery thresholds;
- exact CEFR curriculum data model;
- performance/thermal budgets;
- concurrency model;
- final Rust/Kotlin FFI boundary.

These become evidence-backed ADRs/specifications before implementation.

## 22. Acceptance criteria for LPH v1.0

The specification may not be promoted from draft to approved v1.0 until all of the following exist:

1. PAD/CLM/FDM/APE interfaces are reconciled against this contract;
2. the LLM adapter contract is formally defined;
3. authoritative vs generative responsibilities are testable;
4. mastery/progression authority is represented outside the LLM;
5. speech assessment boundaries are defined;
6. failure containment behavior is specified;
7. offline guarantees are testable;
8. resource-budget interfaces are defined;
9. required ADRs are created for unresolved technology choices;
10. independent architectural review is completed;
11. all normative claims have evidence or are explicitly marked TBD/PROPOSED.

## 23. Architectural consequence

Once approved, the LPH becomes an upstream contract for SRA. SRA must implement the boundaries defined here rather than redefining them implicitly during implementation.

The intended dependency direction is:

```text
Requirements
    |
    v
PAD / CLM / FDM / APE
    |
    v
LPH Specification
    |
    v
SRA
    |
    v
Implementation
    |
    v
Tests + Evidence
```

## 24. Current status

**PROPOSED / DRAFT.**

This document establishes architecture; it does not authorize implementation and does not close unresolved technology decisions.
