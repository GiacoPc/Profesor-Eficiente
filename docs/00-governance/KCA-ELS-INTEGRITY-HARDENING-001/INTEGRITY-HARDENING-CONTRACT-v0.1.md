# KCA/ELS Integrity Hardening — Emergency Corrective Iteration

**ID:** KCA-ELS-INTEGRITY-HARDENING-001  
**Contract:** INTEGRITY-HARDENING-CONTRACT v0.1  
**Status:** PROPOSED / REQUIRES HUMAN APPROVAL  
**Risk:** L2  
**Implementation:** NOT AUTHORIZED  
**ELS readiness:** NOT AUTHORIZED  
**P1 closure:** NOT AUTHORIZED

## 1. Trigger

This iteration is opened because the project demonstrated a concrete integrity failure mode: an audit package and its governing prompt were temporarily incompatible, followed by a circular self-hash manifest defect. The failure exposed broader risks: stale state, incomplete packages, scope drift, and claims based on artifacts that were not proven to correspond to the declared source state.

This is a process/information-integrity correction. It must be resolved before the next external audit package is prepared.

## 2. Authority boundary

KCA governs durable project knowledge and continuity. ELS governs the engineering loop. PGKI governs evidence, authority, conflict, and approval semantics. Git remains the canonical versioned record; Obsidian is a non-authoritative human interface.

This contract may define controls and acceptance criteria, but it cannot authorize its own implementation or promote any proposal to canonical authority.

## 3. Hardening objectives

The resulting system MUST make the following independently checkable before governed work proceeds:

1. **Canonical state identity** — every governed operation binds to an exact repository ref and state commit; current-state claims require fresh identity verification.
2. **Artifact identity** — every material artifact can be bound to an exact byte/content identity and, where applicable, a Git object identity.
3. **Status/authority** — canonical, proposed, evidence, recovery, unknown, conflict, deprecated and superseded states are explicit and cannot be inferred from filename or AI assertion.
4. **Context manifest integrity** — a bootstrap context declares scope, source identities, statuses, required artifacts, and exclusions; unresolved or stale inputs block governed continuation.
5. **Artifact-set completeness** — an audit/transfer package declares its required contents and fails closed when required evidence is absent, mismatched, stale, or outside scope.
6. **Prompt/evidence compatibility** — a governing prompt MUST declare the evidence classes and artifact paths it requires; the package MUST prove that those requirements are satisfied or explicitly unavailable.
7. **Manifest non-circularity** — integrity manifests MUST NOT depend on their own final hash value.
8. **Cross-representation consistency** — Markdown, YAML, manifests, prompts and indexes representing the same contract MUST be semantically consistent; contradictions block promotion.
9. **Freshness** — an artifact copied from an earlier state cannot be presented as current without an explicit source identity and freshness determination.
10. **Failure-closed behavior** — UNKNOWN, CONFLICT, missing identity, missing required artifact, scope mismatch, and unverifiable provenance block PASS and governed continuation.
11. **Reproducible package generation** — package generation MUST be deterministic from a declared source state and specification, with a machine-checkable manifest.
12. **Human approval boundary** — generated packages, validators, context maps and proposed corrections remain non-authoritative until the governing approval step is completed.

## 4. Canonical control-plane model

```text
CANONICAL GIT STATE
      ↓
IDENTITY RESOLUTION
      ↓
KCA CONTEXT MANIFEST
      ↓
TASK-SPECIFIC CONTEXT RESOLUTION
      ↓
ARTIFACT SET / AUDIT PACK SPECIFICATION
      ↓
DETERMINISTIC VALIDATION
      ↓
PASS | UNKNOWN | CONFLICT | FAIL
      ↓
ONLY PASS MAY ENTER GOVERNED WORK
```

An AI may consume this result but cannot replace it with an assertion.

## 5. Required contracts

The implementation phase MUST be preceded by explicit contracts for C01–C06: Canonical Artifact Identity; Context Resolution / Bootstrap; Audit-Pack Manifest; Prompt/Evidence Compatibility; Integrity Validator; and Continuation Gate Integration. The continuation gate must consume the validated current state and MUST NOT be bypassable by manual assertion or alternate undocumented entry points.

## 6. Minimum required identity fields

A governed artifact reference SHOULD be representable as:

```yaml
artifact_id: <stable-id>
path: <repository-path-or-external-qualified-path>
status: CANONICAL | DECIDED | PROPOSED | EVIDENCE | RECOVERY | UNKNOWN | CONFLICT | DEPRECATED | SUPERSEDED
source:
  repository_ref: <ref-if-applicable>
  state_head: <sha-if-applicable>
  tree: <sha-if-applicable>
  content_sha256: <sha256>
  git_blob_sha: <sha-if-applicable>
freshness:
  basis: exact_head | explicit_snapshot | external_timestamp | unknown
  verified: true | false
verification: PASS | UNKNOWN | CONFLICT | FAIL
```

Loss of source identity, status, or verification semantics is not permitted.

## 7. Audit-package integrity contract

A package is admissible only when its governing prompt, prompt identity, scope, required evidence, artifact identities, freshness, non-circular manifest, path boundary, semantic compatibility, contradictions, exact package bytes, and declared source state are all explicitly validated. A ZIP opening successfully is not evidence of package integrity.

## 8. Context integrity contract

A bootstrap MUST reconstruct the bounded task context without conversation memory and MUST state what it knows, does not know, excludes, and the exact canonical state from which context was resolved. It MUST NOT claim that an artifact was reviewed if the artifact was not actually available and verified.

## 9. Threat/failure classes

The implementation test plan MUST cover wrong ref/branch, stale HEAD, changed artifacts, working-tree substitution, content-vs-Git-object mismatch, missing/extra artifacts, scope mismatch, unavailable evidence, circular manifests, duplicate identity, stale/superseded artifacts, path traversal, partial/interrupted generation, concurrency, rewritten history, unsupported topology, undisclosed continuation entry points, manual PASS assertions, and AI conversion of validator failure to PASS.

## 10. Acceptance semantics

`PASS` means the exact criterion was demonstrated by direct evidence. `FAIL` means the required property was tested and did not hold. `UNKNOWN` means it could not be established. `CONFLICT` means authoritative/evidentiary inputs disagree. For this iteration, UNKNOWN, CONFLICT, missing evidence, and unverifiable identity are blocking states and MUST NOT be normalized into PASS.

## 11. Required implementation sequence

```text
APPROVE HARDENING CONTRACT
        ↓
DEFINE C01–C06 CONTRACTS
        ↓
DEFINE ACCEPTANCE MATRIX + FAILURE MODEL
        ↓
INDEPENDENT L2 AUDIT
        ↓
HUMAN APPROVAL
        ↓
IMPLEMENT VALIDATORS / CONTROL PLANE
        ↓
ADVERSARIAL TESTS
        ↓
SELF-AUDIT
        ↓
INDEPENDENT AUDIT
        ↓
RECONCILIATION
        ↓
OPERATIONAL DRILLS
        ↓
HUMAN PROMOTION
```

No implementation is authorized before the first approval and independent L2 review.

## 12. Explicit non-actions

This iteration does NOT modify the existing checkpoint verifier, modify verifier tests, close P1 findings, declare KCA READY, declare ELS operational readiness, install/configure external tools, authorize autonomous agents to mutate canonical state, or treat the repository as operationally hardened merely because this contract exists.

## 13. Decision

**PROPOSED / REQUIRES HUMAN APPROVAL.**

The next authorized action is contract review and independent L2 audit of this hardening specification, not implementation.
