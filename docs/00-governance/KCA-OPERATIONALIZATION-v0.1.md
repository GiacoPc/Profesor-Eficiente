# KCA OPERATIONALIZATION

**Document ID:** KCA-OPS
**Version:** 0.1
**Status:** PROPOSED / REQUIRES HUMAN APPROVAL
**Parent:** `KNOWLEDGE-CONTINUITY-ARCHITECTURE-v1.0.md`
**Recovery authority:** PRCP

## 1. Objective

Convert KCA from a formal architecture into a demonstrably operational continuity system without falsely claiming that local Obsidian, backup, synchronization, or recovery capabilities have already been configured.

This document defines the execution plan and evidence required for the KCA READY gate.

## 2. Operational boundary

The KCA implementation has two categories:

### Repository-verifiable

- KCA specification exists.
- Bootstrap artifacts exist and are internally consistent.
- Governance/recovery documents are versioned.
- Exact HEAD/tree/blob verification can be performed.
- Recovery branch provenance can be inspected.
- Canonical/recovery/proposed status is explicit.

### Environment-dependent

- Obsidian vault actually exists.
- Vault mapping is configured.
- Local synchronization works.
- Independent backup exists.
- Backup restoration works.
- Human workflow has been exercised.
- A second AI can bootstrap from the same pack.

Environment-dependent items MUST NOT be marked complete from repository evidence alone.

## 3. KCA operational phases

### OPS-01 — Canonical mapping

Create a mapping between repository authorities and the human-facing KCA vault.

Minimum mapping:

```text
Repository canonical                    KCA vault
-------------------------------------------------------------
PROJECT-CONSTITUTION.md              → 00-CANON/
PROJECT-STATE.yaml                   → 00-CANON/
CONTEXT-MANIFEST.yaml                → 00-CANON/
DECISION-LEDGER.yaml                 → 01-DECISIONS/
AI-GOVERNANCE.md                     → 00-CANON/
AGENTS.md                            → 00-CANON/
docs/00-governance/*                → 00-CANON/ or 06-RECOVERY/
docs/02-pedagogy/*                  → 00-CANON/
docs/03-cognitive/*                 → 00-CANON/
docs/04-ape/*                        → 00-CANON/
docs/05-domain/*                    → 00-CANON/
docs/architecture/*                 → 00-CANON/
research / exploratory notes         → 02-RESEARCH/
proposals                            → 03-PROPOSALS/
experiments                          → 04-EXPERIMENTS/
evidence / measurements              → 05-EVIDENCE/
forensic / recovery material         → 06-RECOVERY/
indexes / navigation                 → 99-INDEX/
```

The mapping is a logical contract, not proof that a local vault has been created.

### OPS-02 — AI bootstrap

Every AI session must begin from a small bootstrap pack and resolve only task-relevant context.

Required anchors:

1. Constitution.
2. Project State.
3. Context Manifest.
4. Decision Ledger.
5. AI Governance.
6. AGENTS instructions.
7. Architecture Bible.
8. Relevant specification/contract.
9. Relevant evidence/audit pack.

Bootstrap output must explicitly report:

- exact ref/HEAD used;
- relevant artifact statuses;
- unresolved conflicts;
- missing requested artifacts;
- evidence limitations;
- whether work is analysis, proposal, verification, or authorized change.

### OPS-03 — Anti-deletion drill

A controlled test must demonstrate that a material artifact can be removed from a disposable working ref and recovered using Git history/recovery controls without relying on conversation memory.

Required evidence:

- pre-operation HEAD/tree;
- target artifact/blob identity;
- disposable test ref;
- deletion commit;
- recovery operation;
- post-recovery HEAD/tree;
- restored artifact identity;
- comparison result.

Never execute this drill against the forensic preservation branch.

### OPS-04 — Exact identity drill

Demonstrate that a checkpoint can verify:

`ref → HEAD SHA → tree SHA → critical blob SHAs`

The test passes only if an independently retrieved identity matches the recorded identity.

### OPS-05 — Independent backup

Establish at least one recovery copy outside the sole GitHub repository path and outside ChatGPT conversation storage.

The exact provider/location is intentionally environment-dependent and must be recorded by the human owner.

Required evidence:

- backup target class;
- snapshot identifier/date;
- source commit SHA;
- contents/recovery pack manifest;
- restoration procedure.

