from fairest.core.plugins import flatten_rules
from fairest.models import BaseRule


def test_flatten_rules():
    result = flatten_rules([BaseRule()])
    assert len(result) == 1
    result = flatten_rules([BaseRule(), [BaseRule(), BaseRule()]])
    assert len(result) == 3
