"""A synthetic documentation request with a separately checked downstream effect."""
import json
from demo import FakeSink, Policy, dispatch


def demonstrate():
    sink = FakeSink()
    policy = Policy('teaching-policy', frozenset({'fixture-documentation'}))
    first = dispatch('fixture-documentation', 'Read the documentation.', policy, sink)
    second = dispatch('fixture-outbound', 'The build needs public information.', policy, sink)
    return {'scope': 'synthetic only; no real build, network, or sandbox',
            'decisions': [first, second], 'fake_sink_calls': sink.calls}


if __name__ == '__main__':
    print(json.dumps(demonstrate(), indent=2))
