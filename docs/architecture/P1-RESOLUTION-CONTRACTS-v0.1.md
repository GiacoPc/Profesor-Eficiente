# P1 Reconciliation Contracts — v0.1

**Status:** PROPOSED / REQUIRES APPROVAL
**Scope:** Normative reconciliation contracts for C-001 through C-011.
**Purpose:** Remove cross-document ambiguity before LPH v1.0 and SRA.

> This artifact does not promote PAD, CLM, FDM, APE, LPH or SDT to APPROVED. It establishes explicit proposed contracts that must be incorporated into the corresponding specifications and then independently audited.

## Contract 1 — Authority hierarchy (C-001)

The authoritative hierarchy is:

```text
Curriculum Authority
        ↓
CLM learning-state semantics + FDM domain invariants
        ↓
SDT learner-state projection
        ↓
APE pedagogical decision authority
        ↓
LPH linguistic/interaction constraint + validation boundary
        ↓
LLM / bounded generation capability
        ↓
Learner interaction
        ↓
Evidence
```

LPH is **not** above APE, FDM or CLM. LPH may validate and constrain generation and linguistic processing, but cannot authorize pedagogical progression or mutate authoritative learner state.

## Contract 2 — Objective ownership/cardinality (C-002)

For reconciliation purposes:

```text
Curriculum 1 ── * Level
Level 1 ── * Unit
Unit 1 ── * Lesson
Lesson * ── * Competency
Competency * ── * Objective
Objective 1 ── * Criterion
```

`Objective` is a curriculum-authority entity. A competency may support one or more objectives, and an objective may map to one or more competencies where the curriculum explicitly defines that mapping. Criteria belong to the objective/competency assessment contract and must not be confused with separate objectives.

This replaces the ambiguous `Competency → Objective/criteria` wording. Final persistence cardinality remains pending schema validation.

## Contract 3 — Mastery Policy (C-003)

`MasteryPolicy` is an explicit governed contract referenced by lesson/competency evaluation.

Conceptual contract:

```yaml
mastery_policy_id: <stable-id>
version: <version>
competency_id: <id-or-scope>
required_evidence_types: [<type>]
minimum_evidence_conditions: <policy-defined>
assessment_rules: <policy-defined>
stability_requirements: <policy-defined>
transfer_requirements: <policy-defined>
uncertainty_policy: <policy-defined>
allowed_mastery_states: [<controlled-state>]
```

The policy defines mastery; APE, LPH and SDT may reference it but may not redefine its thresholds.

Exact numerical thresholds remain `PENDING/TBD`.

## Contract 4 — Evidence pipeline (C-006, C-011)

The authoritative sequence is:

```text
Raw observation / speech artifact
        ↓
Bounded processing
        ↓
Evidence candidate
        ↓
Evidence validation + provenance
        ↓
Assessment
        ↓
Accepted assessment evidence
        ↓
MasteryPolicy / learning-state interpretation
        ↓
MasteryRecord / ErrorObservation / other domain state
        ↓
SDT projection
        ↓
APE decision
```

Ownership:

- Speech/audio components own capture/measurement results within their contracts.
- LPH may orchestrate linguistic interpretation, constrain classification and validate candidate linguistic output.
- FDM owns authoritative evidence semantics, provenance, state mutation and invariants.
- CLM owns learning-state semantics.
- SDT is the governed learner-state projection.
- APE owns the pedagogical decision, not the evidence truth.

LPH cannot directly write authoritative mastery/progression state.

## Contract 5 — Error lifecycle (C-005)

The authoritative domain term is `ErrorObservation`.

`Error` may be used only as a human-facing/general category term; it is not a second authoritative entity.

Lifecycle:

```text
Evidence
  ↓
ErrorObservation candidate
  ↓
Validation / assessment
  ↓
Accepted ErrorObservation
  ↓
Derived recurrence/weakness summary
  ↓
SDT
```

`recurrence_count` is **not** authoritative by itself. Any recurrence metric must be computed under a future approved policy that considers exposure, evidence quality, spacing and context as required by CLM.

