#!/usr/bin/env python3
"""Self-contained regression tests for the ELS checkpoint verifier."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VERIFIER = ROOT / "tools" / "els" / "checkpoint_integrity_verifier.py"


def run(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def commit(repo: Path, message: str) -> str:
    run("git", "add", ".", cwd=repo)
    p = run("git", "commit", "-m", message, cwd=repo)
    assert p.returncode == 0, p.stderr
    p = run("git", "rev-parse", "HEAD", cwd=repo)
    return p.stdout.strip()


def checkpoint(repo: Path, state_head: str, *, state_tree: str | None = None, storage: str | None = None) -> Path:
    path = repo / "checkpoint.yaml"
    lines = ["repository:", "  ref: main", f"  state_head: {state_head}"]
    if state_tree:
        lines.append(f"  state_tree: {state_tree}")
    if storage:
        lines.append(f"  checkpoint_storage_commit: {storage}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def invoke(repo: Path, path: Path) -> subprocess.CompletedProcess[str]:
    return run("python3", str(VERIFIER), str(path), cwd=repo)


def test_corrected_contract(repo: Path) -> None:
    (repo / "state.txt").write_text("state\n", encoding="utf-8")
    state_head = commit(repo, "state")
    path = checkpoint(repo, state_head)
    commit(repo, "checkpoint")
    p = invoke(repo, path)
    assert p.returncode == 0, p.stdout + p.stderr
    assert "status: PASS" in p.stdout
    assert f"state_head: {state_head}" in p.stdout


def test_historical_storage_conflict(repo: Path) -> None:
    (repo / "state.txt").write_text("state\n", encoding="utf-8")
    state_head = commit(repo, "state")
    path = checkpoint(repo, state_head, storage="0000000000000000000000000000000000000000")
    commit(repo, "checkpoint")
    p = invoke(repo, path)
    assert p.returncode == 2, p.stdout + p.stderr
    assert "CONFLICT" in p.stdout


def test_state_tree_conflict(repo: Path) -> None:
    (repo / "state.txt").write_text("state\n", encoding="utf-8")
    state_head = commit(repo, "state")
    path = checkpoint(repo, state_head, state_tree="0000000000000000000000000000000000000000")
    commit(repo, "checkpoint")
    p = invoke(repo, path)
    assert p.returncode == 2, p.stdout + p.stderr


def test_wrong_ref_conflict(repo: Path) -> None:
    (repo / "state.txt").write_text("state\n", encoding="utf-8")
    state_head = commit(repo, "state")
    path = checkpoint(repo, state_head)
    commit(repo, "checkpoint")
    p = invoke(repo, path)
    assert p.returncode == 0
    p = invoke(repo, path)
    assert p.returncode == 0
    p = run("git", "branch", "-m", "main", "other", cwd=repo)
    assert p.returncode == 0
    p = invoke(repo, path)
    assert p.returncode == 2, p.stdout + p.stderr


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        repo = Path(td)
        run("git", "init", "-b", "main", cwd=repo)
        run("git", "config", "user.name", "ELS Test", cwd=repo)
        run("git", "config", "user.email", "els-test@example.invalid", cwd=repo)
        # Each test uses its own nested repository so state cannot leak.
        tests = [
            test_corrected_contract,
            test_historical_storage_conflict,
            test_state_tree_conflict,
            test_wrong_ref_conflict,
        ]
        for test in tests:
            with tempfile.TemporaryDirectory(dir=repo) as nested:
                r = Path(nested)
                run("git", "init", "-b", "main", cwd=r)
                run("git", "config", "user.name", "ELS Test", cwd=r)
                run("git", "config", "user.email", "els-test@example.invalid", cwd=r)
                test(r)
                print(f"PASS {test.__name__}")


if __name__ == "__main__":
    main()
