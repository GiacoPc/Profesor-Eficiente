# KCA/ELS Integrity Hardening — Emergency Corrective Iteration

**ID:** KCA-ELS-INTEGRITY-HARDENING-001
**Contract:** INTEGRITY-HARDENING-CONTRACT v0.1
**Status:** PROPOSED / REQUIRES HUMAN APPROVAL
**Risk:** L2
**Implementation:** NOT AUTHORIZED
**ELS readiness:** NOT AUTHORIZED
**P1 closure:** NOT AUTHORIZED

## 1. Trigger

This iteration is opened because the project demonstrated a concrete integrity failure mode: an audit package and its governing prompt were temporarily incompatible, followed by a circular self-hash manifest defect. The failure exposed a broader class of risks: stale state, incomplete packages, scope drift, and claims based on artifacts that were not proven to correspond to the declared source state.

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

The hardening target is:

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

The implementation phase MUST be preceded by explicit contracts for:

### C01 — Canonical Artifact Identity

Defines repository ref, state HEAD, tree identity where applicable, path, content hash/blob identity, status, source timestamp/order identity, and verification result. It MUST distinguish the engineering state being referenced from the commit that stores metadata about that state.

### C02 — Context Resolution / Bootstrap

Defines mandatory anchors, task scope, selected artifacts, excluded artifacts, source identities, freshness, status, conflicts, and unavailable evidence. It MUST prohibit silent reconstruction of missing knowledge.

### C03 — Audit-Pack Manifest

Defines package identity/version, governing prompt identity, evidence requirements, included artifacts, exact source identities, content hashes, exclusions, unavailable evidence, and validation result. It MUST be non-circular.

### C04 — Prompt/Evidence Compatibility

Defines a machine-checkable relationship between a governing prompt's declared requirements and the package contents. A prompt requirement without corresponding evidence is `UNAVAILABLE`/`UNKNOWN`, never silently satisfied.

### C05 — Integrity Validator

Defines deterministic validation inputs/outputs and conservative failure semantics. Implementation details are intentionally deferred until the contract is approved.

### C06 — Continuation Gate Integration

Defines the single governed decision required before an ELS iteration can continue from a checkpoint/context/package. This must consume the validated current state and MUST NOT be bypassable by manual assertion or alternate undocumented entry points.

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

Fields may be refined during implementation, but loss of source identity, status, or verification semantics is not permitted.

## 7. Audit-package integrity contract

A package is admissible only when all of the following are true:

- governing prompt is explicitly identified;
- prompt content identity is recorded;
- package scope is explicitly declared;
- every required artifact is present or explicitly classified unavailable;
- included artifact identities are verified against their declared source;
- no stale or superseded artifact is silently presented as current;
- manifest hashes are non-circular;
- package paths do not escape the declared package boundary;
- prompt requirements and evidence inventory are semantically compatible;
- package-level contradictions are classified and block PASS;
- final validation is bound to the exact generated package bytes and source state.

A ZIP opening successfully is not evidence of package integrity.

## 8. Context integrity contract

A bootstrap MUST be sufficient to reconstruct the bounded task context without conversation memory. It MUST state what it knows, what it does not know, what it excluded, and the exact canonical state from which it resolved context.

A context package MUST NOT claim that an artifact was reviewed if the artifact was not actually available and verified.

## 9. Threat/failure classes

The implementation test plan MUST cover at least:

- wrong branch/ref;
- stale HEAD;
- changed artifact after manifest creation;
- working-tree substitution;
- content-vs-Git-object mismatch;
- missing required file;
- extra out-of-scope file;
- stale/superseded artifact;
- duplicate/conflicting artifact identity;
- prompt/package scope mismatch;
- prompt requires unavailable evidence;
- circular manifest/self-hash;
- malformed manifest;
- path traversal/package escape;
- partial package creation;
- interrupted package generation;
- concurrent modification;
- rewritten/force-pushed source history;
- detached or unsupported repository topology;
- undisclosed continuation entry point;
- manual PASS assertion without validator evidence;
- validator failure converted to PASS by an AI agent.

## 10. Acceptance semantics

`PASS` means the exact criterion was demonstrated by direct evidence.

`FAIL` means a required property was tested and did not hold.

`UNKNOWN` means the property could not be established from available evidence.

`CONFLICT` means authoritative/evidentiary inputs disagree.

For this hardening iteration, `UNKNOWN`, `CONFLICT`, missing evidence, and unverifiable identity are blocking states. They MUST NOT be normalized into PASS by interpretation.

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

This iteration does NOT:

- modify the existing checkpoint verifier;
- modify P1-001 through P1-005 contracts;
- close P1 findings;
- declare KCA READY;
- declare ELS operational readiness;
- install or configure Obsidian/MCP/Spec Kit/OpenSpec;
- authorize autonomous agents to mutate canonical state;
- treat the current repository as operationally hardened merely because this contract exists.

## 13. Decision

**PROPOSED / REQUIRES HUMAN APPROVAL.**

The next authorized action is contract review and independent L2 audit of this hardening specification, not implementation.
