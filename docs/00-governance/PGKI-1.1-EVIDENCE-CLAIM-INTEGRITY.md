# PGKI-1.1 — Evidence & Claim Integrity

**Status:** PROPOSED HARDENING — MUST NOT ALTER PGKI-1.0 BASELINE
**Parent baseline:** `PGKI-1.0`
**Purpose:** Formalize controls against unsupported observations, unverifiable claims, contextual hallucination, evidence conflation, and cross-agent state contamination.

## 1. Incident that triggered this hardening

During the PGKI-1.0 human-review workflow, an AI response stated that it had reviewed a screenshot before that screenshot was actually available in the conversation turn. The later screenshot did provide the expected evidence, but the earlier statement was unsupported.

This is classified as an **Evidence Integrity Incident**. It does not invalidate PGKI-1.0 artifacts or its approved baseline; it exposes a control weakness in agent claim discipline.

## 2. Non-negotiable rules

### R1 — No evidence, no claim

An agent MUST NOT assert a repository state, test result, review result, configuration state, file existence, visual observation, benchmark, or other externally verifiable fact without accessible evidence.

### R2 — No observation, no observation claim

An agent MUST NOT say `I saw`, `I reviewed`, `I inspected`, `I verified`, or equivalent unless the referenced evidence was actually available to that agent in the current execution context.

### R3 — Evidence availability precedes interpretation

Before interpreting an attachment, screenshot, tool result, repository file, or external state, the agent MUST establish that the artifact is actually accessible.

### R4 — Evidence and inference are distinct

The following labels MUST remain distinct:

- `OBSERVED` — directly observed from accessible evidence.
- `VERIFIED` — corroborated by an authoritative or machine-checkable source.
- `INFERRED` — logically derived but not directly verified.
- `PROPOSED` — suggested by an agent.
- `UNKNOWN` — insufficient evidence to determine the state.
- `NOT_AVAILABLE` — the referenced evidence is not accessible to the agent.
- `CONFLICT` — authoritative evidence disagrees and requires resolution.

### R5 — Evidence citation is mandatory for critical claims

Critical claims MUST carry an evidence reference that identifies the artifact, source, commit/ref, tool result, or other reproducible evidence.

### R6 — Conversation memory has zero authority over repository state

Conversation memory can assist task reconstruction but cannot establish current repository state, approval state, branch state, test state, or architectural decisions when repository evidence is available or required.

### R7 — Conflicting evidence stops the workflow

If two evidence sources disagree, the agent MUST report `EVIDENCE CONFLICT`, stop dependent decisions, and resolve the discrepancy before proceeding.

### R8 — Absence cannot be proven from silence

An agent MUST NOT claim that no prior integrity failures exist merely because none were found in a limited audit. Absence claims require a defined audit scope and coverage statement.

## 3. Claim record minimum schema

```yaml
claim_id: <stable-id>
statement: <claim>
classification: OBSERVED|VERIFIED|INFERRED|PROPOSED|UNKNOWN|NOT_AVAILABLE|CONFLICT
evidence:
  - source: <repository|github|attachment|ci|test|human-record>
    reference: <stable reference>
    observed_at: <timestamp when applicable>
verification_method: <how corroboration was performed>
agent: <agent identifier>
status: OPEN|RESOLVED
```

## 4. Critical claim classes

The following require explicit evidence before being stated as facts:

- repository/branch/PR state;
- approval/review state;
- CI/test results;
- file existence or content;
- architecture decisions;
- hardware compatibility;
- performance, latency, RAM, thermal or energy results;
- model/runtime/NPU compatibility;
- pedagogical efficacy;
- security properties;
- release/readiness status.

## 5. Two-agent verification for high-impact claims

A secondary auditor SHOULD independently verify high-impact claims before irreversible project gates. The auditor must receive the same immutable evidence set and must not rely on the primary agent's conclusion.

Recommended independence boundary:

`Primary agent -> produces claim + evidence set -> Secondary auditor -> independent verdict -> Human gate`

The secondary auditor is not authoritative over the human decision and does not replace CI or deterministic tests.

## 6. Retrospective audit requirement

Following an evidence-integrity incident, a retrospective audit MUST inspect the defined evidence surface and publish:

1. audit scope;
2. evidence sources inspected;
3. claims sampled or enumerated;
4. findings;
5. unresolved blind spots;
6. confidence/coverage statement;
7. remediation actions.

The result MUST NOT be phrased as absolute proof of absence unless the audit mechanism can establish that property.

## 7. Token-efficient enforcement

Agents MUST use task-routed context. The evidence set for a task should contain only the minimum authoritative artifacts required to establish the claim. Full conversation replay is prohibited unless specifically required by the audit scope.

## 8. Gate rule

For any governance gate:

`NO EVIDENCE -> NO VERIFIED CLAIM -> NO GATE PASS`

An `UNKNOWN` or `NOT_AVAILABLE` result is a valid controlled state and MUST NOT be silently converted into success.
