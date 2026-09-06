# C-011 Integration Matrix — Linguistic Assessment Ownership

**Version:** 0.1-draft
**Status:** PROPOSED / REQUIRES APPROVAL
**Scope:** LPH → linguistic assessment candidate → evidence/assessment → FDM → CLM/SDT/APE

## 1. Canonical boundary

```text
Learner response / speech artifact
          ↓
Bounded linguistic processing
          ↓
LinguisticAssessmentCandidate
          ↓
validation + provenance
          ↓
FDM Evidence / Assessment acceptance
          ↓
CLM learning-state interpretation
          ↓
SDT projection
          ↓
APE decision
```

The candidate is non-authoritative. FDM owns authoritative Evidence and Assessment semantics and mutations.

## 2. Responsibility matrix

| Component | Owns | May produce | Must not do |
|---|---|---|---|
| Audio/Speech capability | bounded capture/measurement | audio refs, measurements, candidates | declare mastery/progression |
| LPH | linguistic processing/constraints | LinguisticAssessmentCandidate | create authoritative Assessment/Evidence directly |
| LLM | probabilistic interpretation/generation | candidate content/interpretation | become evidence authority |
| FDM | domain semantics/invariants | authoritative Evidence/Assessment | delegate authority to candidate/model |
| CLM | learning-state semantics | mastery interpretation under policy | redefine evidence authority |
| SDT | learner-state projection | derived state | promote candidates to truth |
| APE | pedagogical decisions | controlled next action | create assessment truth or bypass FDM |
| MasteryPolicy | governed mastery requirements | policy definition | accept hidden consumer thresholds |

## 3. Critical distinctions

```text
LinguisticAssessmentCandidate ≠ Evidence
LinguisticAssessmentCandidate ≠ Assessment
Assessment ≠ Mastery
Assessment ≠ ProgressionEligibility
Candidate confidence ≠ evidence certainty
Syntax validation ≠ domain acceptance
Model agreement ≠ authoritative truth
Capability failure ≠ learner failure
SDT projection ≠ source evidence
APE decision ≠ assessment creation
```

## 4. Authority tests

- **C011-AUTH-01:** Candidate cannot directly mutate FDM authoritative state.
- **C011-AUTH-02:** FDM can reject a candidate independently of LPH/LLM confidence.
- **C011-AUTH-03:** Accepted Assessment has evidence provenance.
- **C011-AUTH-04:** APE cannot promote a candidate to Assessment through a pedagogical decision alone.
- **C011-AUTH-05:** SDT cannot promote a candidate to Evidence/Assessment.
- **C011-AUTH-06:** Mastery evaluation consumes governed Assessment/Evidence, not raw candidate confidence.

## 5. Evidence/assessment tests

- **C011-E01:** Missing source provenance prevents authoritative acceptance.
- **C011-E02:** Missing criterion/target is rejected when required by the domain contract.
- **C011-E03:** Grammar, pronunciation and prosody candidates retain separate dimensions.
- **C011-E04:** Accepted authoritative Assessment receives a stable assessment identity distinct from candidate identity.
- **C011-E05:** Candidate lineage is retained when it contributes to an accepted record.
- **C011-E06:** Uncertain/insufficient candidate input cannot silently become verified evidence.

## 6. Conflict tests

- **C011-C01:** Conflicting candidate results are represented as controlled conflict/uncertainty where unresolved.
- **C011-C02:** The LLM cannot resolve authoritative conflict merely by selecting the most plausible candidate.
- **C011-C03:** No silent averaging of incompatible dimensions/results occurs without an approved rule.

## 7. Mastery/error/progression isolation

- **C011-M01:** Candidate confidence cannot establish mastery.
- **C011-M02:** Assessment does not itself equal mastery; MasteryPolicy remains the governing policy.
- **C011-M03:** Candidate error classification cannot directly create ErrorObservation.
- **C011-M04:** Candidate/Assessment cannot establish ProgressionEligibility without the complete governed pipeline.

## 8. Model replacement and offline tests

- **C011-R01:** Replacing the linguistic assessment capability does not change FDM authority rules.
- **C011-R02:** Historical authoritative assessments remain stable when a model is upgraded.
- **C011-O01:** Assessment capability unavailable → controlled insufficient/unavailable state, not fabricated evidence.
- **C011-O02:** Core learning/progression remains governed without a remote assessment service.

## 9. Integration gate

C-011 is not considered source-integrated until PAD, CLM, FDM, APE, SDT and LPH contain explicit compatible references and the corresponding automated checks exist.

This matrix is a reconciliation artifact, not an implementation specification and not evidence that the tests already execute.

## 10. Status

**PROPOSED / REQUIRES APPROVAL.**
