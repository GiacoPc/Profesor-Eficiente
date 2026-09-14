# KCA Minimal AI Bootstrap v0.1

**Status:** PROPOSED / REQUIRES HUMAN APPROVAL  
**Scope:** Cross-session project continuity  
**Authority:** Subordinate to PGKI and canonical repository state

## 1. Purpose

Provide the smallest durable context required for an AI agent to resume project work without relying on prior conversational memory.

## 2. Required fields

```yaml
project:
  id: required
  name: required
canonical_state:
  repository: required
  ref: required
  head: required
  state_status: required
active_work:
  iteration_id: required
  objective: required
  phase: required
  status: required
authorization:
  next_action: required
  implementation_authorized: required
  verifier_modification_authorized: required
  promotion_authorized: required
blockers:
  - id: required
    status: required
relevant_artifacts:
  - path: required
    role: required
    identity: optional
constraints:
  - required
unknowns:
  - required when applicable
```

## 3. Bootstrap rules

1. The bootstrap is a pointer to canonical state, not a replacement for canonical state.
2. `head` must identify the repository state being resumed, not merely the commit that stores the bootstrap/checkpoint.
3. The bootstrap must state authorization boundaries explicitly.
4. Missing required fields produce `UNKNOWN` and block autonomous continuation.
5. Contradictory fields produce `CONFLICT` and block continuation.
6. The agent must retrieve the minimum task-specific canonical artifacts after bootstrap.
7. The agent must not infer missing project state from conversational memory.
8. A stale bootstrap must not override newer canonical state.
9. A bootstrap cannot authorize actions forbidden by a current ADR, specification, Constitution, KCA, ELS, or active contract.

## 4. Session-start procedure

```text
BOOTSTRAP
  ↓
VERIFY REPOSITORY IDENTITY
  ↓
VERIFY CANONICAL HEAD
  ↓
READ ACTIVE WORK
  ↓
RESOLVE TASK CONTEXT
  ↓
RETRIEVE MINIMUM SUFFICIENT ARTIFACTS
  ↓
CHECK BLOCKERS / CONFLICTS
  ↓
CONTINUE | PAUSE | BLOCKED | NEEDS_HUMAN
```

## 5. Regeneration

A future automated `kca bootstrap` command may generate this artifact from canonical repository state. Until such automation is implemented and verified, generation remains procedural/manual and must not be described as automatic.

## 6. Operational status

This is a proposed bootstrap contract. It is not itself proof that cross-session continuity has been operationally demonstrated.
