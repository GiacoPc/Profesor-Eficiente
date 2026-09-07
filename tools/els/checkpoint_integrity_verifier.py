#!/usr/bin/env python3
"""ELS checkpoint integrity verifier.

Exit codes:
  0 PASS
  2 CONFLICT
  3 UNKNOWN / invalid input

`state_head` is the resume-state identity. Any historical
`checkpoint_storage_commit` field is treated only as a claim and is checked
against Git-derived evidence; the corrected contract does not require it.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

PASS = 0
CONFLICT = 2
UNKNOWN = 3


def git(*args: str) -> str:
    p = subprocess.run(["git", *args], text=True, capture_output=True)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout).strip() or f"git {' '.join(args)} failed")
    return p.stdout.strip()


def scalar(text: str, key: str) -> str | None:
    m = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.*?)\s*$", text)
    if not m:
        return None
    value = m.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def emit(status: str, reason: str) -> int:
    print(f"status: {status}")
    print(f"reason: {reason}")
    return {"PASS": PASS, "CONFLICT": CONFLICT, "UNKNOWN": UNKNOWN}[status]


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ["git", "merge-base", "--is-ancestor", ancestor, descendant],
        text=True,
        capture_output=True,
    ).returncode == 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("checkpoint", type=Path)
    ap.add_argument("--ref", help="expected repository ref; defaults to checkpoint repository.ref")
    args = ap.parse_args()

    try:
        text = args.checkpoint.read_text(encoding="utf-8")
        ref = scalar(text, "ref")
        state_head = scalar(text, "state_head")
        declared_storage = scalar(text, "checkpoint_storage_commit")

        if not ref or not state_head:
            return emit("UNKNOWN", "checkpoint must contain repository.ref and repository.state_head")

        current_ref = git("symbolic-ref", "--quiet", "--short", "HEAD")
        expected_ref = args.ref or ref
        if current_ref != expected_ref:
            return emit("CONFLICT", f"current ref {current_ref!r} != expected ref {expected_ref!r}")

        git("cat-file", "-e", f"{state_head}^{{commit}}")
        if git("rev-parse", state_head) != state_head:
            return emit("UNKNOWN", "state_head is not a full, directly resolvable commit identity")

        state_tree = scalar(text, "state_tree")
        if state_tree:
            actual_tree = git("rev-parse", f"{state_head}^{{tree}}")
            if actual_tree != state_tree:
                return emit("CONFLICT", f"state_tree {state_tree!r} != Git tree {actual_tree!r}")

        repo_root = Path(git("rev-parse", "--show-toplevel"))
        try:
            checkpoint_path = str(args.checkpoint.resolve().relative_to(repo_root.resolve()))
        except ValueError:
            return emit("UNKNOWN", "checkpoint artifact must reside inside the Git repository")

        storage_candidates = git("log", "--format=%H", "-1", "--", checkpoint_path).splitlines()
        if not storage_candidates:
            return emit("UNKNOWN", "no Git commit contains the checkpoint artifact")
        derived_storage = storage_candidates[0]

        if not is_ancestor(state_head, derived_storage):
            return emit("CONFLICT", "checkpoint storage commit does not descend from state_head")
        if not is_ancestor(derived_storage, "HEAD"):
            return emit("CONFLICT", "checkpoint storage commit is not reachable from current HEAD")

        if declared_storage and declared_storage != derived_storage:
            return emit(
                "CONFLICT",
                f"declared checkpoint_storage_commit {declared_storage!r} != Git-derived {derived_storage!r}",
            )

        print("status: PASS")
        print(f"state_head: {state_head}")
        print(f"checkpoint_storage_commit: {derived_storage}")
        print("reason: checkpoint identity is consistent with repository evidence")
        return PASS
    except Exception as exc:
        return emit("UNKNOWN", str(exc))


if __name__ == "__main__":
    sys.exit(main())
