#!/usr/bin/env python3
"""Regression tests for CI identity resolution."""
from __future__ import annotations

import subprocess

from ci_identity import resolve_identity


def test_symbolic_head() -> None:
    calls = {
        ("rev-parse", "--show-toplevel"): "/repo",
        ("rev-parse", "HEAD"): "abc123",
        ("remote", "get-url", "origin"): "https://github.com/GiacoPc/Profesor-Eficiente.git",
        ("symbolic-ref", "--short", "HEAD"): "feature/test",
    }

    def git(*args: str) -> str:
        return calls[args]

    identity = resolve_identity(git, {})
    assert identity["ref"] == "feature/test"
    assert identity["ref_source"] == "git-symbolic-ref"
    assert identity["execution_ref"] == "feature/test"
    assert identity["engineering_head"] == "abc123"


def test_detached_head_from_github_actions() -> None:
    calls = {
        ("rev-parse", "--show-toplevel"): "/repo",
        ("rev-parse", "HEAD"): "def456",
        ("remote", "get-url", "origin"): "https://github.com/GiacoPc/Profesor-Eficiente.git",
    }

    def git(*args: str) -> str:
        if args == ("symbolic-ref", "--short", "HEAD"):
            raise subprocess.CalledProcessError(128, ["git", *args])
        return calls[args]

    env = {
        "GITHUB_HEAD_REF": "els/iter-0003-p1-001-c-wb001-execution-001",
        "GITHUB_REF": "refs/pull/123/merge",
    }
    identity = resolve_identity(git, env)
    assert identity["ref"] == env["GITHUB_HEAD_REF"]
    assert identity["ref_source"] == "github-actions-env"
    assert identity["execution_ref"] == env["GITHUB_REF"]
    assert identity["engineering_head"] == "def456"


def test_detached_head_without_ci_ref_fails_closed() -> None:
    calls = {
        ("rev-parse", "--show-toplevel"): "/repo",
        ("rev-parse", "HEAD"): "ghi789",
        ("remote", "get-url", "origin"): "https://github.com/GiacoPc/Profesor-Eficiente.git",
    }

    def git(*args: str) -> str:
        if args == ("symbolic-ref", "--short", "HEAD"):
            raise subprocess.CalledProcessError(128, ["git", *args])
        return calls[args]

    try:
        resolve_identity(git, {})
    except RuntimeError as exc:
        assert "engineering ref" in str(exc)
    else:
        raise AssertionError("detached HEAD without CI ref must fail closed")


if __name__ == "__main__":
    test_symbolic_head()
    test_detached_head_from_github_actions()
    test_detached_head_without_ci_ref_fails_closed()
    print("CI identity regression tests: PASS")
