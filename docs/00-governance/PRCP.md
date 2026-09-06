# PROJECT RECOVERY & CONTINUITY PROTOCOL (PRCP)

**Document ID:** PRCP
**Version:** 0.2
**Status:** DECIDED / ACTIVE RECOVERY PROTOCOL
**Effective date:** 2026-09-06

## 1. Purpose

PRCP establishes mandatory controls to prevent loss, ambiguity, silent corruption, or unsupported claims about project knowledge and repository state.

The project entered recovery after an inspected working-tree state proved incomplete. Recovery must preserve evidence before reconstruction and must distinguish verified Git history from recovered conversation knowledge.

## 2. Authority during recovery

1. Git commits, trees, and blobs directly verified in the repository.
2. Approved project specifications and governance artifacts, once directly verified.
3. Historical Git artifacts recovered from verified commits, explicitly classified by provenance.
4. Recoverable conversation content, classified `RECOVERED_FROM_CONVERSATION`, never silently promoted to historical Git fact.
5. AI memory/inference is never authoritative.

## 3. Mandatory controls

### R-01 — Forensic preservation

Before modifying an untrusted ref, preserve its exact verified HEAD in an immutable-by-process forensic branch.

### R-02 — Exact identity

Every checkpoint records branch/ref, commit SHA, tree SHA, timestamp, and critical file/blob SHAs.

### R-03 — Recursive-tree verification

A restoration claim is invalid unless the recursive tree is inspected. Commit messages are not evidence of tree completeness.

### R-04 — Provenance classification

Recovered material uses one of: `VERIFIED_GIT`, `RECOVERED_GIT_HISTORY`, `RECOVERED_FROM_CONVERSATION`, `INFERRED`, `UNKNOWN`, `CONFLICT`.

### R-05 — No destructive repair

Never force-move or overwrite the forensic preservation ref during recovery.

### R-06 — Checkpoint discipline

After every material recovery batch, re-fetch the exact resulting HEAD and verify the recursive tree plus changed critical blobs.

### R-07 — External redundancy

Each major milestone must have a human-readable recovery pack outside the sole conversational context. If binary export is unavailable, the repository must contain the complete textual pack and the limitation must be recorded.

### R-08 — Claim discipline

`OBSERVED`, `VERIFIED`, `REVIEWED`, `PASSED`, and equivalent terms require direct evidence for that exact claim.

### R-09 — Independent audit

P0/P1 governance, architecture, integrity, security, runtime/model, performance, pedagogy and release claims require an independent secondary audit before approval.

### R-10 — Implementation freeze

Recovery remains a blocking gate. No implementation authorization is implied by recovered architecture artifacts.

## 4. Recovery sequence

1. Freeze new architectural approvals.
2. Preserve the untrusted ref.
3. Inventory exact HEAD and recursive tree.
4. Traverse parent commits and surviving Git objects/branches.
5. Recover historical blobs before reconstructing anything manually.
6. Classify every artifact by provenance.
7. Reconcile historical artifacts against known architecture contracts.
8. Create a coherent recovery baseline on a separate branch.
9. Verify exact HEAD/tree/blob identities.
10. Create durable recovery snapshot/pack.
11. Execute governance/schema/invariant checks.
12. Prepare secondary audit pack.
13. Only after audit and human approval, resume P1 integration.

## 5. Recovery gate

**Current gate: RECOVERY IN PROGRESS — NO IMPLEMENTATION AUTHORIZATION.**

Recovery completion requires: a verified historical baseline, explicit classification of missing/recovered artifacts, exact-head verification, durable recovery documentation, and successful independent review where required.
