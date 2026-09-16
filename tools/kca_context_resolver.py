#!/usr/bin/env python3
"""Minimal deterministic KCA/ELS context resolver.

Design goal: generate a compact, provenance-preserving context package from the
repository without replaying a previous chat. It intentionally does not mutate
the repository and does not treat LLM output as authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CORE = [
    "docs/00-governance/PROJECT-CONSTITUTION.md",
    "docs/00-governance/PROJECT-STATE-BASELINE-v1.0.md",
    "docs/00-governance/ARCHITECTURE-BIBLE-v1.0.md",
]
KCA_DIR = "docs/00-governance/KCA-ELS-CONTEXT-ECONOMY-v1.0"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def identity() -> dict:
    return {
        "branch": git("branch", "--show-current"),
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
    }


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def candidate_files() -> list[Path]:
    paths: list[Path] = []
    for rel in CORE:
        p = ROOT / rel
        if p.exists():
            paths.append(p)
    gov = ROOT / KCA_DIR
    if gov.exists():
        paths.extend(sorted(gov.glob("*.md")))
        paths.extend(sorted(gov.glob("*.yaml")))
    return list(dict.fromkeys(paths))


def score(path: Path, terms: list[str]) -> int:
    text = path.read_text(encoding="utf-8", errors="replace").lower()
    name = path.name.lower()
    return sum(text.count(t.lower()) + 3 * name.count(t.lower()) for t in terms)


def resolve(objective: str, limit: int) -> dict:
    terms = [t for t in objective.lower().split() if len(t) > 2]
    files = candidate_files()
    ranked = sorted(((score(p, terms), p) for p in files), key=lambda x: (-x[0], str(x[1])))
    selected = [p for s, p in ranked if s > 0][:limit]
    # C0 is always included where available.
    for rel in CORE:
        p = ROOT / rel
        if p.exists() and p not in selected:
            selected.insert(0, p)
    selected = selected[:limit]

    sources = []
    for p in selected:
        rel = p.relative_to(ROOT).as_posix()
        sources.append({"path": rel, "sha256": sha256_file(p)})

    return {
        "package_id": "kca-context-" + hashlib.sha256(objective.encode()).hexdigest()[:16],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_state": identity(),
        "context_class": "C0+C1",
        "objective": objective,
        "source_artifacts": sources,
        "blockers": [],
        "next_authorized_action": "Use the selected authoritative artifacts to perform the bounded objective.",
        "evidence_refs": [],
        "omitted_context": "Unselected chat history, duplicated prose and irrelevant repository material.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a compact KCA/ELS context package.")
    parser.add_argument("objective", help="One bounded task objective")
    parser.add_argument("--limit", type=int, default=8, help="Maximum source artifacts")
    parser.add_argument("--output", type=Path, help="Write JSON package to this path")
    args = parser.parse_args()
    package = resolve(args.objective, max(1, args.limit))
    payload = json.dumps(package, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
