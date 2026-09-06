# Cross-P1 Reconciliation — C-001…C-011

**Document ID:** CROSS-P1-RECONCILIATION
**Version:** 0.1-draft
**Status:** PROPOSED / REQUIRES APPROVAL
**Scope:** Transversal consistency of the P1 contracts C-001 through C-011

## 1. Purpose

Verify that the eleven P1 resolutions compose into one authority chain without lateral paths that allow probabilistic components, projections, or pedagogical decisions to bypass domain evidence, assessment, mastery, or progression gates.

This is a reconciliation artifact, not evidence that all executable tests have passed.

## 2. Canonical transversal chain

```text
Curriculum / governed policies
          ↓
      CLM / FDM
          ↓
   learner evidence
          ↓
      Assessment
          ↓
     MasteryPolicy
          ↓
    MasteryRecord
          ↓
 ProgressionEligibility
          ↓
          APE
          ↓
 PedagogicalDecision
          ↓
 controlled learner-facing action
```

Parallel bounded capability path:

```text
Learner response / speech
          ↓
 bounded processing
          ↓
 candidate artifacts
          ↓
 validation + provenance
          ↓
 FDM authoritative Evidence / Assessment
```

Candidates never become an alternative authority chain.

## 3. C-001…C-011 composition matrix

| ID | Boundary | Transversal dependency | Required invariant |
|---|---|---|---|
| C-001 | APE/LPH/FDM authority | all downstream contracts | APE decides pedagogical action; FDM enforces domain invariants |
| C-002 | Objective/Competency | curriculum → assessment | assessment targets must resolve to governed curriculum constructs |
| C-003 | MasteryPolicy | assessment → mastery | mastery evaluation requires explicit policy identity/version |
| C-004 | SDT | state → APE | SDT is projection/state, never authority |
| C-005 | ErrorObservation | evidence → error state | error history requires accepted evidence/provenance |
| C-006 | Speech evidence | speech → evidence/assessment | speech processing produces bounded evidence, not mastery/progression |
| C-007 | ProgressionEligibility | mastery/prerequisites → progression | eligibility is a domain result, not an APE preference |
| C-008 | PROGRESS gates | eligibility → APE action | APE cannot emit PROGRESS when mandatory gates fail |
| C-009 | Policy reference | all policy consumers | consumers reference policy; they do not redefine it |
| C-010 | LLM candidate | generation → use | generated content remains non-authoritative |
| C-011 | Linguistic assessment candidate | linguistic processing → assessment | candidate is not authoritative Evidence/Assessment |

## 4. Critical authority invariants

### X-P1-I01 — No lateral authority path

No LPH, LLM, SDT, candidate, speech analyzer, UI, learner preference, or APE conversational output may directly mutate authoritative mastery, progression, evidence, or assessment state outside the FDM governed command/acceptance path.

### X-P1-I02 — Evidence before learner-state mutation

A learner-state judgment must trace through accepted evidence and applicable assessment/policy semantics where required. Candidate confidence is never a substitute.

### X-P1-I03 — Mastery before progression

ProgressionEligibility cannot be satisfied by pedagogical intent. Mandatory mastery/prerequisite gates remain domain constraints.

### X-P1-I04 — Policy identity is preserved

Any authoritative mastery decision retains the exact MasteryPolicy identity/version used.

### X-P1-I05 — Projection cannot become source

SDT may summarize authoritative state but cannot promote its own projection into evidence, assessment, mastery, or progression truth.

### X-P1-I06 — Candidate isolation

LLMGenerationCandidate and LinguisticAssessmentCandidate remain non-authoritative until a separate governed acceptance operation produces the appropriate FDM record.

### X-P1-I07 — Error history remains provenance-bearing

ErrorObservation is derived from governed evidence/assessment pathways and cannot be created, erased, or rewritten merely from candidate output or feedback.

### X-P1-I08 — Uncertainty survives boundaries

Insufficient, ambiguous, conflicting, or unavailable capability output cannot silently become verified evidence, mastery, or learner failure.

### X-P1-I09 — Action is downstream of truth

APE chooses pedagogical action from governed learner state and eligibility context; it does not manufacture the facts needed to justify its preferred action.

### X-P1-I10 — Model replacement isolation

