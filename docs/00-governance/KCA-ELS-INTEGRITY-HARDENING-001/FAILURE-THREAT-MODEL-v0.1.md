# KCA/ELS Integrity Hardening — Failure & Threat Model v0.1

**Status:** PROPOSED / SUPPORTING CONTRACT ARTIFACT  
**Authority:** Non-authoritative until governed approval

## Purpose

Translate the recent prompt/package mismatch, circular manifest defect, and wrong-target write incident into adversarial test classes. This document is a test-planning artifact, not evidence that any control currently works.

| ID | Failure class | Required detection | Blocking outcome |
|---|---|---|---|
| F01 | Wrong ref/branch | identity comparison | UNKNOWN/CONFLICT |
| F02 | Stale state | exact HEAD revalidation | UNKNOWN/CONFLICT |
| F03 | Artifact changed after manifest | content/object recheck | CONFLICT |
| F04 | Working-tree substitution | source-object binding | CONFLICT |
| F05 | Missing required artifact | manifest completeness | UNKNOWN |
| F06 | Extra/out-of-scope artifact | boundary validation | FAIL/CONFLICT |
| F07 | Prompt/package scope mismatch | requirement inventory comparison | CONFLICT |
| F08 | Required evidence unavailable | explicit availability status | UNKNOWN |
| F09 | Circular/self-hash manifest | non-circular manifest rule | FAIL |
| F10 | Duplicate identity | uniqueness validation | CONFLICT |
| F11 | Stale/superseded artifact presented as current | status/freshness validation | CONFLICT |
| F12 | Path traversal/package escape | canonical path validation | FAIL |
| F13 | Partial/interrupted package generation | atomicity/completeness check | UNKNOWN/FAIL |
| F14 | Concurrent modification | pre/post identity comparison | CONFLICT |
| F15 | Rewritten/force-pushed history | ancestry/source identity validation | CONFLICT/UNKNOWN |
| F16 | Unsupported repository topology | declared topology policy | UNKNOWN |
| F17 | Undisclosed continuation entry point | registered-surface inventory | UNKNOWN |
| F18 | Manual PASS assertion | machine evidence requirement | FAIL/UNKNOWN |
| F19 | AI converts validator failure to PASS | promotion gate enforcement | FAIL |
| F20 | Prompt references wrong artifact version | exact artifact identity check | CONFLICT |
| F21 | Wrong-target write / branch parameter omission | explicit target declaration + pre/post ref verification | FAIL/CONFLICT |

## Test design rule

A passing happy-path generation is insufficient. Each failure class requires a negative test demonstrating that the hardening layer refuses to promote the invalid state. Where the environment cannot reproduce a failure class, the result is `UNKNOWN`/`NOT_AVAILABLE`, not PASS.

## Scope

This model covers KCA/ELS information integrity and continuity. It does not establish security certification, workstation disaster recovery, Android process-death behavior, or provider quota guarantees. Those remain separate evidence classes.
