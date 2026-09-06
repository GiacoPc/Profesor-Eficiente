# Mastery Policy — v0.1

**Document ID:** MASTERY-POLICY
**Version:** 0.1-draft
**Status:** PROPOSED / REQUIRES APPROVAL
**Scope:** Authoritative policy contract for competency mastery evaluation
**Implementation status:** NONE — specification only

## 0. Governance status

This document formalizes the `MasteryPolicy` contract required by P1 C-003. It defines the policy boundary and required policy inputs without inventing numerical thresholds that have not yet been validated.

`PENDING`, `TBD`, and `UNKNOWN` values are not implicit defaults and must not be replaced by an AI-generated value.

## 1. Purpose

`MasteryPolicy` defines the governed rules used to determine whether evidence is sufficient to assign a controlled mastery state to a competency.

It is a policy contract, not a learner-state snapshot, pedagogical decision, linguistic generation result, or LLM prompt.

## 2. Authority

`MasteryPolicy` is governed project data/policy.

Consumers may reference an applicable policy by stable identity and version, but may not redefine its authoritative thresholds or requirements locally.

Authority boundary:

```text
Governed MasteryPolicy
        ↓
Evidence + Assessment
        ↓
Mastery evaluation
        ↓
MasteryRecord / state
        ↓
ProgressionEligibility
        ↓
APE pedagogical action
```

The LLM, LPH, APE, SDT, learner dialogue, or UI cannot override the applicable policy at runtime.

## 3. Conceptual contract

```yaml
mastery_policy_id: <stable-id>
version: <version>
scope:
  competency_ids: [<id>]
  curriculum_version: <version-or-scope>
required_evidence_types: [<type>]
minimum_evidence_conditions: <policy-defined>
assessment_rules: <policy-defined>
stability_requirements: <policy-defined>
transfer_requirements: <policy-defined>
uncertainty_policy: <policy-defined>
allowed_mastery_states: [<controlled-state>]
progression_gate_reference: <policy-reference>
status: <PROPOSED|APPROVED|DEPRECATED|SUPERSEDED>
```

This schema is conceptual and not the final persistence schema.

## 4. Policy dimensions

The policy may govern, where applicable:

- required evidence modalities;
- minimum evidence conditions;
- assessment criteria and aggregation;
- temporal stability;
- transfer/generalization evidence;
- uncertainty handling;
- admissible mastery states;
- reassessment conditions;
- progression-gate references.

Exact numerical thresholds, counts, confidence cutoffs, time windows, and weighting are `PENDING/TBD` until validated by the pedagogical authority and evidence.

## 5. Competency specificity

Mastery is competency-specific.

A policy must identify the competency scope or an explicitly governed policy family. A universal threshold must not be assumed merely because it is convenient for implementation.

Different competencies may require different evidence modalities or stability/transfer conditions.

## 6. Evidence and assessment boundary

A `MasteryPolicy` consumes governed assessment inputs; it does not manufacture evidence.

The minimum conceptual flow is:

```text
Observation
  ↓
Evidence
  ↓
Assessment
  ↓
MasteryPolicy evaluation
  ↓
MasteryRecord
```

Insufficient, uncertain, rejected, or conflicting evidence cannot be silently promoted to mastery.

## 7. Mastery states

The policy may permit controlled states such as:

```text
NOT_ASSESSED
INSUFFICIENT_EVIDENCE
DEVELOPING
NEAR_MASTERY
MASTERED
REASSESSMENT_REQUIRED
```

These names remain `PROPOSED` until CLM/FDM reconciliation and approval.

## 8. Progression boundary

Mastery policy evaluation contributes to `ProgressionEligibility` but does not itself become an APE action.

```text
MasteryPolicy evaluation
        ↓
Mastery state/evidence
        ↓
ProgressionEligibility
        ↓
APE may select PROGRESS only if all hard gates are satisfied
```

APE cannot bypass an unsatisfied mastery requirement by selecting a different action or by asking an LLM to declare mastery.

## 9. Policy versioning and reproducibility

Every authoritative mastery evaluation must identify the applicable `mastery_policy_id` and version.

A policy change must not rewrite historical evaluations silently. Historical records must retain sufficient policy provenance to explain the decision made at the time.

Policy replacement/deprecation must be explicit and governed.

## 10. Uncertainty and conflict

The policy must define controlled handling for:

- insufficient evidence;
- uncertain assessment;
- conflicting evidence;
- unavailable required evidence.

Until exact rules are approved, these conditions remain non-mastery and must not be converted into certainty by probabilistic components.

## 11. Runtime consumers

The following components may consume policy references:

- CLM — interprets learning-state semantics under the policy;
- SDT — represents resulting learner state and policy provenance;
- APE — uses policy results/references for pedagogical decisions;
- LPH — receives policy references/constraints where linguistic validation depends on mastery requirements;
- FDM — enforces domain invariants and authoritative mutation boundaries.

None of these consumers may redefine the policy.

## 12. Invariants

### MP-I01 — Explicit policy identity

Every authoritative mastery evaluation identifies an applicable policy and version.

### MP-I02 — No consumer override

APE, LPH, LLM, SDT, UI, or learner interaction cannot override authoritative policy requirements at runtime.

### MP-I03 — Evidence sufficiency

Mastery cannot be assigned when mandatory evidence conditions are not satisfied.

### MP-I04 — Uncertainty preservation

Uncertain or conflicting evidence cannot silently become verified mastery.

### MP-I05 — Historical policy integrity

Historical mastery evaluations retain their applicable policy provenance.

### MP-I06 — Competency specificity

A mastery policy applies only to its declared competency scope or explicitly governed policy family.

## 13. Required validation

Before `MasteryPolicy v1.0` becomes `APPROVED`, the project must validate:

- CEFR/MCER competency requirements;
- evidence modality requirements;
- mastery-state semantics in CLM;
- FDM MasteryRecord and ProgressionEligibility contracts;
- APE decision boundary;
- LPH policy-reference boundary;
- numerical thresholds and aggregation rules;
- uncertainty/conflict behavior;
- deterministic test cases;
- historical reproducibility requirements.

## 14. Status

**PROPOSED / REQUIRES APPROVAL.**

No numerical mastery threshold is asserted by this artifact.
