# Repository Policy

**Status:** APPROVED FOR PGKI-1.0 BASELINE

## Current repository

- Repository: `GiacoPc/Profesor-Eficiente`
- Visibility: `private`
- Default branch: `main`
- Governance branch: `baseline/pgki-1.0`
- Production implementation: not started

## Protection status

`main` is intentionally kept unchanged during baseline construction.

Branch protection is currently **BLOCKED_BY_CURRENT_GITHUB_PLAN**. GitHub reports that protected branches/rulesets for private repositories require a paid plan for a personal account. Therefore the repository must not claim that `main` is protected until that capability is actually enabled and verified.

## Compensating controls while protection is unavailable

1. Architectural work is performed on dedicated branches.
2. The PGKI baseline is isolated in `baseline/pgki-1.0`.
3. Pull request #1 is kept open and unmerged until baseline review is complete.
4. Governance CI runs on pushes and pull requests.
5. Project State records the protection limitation explicitly.
6. No direct change to `main` is required for the current baseline workflow.

## Target protection policy

When the repository plan supports it, `main` should require:

- pull request before merge;
- successful Governance CI;
- conversation resolution where applicable;
- no force pushes;
- no branch deletion;
- human review for architectural/governance changes;
- signed commits if the signing workflow is established.

The exact GitHub enforcement configuration is itself evidence-bearing and must be re-audited after activation.
