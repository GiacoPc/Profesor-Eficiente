# Contradiction Matrix — PAD / CLM / FDM / APE / LPH

**Version:** 0.2
**Status:** PROPOSED / REQUIRES INTEGRATION + INDEPENDENT AUDIT
**Branch:** `architecture/pad-clm-fdm-ape-v1.0`
**Scope:** Cross-document reconciliation before LPH v1.0 and SRA.

## 0. Evidence boundary

This matrix records findings from direct inspection of repository artifacts and the subsequent formalization work. It does not claim inspection of artifacts that were not retrieved.

## 1. P1 findings and resolution status

| ID | Severity | Finding | Resolution artifact | Status |
|---|---|---|---|---|
| C-001 | P1 | LPH section 4 diagram could imply LPH authority above APE/FDM/CLM. | `docs/architecture/P1-RESOLUTION-CONTRACTS-v0.1.md`, Contract 1 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-002 | P1 | Competency/Objectives ownership and cardinality ambiguous. | P1 Contract 2; `docs/05-domain/FDM.md` §4.3–4.4, §6; `docs/02-pedagogy/PAD.md` §4.2 | **INTEGRATED IN FDM + PAD; VERIFIED AGAINST CONTRACT** |
| C-003 | P1 | No explicit authoritative MasteryPolicy contract. | P1 contract, Contract 3 | **RESOLVED AT CONTRACT LEVEL; POLICY SPEC/ADR REQUIRED BEFORE APPROVAL** |
| C-004 | P1 | SDT artifact was missing on inspected branch. | `docs/03-cognitive/SDT.md` | **RESOLVED AS MISSING-ARTIFACT GAP; SDT REMAINS PROPOSED** |
| C-005 | P1 | LPH `Error` versus FDM `ErrorObservation` lifecycle mismatch; recurrence semantics unclear. | P1 contract, Contract 5 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-006 | P1 | Speech evidence → assessment → mastery/SDT ownership/order incomplete. | P1 contract, Contract 4 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-007 | P1 | `ProgressionEligibility` versus APE `PROGRESS` boundary incomplete. | P1 contract, Contract 6 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-008 | P1 | APE progression discretion versus mandatory mastery/progression gates underspecified. | P1 contract, Contract 6 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-009 | P1 | APE/LPH mastery requirements could be interpreted as policy definition. | P1 contract, Contract 7 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-010 | P1 | LLM candidate acceptance/persistence boundary incomplete. | P1 contract, Contract 8 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |
| C-011 | P1 | LPH linguistic assessment versus FDM authoritative evidence ownership ambiguous. | P1 contract, Contract 9 | **RESOLVED AT CONTRACT LEVEL; SOURCE SPEC INTEGRATION REQUIRED** |

## 2. P2 findings retained

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| C-012 | P2 | Intervention taxonomy ownership. | APE policy contract; CLM stores state/semantics. Resolve after P1 integration. |
| C-013 | P2 | Learner preference versus strategy effectiveness. | Require evidence before strategy-state mutation. |
| C-014 | P2 | APE decision authority versus FDM mutation ownership. | FDM enforces invariants/mutations; APE requests decisions. |
| C-015 | P2 | Offline critical path shared invariant. | Retain as cross-cutting invariant; test in SRA. |
| C-016 | P2 | Conceptual schemas not ready for implementation. | Block SRA until contracts are executable/testable. |

## 3. Previously observed missing artifacts

At the time of the original reconciliation the following were not found at expected paths on this branch:

- `docs/01-product/PRD.md`
- `docs/03-cognitive/SDT.md`
- `docs/00-governance/PGKI.md`
- `schemas/project-state.schema.json`
- `schemas/context-manifest.schema.json`
- `tools/validate_governance.py`
- `docs/07-ai/RAG.md`
- `docs/07-ai/LLM-ARCHITECTURE.md`

**Current update:** `docs/03-cognitive/SDT.md` now exists on this branch as v0.1-draft. The remaining gaps are not silently reclassified as resolved by this document.

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

## 5. Gate status

**P1 RECONCILIATION: PARTIALLY RESOLVED / NOT READY FOR APPROVAL.**

The missing SDT artifact has been formally created and the eleven P1 ambiguities have explicit proposed contracts. C-001 has been integrated into PAD, and C-002 has now been integrated into both FDM and PAD and checked against the P1 contract. The remaining P1 contracts still require source-spec integration, the remaining missing governance/AI artifacts must be reconciled, automated checks must cover the contracts, and an independent secondary audit plus human approval is required.

Therefore this work does **not** authorize LPH v1.0, SRA implementation, or final baseline/tagging.
