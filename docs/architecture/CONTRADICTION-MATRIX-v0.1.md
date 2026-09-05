# Contradiction Matrix — PAD / CLM / FDM / APE / LPH

**Version:** 0.1
**Status:** PROPOSED / REQUIRES RESOLUTION
**Branch:** `architecture/pad-clm-fdm-ape-v1.0`
**Scope:** Cross-document reconciliation before LPH v1.0 and SRA.

## 0. Evidence boundary

This matrix was produced from the actual repository artifacts available on the branch at audit time: PAD v0.1, CLM v0.1, FDM v0.1, APE v0.1, LPH-SPEC v0.1, Project Constitution, AI Governance, Decision Ledger, Baseline Reconciliation, Project State, Repository Policy and ADR Policy.

It does not claim that absent artifacts were inspected. Missing artifacts are recorded separately.

## 1. Findings

| ID | Severity | Documents | Finding | Disposition |
|---|---|---|---|---|
| C-001 | P1 | LPH ↔ PAD/APE | LPH section 4 visually places LPH above APE/FDM/CLM, while PAD and APE establish APE as pedagogical decision authority. This can be read as an authority inversion. | MUST CORRECT: LPH must be a boundary/control-harness, not superior to APE. |
| C-002 | P1 | PAD ↔ FDM | PAD hierarchy states `Competency → Objective`; FDM states `Competency → Objective/criteria`, while FDM also makes Objective a curriculum entity. Ownership/cardinality is ambiguous. | MUST RESOLVE in FDM contract; do not implement until objective ownership is explicit. |
| C-003 | P1 | PAD ↔ CLM ↔ FDM ↔ APE | Mastery is intentionally described without numerical thresholds, but all four documents refer to mastery as a required policy/input/output. There is no authoritative mastery-policy contract yet. | OPEN DECISION; create explicit Mastery Policy contract before v1.0. |
| C-004 | P1 | CLM ↔ FDM | CLM defines learning-state semantics and SDT projection; FDM defines SDT as a derived representation, but no formal SDT artifact/schema exists on the inspected branch. | BLOCKER: formalize SDT contract. |
| C-005 | P1 | LPH ↔ FDM | LPH uses `Error` with `recurrence_count` and status values; FDM uses `ErrorObservation`; CLM treats recurrence formula as TBD. The lifecycle/identity semantics are not aligned. | MUST UNIFY terminology and lifecycle; recurrence_count must not become authoritative until policy exists. |
| C-006 | P1 | LPH ↔ FDM ↔ CLM | LPH says speech evidence can feed SDT + Mastery Engine, but the authoritative ownership/order of speech assessment, evidence acceptance, mastery evaluation and SDT update is not fully formalized. | MUST define evidence pipeline contract. |
| C-007 | P1 | APE ↔ FDM | APE emits `progress` as an action while FDM defines `ProgressionEligibility` as a domain state. Boundary is conceptually correct but command/result semantics are not formalized. | MUST define `EvaluateProgressionEligibility` result and APE `PROGRESS` preconditions. |
| C-008 | P1 | APE ↔ PAD | APE says it may decide whether progression is pedagogically appropriate when domain eligibility permits it; PAD says progression follows mastery decision. This is not necessarily contradictory, but precedence is underspecified. | RESOLVE: domain eligibility is a necessary gate; APE may choose PROGRESS only if all mandatory gates pass. |
| C-009 | P1 | LPH ↔ APE | LPH says APE specifies mastery requirements to LPH, while APE says it consumes mastery policy and cannot invent thresholds. The interface must distinguish policy reference from policy definition. | MUST CORRECT: APE passes policy reference/constraints; policy authority remains governed elsewhere. |
| C-010 | P1 | LPH ↔ FDM | LPH conceptual `LLMResult` includes uncertainty/error information; FDM `LLMGenerationCandidate` is non-authoritative. No acceptance/rejection contract defines what evidence can be persisted. | MUST define candidate lifecycle and acceptance boundary. |
| C-011 | P1 | PAD ↔ LPH | PAD calls LPH a linguistic/pedagogical constraint & validation boundary; LPH also lists error classification and speech evidence. FDM has Evaluation/Evidence contexts. Ownership of linguistic assessment is therefore ambiguous. | MUST assign: LPH may orchestrate/validate candidate linguistic analysis, but FDM owns authoritative evidence semantics and domain state. |
| C-012 | P2 | PAD ↔ CLM | Both define learning cycle/reinforcement concepts but neither owns the formal intervention taxonomy. | Consolidate intervention taxonomy in APE policy contract; CLM stores state/semantics. |
| C-013 | P2 | CLM ↔ APE | CLM lists `strategy state` including useful/difficult activity forms; APE may adapt modality/pacing. No contract distinguishes observed learner preference from inferred strategy effectiveness. | Add evidence requirement before strategy-state mutation. |
| C-014 | P2 | FDM ↔ APE | FDM says APE is an application/pedagogical authority operating over FDM; APE document describes itself as authority. This is compatible, but ownership of state mutation must be explicit. | FDM remains invariant/domain enforcement; APE proposes/requests decisions. |
| C-015 | P2 | LPH ↔ PAD | Both specify offline-first critical pedagogy. No contradiction, but dependency language should state that LPH cannot make remote services mandatory. | Keep as shared invariant; test later. |
| C-016 | P2 | All | Many exact schemas are intentionally conceptual. This is appropriate for v0.1 but incompatible with SRA implementation if promoted without contract closure. | Block SRA until Contract Matrix reaches READY. |

## 2. Confirmed governance/document gaps discovered during reconciliation

The following were requested/referenced by existing documents but were **not found at the expected paths on this branch** during direct repository inspection:

- `docs/01-product/PRD.md`
- `docs/03-cognitive/SDT.md`
- `docs/00-governance/PGKI.md`
- `schemas/project-state.schema.json`
- `schemas/context-manifest.schema.json`
- `tools/validate_governance.py`
- `docs/07-ai/RAG.md`
- `docs/07-ai/LLM-ARCHITECTURE.md`

The absence of these files is an observed repository fact for this branch, not a claim that they never existed elsewhere.

## 3. Architectural resolution principles

1. APE is the pedagogical decision authority, not LPH.
2. FDM is the domain/invariant enforcement boundary, not APE or LPH.
3. CLM defines learning-state semantics; SDT is its governed learner-state representation/projection.
4. LPH is a model-independent linguistic/pedagogical harness and validation boundary.
5. LLM generation is non-authoritative.
6. Mastery policy is authoritative but must be represented as an explicit governed contract.
7. Evidence provenance precedes authoritative learner-state mutation.
8. Unknown policy values remain UNKNOWN/PENDING.

## 4. Gate status

**RECONCILIATION STATUS: FAIL / NOT READY FOR LPH v1.0.**

The project has sufficient material to continue formalization, but the identified P1 ambiguities and missing artifacts must be resolved before the LPH can be promoted to an approved v1.0 contract or SRA implementation can begin.
