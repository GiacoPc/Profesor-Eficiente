# LinguisticAssessmentCandidate — Ownership & Acceptance Boundary

**Document ID:** C011-LINGUISTIC-ASSESSMENT-OWNERSHIP
**Version:** 0.1-draft
**Status:** PROPOSED / REQUIRES APPROVAL
**Scope:** LPH linguistic assessment candidates versus FDM authoritative assessment/evidence ownership

## 1. Purpose

Define an explicit, testable boundary between probabilistic/bounded linguistic assessment performed or structured by LPH and authoritative evidence/assessment records owned by FDM.

The objective is to prevent a linguistic model output, speech analyzer, LLM interpretation, or LPH classification from becoming authoritative merely because it is structured, scored, or expressed with confidence.

## 2. Canonical terminology

- **LinguisticAssessmentCandidate**: non-authoritative proposed interpretation of learner linguistic performance produced by LPH or an approved linguistic capability.
- **EvidenceCandidate**: non-authoritative proposed evidence representation awaiting governed validation.
- **Evidence**: authoritative domain record accepted under the FDM evidence contract, with provenance.
- **Assessment**: authoritative domain evaluation of accepted evidence against an explicit criterion/target and applicable policy.
- **AssessmentResult**: the result/value of an assessment; it is not synonymous with the candidate that proposed it.
- **MasteryRecord**: governed learner-state interpretation under MasteryPolicy; neither LPH nor a candidate assessment owns it.

The unqualified word `assessment` must not be used to imply authority when the object is actually a candidate.

## 3. Authority boundary

The canonical sequence is:

```text
Learner response / speech artifact
          ↓
Bounded linguistic processing
          ↓
LinguisticAssessmentCandidate
          ↓
Candidate validation + provenance
          ↓
Evidence / Assessment acceptance contract
          ↓
FDM authoritative Evidence + Assessment
          ↓
CLM learning-state interpretation
          ↓
SDT projection
          ↓
APE pedagogical decision
```

LPH may propose linguistic interpretations. FDM owns authoritative domain semantics, acceptance, provenance and mutation.

## 4. What LPH may produce

LPH may produce a candidate containing, as applicable:

```yaml
linguistic_assessment_candidate:
  candidate_id: <stable-candidate-id>
  learner_id: <id>
  session_id: <id>
  activity_id: <id>
  lesson_id: <id>
  competency_id: <id-or-null>
  source_artifact_references: [<id>]
  linguistic_dimension: <grammar|lexicon|phonology|pronunciation|prosody|discourse|other-governed>
  observed_form: <candidate-observation>
  target_reference: <governed-reference-or-null>
  proposed_result: <candidate-result>
  uncertainty: <explicit>
  capability_metadata: <model/tool/version>
  lineage: <optional-parent-candidate>
}
```

This schema is conceptual. Exact persistence and serialization remain pending FDM/SRA decisions.

## 5. What LPH cannot do

LPH cannot, solely by producing a `LinguisticAssessmentCandidate`:

- create authoritative `Evidence`;
- create authoritative `Assessment`;
- declare a learner correct/incorrect as a domain fact without governed acceptance;
- mutate `MasteryRecord`;
- mutate SDT authoritative state;
- establish `ProgressionEligibility`;
- authorize APE `PROGRESS`;
- redefine assessment criteria or MasteryPolicy;
- erase or rewrite historical evidence.

The same prohibition applies when the candidate originates from an LLM, STT system, pronunciation model, acoustic analyzer, or ensemble.

## 6. Candidate versus evidence

A candidate is a claim about an observation. Evidence is an accepted, provenance-bearing domain record.

```text
candidate claim
    ≠
authoritative evidence
```

A transcript can be evidence of what the system transcribed without being authoritative evidence that the learner's linguistic production was correct. Acoustic measurements can be evidence of measured signal properties without being an authoritative pedagogical judgment. These dimensions must remain separable.

## 7. Candidate versus assessment

A `LinguisticAssessmentCandidate` proposes an evaluation. An FDM `Assessment` records a governed evaluation of accepted evidence against an explicit target/criterion.

Therefore:

```text
LinguisticAssessmentCandidate
        ↓
validation / normalization / provenance check
        ↓
accepted Evidence
        ↓
Assessment
```

Direct candidate → authoritative Assessment is forbidden unless the FDM contract explicitly defines the candidate itself as an accepted evidence input through a governed acceptance command. In that case the resulting authoritative record remains an FDM Assessment/Evidence record, not the candidate.

## 8. Multi-dimensional linguistic assessment

A learner utterance may yield separate candidates for grammar, lexicon, phonology, pronunciation, prosody and discourse. One dimension must not silently overwrite another.

The architecture should preserve:

- source artifact identity;
- dimension assessed;
- observation/measurement;
- target/criterion;
- candidate result;
- uncertainty;
- capability/model provenance;
- acceptance decision;
- authoritative evidence/assessment identity once accepted.

Disagreement between candidate sources must remain explicit until governed resolution.

## 9. Acceptance boundary

FDM acceptance must verify, as applicable:

1. candidate identity and schema validity;
2. source evidence/artifact provenance;
3. learner/session/activity context;
4. applicable competency/objective/criterion;
5. linguistic dimension and target reference;
6. uncertainty and missing-data semantics;
7. capability provenance;
8. policy/version references where applicable;
9. temporal/version consistency;
10. conflict conditions.

Acceptance is not equivalent to trusting a model score. It is a domain operation that creates or updates an authoritative record under FDM invariants.

