from fairest.models import Request
from fairest.plugins_core import SentenceLengthRule
from fairest.plugins_core.BasicText import BasicTextModel


def test_run_section_rule():
    rule = SentenceLengthRule()
    test = "In the classical theory of gravity, which is based on real space-time, the universe can either have " \
           "existed for an infinite time or else it had a beginning at a singularity at some finite time in the past, " \
           "the latter possibility of which, in fact, the singularity theorems indicate, although the quantum theory " \
           "of gravity, on the other hand, suggests a third possibility in which it is possible for space-time to be " \
           "finite in extent and yet to have no singularities that formed a boundary or edge because one is using " \
           "Euclidean space-times, in which the time direction is on the same footing as directions in space. This " \
           "is a sentence that will not be caught by the rule."
    model = BasicTextModel(test)
    reports = rule.run_section_rule(Request(body=test), model, model[0])
    assert len(reports) == 1
