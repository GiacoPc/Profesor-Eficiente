# Independent L2 Audit Mandate — KCA/ELS Context Resolver Correction 001

## Audit language (mandatory)
The audit mandate, audit execution notes, findings, evidence references, verdict, limitations, and handoff must be written in English. The user-assistant coordination conversation may remain in Spanish. Do not translate this mandate into Spanish in the audit package.

## 1. Audit identity
- Repository: `GiacoPc/Profesor-Eficiente`
- Correction branch: `kca/els-context-resolver-correction-001`
- Frozen input baseline: `19bacd64ef723de9919b0d008d1cd78044821ead`
- Current correction-branch head at mandate creation: `481bd37f658f8d839d350d3704aaa3c81211f802`
- Audit type: independent L2 review of resolver correction contract, implementation, tests, provenance, and fail-closed behavior.
- Independence requirement: the auditor must not be the implementation author or rely solely on the implementation author's self-assessment.

## 2. Objective
Determine whether the resolver correction demonstrably prevents false authorization when source identity, dependencies, provenance, or gate state are missing, contradictory, or unverified.

## 3. Required review scope
1. Compare the correction implementation against the frozen baseline and identify all behavioral changes.
2. Review `tools/kca_context_resolver.py` for correctness, security, path handling, Git identity, provenance, deterministic behavior, and error handling.
3. Inspect `DEPENDENCY-MANIFEST.yaml` and verify whether the implementation actually parses and validates its schema and dependency graph, or merely makes assumptions about it.
4. Verify all required C0 sources are mandatory and that missing sources block.
5. Verify dirty tracked and untracked files block canonical claims.
6. Verify emitted source identities match the exact bytes from the declared Git tree.
7. Verify `FAIL`, `UNKNOWN`, and `CONFLICT` prevent authorization and produce a non-zero exit.
8. Test missing dependency nodes, dependency cycles, contradictory statuses, malformed manifest, absent provenance, empty objective, invalid limit, invalid paths, and source files that are absent at HEAD.
9. Verify C3/forensic material is opt-in and cannot silently become current authority.
10. Evaluate the regression tests for meaningful assertions, test isolation, and untested failure modes.
11. Review the F21 boundary. The resolver is read-only; do not accept claims that it enforces target-branch writes. Any future write adapter requires a separate target-declaration, target-HEAD verification, explicit-branch write, re-fetch, and result-verification test suite.
12. Verify the exact audit branch and commit identity before citing any evidence.

## 4. Required adversarial scenarios
- Required core artifact deleted from the declared source tree.
- Dependency manifest absent, malformed, or marked PROPOSED.
- Dependency graph contains a cycle or missing transitive dependency.
- A selected file is changed in the worktree after HEAD was recorded.
- Untracked file could influence candidate selection.
- The same task is run twice on identical frozen source state.
- The resolver is given a whitespace-only objective.
- The resolver is given a non-positive artifact limit.
- A status is UNKNOWN or a source identity conflicts with the declared commit.
- An attempted write has no explicit target branch (as a boundary test for any write adapter, not for this read-only resolver).

## 5. Verdict vocabulary
Use exactly one:
- `PASS`
- `PASS_WITH_LIMITATIONS`
- `FAIL`
- `UNKNOWN`
- `CONFLICT`

Each finding must include severity, requirement, observed evidence, reproduction method, impact, and disposition. Distinguish verified behavior from inference and untested behavior.

## 6. Evidence rules
- Cite exact commit SHA, file path, line range or blob identity, and test command/output where available.
- Do not infer test success from the existence of test files.
- Do not treat an author's self-audit as independent evidence.
- If execution is unavailable, label runtime behavior UNKNOWN.
- If source state cannot be verified, stop and return CONFLICT or UNKNOWN.
- Do not claim token savings without measured comparative results.

## 7. Forbidden conclusions
The audit must not declare production readiness, ELS readiness, autonomous continuation, governance promotion, P1 closure, or merge approval unless each is explicitly within scope and supported by evidence. This mandate does not authorize merge or modification of `main` or the frozen baseline branch.

## 8. Expected deliverables
- English-language audit report.
- Findings register with severity and reproducible evidence.
- Acceptance matrix mapping RCR-01 through RCR-12 to PASS/FAIL/UNKNOWN/CONFLICT.
- Explicit list of tests run and not run.
- Verdict and limitations.
- Reconciliation recommendations; no implementation changes by the auditor unless separately authorized.

## 9. Current known limitation
The correction implementation deliberately blocks authorization while transitive dependency graph validation remains unimplemented. The auditor must assess whether this fail-closed behavior is real and sufficient, but must not mistake it for complete resolver functionality.
