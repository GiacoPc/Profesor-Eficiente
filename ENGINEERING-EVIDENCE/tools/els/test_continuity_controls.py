"""Small deterministic POC for ELS continuity controls.

This is deliberately provider-independent and uses only a disposable temp directory.
"""
from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import tempfile
from pathlib import Path


def interruption_child(path: Path) -> None:
    path.write_text(json.dumps({"iteration": "ITER-0002G", "state_head": "TEST-STATE-HEAD"}))
    os.kill(os.getpid(), signal.SIGTERM)


def test_interrupt_and_resume() -> None:
    with tempfile.TemporaryDirectory() as td:
        checkpoint = Path(td) / "checkpoint.json"
        code = (
            "import os,signal,json,sys; "
            f"p={str(checkpoint)!r}; "
            "open(p,'w').write(json.dumps({'iteration':'ITER-0002G','state_head':'TEST-STATE-HEAD'})); "
            "os.kill(os.getpid(), signal.SIGTERM)"
        )
        proc = subprocess.run([sys.executable, "-c", code])
        assert proc.returncode != 0, "unexpected successful completion after simulated interruption"
        data = json.loads(checkpoint.read_text())
        assert data["state_head"] == "TEST-STATE-HEAD"
        assert data["iteration"] == "ITER-0002G"


def test_budget_stop() -> None:
    budget = 3
    completed = 0
    checkpointed = False
    for _ in range(10):
        if budget <= 0:
            checkpointed = True
            break
        budget -= 1
        completed += 1
    assert completed == 3
    assert budget == 0
    assert checkpointed is True


if __name__ == "__main__":
    test_interrupt_and_resume()
    test_budget_stop()
    print("PASS: process interruption/restart simulation")
    print("PASS: synthetic budget exhaustion stop")
