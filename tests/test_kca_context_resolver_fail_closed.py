import unittest
from unittest.mock import patch

import tools.kca_context_resolver as resolver


class ResolverFailClosedTests(unittest.TestCase):
    def test_empty_objective_is_rejected(self):
        with self.assertRaises(resolver.ResolverError):
            resolver.resolve("   ")

    def test_non_positive_limit_is_rejected(self):
        with self.assertRaises(resolver.ResolverError):
            resolver.resolve("bounded task", limit=0)

    @patch.object(resolver, "repository_identity", return_value={
        "branch": "test-branch", "head": "a" * 40, "tree": "b" * 40
    })
    @patch.object(resolver, "worktree_blockers", return_value=[])
    @patch.object(resolver, "blob_identity")
    @patch("subprocess.check_output", return_value='status: "PROPOSED"')
    def test_unknown_dependency_validation_blocks_authorization(
        self, _git_show, blob_identity, _worktree, _identity
    ):
        def fake_blob(path, head):
            return {
                "path": path,
                "git_blob_sha": "c" * 40,
                "content_sha256": "d" * 64,
            }
        blob_identity.side_effect = fake_blob
        package = resolver.resolve("bounded task", limit=20)
        self.assertEqual(package["status"], "BLOCKED")
        self.assertIsNone(package["next_authorized_action"])
        self.assertTrue(package["blockers"])
        self.assertIn(
            "DEPENDENCY_GRAPH_VALIDATION_NOT_IMPLEMENTED",
            {item["code"] for item in package["blockers"]},
        )

    @patch.object(resolver, "repository_identity", return_value={
        "branch": "test-branch", "head": "a" * 40, "tree": "b" * 40
    })
    @patch.object(resolver, "worktree_blockers", return_value=[{
        "code": "DIRTY_WORKTREE", "state": "UNKNOWN", "detail": "test"
    }])
    @patch.object(resolver, "blob_identity")
    @patch("subprocess.check_output", return_value='status: "PROPOSED"')
    def test_dirty_tree_is_a_blocker(
        self, _git_show, blob_identity, _worktree, _identity
    ):
        blob_identity.side_effect = lambda path, head: {
            "path": path,
            "git_blob_sha": "c" * 40,
            "content_sha256": "d" * 64,
        }
        package = resolver.resolve("bounded task", limit=20)
        self.assertEqual(package["status"], "BLOCKED")
        self.assertIn("DIRTY_WORKTREE", {item["code"] for item in package["blockers"]})


if __name__ == "__main__":
    unittest.main()
