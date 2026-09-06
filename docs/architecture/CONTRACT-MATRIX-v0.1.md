# Contract Matrix — PAD / CLM / FDM / APE / LPH

**Version:** 0.3-draft
**Status:** PROPOSED / REQUIRES APPROVAL

## Cross-P1 authority invariants

The following contracts are mutually dependent and must be evaluated as a single chain:

```text
Curriculum / governed policy
        ↓
accepted Evidence
        ↓
Assessment
        ↓
MasteryPolicy
        ↓
MasteryRecord
        ↓
ProgressionEligibility
        ↓
APE PedagogicalDecision
```

Capability outputs remain candidates until governed acceptance:

```text
LLM / STT / speech / linguistic capability
                 ↓
             candidate
                 ↓
       validation + provenance
                 ↓
       FDM Evidence / Assessment
```

### CM-X01 — No lateral authority

No LPH, LLM, SDT, capability model, candidate or APE conversational output may bypass the FDM governed acceptance/mutation boundary for authoritative Evidence, Assessment, Mastery or Progression.

### CM-X02 — Evidence provenance

Authoritative assessment and learning-state mutation require traceable evidence/provenance where the applicable domain contract requires it.

### CM-X03 — Policy reference isolation

Consumers carry `mastery_policy_id` + version; they cannot introduce hidden thresholds or replacement policy semantics.

### CM-X04 — Progression gate isolation

`ProgressionEligibility` is a domain result. APE `PROGRESS` is downstream and cannot override mandatory domain gates.

### CM-X05 — Candidate isolation

`LLMGenerationCandidate` and `LinguisticAssessmentCandidate` are non-authoritative. Acceptance creates/updates the appropriate FDM record under governed commands; candidate identity does not become domain truth by itself.

### CM-X06 — Projection isolation

SDT is derived learner-state representation and cannot become an alternative evidence/assessment/mastery/progression source.

### CM-X07 — Error provenance

`ErrorObservation` is a provenance-bearing authoritative record; candidate classifications and feedback cannot rewrite its history.

### CM-X08 — Uncertainty preservation

Unknown, insufficient, conflicting or unavailable capability output must remain explicit and cannot silently become verified learner failure or mastery.

### CM-X09 — Model replacement

Replacing LLM/STT/pronunciation/linguistic capabilities cannot change domain authority rules or rewrite historical authoritative state.

## Status

These cross-contract invariants are PROPOSED and require executable tests, exact-head CI verification, independent audit and human approval.
