# Contradiction Matrix — PAD / CLM / FDM / APE / LPH

**Version:** 0.5
**Status:** PROPOSED / REQUIRES INTEGRATION + INDEPENDENT AUDIT
**Branch:** `architecture/pad-clm-fdm-ape-v1.0`
**Scope:** Cross-document reconciliation before LPH v1.0 and SRA.

## 0. Evidence boundary

This matrix records findings from direct inspection of repository artifacts and subsequent formalization work. It does not claim inspection of artifacts that were not retrieved.

## 1. P1 findings and resolution status

| ID | Severity | Finding | Resolution artifact | Status |
|---|---|---|---|---|
| C-001 | P1 | LPH section 4 diagram could imply LPH authority above APE/FDM/CLM. | P1 Contract 1; PAD authority hierarchy | **INTEGRATED + VERIFIED** |
| C-002 | P1 | Competency/Objectives ownership and cardinality ambiguous. | P1 Contract 2; FDM §§4.3–4.4, §6; PAD §4.2 | **INTEGRATED + VERIFIED** |
| C-003 | P1 | No explicit authoritative MasteryPolicy contract. | P1 Contract 3; `docs/architecture/MASTERY-POLICY-v0.1.md`; PAD/CLM/FDM/APE/LPH policy references | **INTEGRATED + VERIFIED** |
| C-004 | P1 | SDT artifact was missing on inspected branch; downstream ownership/authority boundaries required formal reconciliation. | `docs/03-cognitive/SDT.md`; `docs/architecture/SDT-INTEGRATION-MATRIX-v0.1.md`; CLM/FDM/APE/PAD/LPH existing contract sections | **INTEGRATED AT CONTRACT LEVEL + AUTHORITY LIMITS VERIFIED; SDT REMAINS PROPOSED** |
| C-005 | P1 | LPH `Error` versus FDM `ErrorObservation` lifecycle mismatch; recurrence semantics unclear. | P1 Contract 5; `ERROR-OBSERVATION-LIFECYCLE-v0.1.md`; `ERROR-OBSERVATION-INTEGRATION-MATRIX-v0.1.md` | **INTEGRATED AT CONTRACT LEVEL + LIFECYCLE/BOUNDARY VERIFIED; SOURCE-SPEC DIRECT REFERENCES REMAIN PENDING** |
| C-006 | P1 | Speech evidence → assessment → mastery/SDT ownership/order incomplete. | P1 Contract 4; `SPEECH-EVIDENCE-ASSESSMENT-CONTRACT-v0.1.md`; `SPEECH-EVIDENCE-INTEGRATION-MATRIX-v0.1.md` | **INTEGRATED AT CONTRACT LEVEL + AUTHORITY/SEQUENCING VERIFIED; SOURCE-SPEC DIRECT REFERENCES REMAIN PENDING** |
| C-007 | P1 | `ProgressionEligibility` versus APE `PROGRESS` boundary incomplete. | P1 Contract 6 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-008 | P1 | APE progression discretion versus mandatory mastery/progression gates underspecified. | P1 Contract 6 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-009 | P1 | APE/LPH mastery requirements could be interpreted as policy definition. | P1 Contract 7 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-010 | P1 | LLM candidate acceptance/persistence boundary incomplete. | P1 Contract 8 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-011 | P1 | LPH linguistic assessment versus FDM authoritative evidence ownership ambiguous. | P1 Contract 9 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |

## 2. C-005 authority and lifecycle verification

C-005 is now formally defined by a canonical `ErrorObservation` lifecycle contract. The review separates raw observations, governed evidence, assessments, probabilistic error candidates, authoritative error observations, learner-facing feedback and recurrence summaries.

```text
Observation
   ↓
Evidence
   ↓
Assessment
   ↓
ErrorObservationCandidate (optional)
   ↓
Validation / FDM acceptance
   ↓
ErrorObservation (authoritative)
   ↓
CLM error/weakness interpretation
   ↓
SDT derived summary
   ↓
APE reinforcement/reassessment
```

Verified boundaries:

- FDM owns the authoritative `ErrorObservation` entity and mutation/invariant boundary.
- CLM owns error/weakness learning-state semantics.
- SDT carries references/derived summaries and does not replace error history.
- APE consumes accepted error/weakness state and cannot invent error facts.
- PAD owns correction/reinforcement pedagogy, not error-record authority.
- LPH may classify candidate errors and structure linguistic evidence, but cannot directly create authoritative error state.
- LLM output remains non-authoritative.

Recurrence is explicitly a derived signal from accepted observation history under a future approved recurrence policy. A raw `recurrence_count` is not authoritative error truth and cannot independently establish mastery failure, reinforcement need or a learner trait.

The C-005 integration matrix defines ten acceptance tests covering evidence linkage, candidate isolation, uncertainty, historical immutability, recurrence derivation, SDT separation and prevention of APE-created error facts.

No new P1 authority contradiction was identified during the C-005 review. The remaining limitation is that direct normative references may still need to be inserted into each source specification during the broader P1 source-spec integration pass; this is intentionally not claimed as complete.

## 3. C-006 speech evidence → assessment → mastery/SDT verification

C-006 is now formally defined by a dedicated speech evidence/assessment contract and integration matrix. The review explicitly separates speech acquisition and processing from authoritative evidence, assessment, mastery interpretation, learner-state projection and pedagogical decision.

Canonical chain:

