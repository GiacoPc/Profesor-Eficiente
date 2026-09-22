#!/usr/bin/env python3
"""Resolve repository/ref/HEAD identity safely in local and CI checkouts."""
from __future__ import annotations

import os
import subprocess
from collections.abc import Callable


GitFn = Callable[..., str]


def resolve_identity(git: GitFn, environ: dict[str, str] | None = None) -> dict[str, str]:
    env = os.environ if environ is None else environ
    repository = git("rev-parse", "--show-toplevel")
    head = git("rev-parse", "HEAD")
    remote = git("remote", "get-url", "origin")

    try:
        ref = git("symbolic-ref", "--short", "HEAD")
        ref_source = "git-symbolic-ref"
    except (subprocess.CalledProcessError, FileNotFoundError):
        ref = env.get("GITHUB_HEAD_REF") or env.get("GITHUB_REF_NAME") or ""
        ref_source = "github-actions-env" if ref else "unresolved"

    execution_ref = env.get("GITHUB_REF") or ref
    if not ref:
        raise RuntimeError(
            "Unable to resolve an engineering ref: detached HEAD without "
            "GITHUB_HEAD_REF or GITHUB_REF_NAME."
        )

    return {
        "repository": repository,
        "remote": remote,
        "ref": ref,
        "ref_source": ref_source,
        "execution_ref": execution_ref,
        "engineering_head": head,
    }