Do not record credentials or secrets in the repository.

### OPS-06 — Restore drill

Restore a known recovery pack into a clean environment and demonstrate that the project can be reconstructed from durable artifacts without the original conversation.

Pass criteria:

- canonical anchors recovered;
- statuses understandable;
- decision history traceable;
- unresolved items preserved;
- no fabricated missing artifacts;
- exact source identity preserved.

### OPS-07 — Cross-AI continuity

At least two independent AI environments must receive the same bootstrap pack and independently report the same canonical facts and explicit unknowns.

The comparison evaluates:

- authority hierarchy;
- project state;
- active gates;
- key architecture boundaries;
- known missing artifacts;
- recovery status.

An AI agreement is not proof of truth; truth remains anchored to the canonical artifacts and evidence.

### OPS-08 — Context minimization

Demonstrate that a task can be executed from minimum sufficient context without loading the entire conversation.

Evidence should identify:

- task;
- selected anchors;
- selected contracts/specs;
- excluded irrelevant context;
- resulting analysis/proposal;
- any context expansion triggered by dependency/contradiction.

## 4. Evidence ledger

Each operational gate should produce an evidence record with:

```yaml
id: KCA-E-XXXX
operation: <operation>
status: PASS | FAIL | UNKNOWN | NOT_AVAILABLE
performed_at: <timestamp>
operator: <human-or-agent>
source_ref: <ref>
source_head: <sha>
source_tree: <sha-if-applicable>
artifacts: []
method: <brief method>
result: <brief result>
limitations: []
```

`PASS` requires evidence. `UNKNOWN` and `NOT_AVAILABLE` are valid outcomes and must not be converted into PASS by inference.

## 5. KCA readiness gate

KCA READY requires all mandatory controls below:

| Gate | Requirement | Evidence source | Status |
|---|---|---|---|
| KCA-G01 | KCA v1.0 approved | Human approval record | PENDING |
| KCA-G02 | Vault structure exists | Local environment evidence | PENDING |
| KCA-G03 | Repository↔vault mapping tested | Mapping evidence | PENDING |
| KCA-G04 | Bootstrap pack matches exact source state | Git verification | PENDING |
| KCA-G05 | Anti-deletion drill passes | Drill evidence | PENDING |
| KCA-G06 | Exact identity drill passes | Drill evidence | PENDING |
| KCA-G07 | Independent backup exists | Backup evidence | PENDING |
| KCA-G08 | Restore drill passes | Restore evidence | PENDING |
| KCA-G09 | Cross-AI continuity passes | Comparative audit evidence | PENDING |
| KCA-G10 | Context minimization demonstrated | Session evidence | PENDING |
| KCA-G11 | Recovery drill passes | Recovery evidence | PENDING |
| KCA-G12 | Secondary audit passes where required | Independent audit pack | PENDING |
| KCA-G13 | Human owner approves KCA READY | Explicit decision | PENDING |

No gate may be marked PASS solely because the corresponding document exists.

## 6. Failure semantics

- Missing evidence → `UNKNOWN` / `NOT_AVAILABLE`.
- Conflicting evidence → `CONFLICT` and STOP.
- Failed test → `FAIL`; remediation required.
- Successful documentation-only review → does not imply operational PASS.
- AI disagreement → investigate; do not select the more convenient answer.
- Repository corruption → invoke PRCP.

## 7. Security and privacy

No passwords, access tokens, API keys, private keys, personal credentials or secrets belong in KCA artifacts.

Recovery packs must contain identifiers and verification data, not credentials.

## 8. Explicit prohibitions

1. Do not modify `recovery/forensic-2026-09-06`.
2. Do not force-reset forensic preservation refs.
3. Do not call a local Obsidian vault synchronized unless tested.
4. Do not call a backup independent unless its independence is established.
5. Do not call a backup recoverable unless a restoration test exists.
6. Do not call KCA READY before every mandatory gate passes.
7. Do not use conversation memory as recovery evidence.
8. Do not reconstruct missing historical artifacts and label them recovered.
9. Do not promote KCA from PROPOSED without human approval.

## 9. Current state

**KCA-OPS v0.1: PROPOSED / REQUIRES HUMAN APPROVAL.**

The repository currently records the operational plan; it does not establish that the environment-dependent controls have already been executed.
