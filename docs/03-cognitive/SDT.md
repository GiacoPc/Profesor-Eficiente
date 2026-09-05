# Student Digital Twin (SDT) — Contract

**Document ID:** SDT
**Version:** 0.1-draft
**Status:** PROPOSED / NOT YET APPROVED
**Scope:** Governed representation of the learner's evidenced learning state
**Authority:** CLM defines learning-state semantics; FDM defines domain invariants; APE consumes SDT for pedagogical decisions.
**Implementation status:** NONE — specification only

## 0. Purpose

The Student Digital Twin (SDT) is the governed, evidence-backed representation of the learner state required for pedagogical adaptation. It is **not** a generative profile, psychological clone, raw event log, or free-form LLM memory.

SDT exists to provide APE with a consistent learner-state snapshot while preserving provenance, uncertainty, temporal validity, and policy/version references.

## 1. Authority and boundaries

The authority chain is:

```text
Observed input
    ↓
Evidence
    ↓
Assessment
    ↓
CLM learning-state interpretation
    ↓
SDT projection/snapshot
    ↓
APE pedagogical decision
    ↓
FDM invariant enforcement
```

Rules:

1. LLM output cannot directly mutate SDT.
2. APE can request state-changing domain commands but cannot bypass FDM invariants.
3. SDT cannot redefine curriculum, objectives, prerequisites, or mastery policy.
4. SDT must preserve uncertainty when evidence is insufficient.
5. Historical evidence is not rewritten to make the current SDT appear consistent.

## 2. SDT versus source data

SDT is a **derived state representation**. It must not become the sole historical record.

```text
Authoritative evidence/event history
              |
              v
       CLM interpretation
              |
              v
        SDT projection
              |
              v
       APE decision input
```

A repair/rebuild operation must be able to identify the evidence and policy versions from which a state was derived, subject to the final persistence/recovery architecture.

## 3. Snapshot identity and consistency

Every consumable SDT snapshot must expose at least:

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

Exact encoding and persistence semantics are `TBD`.

APE must not make an authoritative decision from a snapshot whose status is `CONFLICT` unless an explicit conflict policy permits a bounded action.

## 4. State domains

### 4.1 Curriculum position

- current level/band;
- current unit/module;
- current lesson;
- active objective identifiers;
- active competency identifiers;
- prerequisite status;
- progression eligibility reference.

Curriculum values are references to governed curriculum data, not copies that can be edited by the SDT.

### 4.2 Competency state

For each relevant competency:

```yaml
competency_id: <id>
mastery_state: <controlled-state>
evidence_sufficiency: <SUFFICIENT|INSUFFICIENT|UNCERTAIN>
confidence_status: <policy-defined>
active_weakness_ids: [<id>]
recurrence_summary: <policy-defined>
stability_status: <policy-defined>
last_assessed_at: <timestamp>
mastery_policy_version: <version>
```

The exact mastery state machine and numerical thresholds remain `PENDING`.

### 4.3 Error/weakness state

SDT stores **references and derived summaries** of `ErrorObservation` records rather than replacing evidence with a single counter.

Conceptual fields:

- active error/weakness identifiers;
- affected competency;
- category;
- evidence count/coverage summary where policy defines it;
- recurrence status;
- last observed time;
- improvement status;
- reinforcement need.

Raw evidence remains in the authoritative evidence layer.

### 4.4 Strategy state

Strategy-related state may represent observed effectiveness of pedagogical interventions, but only when supported by evidence.

It must distinguish:

- learner-stated preference;
- observed difficulty;
- measured intervention effectiveness;
- APE-selected strategy.

A preference alone cannot be treated as evidence that a strategy is pedagogically effective.

### 4.5 Pace/adherence

Only pedagogically justified measures may enter SDT. The model must not become a generalized behavioral-surveillance profile.

## 5. Evidence linkage

Every authoritative derived state element must be traceable to one or more evidence/assessment references or to a governed curriculum/policy reference.

Conceptual:

```yaml
state_element_id: <stable-id>
value: <derived-value>
source_evidence_ids: [<evidence-id>]
source_assessment_ids: [<assessment-id>]
policy_version: <version>
derivation_status: <DERIVED|INSUFFICIENT|UNCERTAIN>
```

Exact representation is `PENDING`.

## 6. Mastery boundary

SDT does not define mastery policy. It carries the result of applying the authoritative `MasteryPolicy` to competency evidence.

