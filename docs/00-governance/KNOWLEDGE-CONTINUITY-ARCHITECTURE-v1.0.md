# KNOWLEDGE CONTINUITY ARCHITECTURE (KCA)

**Document ID:** KCA
**Version:** 1.0
**Status:** PROPOSED / REQUIRES HUMAN APPROVAL
**Effective date:** 2026-09-06
**Scope:** Project knowledge, specifications, decisions, evidence, recovery, AI continuity

## 1. Purpose

KCA defines the durable information architecture that prevents loss of project knowledge, silent corruption, unsupported claims, accidental deletion, and dependency on a single conversation, AI provider, workstation, branch, or interface.

KCA complements PRCP. During recovery, PRCP remains the active recovery protocol and takes precedence for forensic preservation and recovery decisions.

## 2. Core principle

> **The project must remain reconstructable without relying on conversation memory.**

The project knowledge system is intentionally multi-layered. No individual layer is sufficient by itself.

## 3. Authority model

| Layer | Role | Authority |
|---|---|---|
| Human owner | Final project authority and approval | FINAL |
| Canonical Git artifacts | Versioned project record | CANONICAL RECORD |
| GitHub remote | Remote copy, collaboration and review surface | REMOTE REPOSITORY |
| Obsidian/KCA vault | Human knowledge interface and navigation layer | NON-AUTHORITATIVE INTERFACE |
| Independent backup | Disaster-recovery redundancy | RECOVERY COPY |
| AI systems | Analysis, proposal, transformation and governed execution | NON-AUTHORITATIVE AGENT |
| Conversation history | Working context only | NON-AUTHORITATIVE |
| AI memory | Personal/contextual aid only | NON-AUTHORITATIVE |

No lower layer may silently override a higher-authority layer.

## 4. Knowledge states

Every material artifact must have an explicit status when its authority matters:

- `CANONICAL` — approved and authoritative project artifact.
- `DECIDED` — recorded project decision; authority derives from the governing decision mechanism.
- `PROPOSED` — candidate content awaiting approval.
- `EVIDENCE` — factual support, measurement, audit result, test result or external source record.
- `RECOVERY` — material produced or preserved as part of recovery/forensics.
- `UNKNOWN` — existence, content, provenance or validity is not established.
- `CONFLICT` — two or more authoritative/evidentiary records disagree and require resolution.
- `DEPRECATED` / `SUPERSEDED` — retained historical record that no longer governs current work.

Status must not be inferred merely from filename, location, commit message or AI assertion.

## 5. Canonical repository boundary

The Git repository is the canonical versioned project record once an artifact has been approved into the project.

Canonical material includes, as applicable:

- Constitution and governance rules.
- Project state and context manifests.
- Approved specifications and ADRs.
- Architecture documents and formal contracts.
- Schemas and executable governance checks.
- Tests and reproducible evidence.
- Recovery records and forensic provenance.

A copy in Obsidian does not become authoritative merely because it is newer or easier to edit.

## 6. Obsidian / Second Brain boundary

Obsidian is designated as the human-facing **Second Brain / Knowledge Interface** of KCA.

Its purposes are:

1. Navigate the project knowledge graph.
2. Surface relationships between specifications, decisions, evidence and recovery records.
3. Maintain human-readable working notes.
4. Provide an ergonomic context map for future AI sessions.
5. Preserve local copies/snapshots where operationally configured.

Obsidian MUST NOT be treated as the sole source of truth.

Recommended logical areas:

```text
00-CANON/
01-DECISIONS/
02-RESEARCH/
03-PROPOSALS/
04-EXPERIMENTS/
05-EVIDENCE/
06-RECOVERY/
99-INDEX/
```

`00-CANON` contains synchronized references/copies of canonical artifacts; the Git record remains authoritative.

## 7. Git / GitHub boundary

Git provides local history, immutable commit identities in normal history, branching and exact version comparison.

GitHub provides remote hosting, review/collaboration and an additional copy of repository history.

GitHub availability or branch protection status must never be assumed. Protection state must be verified when it is relevant to a claim.

The forensic recovery branch is not to be rewritten as part of normal work.

## 8. Independent backup boundary

A disaster-recovery copy must exist outside the sole GitHub account/repository path and outside the sole ChatGPT conversation.

At minimum, major milestones should produce a human-readable recovery pack containing:

- repository/ref identity;
- exact commit SHA;
- relevant tree SHA;
- critical artifact/blob identities;
- current project state;
- decisions and unresolved conflicts;
- recovery instructions;
- verification results.

Backup existence, freshness and recoverability are operational facts that require direct verification.

## 9. AI session bootstrap contract

Any AI entering the project must follow this order:

1. Read project Constitution.
2. Read current Project State.
3. Read Context Manifest.
4. Identify the task/domain.
5. Resolve only the minimum sufficient canonical context.
6. Load relevant specifications, ADRs, contracts, evidence and tests.
7. Check status and provenance.
8. Detect contradictions or missing artifacts.
9. Declare unknowns before analysis.
10. Perform analysis/proposal.
11. Produce evidence for factual claims.
12. Request/obtain human approval before promoting governed proposals.
13. Update canonical artifacts only through the approved project workflow.
14. Verify resulting commit/tree/blob identities.

The AI must not reconstruct missing historical knowledge from plausibility and present it as fact.

## 10. Claim-integrity rules

KCA inherits the following hard rules:

### KCA-I01 — NO EVIDENCE → NO VERIFIED CLAIM