Historical ErrorObservation records are immutable; derived summaries may be recomputed.

## Contract 6 — Progression eligibility and APE PROGRESS (C-007, C-008)

`ProgressionEligibility` is a domain result. APE `PROGRESS` is a pedagogical action.

Conceptual eligibility:

```yaml
eligibility_id: <stable-id>
learner_id: <id>
lesson_id: <id>
status: <ELIGIBLE|INELIGIBLE|INSUFFICIENT_EVIDENCE|CONFLICT>
unsatisfied_prerequisite_ids: [<id>]
unsatisfied_mastery_ids: [<id>]
policy_versions: [<version>]
evidence_references: [<id>]
state_version: <version>
```

Hard precondition for APE `PROGRESS`:

```text
ProgressionEligibility.status == ELIGIBLE
AND
no mandatory prerequisite is unsatisfied
AND
all applicable mastery gates are satisfied
AND
snapshot is consistent/not stale
AND
no unresolved blocking conflict exists
```

If any hard precondition fails, APE cannot emit an authoritative `PROGRESS` action.

APE may choose `HOLD`, `REINFORCE`, `REASSESS`, or another permitted action when eligibility is not satisfied.

## Contract 7 — Mastery-policy reference boundary (C-009)

APE/LPH interfaces must use:

- `mastery_policy_id`;
- `mastery_policy_version`;
- applicable constraints/required evidence references.

They must **not** contain an authoritative ad-hoc threshold that overrides the governed policy.

Thus the phrase "mastery requirements" means a reference to the applicable governed policy, not a policy definition generated by APE or LPH.

## Contract 8 — Generation candidate lifecycle (C-010)

The authoritative generation lifecycle is:

```text
LLMRequest
   ↓
LLMGenerationCandidate (GENERATED)
   ↓
Schema / linguistic / pedagogical validation
   ├── REJECTED → discard candidate / repair / regenerate
   └── ACCEPTABLE → controlled delivery or explicit acceptance
```

A candidate is not learner evidence merely because it contains a classification or assessment-like statement.

If a candidate is converted into an assessment input, that conversion must create a separate assessment/evidence record with provenance identifying the candidate and the validating component/policy. LLM text cannot directly become authoritative mastery state.

Historical candidates are immutable records where persistence is required; repair creates a new candidate rather than rewriting the old one.

## Contract 9 — Linguistic assessment ownership (C-011)

LPH is responsible for **linguistic processing/validation boundaries**. FDM is responsible for **authoritative domain evidence semantics**.

Therefore:

```text
LPH linguistic assessment candidate
              ↓
        Evidence contract
              ↓
      FDM authoritative record
```

The term `assessment` must be qualified by role when necessary:

- `LinguisticAssessmentCandidate` = non-authoritative LPH result.
- `Assessment` = domain evaluation record tied to explicit criteria/policy.

Final names may be adjusted during FDM v0.2, but the authority boundary is normative.

## Contract 10 — Conflict and uncertainty

If authoritative inputs disagree, the system produces `CONFLICT` rather than silently selecting one.

If evidence is insufficient, the system produces `INSUFFICIENT_EVIDENCE` or the applicable controlled state.

Neither condition permits an LLM, LPH, APE or SDT to invent certainty.

## Contract 11 — State ownership

- FDM enforces domain invariants and authoritative mutations.
- CLM defines learning-state semantics.
- SDT represents derived learner state.
- APE selects pedagogical actions.
- LPH constrains/validates linguistic generation and candidate interpretation.
- LLM generates probabilistic candidates.

No layer may silently assume another layer's authority.

## Contract 12 — Acceptance gate

C-001 through C-011 are considered **RESOLVED AT CONTRACT LEVEL** only when:

1. these contracts are reviewed against PAD/CLM/FDM/APE/LPH/SDT;
2. corresponding source specifications incorporate or explicitly reference them;
3. the contradiction matrix dispositions are updated with exact artifact references;
4. automated consistency checks are added where applicable;
5. an independent secondary AI audit is completed for this P1 reconciliation;
6. human project approval is recorded.

Until then the project gate remains `NOT READY`.