## 10. Rejection and uncertainty

Candidate outcomes should be explicit:

```text
PENDING_VALIDATION
       ├── ACCEPTED_FOR_DOMAIN_USE
       ├── REJECTED
       ├── INSUFFICIENT
       └── CONFLICT
```

`INSUFFICIENT` means the candidate cannot support the intended authoritative use. It must not be converted into learner failure.

`CONFLICT` means authoritative or independently relevant candidate inputs disagree in a way that the governed contract cannot safely resolve. It must not be silently averaged or selected by LLM preference.

## 11. Mastery boundary

A linguistic assessment candidate cannot establish mastery directly.

The governed path remains:

```text
Candidate(s)
    ↓
accepted Evidence
    ↓
Assessment
    ↓
MasteryPolicy(identity + version)
    ↓
Mastery evaluation
    ↓
MasteryRecord
```

No candidate confidence, STT confidence, pronunciation score, acoustic score, LLM confidence, conversational fluency, self-report, or APE preference is an implicit mastery threshold.

## 12. ErrorObservation boundary

A linguistic candidate may propose an error classification, but it cannot directly create authoritative `ErrorObservation`.

The governed path is:

```text
LinguisticAssessmentCandidate
        ↓
accepted Evidence / Assessment
        ↓
ErrorObservation acceptance
```

Historical error records remain governed FDM records and are not rewritten to match later candidate output.

## 13. SDT and APE boundary

SDT receives governed projections/summaries from authoritative state. APE consumes governed learner state and assessment context to select pedagogical action.

Neither SDT nor APE should promote a candidate directly to authoritative assessment/evidence.

## 14. LLM boundary

If an LLM contributes linguistic interpretation, its output remains a candidate. Structured JSON, tool-call format, high confidence, validation of syntax, or model-provider reputation does not change its authority class.

LLM-generated explanatory language may be delivered separately from the authoritative assessment record.

## 15. Provenance and replay

Authoritative assessment should preserve enough provenance to identify:

- source evidence/artifact;
- candidate lineage where applicable;
- capability/model/version;
- relevant criterion/target;
- applicable policy/version;
- acceptance command/event;
- domain/schema version;
- timestamp and state/version context.

Exact replay guarantees remain pending runtime/model decisions. Provenance must not be confused with reproducibility.

## 16. Offline and failure containment

The core learning path must remain operational without network access after local assets are provisioned. Failure of an assessment capability must result in controlled uncertainty/unavailability, not fabricated evidence or learner failure.

A failed linguistic analyzer must not authorize progression or mutate mastery merely because another component needs a result.

## 17. Invariants

### C011-I01 — Candidate non-authority

A `LinguisticAssessmentCandidate` cannot directly mutate authoritative FDM state.

### C011-I02 — Evidence provenance

Every authoritative assessment must reference accepted evidence or an explicitly governed evidence source.

### C011-I03 — Criterion traceability

An authoritative assessment must identify the applicable target/criterion where the domain contract requires one.

### C011-I04 — Dimension separation

Independent linguistic dimensions cannot overwrite one another without an explicit governed rule.

### C011-I05 — Uncertainty preservation

Unknown, insufficient, ambiguous or conflicting candidate information cannot silently become verified assessment.

### C011-I06 — Policy isolation

Assessment consumers cannot redefine MasteryPolicy or convert an assessment score into mastery through hidden thresholds.

### C011-I07 — Historical integrity

Authoritative evidence and assessments are not rewritten merely to reconcile a later candidate.

### C011-I08 — Model replacement isolation

Replacing the linguistic capability/model cannot silently change FDM authority rules or historical records.

### C011-I09 — Attribution

Every authoritative assessment mutation is attributable to a governed command/event and provenance chain.

### C011-I10 — Failure containment

Capability failure cannot be represented as learner failure without valid evidence supporting that conclusion.

## 18. Acceptance tests

- **C011-T01:** LPH candidate cannot directly persist as authoritative Assessment.
- **C011-T02:** Candidate lacking provenance is rejected or remains non-authoritative.
- **C011-T03:** Accepted assessment references valid evidence and criterion/target where required.
- **C011-T04:** Grammar and pronunciation candidates remain dimensionally distinct.
- **C011-T05:** Conflicting candidate results produce controlled conflict/uncertainty rather than silent selection.
- **C011-T06:** Candidate confidence alone cannot establish mastery.
- **C011-T07:** Candidate error classification cannot directly create ErrorObservation without governed acceptance.
- **C011-T08:** LLM-generated assessment language remains non-authoritative until separately accepted.
- **C011-T09:** Assessment retains policy/version provenance when applicable to mastery evaluation.
- **C011-T10:** Analyzer failure does not produce learner-failure evidence.
- **C011-T11:** Replacing the assessment model does not rewrite historical authoritative assessment.
- **C011-T12:** Authoritative assessment mutation is traceable to evidence, criterion/policy context and domain command/event.

## 19. Open decisions

The following remain unresolved and must not be invented:

- final candidate schema;
- final FDM Evidence/Assessment schemas;
- exact acceptance commands/events;
- candidate-to-evidence conversion rules;
- confidence/uncertainty semantics;
- calibration and disagreement policy;
- linguistic taxonomy;
- criterion/target representation;
- persistence and retention;
- executable test implementation;
- runtime and performance budgets;
- secondary audit outcome.

## 20. Status

**PROPOSED / REQUIRES APPROVAL.**

C-011 is resolved here at the conceptual authority/ownership level only. Source-spec integration, executable validation, independent audit and human approval remain required.
