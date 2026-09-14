# KCA Context Economy v0.1

**Status:** PROPOSED / REQUIRES HUMAN APPROVAL  
**Scope:** Knowledge Continuity Architecture (KCA) operational efficiency  
**Authority:** Subordinate to PGKI; does not alter evidence, authority, or approval rules

## 1. Purpose

KCA Context Economy defines how the project minimizes unnecessary context transfer, file uploads, repeated document ingestion, and redundant historical narration while preserving evidence, traceability, and methodological rigor.

The objective is not to optimize for shortest responses. The objective is to minimize **unnecessary context cost** while retaining the **minimum sufficient context** required for a correct and auditable decision.

## 2. Core principle

> **Minimum sufficient context, maximum necessary evidence.**

Context may be reduced when the omitted material is demonstrably irrelevant to the current decision. Evidence may not be omitted when it is required to verify the claim or decision.

## 3. Context classes

### C0 — Session bootstrap

Only the current project identity, state, active work, authorized action, blockers, relevant artifact identifiers, and mandatory prohibitions.

### C1 — Task context

C0 plus the minimum set of canonical artifacts required for the current task.

### C2 — Cross-contract context

C1 plus directly coupled contracts, matrices, ADRs, evidence, or tests when a cross-boundary dependency requires them.

### C3 — Forensic context

Expanded historical/recovery material only when a contradiction, integrity incident, provenance question, or recovery operation requires it.

C3 must never be the default.

## 4. Context selection rules

1. Resolve the task before retrieving context.
2. Retrieve canonical identifiers before document bodies where possible.
3. Reuse already verified unchanged artifacts instead of re-reading them.
4. Retrieve only directly relevant artifacts first.
5. Expand context only when evidence exposes a dependency, contradiction, or uncertainty.
6. Never replace required primary evidence with a summary solely to reduce context cost.
7. Historical material is loaded only when current canonical state is insufficient.
8. Unknown or unavailable evidence remains explicitly UNKNOWN/NOT_AVAILABLE.
9. Context optimization cannot change authority precedence.
10. Context optimization cannot authorize implementation or progression.

## 5. Repository-first interaction

Canonical repository artifacts should be retrieved from the repository when the required information is already present there and the connector/tooling can access it reliably. User file upload is the fallback, not the default.

## 6. Repetition control

The system should not repeatedly restate:
- settled architectural decisions;
- unchanged historical incidents;
- unchanged artifact contents;
- previously verified identities;
- generic methodology explanations.

A concise state reference may replace repetition when it preserves the required identifiers and evidence references.

## 7. Safety boundary

Context reduction is never allowed to:
- convert UNKNOWN into VERIFIED;
- convert INFERENCE into FACT;
- hide a contradiction;
- remove a blocking finding;
- bypass a required audit;
- bypass human approval;
- authorize autonomous continuation;
- mutate canonical state without the governing authorization.

## 8. Operational status

This document defines a proposed efficiency policy. It does not claim that the policy is implemented, automatically enforced, or integrated into every agent/runtime.
