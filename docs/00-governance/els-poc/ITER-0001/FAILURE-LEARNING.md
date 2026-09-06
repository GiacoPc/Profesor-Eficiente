# Failure Learning — ELS-POC-001

## FL-001 — Checkpoint identity ambiguity

**Observed:** The intentional pause checkpoint records the repository HEAD immediately before the checkpoint file is committed (`cf9e9c4c129385a6e20e4d353173fba644417c8b`). The checkpoint file itself is then committed, moving the branch HEAD to `8d297e30121a7e74558617cdfd180ac2f8a9d0d3`.

**Impact:** A literal resume rule of “verify branch ref equals the checkpoint HEAD” is ambiguous/incorrect when the checkpoint artifact is stored in the same repository commit that creates the durable checkpoint.

**Classification:** PROCESS/DESIGN DEFECT, not a repository corruption finding.

**Root cause:** ELS v0.1 did not distinguish the engineering state being checkpointed from the commit that durably stores the checkpoint record.

**Required correction:** A checkpoint must distinguish at minimum:
- `state_head`: exact repository state being resumed;
- `checkpoint_commit`: exact commit containing the checkpoint record;
- `checkpoint_tree`: optional exact tree identity.

Resume must verify the durable checkpoint record and then verify the intended state identity according to the checkpoint semantics, rather than requiring the branch HEAD to equal the pre-checkpoint state head.

**Preventive control:** Add an explicit checkpoint identity contract to ELS and a regression test for “checkpoint commit differs from state head.”
