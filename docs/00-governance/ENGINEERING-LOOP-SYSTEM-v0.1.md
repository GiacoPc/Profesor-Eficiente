# ENGINEERING LOOP SYSTEM (ELS)

**Document ID:** ELS
**Version:** 0.1
**Status:** PROPOSED / REQUIRES HUMAN APPROVAL
**Scope:** Project engineering execution, AI-assisted development, audit, reconciliation, checkpointing, recovery and cross-agent continuity
**Parent governance:** KCA / PGKI / PRCP

## 1. Purpose

The Engineering Loop System (ELS) defines a controlled iterative engineering process for Profesor Eficiente from requirements and architecture through implementation, verification, audit, reconciliation, checkpointing and release readiness.

ELS exists to prevent the project from depending on:

- a single conversation;
- a single AI provider or model;
- a single IDE;
- implicit model memory;
- unverified AI assertions;
- uncontrolled context growth;
- undocumented decisions;
- silent omissions or regressions;
- unbounded repair loops;
- token/quota exhaustion without recoverable state.

ELS is a process/governance system, not an LLM, IDE, framework or coding agent.

## 2. Authority boundary

ELS operates below project governance and above individual execution agents.

```text
Human Owner
    |
    v
PGKI / KCA / PRCP
    |
    v
Engineering Loop System
    |
    +-- Specification / Planning
    +-- Implementation
    +-- Testing / Evidence
    +-- Self-Audit
    +-- Secondary Audit
    +-- Reconciliation
    +-- Checkpoint / Recovery
    |
    v
Product Architecture
    |
    +-- PAD
    +-- CLM / SDT
    +-- APE
    +-- FDM
    +-- LPH
    +-- AI / Runtime / Android implementation
```

ELS does not replace KCA, PGKI, PAD, CLM, SDT, APE, FDM or LPH.

The LPH remains a product-domain linguistic/pedagogical boundary. It does not become the project-wide engineering orchestrator merely because it is called a harness.

## 3. Core principles

### ELS-I01 — Evidence before verified claim

No AI statement may be promoted to VERIFIED without direct supporting evidence for the exact claim.

### ELS-I02 — Canonical state before continuation

An iteration may continue only from a verified project state/checkpoint. Conversation memory is not a checkpoint.

### ELS-I03 — Proposal is not authority

An AI-generated plan, specification, code change or audit verdict does not become authoritative without the applicable approval mechanism.

### ELS-I04 — Candidate is not evidence

Generated content, model output, analyzer output and proposed findings remain candidates until accepted through their governing contract.

### ELS-I05 — Failure is information

Every material failure must be classified and, where useful, converted into a reusable preventive rule, regression test, process improvement or knowledge artifact.

### ELS-I06 — Conflict stops promotion

A material contradiction between authoritative records or material evidence produces CONFLICT and blocks promotion until resolved.

### ELS-I07 — Minimum sufficient context

An agent receives the smallest context set sufficient for the task. Context expands only when dependency, contradiction or verification requires it.

### ELS-I08 — Interruptible by design

Every material iteration must be recoverable after interruption, quota exhaustion, tool failure, model replacement or workstation failure.

### ELS-I09 — Bounded autonomy

Agents may execute only within an explicitly authorized task and risk level. High-risk actions require stronger gates and, where applicable, human approval and secondary audit.

### ELS-I10 — No infinite loops

Repair, audit and reconciliation cycles have explicit retry/escalation limits.

## 4. Engineering Loop state machine

The canonical loop is:

```text
BOOTSTRAP
   |
   v
CONTEXT_RESOLUTION
   |
   v
OBJECTIVE
   |
   v
SPECIFICATION
   |
   v
PLAN
   |
   v
EXECUTION
   |
   v
TEST
   |
   v
EVIDENCE
   |
   v
SELF_AUDIT
   |
   +---- FAIL/UNKNOWN/CONFLICT ---> REMEDIATE / ESCALATE
   |
   v
SECONDARY_AUDIT (when required)
   |
   v
RECONCILIATION
   |
   +---- CONFLICT -----------------> STOP / HUMAN_DECISION
   |
   v
CONVERGENCE_CHECK
   |
   +---- NOT_CONVERGED ------------> NEXT_ITERATION
   |
   v
CHECKPOINT
   |
   v
READY_FOR_NEXT_TASK / CONVERGED
```

Terminal/control states:

