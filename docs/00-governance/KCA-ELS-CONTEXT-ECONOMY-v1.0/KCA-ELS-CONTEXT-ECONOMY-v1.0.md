# KCA-ELS-CONTEXT-ECONOMY v1.0

**Status:** IMPLEMENTED ON ISOLATED BRANCH / REQUIRES VALIDATION
**Authority:** subordinate to PGKI, KCA and approved ADRs
**Purpose:** reduce conversational context consumption without reducing evidence integrity.

## 1. Scope

This contract defines how project context is selected, minimized, packaged and consumed by an AI session. It does not make chat history, Obsidian, an LLM summary, or an external memory system authoritative.

## 2. Authority model

1. Git repository artifacts and approved decisions remain canonical.
2. Obsidian is a human-facing navigation/knowledge interface.
3. Chat history is transient working context.
4. Generated context packages are derived artifacts.
5. AI-generated summaries are never promoted to FACT without authoritative evidence.

## 3. Context classes

- **C0 Bootstrap:** minimum project identity, governance, current state, active objective and operating constraints.
- **C1 Task:** only the artifacts/evidence required for the current task.
- **C2 Cross-contract:** additional authoritative dependencies required to avoid violating adjacent contracts.
- **C3 Forensic:** exact historical evidence, hashes, diffs, incident records and recovery material; loaded only when required.

Default resolution is C0 + C1. C2 and C3 are demand-driven.

## 4. Core invariant

> The smallest sufficient context must be selected from authoritative sources; minimization may remove redundancy, never provenance or blocking evidence.

## 5. Mandatory behavior

- Resolve exact artifact identity before using content as authority.
- Prefer repository retrieval over chat-history reconstruction.
- Never infer missing evidence from prior conversation.
- Preserve status/evidence labels from PGKI.
- FAIL, UNKNOWN or CONFLICT on a governed dependency blocks governed continuation.
- A context package must identify its source artifacts and resolution timestamp.
- A new chat must be able to continue from C0 without requiring the full previous chat.
- Closing a chat must not terminate project continuity.
- Context compression must be reproducible from the same source state and policy.

## 6. Explicit non-goals

This v1.0 does not implement automatic injection into ChatGPT, external MCP memory, semantic vector databases, or autonomous repository mutation. Those are separate integrations and require independent validation.

## 7. Safety / F21

Any repository write performed by tooling associated with this system must follow:

`TARGET REF DECLARED -> TARGET REF RESOLVED -> TARGET HEAD VERIFIED -> WRITE WITH EXPLICIT TARGET -> RE-FETCH TARGET -> VERIFY RESULT`

Omission of an explicit target branch is a blocking error for governed writes.

## 8. Context budget policy

The resolver should optimize for:

`decision-relevant evidence / context cost`

Priority order:
1. Current approved decision/ADR
2. Active contract/specification
3. Exact dependency artifacts
4. Required test/evidence
5. Current project state
6. Historical/forensic material only when necessary

No arbitrary token percentage is treated as a governance fact until empirically measured.

## 9. Continuation contract

A continuation is valid only when the resolver can establish:

- project identity;
- current authoritative state;
- active objective;
- applicable constraints;
- required source artifacts;
- unresolved blockers/conflicts;
- next authorized action.

Otherwise the system returns `BLOCKED`, `UNKNOWN`, `CONFLICT`, or `NEEDS_HUMAN` rather than fabricating continuity.

## 10. Validation gate

This implementation is not considered operationally complete until an independent audit verifies the resolver policy, source identity, C0-C3 behavior, context minimization, provenance preservation, F21 write controls, and fail-closed continuation semantics.
