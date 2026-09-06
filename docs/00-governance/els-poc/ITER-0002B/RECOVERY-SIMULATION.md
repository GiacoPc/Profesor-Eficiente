# ELS-POC-002B — Recovery Simulation

Status: EXECUTED / SIMULATION RECORD
Risk: L2
Branch: `recovery/els-poc-002`

## 1. Checkpoint identity contract

The checkpoint model treats these as distinct identities:

- `state_head`: exact repository state being checkpointed.
- `checkpoint_commit`: commit that durably stores the checkpoint record.

A checkpoint is invalid if these concepts are collapsed into a single `HEAD` field.

## 2. Crash simulation

Simulated interruption point: immediately after durable checkpoint creation and before the next engineering action.

Conversation context available after restart: NONE.

Required recovery inputs:

1. durable checkpoint record;
2. repository ref/state identity;
3. checkpoint commit identity;
4. objective and pending action recorded by the checkpoint.

Expected result: resume from durable state, not from conversational recollection.

Result: PASS at process level.

## 3. Cross-agent handoff simulation

Receiving agent is assumed to have no prior conversation context.

Minimum handoff package:

- source repository ref;
- `state_head`;
- `checkpoint_commit`;
- completed work;
- pending work;
- evidence;
- failures/unknowns;
- constraints;
- next authorized action.

Result: PASS at contract/process level.

## 4. Context minimization

The receiving agent must not require the complete conversation or complete repository history when the checkpoint identifies the relevant artifacts and state.

Result: PASS at contract/process level.

## 5. Exact identity verification

Recovery requires checking that the intended `state_head` is the repository state being resumed and that the `checkpoint_commit` is the durable record containing the checkpoint. Equality between the two is neither required nor expected.

Result: PASS at contract level; automated implementation is NOT PRESENT in this POC.

## 6. Limitations

This is a controlled process simulation. It does not constitute a real workstation crash, provider quota exhaustion, or independently executed second-agent recovery test.

No production-readiness claim is made.