- `CONTINUE`
- `PAUSE`
- `BLOCKED`
- `NEEDS_HUMAN`
- `FAILED`
- `CONFLICT`
- `RECOVER`
- `CONVERGED`
- `NOT_AVAILABLE`

An agent must never silently convert one control state into another.

## 5. Iteration risk levels

### L0 — Low-risk mechanical task

Examples:

- local refactor with no contract change;
- formatting;
- deterministic rename;
- isolated test repair where intended behavior is already authoritative.

Minimum flow:

```text
TASK -> EXECUTE -> TEST -> CHECKPOINT
```

### L1 — Normal engineering task

Examples:

- new implementation component;
- non-trivial bug fix;
- new adapter;
- moderate schema/code changes.

Minimum flow:

```text
BOOTSTRAP -> CONTEXT -> OBJECTIVE -> PLAN -> EXECUTE
-> TEST -> EVIDENCE -> SELF-AUDIT -> RECONCILE -> CHECKPOINT
```

### L2 — Critical architecture/governance task

Examples:

- changes to authority boundaries;
- mastery/progression semantics;
- governance/KCA/PGKI changes;
- security/privacy architecture;
- runtime/model architecture;
- release authorization;
- major persistence or migration changes.

Required flow:

```text
BOOTSTRAP -> CONTEXT -> SPEC -> IMPACT ANALYSIS -> PLAN
-> EXECUTE -> TEST -> EVIDENCE -> SELF-AUDIT
-> SECONDARY AUDIT -> RECONCILIATION -> HUMAN APPROVAL
-> CHECKPOINT
```

Risk classification is conservative: ambiguity escalates to the higher level.

## 6. Bootstrap contract

Every new agent/session must establish:

1. exact repository ref and HEAD;
2. current tree identity when relevant;
3. project authority hierarchy;
4. current project state;
5. active governance status;
6. relevant task specification;
7. relevant ADRs/contracts;
8. relevant tests/evidence;
9. unresolved conflicts;
10. missing requested artifacts;
11. current checkpoint, if resuming;
12. authorized action and risk level.

Bootstrap output must explicitly distinguish:

- `OBSERVED`
- `VERIFIED`
- `INFERRED`
- `PROPOSED`
- `UNKNOWN`
- `NOT_AVAILABLE`
- `CONFLICT`

No agent may infer that a missing artifact exists merely because a prior conversation mentioned it.

## 7. Context resolution

Context selection follows:

```text
Task
  -> Project anchors
  -> Task/domain classification
  -> Relevant canonical specification
  -> Relevant decisions/contracts
  -> Relevant evidence/tests
  -> Relevant prior findings
  -> Current checkpoint
```

The entire conversation and entire repository are not loaded by default.

Context expansion is justified only by:

- dependency;
- contradiction;
- missing prerequisite;
- required verification;
- impact analysis;
- audit scope.

The context resolver must record what was included and what was intentionally excluded for L1/L2 work.

## 8. Objective contract

Every L1/L2 iteration must have one explicit primary objective.

```yaml
iteration_id: ITER-XXXX
risk_level: L0 | L1 | L2
objective_id: OBJ-XXXX
objective: <single primary outcome>
acceptance_criteria: []
authorized_scope: []
forbidden_scope: []
```

An iteration must not silently expand its objective.

New objectives become new iterations or explicit scope amendments.

## 9. Specification before implementation

For L1/L2 work, implementation begins only after the applicable specification or contract is identified.

If the governing specification is missing, contradictory or undefined:

```text
STOP -> classify UNKNOWN/CONFLICT -> resolve governance
```

The agent must not invent a missing contract to unblock itself.

## 10. Planning contract

The plan must identify:

- intended files/artifacts;
- dependencies;
- acceptance criteria;
- tests;
- evidence required;
- risks;
- rollback/recovery considerations;
- expected checkpoint boundaries.

For L2 tasks, the plan must also identify affected authority boundaries and required secondary-audit scope.

## 11. Execution boundary

Agents may modify only:

- explicitly authorized working refs;
- explicitly authorized paths/scope;
- artifacts permitted by the task.

The forensic preservation branch `recovery/forensic-2026-09-06` remains immutable and must never be used as a normal work target.

Before destructive operations, the applicable KCA/PRCP anti-deletion procedure is mandatory.

## 12. Test and evidence contract

Tests are evidence producers, not authority by themselves.

Each material test result records:

```yaml
test_id: TEST-XXXX
status: PASS | FAIL | BLOCKED | NOT_RUN
source_ref: <ref>
source_head: <sha>
method: <method>
result: <result>
artifacts: []
limitations: []
```

