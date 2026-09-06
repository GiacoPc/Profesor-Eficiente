# Plan

1. Bootstrap exact ref/HEAD and identify ELS as the governing process under test.
2. Resolve minimum sufficient context and record exclusions.
3. Execute only inside the POC directory.
4. Create an intentional interruption checkpoint before the simulated continuation step.
5. Resume from checkpoint using repository verification, not conversation recollection.
6. Exercise anti-loop behavior with a synthetic repeated failure.
7. Record test results and evidence.
8. Perform self-audit and reconciliation.
9. Produce a final checkpoint and convergence decision.

Expected control states during the drill: CONTINUE -> PAUSE -> RECOVER -> CONTINUE -> CONVERGED.
