# P1-001 L3 External Audit Handoff v0.1

## Purpose

This document defines the transfer protocol for an external AI auditor that has no access to the project's conversational history.

## Independence requirement

The external auditor must receive the L3 audit packet as its primary context and must not receive:
- project chat history;
- private reasoning or working notes;
- prior L2 verdicts as authoritative conclusions;
- statements about what result the project team expects.

The auditor may receive the governing contract and evidence explicitly contained in the packet.

## Required auditor deliverable

The auditor must return a signed/dated textual report containing:

1. P1-001-A result: PASS / FAIL / UNKNOWN / CONFLICT.
2. P1-001-B result: PASS / FAIL / UNKNOWN / CONFLICT.
3. P1-001-C result: PASS / FAIL / UNKNOWN / CONFLICT.
4. P1-001-D result: PASS / FAIL / UNKNOWN / CONFLICT.
5. P1-001-E result: PASS / FAIL / UNKNOWN / CONFLICT.
6. Evidence citation for every result.
7. Any contradiction found between contract, specification, code, CI evidence, and observed artifact.
8. Explicit evidence boundaries and non-claims.
9. Whether the supplied evidence satisfies the contract's closure prerequisites.
10. Any missing evidence required before closure.

## Prohibited auditor behavior

The auditor must not:
- infer a PASS from the project's prior audit conclusions;
- treat a CI success as proof of properties not exercised by that CI run;
- promote POSIX SIGTERM evidence to workstation crash, power loss, or Android process death;
- promote WB-001 evidence to unsupported persistence boundaries;
- modify repository files;
- authorize continuation.

## Acceptance of the L3 report

The L3 report becomes evidence only after:
- its provenance is recorded;
- its input packet version/hash is recorded;
- its independence conditions are confirmed;
- discrepancies with L2 are reconciled;
- human review is completed.

L3 is an evidence source, not an authority.

## External execution files

Master prompt for Grok:
`P1-001-L3-GROK-MASTER-PROMPT-v0.1.md`

Master prompt blob SHA:
`645d5bfbbf9bd9adf9319a05eda4b3be8050ab69`

Response capture template:
`P1-001-L3-RESPONSE-CAPTURE-TEMPLATE-v0.1.md`

Response template blob SHA:
`1411e63ab324dbbd3fcdb9fa1c3455bd851b31ea`

The intended transfer package is therefore:
1. `P1-001-L3-EXTERNAL-AUDIT-PACKET-v0.1.md`
2. `P1-001-L3-HANDOFF-INSTRUCTIONS-v0.1.md`
3. `P1-001-L3-GROK-MASTER-PROMPT-v0.1.md`
4. `P1-001-L3-RESPONSE-CAPTURE-TEMPLATE-v0.1.md`

The external auditor should receive the packet plus the master prompt. The response template is for the project side to capture the returned report and provenance.

## Current packet identity

Packet:
P1-001-L3-EXTERNAL-AUDIT-PACKET-v0.1.md

Packet blob SHA:
1bbe5f35020681891bdd40ebe096ad2d76dc8c2b

Packet branch:
audit/l3-p1-001-external-packet-001

Packet commit:
167334d83224bfd7f830c7b795210fddd55b6552

## Current state

L3 external execution: NOT YET PERFORMED.

P1-001 closure: NOT AUTHORIZED.

Continuation: NOT AUTHORIZED.