A claim such as `tests_passed` requires evidence tied to the relevant exact state.

Historical test success must not be presented as current-head success without current verification.

## 13. Self-audit

Every L1/L2 iteration performs a structured self-audit before reconciliation.

Minimum checks:

### Integrity

- Did I claim anything without evidence?
- Did I confuse inference with observation?
- Did I invent a missing artifact?

### Scope

- Did the work stay inside the authorized objective?
- Did implementation change an unapproved authority boundary?

### Consistency

- Does the result contradict a current canonical artifact?
- Did I create duplicate/conflicting definitions?

### Completeness

- Were acceptance criteria addressed?
- Were required tests/evidence produced?
- Are known omissions explicit?

### Regression

- Could the change invalidate an earlier invariant, contract or test?

### Continuity

- Can another agent resume from the resulting checkpoint without this conversation?

Self-audit is a detection mechanism. It is not independent verification.

## 14. Secondary AI audit

For mandatory L2 categories and any task escalated by risk, an independent AI/model/provider should audit a compact Audit Pack.

The Audit Pack should contain:

- objective and acceptance criteria;
- applicable specification/ADR;
- changed artifacts;
- relevant tests and exact results;
- evidence;
- self-audit;
- known limitations;
- previous relevant audit findings;
- checkpoint/source identity.

The secondary auditor returns:

- `PASS`
- `PASS_WITH_LIMITATIONS`
- `FAIL`
- `UNKNOWN`
- `CONFLICT`

An AI agreement is not proof of truth. Canonical artifacts and executable/empirical evidence remain authoritative.

## 15. Reconciliation

Reconciliation answers:

> Does the result remain compatible with the project knowledge that already governs this area?

Minimum reconciliation dimensions:

1. authority hierarchy;
2. requirements traceability;
3. architectural contracts;
4. domain invariants;
5. decisions/ADRs;
6. tests/evidence;
7. unresolved conflicts;
8. project state;
9. downstream impact;
10. future agent resumability.

A reconciliation result may be:

- `CONVERGED`
- `CONVERGED_WITH_LIMITATIONS`
- `NOT_CONVERGED`
- `CONFLICT`
- `BLOCKED`

`CONVERGED` means the iteration satisfied its defined acceptance criteria and reconciliation scope. It does not mean the entire product is complete.

## 16. Convergence criteria

An iteration is converged only when:

- objective is satisfied;
- acceptance criteria are satisfied or explicitly waived by the authorized human decision;
- required tests have evidence;
- required audits have completed;
- no unresolved blocking conflict exists;
- canonical/project state impact is recorded;
- checkpoint can reproduce the relevant state.

No agent may declare project-wide convergence from a local task result.

## 17. Checkpoint contract

Every material iteration produces a checkpoint.

```yaml
checkpoint_id: CP-XXXX
iteration_id: ITER-XXXX
created_at: <timestamp>
status: IN_PROGRESS | PAUSED | BLOCKED | CONVERGED | FAILED | RECOVERABLE
repository:
  ref: <ref>
  head: <sha>
  tree: <sha-if-required>
objective:
  id: <id>
  summary: <text>
phase: <state>
completed_steps: []
current_step: <step>
pending_steps: []
changed_artifacts: []
test_results: []
evidence_ids: []
audit_ids: []
decision_ids: []
conflicts: []
blockers: []
known_unknowns: []
next_authorized_action: <action>
resume_instructions: <minimal instructions>
```

The checkpoint must be understandable without the originating conversation.

## 18. Token and context budget manager

ELS includes a logical Context & Budget Manager (CBM).

CBM does not assume that an external UI exposes an exact remaining quota.

Budget states may therefore be:

- `KNOWN`
- `ESTIMATED`
- `UNKNOWN`
- `EXHAUSTION_RISK`
- `STOPPED_FOR_BUDGET`

CBM controls engineering behavior rather than attempting to guess an unavailable provider quota.

Before expensive work, the loop estimates:

- context load;
- expected tool/model work;
- audit cost;
- checkpoint cost;
- remaining task complexity;
- safety margin.

If exhaustion risk becomes material, the loop must checkpoint before starting a non-recoverable operation.

## 19. Token exhaustion protocol

When quota exhaustion is detected or strongly suspected:

```text
STOP NEW WORK
   -> SAVE CHECKPOINT
   -> VERIFY REPOSITORY STATE
   -> RECORD LAST COMPLETED STEP
   -> RECORD CURRENT/PENDING STEP
   -> RECORD NEXT AUTHORIZED ACTION
   -> STOP
```

