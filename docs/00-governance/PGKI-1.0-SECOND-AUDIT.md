# PGKI-1.0 — Second Audit Report

**Audit status:** PASS WITH EXPLICIT PLATFORM EXCEPTION
**Audited branch:** `baseline/pgki-1.0`
**Audited HEAD before this report:** `955a6dc481074d9afc54db58a0c4f1733f755f4a`
**CI evidence:** Governance run `33190840076`, conclusion `success`

## Scope

This second audit verifies that the P0 findings from the first audit were corrected and that new evidence was generated.

## P0 findings and disposition

| Finding | Disposition | Evidence |
|---|---|---|
| Project State said CI was pending | FIXED | `PROJECT-STATE.yaml` now records `ci_governance_validation: VERIFIED` |
| Context Manifest recursively bootstrapped itself | FIXED | `CONTEXT-MANIFEST.yaml` bootstrap no longer includes itself |
| Decision Ledger lacked evidence metadata | FIXED | v1.1 ledger schema requires evidence and affected artifacts |
| "Significant change" ADR rule was ambiguous | FIXED | `CHANGE-CLASSIFICATION.md` defines objective change classes and stop conditions |
| Secret scan was too narrow | IMPROVED | Governance CI scans additional common credential patterns |
| Governance CI had a false-negative terminology gate | FIXED | Redundant terminology gate removed after observed failure; core invariant checks retained |
| Branch protection was undocumented | FIXED WITH PLATFORM EXCEPTION | `REPOSITORY-POLICY.md` records the verified plan limitation and compensating controls |

## Evidence

The final successful Governance run for the audited HEAD completed:

- required-file validation: SUCCESS;
- YAML validation: SUCCESS;
- governance invariant/state consistency: SUCCESS;
- basic secret hygiene: SUCCESS.

## Platform exception

`main` is not protected because the current GitHub plan does not provide protected branches/rulesets for this private personal repository. This is not treated as a hidden or unresolved state. It is explicitly recorded as `BLOCKED_BY_CURRENT_GITHUB_PLAN` with compensating controls.

The baseline therefore cannot claim full GitHub enforcement parity. The exception must be revisited if the repository is upgraded to a plan supporting private-repository branch protection.

## Second-audit conclusion

The P0 governance findings are corrected or explicitly controlled. The baseline is **READY FOR HUMAN MERGE REVIEW**, subject to acceptance of the documented GitHub-plan exception.

The baseline is not yet tagged `PGKI-1.0`; tagging remains a post-merge operation.
