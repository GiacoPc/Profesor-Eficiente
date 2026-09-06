# Adaptive Pedagogical Engine (APE)

**Document ID:** APE
**Version:** 0.1-draft
**Status:** PROPOSED / NOT YET APPROVED
**Scope:** Pedagogical decision engine for Profesor-Eficiente
**Implementation status:** NONE — specification only

## 0. Governance status

APE formalizes the intended pedagogical decision authority from zero. It does not select a concrete AI model, inference runtime, database, Android implementation, or optimization strategy.

The APE is a governed decision component. It may consume probabilistic evidence, but its authoritative outputs must be constrained by explicit policy and domain invariants.

## 1. Purpose

APE determines **what the tutor should do next, why it should do it, and under what constraints**, based on curriculum authority and the learner's evidenced state.

APE is the intended "director de orquesta" of the pedagogical process.

## 2. Authority boundary

APE has pedagogical decision authority, but it does not own every piece of truth.

```text
Curriculum authority ─────┐
                          │
CLM / SDT learner state ──┼→ APE → pedagogical action
                          │
FDM domain constraints ───┘
```

The LLM is a bounded capability invoked by the resulting action specification.

## 3. What APE may decide

Subject to approved policies, APE may determine:

- which lesson/activity should run;
- which objective/competency should be targeted;
- whether reinforcement is needed;
- which weakness has priority;
- which activity mode is appropriate;
- difficulty within approved bounds;
- correction/reinforcement strategy;
- whether the learner is eligible for assessment or reassessment;
- whether progression is pedagogically appropriate when domain eligibility permits it;
- what constraints should be supplied to the generation/linguistic layer.

## 4. What APE may not decide arbitrarily

APE must not:

- rewrite authoritative curriculum;
- silently change CEFR/MCER objectives;
- invent prerequisites;
- bypass mandatory prerequisites;
- redefine mastery thresholds without an approved policy change;
- erase historical learner evidence;
- convert insufficient evidence into verified mastery;
- make a remote service a hidden pedagogical dependency;
- delegate its authority wholesale to an LLM.

If a required policy is undefined, APE must enter a controlled `POLICY_UNDEFINED` / equivalent state rather than inventing a value.

## 5. Inputs

APE conceptually consumes:

### 5.1 Curriculum contract

- current curriculum version;
- lesson;
- objectives;
- competency targets;
- prerequisites;
- permitted activities;
- mastery-policy reference (`mastery_policy_id` + `mastery_policy_version`).

### 5.2 Learner state contract

- SDT snapshot/version;
- competency mastery states;
- evidence sufficiency;
- active weaknesses;
- recurring errors;
- recent performance;
- reinforcement requirements;
- progression eligibility;
- applicable mastery-policy reference/provenance.

### 5.3 Context contract

- current session;
- current activity state;
- learner response/evidence available for decision;
- applicable policy versions;
- safety/governance constraints.

### 5.4 Capability contract

APE may know which local capabilities are available, such as speech recognition, pronunciation assessment, TTS, or LLM generation, but pedagogical semantics must not depend on a specific vendor/model name.

## 6. Output

APE should produce a structured `PedagogicalDecision` rather than free-form instructions.

Conceptual contract:

```yaml
decision_id: <stable-id>
state_version: <learner-state-version>
lesson_id: <lesson-id>
objective_ids: [<id>]
competency_ids: [<id>]
action: <teach|practice|assess|reinforce|reassess|consolidate|progress|hold>
rationale_codes: [<controlled-code>]
constraints:
  linguistic: <reference>
  interaction: <reference>
  correction: <reference>
  mastery_policy:
    id: <mastery-policy-id>
    version: <mastery-policy-version>
required_evidence: [<type>]
next_allowed_states: [<state>]
policy_versions: [<version>]
```

The `mastery_policy` fields are references, not an embedded ad-hoc policy definition. Exact schema is `PENDING`.

## 7. Decision cycle

```text
1. Load authoritative curriculum context
2. Load consistent learner/SDT snapshot
3. Determine current domain state
4. Check prerequisites
5. Resolve applicable MasteryPolicy reference
6. Identify target objective/competency
7. Evaluate evidence sufficiency
8. Select pedagogical action
9. Apply constraints/policies
10. Emit structured decision
11. Execute action
12. Collect new evidence
13. Re-evaluate
```

The cycle is deterministic once all policy inputs and assessed evidence are fixed, although some inputs may originate from probabilistic components.

If the applicable MasteryPolicy cannot be resolved consistently, APE must not substitute an ad-hoc threshold; it must use the controlled policy/conflict handling defined by the domain contracts.

## 8. Decision priority

APE requires a conflict-resolution hierarchy. Proposed ordering:

```text
Safety / governance constraints
        ↓
Curriculum authority
        ↓
Mandatory prerequisites
        ↓
Mastery / assessment policy
        ↓
Current evidenced learner need
        ↓
Pedagogical optimization
        ↓
Conversational preference
```

This ordering is `PROPOSED` and requires approval.

## 9. State-dependent actions

APE should select among controlled action classes rather than arbitrary free-form plans.

### `TEACH`
Introduce or model material required by the current objective.

### `PRACTICE`
Provide controlled practice for an objective/competency.

### `ASSESS`
Collect evidence needed to evaluate a competency.

### `REINFORCE`
Target an evidenced weakness or unstable mastery state.

### `REASSESS`
Collect new evidence after intervention.

### `CONSOLIDATE`
Reuse a competency in varied contexts when curriculum/policy requires stability or transfer.

### `HOLD`
Do not progress because evidence/policy is insufficient.

### `PROGRESS`
Request the next eligible pedagogical state only when domain and mastery policies permit it.

