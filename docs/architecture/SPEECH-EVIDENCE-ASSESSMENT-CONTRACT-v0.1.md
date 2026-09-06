# C-006 — Speech Evidence → Assessment Contract

**Version:** 0.1-draft  
**Status:** PROPOSED / REQUIRES APPROVAL  
**Scope:** Formal boundary for speech/audio evidence, assessment, mastery interpretation, SDT projection and APE decision-making.  
**Authority:** This contract reconciles C-006 only; it does not approve PAD, CLM, FDM, APE, LPH, SDT or SRA.

## 1. Problem addressed

Speech is a multi-stage evidence pipeline. Capture, speech-to-text, acoustic/prosodic measurement, pronunciation analysis, linguistic interpretation and pedagogical decision are distinct responsibilities.

C-006 exists because collapsing these stages can incorrectly make an STT engine, acoustic model, pronunciation scorer, LPH or LLM the authoritative owner of mastery or learner state.

## 2. Normative authority chain

```text
Learner speech
    ↓
Audio capture artifact
    ↓
Bounded speech processing
    ├─ transcript candidate
    ├─ acoustic/prosodic measurements
    └─ pronunciation/phonological candidate measures
    ↓
Speech Evidence Candidate(s)
    ↓
Evidence validation + provenance
    ↓
Authoritative Evidence
    ↓
Assessment against explicit criterion/target
    ↓
Accepted Assessment
    ↓
MasteryPolicy / CLM learning-state interpretation
    ├─ MasteryRecord where applicable
    ├─ ErrorObservation where applicable
    └─ other governed learning state
    ↓
SDT projection
    ↓
APE pedagogical decision
```

The direction is normative. A downstream component cannot bypass an earlier authoritative boundary merely because its output is probabilistically strong.

## 3. Speech processing roles

### 3.1 Audio capture

Owns acquisition and local reference to the learner's speech artifact under the audio/data contract.

It does not decide correctness, mastery or progression.

### 3.2 STT

Produces a transcript candidate and associated uncertainty/metadata.

STT output is an observation/processing result, not authoritative proof of what the learner intended or of linguistic correctness.

A transcript may be used as one evidence component and must retain provenance.

### 3.3 Acoustic/prosodic analysis

May produce measurable features such as timing, duration, intensity, pitch-related or other supported acoustic/prosodic measurements.

A measurement is not itself a pedagogical judgment. The project must not claim a dimension is measurable until the selected method has demonstrated adequate validity for the intended use.

### 3.4 Pronunciation/phonological analysis

May produce candidate segmental or phonological assessments where supported by evidence and the applicable evaluation contract.

It cannot independently establish mastery or progression.

### 3.5 LPH

LPH may combine linguistic representations, constrain interpretation, classify candidates and validate linguistic output.

LPH is not the authoritative owner of learner mastery, progression, or durable learner state.

### 3.6 LLM

The LLM may interpret structured evidence or generate candidate feedback/explanations.

It cannot convert its own interpretation directly into authoritative evidence, mastery, SDT state or progression.

## 4. Evidence taxonomy

The system must distinguish at least:

- `AudioArtifactReference` — reference to captured local audio;
- `TranscriptCandidate` — candidate transcription result;
- `AcousticMeasurementSet` — measured acoustic/prosodic features;
- `PronunciationAssessmentCandidate` — candidate pronunciation/phonological result;
- `LinguisticAssessmentCandidate` — non-authoritative linguistic interpretation;
- `SpeechEvidenceCandidate` — aggregate candidate evidence awaiting governed validation;
- `Evidence` — authoritative evidence record under FDM provenance rules;
- `Assessment` — evaluation of accepted evidence against an explicit target/criterion.

These are not interchangeable records.

## 5. Provenance requirements

Authoritative speech evidence must retain enough provenance to reconstruct what was evaluated, including where applicable:

```yaml
evidence_id: <stable-id>
learner_id: <stable-id>
session_id: <stable-id>
activity_id: <stable-id>
lesson_id: <stable-id>
competency_id: <stable-id-or-unknown>
source_type: speech
observed_at: <timestamp>
raw_audio_reference: <local-reference-or-omitted-by-policy>
processing_chain: [<component/version>]
input_references: [<artifact-or-candidate-id>]
uncertainty: <explicit-value-or-state>
assessment_reference: <assessment-id-or-null>
```

Exact persistence schema is `PENDING/TBD`.

## 6. Assessment boundary

Assessment evaluates accepted evidence against an explicit target, criterion or competency requirement.

Assessment must identify:

- the evidence evaluated;
- the criterion/target;
- the assessing component or policy;
- uncertainty or insufficiency;
- relevant model/component version where applicable;
- provenance sufficient for audit.

An assessment result is not automatically mastery. Mastery interpretation occurs only through the applicable governed `MasteryPolicy` and CLM semantics.

## 7. Multi-dimensional speech assessment

Speech performance may provide evidence for multiple dimensions, but each dimension must be assessed separately where its validity and curriculum relevance require it.

Conceptually:

```text
Speech
 ├─ lexical/grammatical evidence
 ├─ phonological evidence
 ├─ pronunciation evidence
 ├─ timing evidence
 ├─ prosodic evidence
 └─ discourse/communicative evidence
```

A failure or success in one dimension must not silently be copied into another dimension.

## 8. Uncertainty and ambiguity