The next session must not infer where the previous session stopped.

It loads the latest checkpoint, verifies repository identity, then resumes only from the verified state.

The exact provider quota mechanism is environment-dependent and is not assumed by ELS.

## 20. Crash/restart protocol

For unexpected interruption:

```text
INTERRUPTION
   -> DISCOVER LATEST CHECKPOINT
   -> VERIFY REF/HEAD/TREE
   -> VERIFY CHANGED ARTIFACTS
   -> VERIFY TEST STATE
   -> CLASSIFY PARTIAL WORK
   -> RESUME OR ROLLBACK
```

If the state cannot be established reliably:

`STOP -> UNKNOWN -> INVESTIGATE`.

Never resume from model recollection alone.

## 21. Anti-loop guard

Repair and reconciliation loops are bounded.

Recommended initial policy:

```yaml
max_same_failure_attempts: 2
max_repair_attempts_per_iteration: 3
on_repeat_failure: ESCALATE
on_new_failure_class: REASSESS
on_contradiction: STOP
```

These numbers are PROPOSED and require empirical validation before becoming normative.

The loop must detect:

- identical failure recurrence;
- oscillating fixes;
- regression of a previously passing test;
- changing symptoms without root-cause progress;
- repeated context expansion without convergence.

## 22. Error-learning loop

Material failures become reusable project knowledge through:

```text
FAILURE
  -> CLASSIFY
  -> ROOT CAUSE
  -> CORRECTIVE ACTION
  -> PREVENTIVE CONTROL
  -> REGRESSION TEST / RULE / ADR / CHECKLIST
  -> VERIFY
  -> RECORD LESSON
```

A lesson is not automatically authoritative merely because an agent generated it.

Promotion follows the applicable governance path.

Recommended lesson schema:

```yaml
lesson_id: LESSON-XXXX
source_iteration: ITER-XXXX
failure_class: <class>
root_cause: <evidence-backed or UNKNOWN>
correction: <action>
prevention: <control>
regression_test: <id-or-null>
status: PROPOSED | APPROVED | REJECTED
```

## 23. Anti-hallucination controls

ELS adopts the following mandatory prohibitions:

1. No claiming to have inspected a file, screenshot, repository, test, branch or tool result unless it was actually inspected.
2. No claiming a test passed without exact supporting evidence.
3. No claiming a branch is protected without current verification.
4. No claiming an artifact was recovered unless its provenance was verified.
5. No replacing a missing artifact with an AI reconstruction and calling it recovered history.
6. No converting AI consensus into proof.
7. No silently resolving contradictions.
8. No silently upgrading `PROPOSED`, `UNKNOWN` or `INFERRED` into authoritative state.

These rules inherit KCA/PGKI and PRCP authority.

## 24. Multi-agent handoff

Agents are interchangeable execution components.

A handoff package contains:

```yaml
handoff_id: HANDOFF-XXXX
source_agent: <agent/provider>
target_agent: <agent/provider>
checkpoint_id: <id>
source_head: <sha>
task: <task>
completed: []
pending: []
known_failures: []
known_unknowns: []
constraints: []
next_authorized_action: <action>
```

The receiving agent must verify the repository state rather than trusting the handoff alone.

## 25. IDE boundary

An IDE is an execution environment, not a source of truth.

Codex, Claude Code, OpenCode, Cursor, ZCode, Antigravity, VS Code and Android Studio may be used as interchangeable components subject to verified capabilities and project policy.

Only one authorized writer should modify a given working ref at a time unless concurrency is explicitly designed and controlled.

Android Studio remains the preferred Android-specific verification environment for build/device/profiling tasks, subject to later empirical validation.

## 26. Framework adapter boundary

ELS must remain framework-neutral.

Spec-driven frameworks such as OpenSpec or Spec Kit may be adopted as adapters/components for specification, planning and task execution.

They do not automatically replace:

- PGKI;
- KCA;
- PRCP;
- project state;
- evidence governance;
- secondary audit;
- checkpoint/recovery;
- human authority.

Framework adoption requires a fit assessment and a bounded proof of concept before becoming project infrastructure.

## 27. Obsidian integration boundary

Obsidian is the human-facing KCA Second Brain / Knowledge Interface.

ELS may publish iteration artifacts into the KCA vault, but the canonical Git record remains authoritative.

Recommended flow:

```text
ELS iteration
   -> checkpoint/evidence
   -> canonical Git artifact
   -> Obsidian navigation/snapshot
```