Exact action taxonomy is `PENDING`.

## 10. Mastery decision boundary

APE must not treat an LLM's natural-language statement such as "you mastered this" as mastery evidence by itself.

Instead:

```text
Evidence
  ↓
Assessment
  ↓
MasteryPolicy (identity + version)
  ↓
Mastery state
  ↓
Progression eligibility
  ↓
APE action
```

APE can request assessment/reassessment but must not invent or locally override the MasteryPolicy scoring algorithm, thresholds, evidence requirements, stability requirements, or transfer requirements.

## 11. Reinforcement selection

APE should prioritize reinforcement using evidence such as:

- active competency weakness;
- recurrence;
- recent failed/uncertain evidence;
- insufficient evidence;
- instability after apparent mastery;
- transfer failure.

Potential interventions include retrieval, chunking, shadowing, controlled repetition, communicative reuse, and targeted explanation.

Exact scoring/prioritization function is `TBD`.

## 12. Adaptation constraints

APE may adapt execution inside approved bounds.

For example:

```text
Approved objective
      |
      +--> easier exercise
      +--> standard exercise
      +--> harder exercise
      +--> speech practice
      +--> text practice
```

provided the selected action remains valid for the competency and policy.

APE may not use adaptivity as a mechanism to evade a mastery gate.

## 13. LLM orchestration

APE does not prompt the LLM directly with unconstrained "teach whatever is appropriate" authority.

Instead:

```text
APE decision
   ↓
LPH task/constraint contract
   ↓
LLM Gateway
   ↓
Candidate generation
   ↓
LPH validation
   ↓
Controlled delivery
```

The LLM receives a bounded pedagogical task.

## 14. LLM failure behavior

If generation fails, APE must be able to select a fallback action without changing the learner's authoritative state incorrectly.

Examples:

- malformed output → regenerate/fallback;
- unsupported linguistic claim → reject candidate;
- unavailable model → local alternate capability or non-LLM fallback if defined;
- insufficient assessment evidence → request additional evidence;
- conflicting evidence → hold/reassess according to policy.

Exact fallback matrix is `PENDING`.

## 15. Evidence and provenance

Every authoritative APE decision should be traceable to:

- learner-state snapshot/version;
- curriculum version;
- applicable MasteryPolicy ID/version;
- relevant evidence references;
- decision ID;
- decision timestamp;
- outcome where available.

This permits retrospective audit without relying on conversation history.

## 16. Determinism

APE should be deterministic for identical:

- authoritative curriculum state;
- learner-state snapshot;
- evidence set;
- policy versions;
- capability availability;
- deterministic randomization seed, if randomized activity selection is later approved.

If a probabilistic component is an input, its uncertainty/provenance must remain explicit.

## 17. Contradiction handling

If APE receives conflicting authoritative inputs, it must not silently choose one.

Examples:

```text
curriculum says prerequisite satisfied
          vs
learner state says prerequisite unsatisfied
```

Result should be a controlled `CONFLICT` / escalation state until the source-of-truth discrepancy is resolved.

Likewise, if evidence is insufficient for a mastery decision, the correct outcome is not fabricated certainty.

If the applicable MasteryPolicy is undefined, unavailable, stale, or conflicting, APE must not invent or infer a replacement policy.

## 18. Offline-first requirement

The APE's critical decision path must function without network access after required local assets are provisioned.

No remote LLM may be a mandatory prerequisite for:

- deciding the current pedagogical state;
- enforcing prerequisites;
- evaluating progression eligibility;
- maintaining authoritative learner state.

## 19. Performance boundary

APE is a policy/decision component and must not require large-model inference for deterministic state transitions or policy checks.

Resource-heavy generation/assessment should remain behind bounded capability interfaces.

No CPU/RAM/NPU/GPU target is asserted here without measurement.

## 20. Security/privacy

APE should receive the minimum learner data required for the pedagogical decision.

Sensitive raw audio or other raw artifacts should be referenced through controlled evidence identifiers where possible rather than copied into every decision payload.

Exact data minimization, encryption, retention, and access policy are `PENDING`.

## 21. Testing contract

Minimum tests:

- prerequisite enforcement;
- mastery-gate enforcement;
- mastery-policy identity/version resolution;
- rejection of ad-hoc mastery thresholds;
- reinforcement selection;
- deterministic replay;
- conflict handling;
- insufficient-evidence handling;
- invalid curriculum/reference handling;
- LLM-independent progression tests;
- offline decision tests;
- state-version/concurrency tests;
- provenance/traceability tests.

A key acceptance test is:

> Removing or replacing the LLM must not permit invalid progression or corrupt authoritative learner state.

## 22. Open decisions

- exact decision state machine;
- exact MasteryPolicy schema;
- exact numerical mastery thresholds and aggregation rules;
- exact SDT schema;
- exact evidence sufficiency rules;
- intervention selection algorithm;
- conflict-resolution hierarchy approval;
- randomization policy, if any;
- capability availability semantics;
- final FDM command/event contract;
- final LPH contract.

## 23. Acceptance criteria for APE v1.0

APE cannot become `APPROVED` until:

- PAD pedagogical rules are mapped to decision policies;
- CLM/SDT inputs are formally defined;
- FDM commands/events and invariants are mapped;
- LPH generation/validation boundary is reconciled;
- mastery/progression authority is formally testable;
- conflict and insufficient-evidence handling is defined;
- deterministic replay requirements are testable;
- traceability is complete;
- independent architectural review is completed.

## 24. Status

**PROPOSED / NOT YET APPROVED.**

APE v0.1 establishes the intended pedagogical decision authority while deliberately leaving numerical policies and implementation technology unresolved.
