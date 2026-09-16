# Context Resolution Protocol v1.0

## Objective
Generate the minimum sufficient, provenance-preserving context for one governed task.

## Procedure

### 1. Identify
Resolve repository, branch/ref, current HEAD and task objective. If identity is ambiguous, stop.

### 2. Bootstrap C0
Load only project identity, governance authority, current state, active objective and hard constraints.

### 3. Resolve C1
Select exact artifacts needed to perform the task. Prefer approved current artifacts over historical material.

### 4. Resolve dependencies
Add C2 only when an active contract depends on another contract, policy, decision or evidence set.

### 5. Resolve forensic material
Add C3 only when exact historical state, incident evidence, hashes, diffs or recovery information is necessary.

### 6. Preserve provenance
For every authoritative claim retained in the package, preserve source path/identity and status/evidence classification.

### 7. Minimize
Remove duplicated prose, conversational repetition and irrelevant historical narrative. Never remove the evidence required to reproduce or audit a decision.

### 8. Validate
Check required fields, source identities, blockers and next authorized action.

### 9. Gate
- `FAIL` -> BLOCKED
- `UNKNOWN` -> BLOCKED
- `CONFLICT` -> BLOCKED
- missing source identity -> BLOCKED
- missing objective -> BLOCKED
- unresolved target identity for a write -> BLOCKED

### 10. Emit
Return one compact context package. The package is derived, disposable and reproducible; Git remains authoritative.

## F21 write rule

Before any governed write, resolve the target ref and verify its HEAD. The write operation must carry the explicit target branch/ref. After the write, re-fetch the target and verify the resulting identity. A missing explicit target is a hard stop.

## Continuation

The resolver must make it possible to start a fresh chat with C0 + the task-specific C1 package. Full chat history is not a required continuity mechanism.

## Non-claims

This protocol does not claim a fixed percentage of token savings. Savings must be measured experimentally against a defined baseline.
