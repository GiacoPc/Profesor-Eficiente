# C-007 / C-008 — Progression Eligibility & APE PROGRESS Contract

**Version:** 0.1-draft  
**Status:** PROPOSED / REQUIRES APPROVAL  
**Scope:** Separation between authoritative domain eligibility and APE pedagogical progression action.

## 1. Problem

The system must distinguish two different questions:

1. **Is the learner objectively eligible to progress?** → `ProgressionEligibility`.
2. **What should the tutor do next?** → APE pedagogical decision.

`PROGRESS` must never become a second, informal mastery/progression evaluator.

## 2. Normative authority

```text
Curriculum / prerequisites
        ↓
Accepted evidence + assessments
        ↓
MasteryPolicy evaluation
        ↓
MasteryRecord / learner state
        ↓
ProgressionEligibility
        ↓
APE decision
        ↓
PROGRESS | HOLD | REINFORCE | REASSESS | other permitted action
```

`ProgressionEligibility` is an authoritative domain result. APE consumes it; APE does not redefine it.

## 3. ProgressionEligibility contract

Conceptual v0.1 structure:

```yaml
eligibility_id: <stable-id>
learner_id: <stable-id>
current_lesson_id: <stable-id>
target_lesson_id: <stable-id-or-null>
status: ELIGIBLE | INELIGIBLE | INSUFFICIENT_EVIDENCE | CONFLICT
unsatisfied_prerequisite_ids: [<id>]
unsatisfied_mastery_ids: [<id>]
mastery_policy_refs:
  - policy_id: <id>
    version: <version>
evidence_references: [<id>]
assessment_references: [<id>]
state_version: <version>
evaluated_at: <timestamp>
reason_codes: [<controlled-code>]
```

Exact schema, persistence representation and reason-code taxonomy remain `PENDING/TBD`.

## 4. Hard gates for PROGRESS

APE may emit an authoritative `PROGRESS` action only if all mandatory gates are satisfied:

```text
ProgressionEligibility.status == ELIGIBLE
AND
all mandatory prerequisites satisfied
AND
all applicable mastery gates satisfied
AND
required evidence is sufficient
AND
applicable MasteryPolicy identity/version is valid
AND
learner-state snapshot is consistent / not stale
AND
no unresolved blocking CONFLICT exists
AND
requested transition is valid for the current curriculum state
```

These are **hard gates**, not preferences.

If any hard gate fails, APE cannot authorize `PROGRESS`.

## 5. Status semantics

### ELIGIBLE

All mandatory conditions required for the evaluated transition are satisfied at the evaluation snapshot.

### INELIGIBLE

At least one mandatory prerequisite or mastery condition is not satisfied.

### INSUFFICIENT_EVIDENCE

The system lacks enough valid evidence to establish eligibility. This is not equivalent to learner failure.

### CONFLICT

Blocking authoritative inputs disagree or cannot be reconciled under current governance. The system must not silently choose a favorable interpretation.

## 6. APE behavior

APE receives the eligibility result and determines the pedagogical response within its authority.

Examples:

```text
ELIGIBLE
   → PROGRESS (when pedagogically appropriate and transition is valid)

INELIGIBLE
   → REINFORCE / PRACTICE / REASSESS / HOLD

INSUFFICIENT_EVIDENCE
   → ASSESS / REASSESS / PRACTICE / HOLD

CONFLICT
   → HOLD / REASSESS / controlled conflict handling
```

The exact action taxonomy remains governed by the APE specification and is not redefined here.

`ELIGIBLE` does not mean APE is forced to progress immediately; it means the hard eligibility barrier is open. APE retains pedagogical decision authority over timing/action, subject to curriculum and domain constraints.

Conversely, APE cannot turn `INELIGIBLE`, `INSUFFICIENT_EVIDENCE` or blocking `CONFLICT` into `PROGRESS` through conversational preference, LLM persuasion or an ad-hoc threshold.

## 7. Snapshot consistency

Eligibility is evaluated against a state snapshot/version.

A progression action must verify that the authoritative state has not changed in a way that invalidates the eligibility result between evaluation and action.

Conceptually:

```text
EvaluateEligibility(state_version = V)
             ↓
ProgressionEligibility(V)
             ↓
APE requests PROGRESS
             ↓
FDM/domain validation checks current version
             ↓
if compatible → authorize transition
if stale/conflicting → reject/hold/re-evaluate
```

This prevents stale mastery or prerequisite state from authorizing progression.

## 8. Mastery precedence

Mastery is evaluated through the explicit applicable `MasteryPolicy`. APE cannot replace that policy with an internal score.

