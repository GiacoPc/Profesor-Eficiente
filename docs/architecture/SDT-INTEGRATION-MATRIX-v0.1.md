# SDT Integration Matrix — CLM / FDM / APE / PAD / LPH

**Document ID:** SDT-INTEGRATION-MATRIX
**Version:** 0.1
**Status:** PROPOSED / REQUIRES APPROVAL
**Branch:** `architecture/pad-clm-fdm-ape-v1.0`
**Scope:** Formal cross-document integration and authority-boundary verification for SDT v0.1.

## 0. Purpose

This artifact formalizes how `docs/03-cognitive/SDT.md` is consumed by CLM, FDM, APE, PAD and LPH without duplicating or redefining SDT semantics in downstream documents.

SDT remains a governed learner-state projection. It is not a new authority layer.

## 1. Canonical authority chain

```text
Observed input
    ↓
Evidence
    ↓
Assessment
    ↓
CLM learning-state interpretation
    ↓
SDT projection / snapshot
    ↓
APE pedagogical decision
    ↓
FDM invariant enforcement / authoritative mutation
```

LPH is a bounded linguistic/interaction constraint and validation layer below APE. LLM output is non-authoritative.

## 2. Integration map

| Source | Existing contract location | SDT integration | Authority boundary | Verification status |
|---|---|---|---|---|
| SDT | `docs/03-cognitive/SDT.md` §§1–14 | Defines learner-state projection, snapshot identity, provenance, uncertainty, temporal/version boundaries and non-authority | SDT cannot define curriculum/mastery/progression or directly mutate itself from LLM output | VERIFIED |
| CLM | `docs/03-cognitive/CLM.md` §§2–4, 15–23 | CLM defines learning-state semantics; SDT is the runtime representation/projection | CLM owns semantics; SDT represents derived state; neither delegates authority to LLM | VERIFIED |
| FDM | `docs/05-domain/FDM.md` §§4.7, 6, 10, 11, 17 | FDM models SDT as a governed derived learner-state entity and enforces mutation/invariant boundaries | FDM remains authoritative domain/invariant boundary; SDT is not an invariant bypass | VERIFIED |
| APE | `docs/04-ape/APE.md` §§2, 5–7, 15–18, 21–24 | APE consumes an SDT snapshot/version as decision input | APE decides pedagogical action; SDT does not decide action; stale/conflicted state cannot silently drive authoritative decisions | VERIFIED |
| PAD | `docs/02-pedagogy/PAD.md` §§3, 11–16, 18–19 | PAD defines pedagogical information required from learner state and identifies SDT as intended learner-state representation | PAD consumes SDT; it does not own persistence or redefine SDT schema | VERIFIED |
| LPH | `docs/architecture/LINGUISTIC-PEDAGOGICAL-HARNESS-SPEC.md` §§3–5, 9, 11–16 | LPH operates after APE and uses bounded learner context; speech/evidence returns through governed pipeline | LPH cannot mutate SDT, authorize progression or redefine policy; LLM cannot mutate SDT | VERIFIED |

## 3. Required SDT snapshot contract

Consumers must treat the following as the minimum conceptual contract from SDT v0.1:

```yaml
sdt_id: <stable-learner-state-id>
learner_id: <stable-id>
state_version: <monotonic-or-equivalent-version>
computed_at: <timestamp>
source_watermark: <authoritative-evidence-position>
curriculum_version: <version>
policy_versions: [<version>]
status: <VALID|STALE|CONFLICT|INSUFFICIENT_EVIDENCE>
```

Exact serialization/persistence remains `PENDING`.

## 4. Authority tests

The following must be true independently of implementation technology:

**SDT-AUTH-01 — No self-authority**  
SDT represents state; it cannot select `TEACH`, `PRACTICE`, `REINFORCE`, `REASSESS`, `HOLD` or `PROGRESS` as a pedagogical authority.

**SDT-AUTH-02 — No curriculum authority**  
SDT may reference curriculum position but cannot modify objectives, competencies or prerequisites.

**SDT-AUTH-03 — No mastery-policy authority**  
SDT carries the result/reference of policy evaluation; it cannot define thresholds, evidence counts, weighting, stability or transfer requirements.

**SDT-AUTH-04 — No progression authority**  
SDT carries `ProgressionEligibility`; APE selects the pedagogical action subject to domain gates.

**SDT-AUTH-05 — No LLM mutation**  
LLM output cannot directly mutate authoritative SDT.

**SDT-AUTH-06 — Provenance required**  
Authoritative derived state must remain traceable to evidence/assessment or governed curriculum/policy references.

**SDT-AUTH-07 — Uncertainty preserved**  
`CONFLICT`, `STALE`, or insufficient evidence cannot silently become verified mastery.

**SDT-AUTH-08 — Version safety**  
A stale snapshot cannot silently overwrite a newer authoritative state or produce an unvalidated authoritative decision.

## 5. Deliberate non-duplication rule

CLM, FDM, APE, PAD and LPH must reference SDT v0.1 rather than copy its full schema. If a consumer requires a field not defined by SDT, the dependency must be recorded as a proposal/PENDING item rather than silently extending the contract.

## 6. Implementation consequence

This matrix does not authorize implementation. SRA must later define serialization, transaction boundaries, event ordering, concurrency behavior and persistence mapping while preserving the authority constraints above.

## 7. Acceptance gate for C-004

C-004 can be considered integrated at contract level when:

1. SDT exists as a governed artifact;
2. CLM identifies SDT as the state representation;
3. FDM represents SDT as a derived domain entity and preserves invariant enforcement;
4. APE consumes SDT as decision input without delegating authority to SDT;
5. PAD consumes SDT for pedagogical state requirements;
6. LPH remains below APE and cannot mutate SDT;
7. the eight authority tests above are accepted as test requirements;
8. contradiction review finds no P1 authority conflict;
9. SDT remains `PROPOSED / NOT YET APPROVED` until its own acceptance criteria are satisfied.

## 8. Status

**PROPOSED / REQUIRES APPROVAL.**

This matrix formalizes C-004 integration without promoting unresolved SDT schema, persistence, mastery or temporal parameters to decisions.
