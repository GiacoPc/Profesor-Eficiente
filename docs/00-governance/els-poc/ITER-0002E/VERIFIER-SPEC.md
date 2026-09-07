# ELS-POC-002E — Checkpoint Integrity Verifier Specification

**Status:** PROPOSED / EXECUTION EVIDENCE PENDING

## Purpose
Provide a minimal mechanical guard that detects ambiguity or contradiction between the engineering state named by a checkpoint and the Git evidence that stores that checkpoint.

## Inputs
- checkpoint file path;
- current Git working reference;
- Git object database/history.

## Required checks
1. `repository.ref` exists and matches the current symbolic branch, unless an explicit expected ref is supplied.
2. `repository.state_head` exists and resolves to a commit.
3. Optional `repository.state_tree` matches the tree resolved from `state_head`.
4. The checkpoint artifact is present in Git history.
5. The Git-derived commit containing the checkpoint artifact descends from `state_head`.
6. The Git-derived checkpoint-storage commit is reachable from current `HEAD`.
7. A historical `checkpoint_storage_commit` payload field, when present, is treated as a claim and must match Git-derived evidence; it is never treated as authoritative proof.

## Status semantics
- `PASS`: all required checks are consistent.
- `CONFLICT`: contradictory repository/checkpoint identity or ancestry is detected.
- `UNKNOWN`: required evidence cannot be established (missing fields, unresolved objects, detached/unsupported state, or artifact outside repository).

## Deliberate design property
The verifier does **not** require `state_head == HEAD`. A checkpoint commit may advance `HEAD` after the state being checkpointed. This directly tests the defect found in ELS-POC-001 and the reconciliation from ELS-POC-002D.

## Safety boundary
The verifier is read-only with respect to Git history and checkpoint files. It must not repair, rewrite, force-update, merge, cherry-pick, or delete repository state.