`VERIFIED`, `OBSERVED`, `REVIEWED`, `PASSED` and equivalent claims require direct supporting evidence for that exact claim.

### KCA-I02 — NO CANONICAL RECORD → NO PROJECT MEMORY

Conversation context, AI memory, or an unsaved note is not authoritative project memory.

### KCA-I03 — NO ARTIFACT → NO RECONSTRUCTION CLAIM

If a requested historical artifact cannot be located in inspected evidence, classify it as `UNKNOWN` / `NOT_FOUND_IN_INSPECTED_GIT` rather than silently recreating it as recovered history.

### KCA-I04 — NO EXACT HEAD → NO STATE CLAIM

Claims about current repository state require verification of the exact relevant ref/HEAD.

### KCA-I05 — NO APPROVAL → NO AUTHORITY

A proposal does not become canonical because an AI generated it or because it is technically plausible.

### KCA-I06 — CONFLICT → STOP

Material contradiction between authoritative records blocks promotion until explicitly resolved.

### KCA-I07 — AI IS NOT SOURCE OF TRUTH

An AI verdict is evidence or analysis, never the canonical authority by itself.

## 11. Change-control protocol

All governed knowledge changes follow:

```text
Need / Finding
    ↓
Classification
    ↓
Impact analysis
    ↓
Proposal
    ↓
Evidence
    ↓
Decision / Approval
    ↓
Canonical update
    ↓
Git commit
    ↓
Exact HEAD/tree verification
    ↓
Backup / recovery snapshot
```

For P0/P1 changes, the applicable PGKI/PRCP secondary-audit requirements remain mandatory.

## 12. Anti-deletion controls

Before destructive or potentially destructive operations:

1. Identify the exact target ref/path.
2. Verify current HEAD and relevant blob/tree identity.
3. Preserve recoverable state when required by PRCP.
4. Record the intended change.
5. Perform the change only on an authorized working ref.
6. Re-fetch the resulting HEAD.
7. Verify the recursive tree and critical artifacts.
8. Record evidence.

No commit message is accepted as proof that the intended tree was preserved.

## 13. Context minimization

Future AI sessions must not ingest the entire conversation or repository by default.

Context should be resolved from:

```text
Project anchors
→ task classification
→ relevant canonical artifacts
→ relevant decisions/contracts
→ relevant evidence/tests
→ unresolved conflicts
```

Context expands only when dependency or contradiction analysis requires it.

## 14. Recovery protocol

When knowledge loss, deletion or corruption is suspected:

```text
STOP WRITES
    ↓
PRESERVE EXACT REF
    ↓
VERIFY HEAD / TREE
    ↓
INSPECT HISTORY / OBJECTS
    ↓
RECOVER VERIFIED ARTIFACTS
    ↓
CLASSIFY PROVENANCE
    ↓
RECONCILE
    ↓
CREATE RECOVERY BASELINE
    ↓
VERIFY
    ↓
INDEPENDENT AUDIT
    ↓
HUMAN APPROVAL
    ↓
RESUME NORMAL WORK
```

PRCP governs forensic recovery details.

## 15. Required integrity checkpoints

At minimum, checkpoints are required:

- before a recovery operation;
- after a material recovery batch;
- before promotion of a P0/P1 artifact;
- after canonical changes;
- before release authorization;
- after restoration from backup.

Each checkpoint records enough identity information to reproduce the verification.

## 16. Cross-AI continuity

The project must be portable between ChatGPT, Grok, IDE agents and future AI systems.

Portability depends on repository artifacts, not provider-specific memory.

The minimum bootstrap pack should reference:

- `PROJECT-CONSTITUTION.md`
- `PROJECT-STATE.yaml`
- `CONTEXT-MANIFEST.yaml`
- `DECISION-LEDGER.yaml`
- `AI-GOVERNANCE.md`
- `AGENTS.md`
- `docs/ARCHITECTURE-BIBLE.md`
- current task specification
- relevant ADRs/contracts
- relevant evidence and audit packs

## 17. Operational readiness gate

KCA is **NOT READY** until all of the following are demonstrated:

- [ ] KCA specification approved by human owner.
- [ ] Obsidian vault structure created and mapped to repository paths.
- [ ] Canonical synchronization rule documented.
- [ ] Bootstrap pack validated against current repository state.
- [ ] Anti-deletion procedure tested.
- [ ] Exact-head/tree verification procedure tested.
- [ ] Independent backup mechanism established.
- [ ] Backup restoration test completed.
- [ ] P0/P1 secondary-audit procedure available.
- [ ] AI session bootstrap tested with at least two independent AI environments.
- [ ] Context-minimization workflow demonstrated.
- [ ] Recovery drill completed without relying on conversation memory.
- [ ] Human owner approves KCA readiness.

Until this gate passes, KCA remains `PROPOSED` and project implementation remains blocked by PRCP.

## 18. Non-goals

KCA does not:

- define English curriculum;
- replace PAD, CLM, SDT, APE or FDM;
- define mastery thresholds;
- authorize implementation;
- make Obsidian authoritative;
- guarantee recovery merely by existing as a document;
- eliminate the need for independent backups and verification.

## 19. Current status

**KCA v1.0: PROPOSED / REQUIRES HUMAN APPROVAL.**

This document formalizes the proposed knowledge-continuity architecture. Its existence is not evidence that the operational controls listed in Section 17 have already been implemented or tested.
