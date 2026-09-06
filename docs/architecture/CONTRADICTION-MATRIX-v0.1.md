# Contradiction Matrix — PAD / CLM / FDM / APE / LPH

**Version:** 0.6
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
| C-007 | P1 | `ProgressionEligibility` versus APE `PROGRESS` boundary incomplete. | P1 Contract 6; `PROGRESSION-ELIGIBILITY-CONTRACT-v0.1.md`; `PROGRESSION-ELIGIBILITY-INTEGRATION-MATRIX-v0.1.md` | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-008 | P1 | APE progression discretion versus mandatory mastery/progression gates underspecified. | P1 Contract 6; `PROGRESSION-ELIGIBILITY-CONTRACT-v0.1.md`; `PROGRESSION-ELIGIBILITY-INTEGRATION-MATRIX-v0.1.md` | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-009 | P1 | APE/LPH mastery requirements could be interpreted as policy definition. | P1 Contract 7; `MASTERY-POLICY-REFERENCE-BOUNDARY-INTEGRATION-MATRIX-v0.1.md`; APE §6, §7, §10, §17, §21 | **SOURCE-SPEC BOUNDARY INTEGRATED; CLM/FDM/LPH REFERENCES VERIFIED; APPROVAL/AUTOMATION PENDING** |
| C-010 | P1 | LLM candidate acceptance/persistence boundary incomplete. | P1 Contract 8 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-011 | P1 | LPH linguistic assessment versus FDM authoritative evidence ownership ambiguous. | P1 Contract 9 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |

## 2. C-009 mastery-policy reference boundary verification

C-009 is formally defined by P1 Contract 7 and the dedicated integration matrix. The central distinction is normative:

```text
MasteryPolicy definition
        ↓
policy reference (id + version)
        ↓
consumer use / enforcement
```

A consumer may carry a policy reference and governed constraint/evidence references, but may not recreate the authoritative policy definition locally.

Directly inspected source specifications establish the same boundary:

- `MASTERY-POLICY-v0.1.md` defines the policy as governed project data and prohibits consumer override.
- `CLM.md` states that MasteryPolicy defines applicable mastery requirements while CLM preserves policy identity/version and does not define thresholds.
- `FDM.md` states that consumers reference policy identity/version, `MasteryRecord` retains policy provenance, and `EvaluateMastery` cannot accept an ad-hoc threshold.
- `APE.md` now explicitly distinguishes policy references from embedded ad-hoc definitions and requires validation of policy identity/version/scope.
- `LINGUISTIC-PEDAGOGICAL-HARNESS-SPEC.md` states that APE/LPH reference policy identity/version and do not redefine thresholds/evidence requirements.

Forbidden fallback is explicit: undefined, unavailable, stale, malformed, out-of-scope or conflicting policy references must enter controlled resolution; no hard-coded or LLM-generated replacement is authoritative.

### C-009 acceptance tests

The dedicated matrix defines C009-T01 through C009-T10 covering explicit reference, ad-hoc threshold rejection, LPH non-override, LLM non-authority, historical provenance, version mismatch, scope mismatch, deterministic replay, consumer isolation and hidden fallback.

### Remaining gate

C-009 is **not APPROVED**. Automated executable checks, independent secondary AI audit and human approval remain pending. This status does not claim those activities have occurred.

## 3. P2 findings retained

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| C-012 | P2 | Intervention taxonomy ownership. | APE policy contract; CLM stores state/semantics. Resolve after P1 integration. |
| C-013 | P2 | Learner preference versus strategy effectiveness. | Require evidence before strategy-state mutation. |
| C-014 | P2 | APE decision authority versus FDM mutation ownership. | FDM enforces invariants/mutations; APE requests decisions. |
| C-015 | P2 | Offline critical path shared invariant. | Retain as cross-cutting invariant; test in SRA. |
| C-016 | P2 | Conceptual schemas not ready for implementation. | Block SRA until contracts are executable/testable. |

## 4. Resolution principles

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
15. A MasteryPolicy reference is not a policy definition; consumer components cannot introduce hidden thresholds or fallback policy semantics.

## 5. Gate status

**P1 RECONCILIATION: PARTIALLY RESOLVED / NOT READY FOR APPROVAL.**

C-001 through C-004 are integrated at contract level with repository evidence. C-005 and C-006 are formally specified with dedicated canonical contracts/integration matrices. C-009 now has dedicated boundary formalization plus direct source-spec boundary verification. Remaining P1 contracts, automated contract checks, exact-head CI verification, independent secondary audit and human approval remain required.

Therefore this work does **not** authorize LPH v1.0, SRA implementation, or final baseline/tagging.
