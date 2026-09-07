# ELS-POC-002D — Checkpoint Reconciliation

**Status:** EXECUTED / RECONCILIATION RECORD
**Risk:** L2
**Branch:** `recovery/els-poc-002`

## 1. Conflict preserved

The original POC-002B checkpoint remains unchanged. It declares `state_head: 4c641c124b10a4d15c81639121493b186d5298a6` and `checkpoint_commit: 408a51fae47747a3ddd22918ce639b135b15bf2b`. The original record is preserved as evidence and is not silently rewritten.

## 2. Repository evidence

The repository evidence establishes that the checkpoint artifact itself was subsequently stored in commit `14eedc5f5ce081f132e2486ccf5e9ce35d33129d`. The checkpoint therefore contains a stale/incorrect storage identity relative to the actual commit that contains the checkpoint file.

## 3. Root cause

The process treated `checkpoint_commit` as payload data even though the payload is written by that commit. This creates an authoring-order/self-reference hazard. A checkpoint record cannot safely require its own future storage commit SHA as authoritative content.

## 4. Corrected contract proposal

The checkpoint's authoritative payload identifies the engineering state being checkpointed, not the commit that stores the payload:

```yaml
repository:
  ref: <working ref>
  state_head: <exact engineering state being checkpointed>
  state_tree: <optional exact tree identity>
```

The storage commit is external Git metadata and MUST be derived from repository history or an external durable index after storage. It is not a self-authored field required for checkpoint validity.

If a handoff needs to identify the storage commit, it may carry `checkpoint_storage_commit` as a derived/verified metadata field, but that field must never be trusted solely because the checkpoint payload asserts it.

## 5. Reconciliation decision

`CONFLICT_RESOLVED_AT_MODEL_LEVEL / IMPLEMENTATION PENDING`

The original conflict is not erased. The corrected contract is a proposal and is not yet normative until the applicable ELS governance approval is completed.

## 6. Required regression behavior

A compliant checkpoint implementation/process must:

1. create a checkpoint for a known `state_head`;
2. persist the checkpoint in a later storage commit;
3. avoid requiring the storage commit SHA inside the payload before that commit exists;
4. independently derive/verify storage identity from Git;
5. preserve both identities without conflating them;
6. reject a handoff whose declared derived metadata conflicts with repository evidence;
7. permit recovery when the authoritative `state_head` and checkpoint payload are otherwise valid.

## 7. Gate status

ELS-G03: **NOT YET PASS**.

This reconciliation removes the identified conceptual ambiguity but does not establish an automated checkpoint verifier, real crash recovery, real quota exhaustion recovery, or independent secondary audit.

No production-readiness claim is made.