```text
Competency evidence
      ↓
Assessment
      ↓
MasteryPolicy
      ↓
MasteryRecord
      ↓
SDT competency state
```

If the policy is undefined, SDT must represent the state as policy-undefined/insufficient rather than inventing a threshold.

## 7. Progression boundary

SDT carries `ProgressionEligibility` as a domain result/reference. It does not decide progression.

```text
Mastery + prerequisites + applicable policy
                 ↓
      ProgressionEligibility
                 ↓
              SDT
                 ↓
               APE
```

`ELIGIBLE` is a necessary condition for APE `PROGRESS`; it is not by itself an instruction to progress.

## 8. Temporal behavior

SDT must distinguish current state from historical evidence.

A competency can move from apparent mastery to reassessment-required when later valid evidence demonstrates instability, regression, or insufficient transfer according to policy.

No forgetting curve, decay coefficient, recurrence formula, or temporal threshold is fixed by SDT v0.1.

## 9. Uncertainty and conflict

SDT supports explicit states for:

- `VALID`;
- `STALE`;
- `INSUFFICIENT_EVIDENCE`;
- `CONFLICT`.

The final controlled vocabulary may be refined by FDM/SRA, but uncertainty must never be silently collapsed into success.

When two authoritative inputs conflict, SDT records the conflict condition and preserves provenance; it does not arbitrarily select a winner.

## 10. Update contract

The proposed update sequence is:

```text
Capture observation
      ↓
Validate evidence
      ↓
Assess evidence
      ↓
Apply learning-state policy
      ↓
Update authoritative evidence/state
      ↓
Project SDT version N+1
      ↓
APE reads consistent snapshot
```

The exact transaction/event mechanism remains a later SRA decision.

## 11. Concurrency rule

A stale SDT snapshot must not overwrite a newer authoritative state.

A decision referencing `state_version=N` must be rejected, retried, or explicitly revalidated if execution detects that the authoritative state has advanced beyond N, according to the final consistency policy.

## 12. Offline requirement

The SDT critical path must be available offline after required local assets are provisioned. Remote services cannot be required to maintain authoritative learner state or progression eligibility.

## 13. Privacy boundary

SDT should contain the minimum derived learner data required for pedagogy. Raw audio, raw transcripts, and other large/sensitive artifacts should be referenced rather than duplicated into every SDT snapshot where possible.

Retention, deletion, encryption, and access rules belong to the data/security architecture and remain `PENDING`.

## 14. Testable invariants

**SDT-I01 — Evidence linkage:** authoritative state has traceable provenance.

**SDT-I02 — No LLM mutation:** LLM output cannot directly mutate authoritative SDT.

**SDT-I03 — Uncertainty preservation:** uncertain/insufficient evidence cannot become verified mastery without a policy-governed transition.

**SDT-I04 — Policy reference:** mastery state identifies the applicable mastery-policy version.

**SDT-I05 — Progression separation:** SDT carries eligibility; APE selects pedagogical action.

**SDT-I06 — Historical integrity:** SDT projection cannot rewrite historical evidence.

**SDT-I07 — Version consistency:** stale snapshots cannot silently overwrite newer state.

**SDT-I08 — Offline critical path:** authoritative learner-state maintenance does not require a network service.

## 15. Dependencies

- PAD: pedagogical state requirements;
- CLM: learning-state semantics;
- FDM: entities, invariants, events and mutation boundaries;
- APE: decision input/output contract;
- LPH: linguistic evidence and assessment boundary;
- data/security architecture: persistence and privacy.

## 16. Open decisions

- final schema/serialization;
- mastery state machine and thresholds;
- evidence sufficiency/confidence policy;
- recurrence calculation;
- temporal stability model;
- transfer criteria;
- intervention-effectiveness model;
- persistence/transaction model;
- retention/deletion values.

## 17. Acceptance criteria for SDT v1.0

SDT cannot become `APPROVED` until:

1. CLM semantics map one-to-one to the required state domains;
2. FDM entities/events and mutation boundaries are mapped;
3. APE snapshot contract is finalized;
4. MasteryPolicy and ProgressionEligibility contracts are approved;
5. evidence provenance is testable;
6. concurrency/replay semantics are specified;
7. privacy/data contracts are reconciled;
8. independent review is completed for the applicable risk class.

## 18. Status

**PROPOSED / NOT YET APPROVED.**

SDT v0.1 closes the previously missing-artifact gap by defining the learner-state contract, while deliberately leaving numerical mastery, retention, and persistence choices unresolved.
