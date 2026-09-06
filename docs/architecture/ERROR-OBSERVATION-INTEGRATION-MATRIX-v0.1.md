# C-005 — ErrorObservation Integration Matrix

**Document ID:** ERROR-OBSERVATION-INTEGRATION-MATRIX
**Version:** 0.1
**Status:** PROPOSED / REQUIRES APPROVAL
**Branch:** `architecture/pad-clm-fdm-ape-v1.0`
**Scope:** Cross-document integration of `ErrorObservation` lifecycle.

## 1. Canonical contract

`docs/architecture/ERROR-OBSERVATION-LIFECYCLE-v0.1.md` is the canonical contract for terminology, lifecycle, authority and recurrence semantics.

It does not replace PAD, CLM, FDM, APE or LPH. Those artifacts retain their bounded responsibilities and reference this contract rather than independently redefining `ErrorObservation` semantics.

## 2. Cross-document integration

| Artifact | Responsibility | C-005 integration | Authority limit |
|---|---|---|---|
| PAD | Defines correction/reinforcement pedagogy | Learner output → evidence → assessment → error/strength classification → feedback → practice → reassessment | PAD does not create authoritative error records or redefine lifecycle state |
| CLM | Defines learning-state semantics | Accepted `ErrorObservation` feeds error/weakness state; recurrence is derived, not a raw counter | CLM interprets state; it does not fabricate observations |
| FDM | Owns domain entity/events/invariants | `ErrorObservation` is canonical authoritative domain record; candidate and accepted states are separated | FDM enforces evidence provenance, historical integrity and candidate isolation |
| APE | Selects pedagogical action | Uses accepted error/weakness state to prioritize reinforcement/reassessment | APE does not invent error facts or mutate historical observations directly |
| SDT | Represents derived learner state | Stores references/derived error summaries rather than replacing error history | SDT has no error-authority or pedagogical decision authority |
| LPH | Linguistic processing/validation | May produce `ErrorObservationCandidate` from bounded linguistic evidence | LPH/LLM cannot directly create authoritative error state |

## 3. Canonical lifecycle

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
ErrorObservation
   ↓
CLM error/weakness interpretation
   ↓
SDT projection
   ↓
APE reinforcement/reassessment decision
   ↓
new evidence
```

## 4. Critical distinctions

1. An observation is not automatically an error.
2. An LLM classification is not automatically an authoritative `ErrorObservation`.
3. Feedback is not an error record.
4. A recurrence count is not an error record.
5. SDT summaries do not replace historical `ErrorObservation` records.
6. Resolution of an error does not delete or rewrite its historical observation.
7. Later evidence may reopen an error pattern without mutating historical observations.

## 5. Minimum authoritative provenance

An accepted `ErrorObservation` must be traceable to:

- `error_id`;
- source `evidence_id`;
- assessment/provenance information;
- affected competency when determinable;
- governed error category when determinable;
- uncertainty status;
- governing policy where applicable.

## 6. Recurrence boundary

```text
Accepted ErrorObservation history
          ↓
Approved recurrence policy
          ↓
RecurrenceSummary
          ↓
CLM / SDT
          ↓
APE
```

No raw `recurrence_count` may independently establish mastery failure, reinforcement need, or learner trait.

## 7. C-005 acceptance tests

- **EO-T01:** no authoritative error without source evidence.
- **EO-T02:** LLM/LPH candidate cannot bypass acceptance.
- **EO-T03:** rejected candidate produces no authoritative error mutation.
- **EO-T04:** uncertain classification remains uncertain/non-authoritative until governed acceptance.
- **EO-T05:** accepted historical observation is immutable.
- **EO-T06:** recurrence is derived from accepted history under approved policy.
- **EO-T07:** SDT cannot replace canonical error history.
- **EO-T08:** APE cannot create an error merely because reinforcement is desired.
- **EO-T09:** feedback delivery cannot itself establish error truth.
- **EO-T10:** later valid evidence can change active/resolved status without rewriting history.

## 8. Gate

C-005 is integrated at contract level when the canonical lifecycle is referenced by the source specifications, the FDM mutation boundary is explicit, recurrence remains policy-derived, and authority tests are accepted.

Final taxonomy, severity, recurrence formula, persistence schema and event schema remain `PENDING` and block v1.0 approval.

**Status: PROPOSED / REQUIRES APPROVAL.**
