# ELS v0.1.1 — Checkpoint Identity Amendment

**Status:** PROPOSED / REQUIRES HUMAN APPROVAL
**Parent:** `docs/00-governance/ENGINEERING-LOOP-SYSTEM-v0.1.md`
**Trigger:** ELS-POC-001 / FL-001

## Normative correction
A durable checkpoint stored in the same repository may itself advance the branch HEAD. Therefore ELS must distinguish:

```yaml
repository:
  ref: <ref>
  state_head: <exact repository state being checkpointed>
  state_tree: <optional tree identity>
  checkpoint_commit: <commit that durably stores the checkpoint>
  checkpoint_tree: <optional tree identity of checkpoint commit>
```

`state_head` identifies the engineering state to resume from. `checkpoint_commit` identifies the durable checkpoint record. Resume verification must first verify `checkpoint_commit` and the checkpoint contents, then verify that `state_head` is the intended state according to the checkpoint's phase semantics. It must NOT require `ref == state_head` when the checkpoint record was committed afterward.

## Required regression test
A compliant implementation/process must pass the case where writing the checkpoint changes the branch HEAD while preserving an unambiguous reference to the pre-checkpoint state.

## Compatibility
This amendment changes only checkpoint identity semantics. It does not authorize product implementation or alter PGKI/KCA authority.