If STT, acoustic analysis, pronunciation analysis or linguistic interpretation is uncertain, the uncertainty must survive into the evidence/assessment decision.

Examples:

- low-confidence transcript;
- overlapping plausible transcripts;
- noisy audio;
- unsupported acoustic inference;
- insufficient speech sample;
- disagreement between assessment components.

These conditions must produce `INSUFFICIENT_EVIDENCE`, `UNCERTAIN`, or `CONFLICT` as applicable rather than an invented binary judgment.

## 9. Mastery boundary

The authoritative mastery chain is:

```text
Speech evidence
      ↓
Accepted evidence
      ↓
Assessment
      ↓
Applicable MasteryPolicy(identity + version)
      ↓
Mastery evaluation
      ↓
MasteryRecord / learning-state update
```

No STT engine, acoustic model, pronunciation scorer, LPH component, LLM, UI or APE prompt may replace the governing policy with an ad-hoc threshold.

A missing, stale, undefined or conflicting policy blocks authoritative mastery interpretation.

## 10. SDT boundary

SDT receives a governed projection of authoritative learning state.

SDT must not treat a raw transcript, raw acoustic feature, candidate assessment, LLM opinion or unvalidated speech score as equivalent to authoritative longitudinal learner state.

A speech-derived SDT change must be traceable to the accepted evidence/assessment and applicable policy semantics.

## 11. APE boundary

APE consumes governed learner state and progression/mastery results to decide what pedagogical action should occur next.

APE may choose actions such as reinforcement, reassessment, practice or progression only within its existing authority contract and hard domain gates.

APE does not reinterpret raw speech signals to manufacture evidence.

## 12. Offline critical path

The critical path from learner speech to required core pedagogical decisions must not require a remote service.

Any optional remote enhancement, if ever introduced, must remain outside the authoritative offline path and cannot become a hidden dependency for mastery/progression.

Exact runtime topology remains `PENDING` until SRA.

## 13. Failure and fallback semantics

A speech component failure must not be converted into learner failure.

Examples:

```text
Audio unavailable
    → no speech evidence
    → controlled retry / alternate permitted activity

STT unavailable or too uncertain
    → transcript evidence insufficient
    → do not invent transcript

Acoustic analysis unavailable
    → corresponding dimension unassessed
    → do not infer failure

Assessment components conflict
    → CONFLICT
    → governed resolution/reassessment

No valid evidence
    → INSUFFICIENT_EVIDENCE
    → no mastery claim
```

Exact user-facing recovery behavior is a PAD/SRA decision and remains `PENDING`.

## 14. Required invariants

**C006-I01 — Provenance:** authoritative speech evidence references its source artifact/observation and processing provenance.

**C006-I02 — Component non-authority:** STT, acoustic, pronunciation, LPH and LLM components cannot independently mutate authoritative mastery, progression or SDT state.

**C006-I03 — Evidence before mastery:** no authoritative mastery evaluation occurs without accepted evidence and an explicit applicable MasteryPolicy.

**C006-I04 — Dimension separation:** evidence for one speech dimension cannot silently establish another dimension.

**C006-I05 — Uncertainty preservation:** uncertainty, insufficiency and conflict remain explicit.

**C006-I06 — Failure neutrality:** processing failure does not become learner failure.

**C006-I07 — Offline critical path:** required core speech-driven pedagogical decisions do not depend on remote services.

**C006-I08 — Version traceability:** assessment-relevant component/model versions are attributable where they affect interpretation.

**C006-I09 — State projection:** SDT changes are derived from authoritative evidence/state, not raw model output.

**C006-I10 — Pedagogical separation:** APE consumes governed assessment/state and does not manufacture evidence from raw speech signals.

## 15. Acceptance tests

- **C006-T01:** No authoritative evidence exists without source/provenance.
- **C006-T02:** A transcript candidate alone cannot establish mastery.
- **C006-T03:** A high-confidence STT result cannot bypass assessment/policy.
- **C006-T04:** Acoustic/prosodic measurements cannot directly establish progression.
- **C006-T05:** Conflicting speech assessments remain `CONFLICT` until governed resolution.
- **C006-T06:** Insufficient/noisy audio cannot be recorded as learner failure.
- **C006-T07:** LLM speech interpretation cannot directly mutate SDT/mastery.
- **C006-T08:** APE cannot create evidence merely to justify reinforcement or progression.
- **C006-T09:** A speech-derived mastery decision references the exact applicable MasteryPolicy identity/version.
- **C006-T10:** A remote service outage cannot invalidate the offline authoritative path.
- **C006-T11:** A dimension not supported by the selected measurement method remains unassessed.
- **C006-T12:** Reassessment produces new evidence/assessment records rather than rewriting historical evidence.

## 16. Open decisions

- final speech evidence schema;
- final audio retention/reference policy;
- STT engine and confidence semantics;
- acoustic/prosodic feature set and validity evidence;
- pronunciation/phonological assessment method;
- cross-component calibration and disagreement policy;
- assessment confidence semantics;
- exact MasteryPolicy integration for speech competencies;
- exact SDT speech-derived fields;
- runtime/offline topology;
- performance/thermal budgets;
- privacy/security controls for audio.

## 17. Status

**PROPOSED / REQUIRES APPROVAL.**

C-006 is formally specified at contract level. This artifact does not claim that speech-model validity, final schemas, runtime architecture, or mastery thresholds have been empirically verified.
