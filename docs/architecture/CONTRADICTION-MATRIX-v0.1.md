# Contradiction Matrix — PAD / CLM / FDM / APE / LPH

**Version:** 0.3
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
| C-005 | P1 | LPH `Error` versus FDM `ErrorObservation` lifecycle mismatch; recurrence semantics unclear. | P1 Contract 5 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-006 | P1 | Speech evidence → assessment → mastery/SDT ownership/order incomplete. | P1 Contract 4 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-007 | P1 | `ProgressionEligibility` versus APE `PROGRESS` boundary incomplete. | P1 Contract 6 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-008 | P1 | APE progression discretion versus mandatory mastery/progression gates underspecified. | P1 Contract 6 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-009 | P1 | APE/LPH mastery requirements could be interpreted as policy definition. | P1 Contract 7 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-010 | P1 | LLM candidate acceptance/persistence boundary incomplete. | P1 Contract 8 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-011 | P1 | LPH linguistic assessment versus FDM authoritative evidence ownership ambiguous. | P1 Contract 9 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |

## 2. C-004 authority verification

The C-004 review found no new P1 authority contradiction after reconciling SDT across the five consuming/adjacent contracts.

Verified boundaries:

```text
CLM  = defines learning-state semantics
SDT  = represents/projected learner state
FDM  = owns domain invariants + authoritative mutation boundary
APE  = owns pedagogical decisions
LPH  = linguistic/interaction constraint + validation boundary
LLM  = bounded probabilistic generation/interpretation capability
```

The integration matrix `SDT-INTEGRATION-MATRIX-v0.1.md` records eight explicit authority tests covering self-authority, curriculum authority, mastery-policy authority, progression authority, LLM mutation, provenance, uncertainty, and stale-state/version safety.

No unresolved C-004 issue was found that justifies inventing additional SDT authority or changing the authority hierarchy.

## 3. P2 findings retained

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| C-012 | P2 | Intervention taxonomy ownership. | APE policy contract; CLM stores state/semantics. Resolve after P1 integration. |
| C-013 | P2 | Learner preference versus strategy effectiveness. | Require evidence before strategy-state mutation. |
| C-014 | P2 | APE decision authority versus FDM mutation ownership. | FDM enforces invariants/mutations; APE requests decisions. |
| C-015 | P2 | Offline critical path shared invariant. | Retain as cross-cutting invariant; test in SRA. |
| C-016 | P2 | Conceptual schemas not ready for implementation. | Block SRA until contracts are executable/testable. |

## 4. Previously observed missing artifacts

At the time of the original reconciliation the following were not found at expected paths on this branch:

- `docs/01-product/PRD.md`
- `docs/00-governance/PGKI.md`
- `schemas/project-state.schema.json`
- `schemas/context-manifest.schema.json`
- `tools/validate_governance.py`
- `docs/07-ai/RAG.md`
- `docs/07-ai/LLM-ARCHITECTURE.md`

`docs/03-cognitive/SDT.md` is no longer a missing-artifact gap; it exists as v0.1-draft. The remaining gaps are not silently reclassified as resolved.

## 5. Resolution principles

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

## 6. Gate status

**P1 RECONCILIATION: PARTIALLY RESOLVED / NOT READY FOR APPROVAL.**

C-001, C-002, C-003 and C-004 are now integrated at contract level with repository evidence. C-004 specifically has a dedicated integration matrix and explicit authority tests across CLM/FDM/APE/PAD/LPH. The remaining P1 contracts still require source-spec integration, remaining missing governance/AI artifacts must be reconciled, automated checks must cover the contracts, and independent secondary audit plus human approval is required.

Therefore this work does **not** authorize LPH v1.0, SRA implementation, or final baseline/tagging.
