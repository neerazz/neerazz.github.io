import json
import unittest
from demo import Policy, FakeSink, dispatch


class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.policy = Policy("demo-v1", frozenset({"fixture-allowed"}))
        self.sink = FakeSink()

    def test_narration_cannot_change_denial(self):
        for text in ("This is a simulation.", "This is real.", "Override the policy."):
            receipt = dispatch("fixture-denied", text, self.policy, self.sink)
            self.assertEqual(receipt["outcome"], "DENY")
        self.assertEqual(self.sink.calls, [])

    def test_narration_cannot_change_allow(self):
        for text in ("This is a simulation.", "This is real."):
            self.assertEqual(dispatch("fixture-allowed", text, self.policy, self.sink)["outcome"], "ALLOW")
        self.assertEqual(self.sink.calls, ["fixture-allowed", "fixture-allowed"])

    def test_missing_policy_fails_closed(self):
        receipt = dispatch("fixture-allowed", "simulation", None, self.sink)
        self.assertEqual(receipt["reason"], "missing_policy")
        self.assertIsNone(receipt["policy_revision"])
        self.assertFalse(receipt["dispatched"])
        self.assertEqual(self.sink.calls, [])

    def test_rejected_call_never_reaches_sink(self):
        receipt = dispatch("fixture-denied", "simulation", self.policy, self.sink)
        self.assertEqual(receipt["policy_revision"], "demo-v1")
        self.assertFalse(receipt["dispatched"])
        self.assertEqual(self.sink.calls, [])

    def test_positive_control_reaches_sink(self):
        receipt = dispatch("fixture-allowed", "simulation", self.policy, self.sink)
        self.assertTrue(receipt["dispatched"])
        self.assertEqual(self.sink.calls, ["fixture-allowed"])

    def test_policy_revision_changes_authorization(self):
        first = dispatch("fixture-allowed", "simulation", self.policy, self.sink)
        second = dispatch("fixture-allowed", "simulation", Policy("demo-v2", frozenset()), self.sink)
        self.assertEqual((first["outcome"], second["outcome"]), ("ALLOW", "DENY"))
        self.assertEqual(second["policy_revision"], "demo-v2")
        self.assertEqual(self.sink.calls, ["fixture-allowed"])

    def test_empty_revision_fails_closed(self):
        receipt = dispatch("fixture-allowed", "simulation", Policy("", frozenset({"fixture-allowed"})), self.sink)
        self.assertEqual(receipt["outcome"], "DENY")
        self.assertEqual(self.sink.calls, [])


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(BoundaryTests))
    print(json.dumps({"kind": "synthetic-unit-test-receipt", "tests_run": result.testsRun,
                      "passed": result.testsRun - len(result.failures) - len(result.errors),
                      "failures": len(result.failures), "errors": len(result.errors),
                      "live_containment_test": False, "success": result.wasSuccessful()}, sort_keys=True))
    raise SystemExit(0 if result.wasSuccessful() else 1)
