# ITER-0003-P1-RESOLUTION-002 — Correction Reconciliation v0.1

**Status:** PROPOSED / PENDING INDEPENDENT RE-AUDIT
**Risk:** L2
**Parent audit:** ITER-0003-P1-RESOLUTION-001 independent contract audit
**Parent contract:** P1-RESOLUTION-CONTRACT-v0.1

## 1. Trigger

The independent substantive audit of ITER-0003-P1-RESOLUTION-001 returned `PASS_WITH_LIMITATIONS` and identified one material P1 specification conflict: the Markdown dependency graph did not contain `P1-001 -> P1-002`, while the YAML acceptance matrix declared `P1-002.dependencies: [P1-001]`.

The audit also identified four P2 strengthening opportunities:

- definition of `independently executed` in P1-001-B;
- fail-closed treatment of unsupported/undeclared repository topologies in P1-002-C;
- extension of P1-004-E beyond a single named workflow;
- explicit versioned declaration of supported repository topologies.

## 2. Reconciliation decision

The dependency conflict is resolved at the specification-model level by preserving the dependency graph already expressed in the parent Markdown contract and removing the unnecessary `P1-001 -> P1-002` edge from the corrected matrix model.

The corrected graph is:

```text
P1-001 -> P1-004
P1-002 -> P1-005
P1-005 -> P1-004
P1-003 -> P1-004
```

No dependency `P1-001 -> P1-002` is permitted.

## 3. Strengthening decisions

The following P2 findings are incorporated into the correction proposal rather than silently ignored:

### P2-C-001
`P1-001-B` now defines independent execution in terms of a separately identifiable test execution, target process/state, interruption mechanism, durable evidence, and exact repository identity. Test independence is not conflated with real-world failure-class evidence.

### P2-C-002
Unsupported or undeclared repository topologies must resolve to `UNKNOWN` or `CONFLICT`; silent acceptance is prohibited.

### P2-C-003
P1-004 non-bypassability is defined over the governed continuation surface, including alternate registered and parallel continuation mechanisms. An undisclosed continuation mechanism leaves universal non-bypassability unproven.

### P2-C-004
A versioned declaration of supported and unsupported repository topology classes is made an implementation-admissibility requirement.

## 4. Boundary preservation

The correction proposal does not authorize:

- verifier changes;
- verifier-test changes;
- implementation;
- P1 closure;
- ELS operational readiness;
- autonomous continuation.

`ELS-CHECKPOINT v0.2` remains a separate approved artifact and is not re-approved by this iteration.

## 5. Required verification

The correction remains provisional until:

1. the corrected contract and matrix are cross-compared;
2. all R-001 through R-010 criteria are evidenced;
3. a fresh independent L2 secondary audit is completed;
4. the external audit is reconciled against repository evidence;
5. the human project authority explicitly approves the corrected contract.

## 6. Current conclusion

**CONVERGED_AT_PROPOSAL_LEVEL / NOT APPROVED**

The correction model is internally defined, but no claim is made that the parent contract has already been amended or approved. The parent contract remains blocked for implementation until the correction is applied to the authoritative specification pair and passes the required independent re-audit and human approval gates.