Progression therefore follows:

```text
Evidence
 → Assessment
 → MasteryPolicy
 → Mastery state
 → ProgressionEligibility
 → APE action
```

A learner being conversationally fluent in an interaction does not itself override a mandatory curriculum mastery gate.

## 9. Prerequisite precedence

Mandatory curriculum prerequisites are hard constraints. APE may select reinforcement or reassessment but cannot waive a prerequisite unless the curriculum/domain contract explicitly permits that transition.

A recommendation to skip a prerequisite is not an authoritative progression command.

## 10. No hidden mastery inference

The following cannot establish eligibility by themselves:

- LLM confidence;
- conversational fluency impression;
- STT confidence;
- pronunciation-model score;
- acoustic/prosodic score;
- learner self-report;
- UI state;
- previous APE recommendation.

They may contribute evidence where the applicable curriculum, assessment and MasteryPolicy allow it, but they cannot bypass the governed chain.

## 11. Conflict handling

Blocking conflicts must be represented explicitly.

Examples:

```text
MasteryRecord says MASTERED
but required evidence is stale/invalid
→ eligibility must not silently become ELIGIBLE.

Prerequisite state changed after eligibility evaluation
→ stale eligibility → re-evaluate.

Two authoritative assessments conflict
→ CONFLICT under applicable resolution policy.
```

Exact conflict-resolution policy remains `PENDING/TBD` where not already governed.

## 12. Failure neutrality

Technical or processing failures do not automatically imply `INELIGIBLE`.

Where required evidence cannot be established because a component failed, the result should normally be `INSUFFICIENT_EVIDENCE` or a controlled unavailable state, according to the final domain/error contract.

This preserves the distinction between **learner has not demonstrated mastery** and **system failed to obtain valid evidence**.

## 13. Invariants

**P78-I01 — Domain authority:** `ProgressionEligibility` is authoritative domain state/result, not an LLM/APE-local opinion.

**P78-I02 — Hard gate:** APE cannot emit `PROGRESS` when mandatory eligibility is not satisfied.

**P78-I03 — Policy identity:** applicable mastery policy ID/version is attributable.

**P78-I04 — Prerequisite integrity:** mandatory prerequisites cannot be silently waived.

**P78-I05 — Evidence sufficiency:** insufficient evidence cannot become eligibility through inference.

**P78-I06 — Snapshot integrity:** stale eligibility cannot authorize an incompatible transition.

**P78-I07 — Conflict integrity:** blocking conflict prevents authoritative progression until governed resolution/reassessment.

**P78-I08 — Separation:** eligibility and pedagogical action remain separate concepts and records.

**P78-I09 — Failure neutrality:** technical failure does not become learner failure.

**P78-I10 — Traceability:** progression action references the eligibility evaluation/state version on which it relies.

## 14. Acceptance tests

- **P78-T01:** `INELIGIBLE` cannot produce authoritative `PROGRESS`.
- **P78-T02:** `INSUFFICIENT_EVIDENCE` cannot produce authoritative `PROGRESS`.
- **P78-T03:** blocking `CONFLICT` cannot produce authoritative `PROGRESS`.
- **P78-T04:** unsatisfied mandatory prerequisite blocks `PROGRESS`.
- **P78-T05:** missing/stale MasteryPolicy blocks authoritative eligibility/mastery interpretation.
- **P78-T06:** APE cannot use an ad-hoc threshold to override `ProgressionEligibility`.
- **P78-T07:** stale eligibility is rejected when authoritative state changed incompatibly.
- **P78-T08:** technical evidence-processing failure does not automatically mark the learner ineligible for lack of performance.
- **P78-T09:** a conversationally convincing LLM response cannot independently establish progression eligibility.
- **P78-T10:** every authoritative `PROGRESS` action references the eligibility result and compatible state version.
- **P78-T11:** `ELIGIBLE` permits progression but does not force immediate progression when APE has a valid pedagogical reason to consolidate/reassess.
- **P78-T12:** a prerequisite waiver is rejected unless explicitly authorized by curriculum/domain policy.

## 15. Open decisions

- exact eligibility reason-code taxonomy;
- target transition representation;
- policy for optional versus mandatory prerequisites;
- exact stale-version/conflict resolution semantics;
- persistence/event schema;
- transactional/concurrency mechanism;
- exact mapping to APE action taxonomy;
- numerical mastery thresholds and stability/transfer requirements;
- automated executable checks.

## 16. Status

**PROPOSED / REQUIRES APPROVAL.**

C-007/C-008 are formally reconciled at contract level. This document does not claim implementation, empirical validation, source-spec integration, CI success or final approval.