Obsidian must not become an ungoverned parallel authority.

## 28. Required iteration deliverables

L1/L2 iterations should produce, as applicable:

```text
ITER-XXXX/
  INPUT.yaml
  CONTEXT.yaml
  OBJECTIVE.md
  PLAN.md
  CHANGES.md
  TEST-RESULTS.md
  EVIDENCE.yaml
  SELF-AUDIT.md
  SECONDARY-AUDIT.md
  RECONCILIATION.md
  CHECKPOINT.yaml
```

Not every artifact is mandatory for L0. Artifact requirements are determined by risk level and task type.

## 29. Minimal durable state

At all times the project should be able to answer:

- What are we doing?
- Why are we doing it?
- What authority governs it?
- What has been verified?
- What has changed?
- What failed?
- What remains unknown?
- Where exactly did we stop?
- What is the next authorized action?

If the system cannot answer these questions from durable artifacts, continuity is degraded and the loop must not pretend otherwise.

## 30. Release boundary

ELS does not authorize release by itself.

Release readiness requires the project-specific release gate, including applicable:

- functional verification;
- architecture verification;
- security/privacy review;
- performance/thermal validation;
- pedagogical validation;
- offline behavior validation;
- model/runtime validation;
- secondary audit;
- human approval.

## 31. Governance integration

ELS integrates with KCA as follows:

```text
KCA
  |
  +-- durable knowledge
  +-- bootstrap
  +-- continuity
  +-- recovery
  |
  v
ELS
  |
  +-- execution loop
  +-- evidence
  +-- audit
  +-- reconciliation
  +-- checkpoint
  |
  v
Canonical Git record
```

ELS integrates with PGKI by applying its authority hierarchy, status vocabulary, evidence rules and secondary-audit requirements.

ELS integrates with PRCP whenever corruption, deletion or provenance uncertainty is suspected.

## 32. Operational gates

The following gates are proposed:

| Gate | Requirement | Status |
|---|---|---|
| ELS-G01 | ELS v0.1 human approval | PENDING |
| ELS-G02 | Iteration artifact contract tested | PENDING |
| ELS-G03 | Checkpoint/resume drill passes | PENDING |
| ELS-G04 | Token-exhaustion simulation passes | PENDING |
| ELS-G05 | Anti-loop guard tested | PENDING |
| ELS-G06 | Self-audit tested | PENDING |
| ELS-G07 | Secondary-audit handoff tested | PENDING |
| ELS-G08 | Reconciliation tested | PENDING |
| ELS-G09 | Cross-agent handoff tested | PENDING |
| ELS-G10 | Obsidian publication workflow tested | PENDING |
| ELS-G11 | OpenSpec/Spec Kit fit assessment completed | PENDING |
| ELS-G12 | Human owner approves ELS operational readiness | PENDING |

No gate may be marked PASS solely because this document exists.

## 33. Initial implementation strategy

ELS should initially be implemented as a small, auditable process layer rather than a large autonomous framework.

Phase 1 — Contract

- freeze ELS state machine;
- define checkpoint schema;
- define iteration artifact schema;
- define audit-pack schema;
- define evidence ledger integration.

Phase 2 — Dry run

Run a non-destructive architecture task through:

```text
bootstrap -> context -> objective -> plan -> audit -> checkpoint
```

Phase 3 — Interruption test

Simulate quota exhaustion/interruption after a known intermediate step and resume from checkpoint.

Phase 4 — Agent handoff

Run the continuation with a different AI environment.

Phase 5 — Framework fit

Evaluate OpenSpec and Spec Kit against the already-defined ELS contracts rather than allowing either framework to redefine project governance.

Phase 6 — IDE execution

Only after the dry runs pass should the project use the loop for real implementation work.

## 34. Non-goals

ELS does not:

- make AI autonomous authority;
- guarantee zero hallucinations;
- guarantee unlimited token availability;
- replace human decisions;
- replace Git/KCA;
- replace project architecture;
- make an IDE authoritative;
- make Obsidian authoritative;
- automatically make OpenSpec or Spec Kit authoritative;
- declare KCA READY;
- authorize product implementation before upstream gates permit it.

## 35. Current status

**ELS v0.1: PROPOSED / REQUIRES HUMAN APPROVAL.**

This document defines the proposed Engineering Loop System. Its existence does not prove that the loop has been operationally tested.

The initial numeric anti-loop limits are explicitly provisional and require empirical validation.