Changing LLM, STT, pronunciation, acoustic, or linguistic-analysis capability cannot alter authoritative domain rules or historical records.

## 5. Cross-boundary failure scenarios

| Scenario | Expected result |
|---|---|
| LLM says learner mastered lesson | ignored as mastery authority; requires governed evidence/policy path |
| LPH marks pronunciation correct | remains candidate until accepted by FDM |
| SDT says learner is ready | treated as projection; progression must be evaluated by domain rules |
| APE wants to progress despite failed mastery | PROGRESS rejected/blocked by hard gates |
| STT confidence is high but evidence is ambiguous | uncertainty/insufficiency preserved |
| analyzer unavailable | capability failure, not learner failure |
| candidate conflicts with accepted assessment | controlled conflict; no silent overwrite |
| feedback says an error never occurred | feedback cannot rewrite ErrorObservation history |
| policy unavailable | controlled policy-resolution/insufficient state; no invented threshold |
| new model produces different score | historical authoritative assessment remains stable; new candidate follows governed path |

## 6. End-to-end acceptance tests

- **XP1-T01:** Candidate output cannot directly create authoritative Evidence/Assessment.
- **XP1-T02:** Authoritative Assessment has source evidence and criterion/target provenance where required.
- **XP1-T03:** Assessment used for mastery identifies MasteryPolicy identity/version.
- **XP1-T04:** Mastery failure prevents ProgressionEligibility from becoming ELIGIBLE when the gate is mandatory.
- **XP1-T05:** APE PROGRESS is rejected when ProgressionEligibility is not ELIGIBLE.
- **XP1-T06:** SDT cannot authorize progression independently.
- **XP1-T07:** ErrorObservation requires governed evidence provenance.
- **XP1-T08:** Conflicting candidates do not silently overwrite authoritative records.
- **XP1-T09:** Capability failure does not become learner failure.
- **XP1-T10:** Replacing an AI model does not rewrite historical authoritative state.
- **XP1-T11:** No consumer introduces an ad-hoc mastery threshold.
- **XP1-T12:** Curriculum Objective/Competency references used by assessment resolve to governed curriculum data.

## 7. Reconciliation findings

### RF-001 — Core authority chain is now conceptually closed

The eleven contracts compose into a coherent chain with FDM as authoritative domain/invariant boundary and APE as pedagogical decision authority. No intentional lateral authority path remains in the current contract set.

**Qualification:** This is a contract-level finding, not executable proof.

### RF-002 — Evidence and assessment are the central trust boundary

C-005, C-006, C-010 and C-011 converge on one rule: probabilistic observations and candidates must become authoritative only through provenance-bearing domain acceptance. This is the critical trust boundary for speech and LLM-mediated learning.

### RF-003 — Mastery and progression are downstream gates

C-003, C-007 and C-008 establish that neither APE preference nor model confidence can substitute for MasteryPolicy, MasteryRecord, prerequisites, or ProgressionEligibility.

### RF-004 — SDT is intentionally non-authoritative

C-004 prevents learner-state projection from becoming a second source of truth. APE consumes SDT; FDM remains the domain enforcement boundary.

### RF-005 — Error state is subordinate to provenance

C-005 prevents error history from becoming a free-form memory generated by feedback or model interpretation.

## 8. Remaining transversal risks

1. Evidence/Assessment schemas and acceptance/event semantics remain conceptual.
2. MasteryPolicy scope/cardinality and final thresholds remain pending.
3. Conflict/uncertainty executable semantics remain pending.
4. SDT synchronization/concurrency remains pending.
5. Curriculum criterion traceability remains pending.
6. No cross-contract schema compatibility suite has been evidenced.
7. No executable C-001…C-011 invariant suite has been evidenced.
8. Exact-head CI and independent secondary audit remain pending.
9. Performance/thermal behavior remains an SRA/benchmark concern.

## 9. Gate decision

**CROSS-P1 GATE: PASS AT CONTRACT/CONCEPTUAL LEVEL — NOT READY FOR APPROVAL.**

The P1 contracts are compositionally consistent at the inspected contract level. This does not close P1. Required next gates are direct normative source-spec integration, executable checks, schema compatibility validation, exact-head CI, independent secondary AI audit, and human approval.

No implementation authorization is granted by this document.