```text
Learner speech
   ↓
Audio artifact
   ↓
Bounded speech processing
   ├─ transcript candidate
   ├─ acoustic/prosodic measurements
   └─ pronunciation/phonological candidate measures
   ↓
Speech Evidence Candidate(s)
   ↓
FDM evidence validation + provenance
   ↓
Authoritative Evidence
   ↓
Assessment
   ↓
MasteryPolicy + CLM interpretation
   ↓
MasteryRecord / ErrorObservation / other governed state
   ↓
SDT projection
   ↓
APE pedagogical decision
```

Verified authority boundaries:

- Audio capture owns acquisition/reference, not correctness or mastery.
- STT produces transcript candidates; transcript output is not itself linguistic correctness or mastery evidence.
- Acoustic/prosodic analysis produces measurements; measurements do not independently authorize pedagogy/progression.
- Pronunciation/phonological analysis produces bounded candidate assessments; it cannot bypass evidence/assessment boundaries.
- LPH may structure linguistic evidence and validate candidates, but cannot directly mutate mastery, progression or authoritative SDT.
- FDM owns authoritative evidence/provenance and domain mutation/invariants.
- CLM interprets accepted evidence as learning state.
- MasteryPolicy defines applicable mastery requirements; consumers reference identity/version rather than inventing thresholds.
- SDT receives governed projections and cannot replace authoritative speech history.
- APE decides pedagogical action from governed state and cannot manufacture evidence from raw speech signals.
- LLM output remains a bounded, non-authoritative candidate.

Critical integrity rules:

1. Transcript ≠ linguistic correctness.
2. Acoustic measurement ≠ pedagogical assessment.
3. Candidate assessment ≠ authoritative assessment.
4. Assessment ≠ mastery.
5. Mastery ≠ progression action.
6. Speech-processing failure ≠ learner failure.
7. Unsupported/uncertain speech dimensions remain unassessed/uncertain.
8. Conflicting assessments remain `CONFLICT` until governed resolution.
9. Mastery interpretation requires explicit `MasteryPolicy` identity/version.
10. Reassessment creates new evidence/assessment records rather than rewriting historical evidence.

The C-006 integration matrix defines authority, evidence-integrity and offline-path acceptance tests. The contract intentionally leaves model choice, measurement validity, final schemas, runtime topology and numerical mastery thresholds pending empirical/SRA work.

C-006 is therefore **integrated at contract level**, but direct normative references inside every source specification and automated executable checks remain pending. No empirical claim about the validity of a specific STT/acoustic/pronunciation model is made by this reconciliation.

## 4. P2 findings retained

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| C-012 | P2 | Intervention taxonomy ownership. | APE policy contract; CLM stores state/semantics. Resolve after P1 integration. |
| C-013 | P2 | Learner preference versus strategy effectiveness. | Require evidence before strategy-state mutation. |
| C-014 | P2 | APE decision authority versus FDM mutation ownership. | FDM enforces invariants/mutations; APE requests decisions. |
| C-015 | P2 | Offline critical path shared invariant. | Retain as cross-cutting invariant; test in SRA. |
| C-016 | P2 | Conceptual schemas not ready for implementation. | Block SRA until contracts are executable/testable. |

## 5. Previously observed missing artifacts

At the time of the original reconciliation the following were not found at expected paths on this branch:

- `docs/01-product/PRD.md`
- `docs/00-governance/PGKI.md`
- `schemas/project-state.schema.json`
- `schemas/context-manifest.schema.json`
- `tools/validate_governance.py`
- `docs/07-ai/RAG.md`
- `docs/07-ai/LLM-ARCHITECTURE.md`

`docs/03-cognitive/SDT.md` is no longer a missing-artifact gap; it exists as v0.1-draft. The remaining gaps are not silently reclassified as resolved.

## 6. Resolution principles

1. APE is the pedagogical decision authority.
2. FDM is the domain/invariant enforcement boundary.
3. CLM defines learning-state semantics; SDT represents governed learner state.
4. LPH is a model-independent linguistic/pedagogical constraint and validation boundary.
5. LLM generation is non-authoritative.
6. MasteryPolicy is an explicit governed contract; consumers reference it rather than redefining it.
7. Evidence provenance precedes authoritative state mutation.
8. Uncertainty and conflict remain explicit.
9. `ProgressionEligibility` is a domain result; `PROGRESS` is an APE action subject to hard gates.
10. Source specifications must incorporate the contracts before promotion to v1.0.
11. SDT is a projection/state representation and cannot become an additional decision authority.
12. `ErrorObservation` is the canonical authoritative error record; candidates, feedback and derived summaries cannot replace its provenance-bearing history.
13. Speech processing components are bounded evidence producers; they are not pedagogical authorities.
14. Speech-derived mastery requires accepted evidence, assessment and explicit MasteryPolicy provenance.

## 7. Gate status

**P1 RECONCILIATION: PARTIALLY RESOLVED / NOT READY FOR APPROVAL.**

C-001 through C-004 are integrated at contract level with repository evidence. C-005 and C-006 are formally specified with dedicated canonical contracts/integration matrices and explicit authority/lifecycle/sequence tests. C-005 and C-006 remain subject to direct source-spec integration. Remaining P1 contracts, missing governance/AI artifacts, automated contract checks, exact-head CI verification, independent secondary audit and human approval remain required.

Therefore this work does **not** authorize LPH v1.0, SRA implementation, or final baseline/tagging.
