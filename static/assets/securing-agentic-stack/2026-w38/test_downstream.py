import unittest
from downstream_demo import demonstrate


class DownstreamTests(unittest.TestCase):
    def test_allowed_front_door_does_not_authorize_downstream(self):
        result = demonstrate()
        self.assertEqual([r['outcome'] for r in result['decisions']], ['ALLOW', 'DENY'])
        self.assertEqual(result['fake_sink_calls'], ['fixture-documentation'])
        self.assertFalse(result['decisions'][1]['dispatched'])

    def test_receipts_share_evaluated_policy(self):
        result = demonstrate()
        self.assertEqual({r['policy_revision'] for r in result['decisions']}, {'teaching-policy'})


if __name__ == '__main__':
    unittest.main()
