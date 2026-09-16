# F21 Incident Record — Wrong-Target Write During L2 Preparation

**Status:** OPEN / FORENSIC
**Incident:** An L2 audit prompt creation omitted the explicit `branch` parameter and the GitHub contents write landed on `main`.
**Observed main commit after write:** `bbc159b1cba1ef18f7ff9003eebede2673cb86ce`
**Known-good main commit before incident:** `11fe4130ddcf70c4b21be056491fe599741adea9`
**Affected artifact:** `docs/00-governance/KCA-ELS-CONTEXT-ECONOMY-v1.0/INDEPENDENT-L2-AUDIT-PROMPT-v0.1.md`

## Evidence

The artifact was independently fetched from `main` after the write and confirmed present there. This incident is retained as evidence for F21 audit scope.

## Containment

The accidental commit is preserved on a recovery/forensic branch. `main` is to be restored to the known-good commit before any further governed work.

## Control implication

This demonstrates that F21 remains operationally relevant: documentation of explicit-target rules is insufficient unless every write operation is itself verified to carry the intended target. Future writes require pre-write target declaration, target HEAD verification, explicit branch/ref propagation, post-write refetch and result verification.

## Classification

FACT: the write landed on `main`.
EVIDENCE: post-write fetch of the artifact from `main`.
INFERENCE: none required to establish the incident.
UNKNOWN: whether any other unintended state changed beyond the identified commit; verify by commit/tree comparison.
