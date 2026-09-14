# Independent L2 Audit Request — KCA Context Economy

**Status:** REQUESTED / NOT EXECUTED
**Target branch:** `kca/els-integrity-hardening-001`
**Target HEAD:** `90cf848c088987610901c2143390d551c51d46fd`
**Scope:** KCA Context Economy, KCA-ELS Compact Response, KCA Minimal AI Bootstrap, Repository-first/File-upload-last, and their integration with PGKI/KCA/ELS.

## Auditor independence
The substantive audit must be performed by a genuinely independent model/provider. A self-review by the same model that authored the policies does not satisfy the L2 independence requirement.

## Required audit questions
1. Are the four policies semantically compatible with PGKI, KCA, and ELS?
2. Do they accidentally create a new authority layer?
3. Can context minimization cause evidence loss or hidden uncertainty?
4. Can Repository-first suppress necessary external/local evidence?
5. Can Minimal Bootstrap become stale, authoritative, or unsafe?
6. Can Compact Response conceal blockers, conflicts, or negative findings?
7. Are C0/C1/C2/C3 context classes sufficiently deterministic?
8. Are the policies enforceable without creating unsafe autonomous continuation?
9. Are there contradictions between Markdown and YAML representations?
10. Are there bypasses or failure modes not identified by the self-audit?
11. Is the claim of `PASS_WITH_LIMITATIONS` justified by the supplied evidence?
12. What P0/P1/P2/P3 findings remain?

## Protected boundaries
The auditor may not authorize implementation, modify canonical artifacts, close the hardening iteration, or declare KCA/ELS operational readiness.

## Required verdict
Use exactly one primary verdict:
- PASS
- PASS_WITH_LIMITATIONS
- FAIL
- UNKNOWN
- CONFLICT

A verdict of PASS_WITH_LIMITATIONS, FAIL, UNKNOWN, or CONFLICT does not authorize promotion.
