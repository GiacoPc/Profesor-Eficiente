# PROJECT RECOVERY & CONTINUITY PROTOCOL (PRCP)

**Document ID:** PRCP
**Version:** 0.1
**Status:** DECIDED / ACTIVE RECOVERY PROTOCOL
**Effective date:** 2026-09-06

## 1. Purpose

PRCP establishes mandatory controls to prevent loss, ambiguity, or silent corruption of project knowledge and repository state.

The project is currently in **RECOVERY REQUIRED** status. Architectural knowledge remains recoverable from the conversation record, while the inspected Git tree is not considered complete or authoritative for the previously developed artifact set until reconciliation is finished.

## 2. Source-of-truth hierarchy during recovery

1. Git objects/commits actually verified in the repository.
2. Approved project specifications and governance artifacts, once verified in Git.
3. Recoverable architectural content from the project conversation, explicitly labeled `RECOVERED` and `UNVERIFIED` until revalidated.
4. Conversation history as historical evidence, never as an implicit source of truth.
5. AI memory/model inference is never authoritative.

No artifact is promoted to `APPROVED` merely because it can be reconstructed from memory or conversation.

## 3. Mandatory recovery controls

### R-01 — Forensic preservation

Before modifying an untrusted project ref, create a preservation branch pointing to its exact verified HEAD. The preservation ref must never be rewritten during recovery.

### R-02 — Exact-HEAD identity

Every recovery checkpoint records branch name, commit SHA, tree SHA, timestamp, and relevant file/blob SHAs.

### R-03 — Tree completeness verification

A recovery checkpoint is invalid unless the recursive Git tree is inspected and its result is recorded. A commit message claiming restoration is not evidence of tree completeness.

### R-04 — Artifact classification

Every recovered item must carry one of: `FACT`, `RECOVERED`, `INFERRED`, `UNKNOWN`, `CONFLICT`.

### R-05 — No silent reconstruction

Missing files may be reconstructed from conversation evidence only when their content is sufficiently recoverable. Reconstruction must be explicitly labeled and cannot silently replace a verified historical artifact.

### R-06 — No destructive repair

Recovery must first preserve the observed state, then create a separate recovery branch. Existing forensic refs are immutable by process.

### R-07 — Checkpoint after material milestones

After every major recovery batch, record a manifest and verify the exact resulting HEAD before proceeding.

### R-08 — Local redundancy

For each major milestone, produce a human-readable snapshot/recovery pack suitable for storage outside GitHub. If binary packaging is unavailable in the active environment, the repository must contain the complete textual recovery pack and manifest, and the user must be informed of the limitation.

### R-09 — Independent audit

P0/P1 governance, architecture, integrity, model/runtime, security, performance and release claims require independent secondary review before approval.

### R-10 — Claim discipline

No statement may use `VERIFIED`, `OBSERVED`, `REVIEWED`, `PASSED`, or equivalent language unless direct evidence for that exact claim has been inspected.

## 4. Recovery sequence

1. Freeze conceptual progression; no new architectural contract is approved during forensic inventory.
2. Preserve current untrusted branch state.
3. Inventory current recursive tree and exact HEAD.
4. Traverse recent parent commits and surviving Git objects/branches to locate recoverable artifacts.
5. Build a recovery manifest distinguishing `VERIFIED`, `RECOVERED`, `MISSING`, and `CONFLICT`.
6. Reconstruct only missing artifacts that are sufficiently supported by conversation evidence.
7. Reconcile reconstructed artifacts against the surviving contracts and Architecture Bible.
8. Create a coherent recovery baseline.
9. Verify recursive tree, commit, and file/blob identities.
10. Create a downloadable/local snapshot outside GitHub when tooling permits.
11. Run executable governance/consistency checks.
12. Prepare the independent secondary audit pack.
13. Only after audit and human approval, resume P1 source-spec integration and later SRA work.

## 5. Recovery gate

**Current gate: RECOVERY IN PROGRESS — NO IMPLEMENTATION AUTHORIZATION.**

Recovery is complete only when the Recovery Manifest is internally consistent, the reconstructed baseline is explicitly classified, the exact HEAD is verified, and the user has a durable external snapshot or equivalent independently retrievable recovery pack.

## 6. Prohibited shortcuts

- Treating a commit message as proof of tree contents.
- Treating AI memory as repository state.
- Treating a prior assistant claim as evidence.
- Force-moving a branch before preserving its current HEAD.
- Claiming CI success for a different commit.
- Marking reconstructed material as historically verified without a Git/object or source citation.
- Continuing into implementation merely because the conceptual architecture is coherent.
