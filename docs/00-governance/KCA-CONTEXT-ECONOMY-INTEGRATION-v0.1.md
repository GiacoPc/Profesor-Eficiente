# KCA Context Economy Integration v0.1

**Status:** PROPOSED / REQUIRES HUMAN APPROVAL  
**Scope:** Integration contract for KCA Context Economy, Compact Response, Minimal AI Bootstrap, and Repository-first/File-upload-last  
**Authority:** Subordinate to PGKI/KCA/ELS; does not alter their authority hierarchy

## 1. Purpose

This document binds the four proposed efficiency policies into one operational model without claiming that any of them is automatically enforced.

## 2. Components

| ID | Component | Primary responsibility |
|---|---|---|
| CE-01 | KCA Context Economy | minimize unnecessary context while preserving necessary evidence |
| CE-02 | KCA-ELS Compact Response | minimize conversational overhead without hiding material information |
| CE-03 | KCA Minimal AI Bootstrap | provide the minimum durable state required for safe session resumption |
| CE-04 | Repository-first / File-upload-last | choose the lowest-cost reliable acquisition path for project artifacts |

## 3. Combined flow

```text
CURRENT CANONICAL STATE
        ↓
MINIMAL BOOTSTRAP
        ↓
REPOSITORY-FIRST ACQUISITION
        ↓
CONTEXT CLASS C0/C1/C2/C3
        ↓
TASK / EVIDENCE ANALYSIS
        ↓
COMPACT RESPONSE
        ↓
CHECKPOINT / CONTINUATION DECISION
```

C3 forensic context is entered only when current evidence requires it.

## 4. Non-negotiable invariants

1. Evidence requirements outrank context-minimization goals.
2. Canonical state outranks conversational memory.
3. A summary cannot replace required primary evidence.
4. Repository retrieval must be bound to the relevant ref when state identity matters.
5. Upload fallback must preserve identity/version/provenance when the artifact becomes evidence.
6. Compact output cannot hide blockers, conflicts, uncertainty, or required findings.
7. Bootstrap cannot authorize an action forbidden by current governance.
8. None of the four components can authorize implementation, promotion, mastery, progression, or autonomous continuation.
9. `UNKNOWN` and `CONFLICT` remain blocking states wherever the governing contract says they are blocking.
10. Provider quota limits are not bypassed or represented as controllable by these policies.

## 5. Efficiency decision rule

Before acquiring context, ask:

```text
Is the information already canonical?
  YES → retrieve the specific artifact/ref.
  NO  → determine whether user upload or an independent source is required.

Is the artifact necessary for the current decision?
  NO  → do not acquire it.
  YES → acquire minimum sufficient context.

Does verification require primary evidence?
  YES → preserve/retrieve that evidence.
  NO  → a verified concise reference may suffice.
```

## 6. Required auditability

Future implementation must be able to demonstrate, at minimum:
- selected context class;
- selected artifact acquisition path;
- canonical ref used when relevant;
- reason for escalation to larger context;
- whether an upload fallback was used;
- preservation of blocking findings;
- bootstrap identity and authorization state.

## 7. Relationship to external skills

External communication/attention-management skills may influence presentation only after this integration contract and higher-order governance are respected. They cannot redefine evidence requirements, authority, blocking semantics, or project state.

## 8. Approval and implementation boundary

Approval of this integration proposal does not imply implementation approval. Implementation requires separately defined executable controls, tests, evidence, and appropriate review.

## 9. Current disposition

`PROPOSED / NOT IMPLEMENTED / NOT OPERATIONALLY VERIFIED`
