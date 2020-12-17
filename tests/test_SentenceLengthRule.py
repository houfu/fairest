#  Copyright (c) 2020. Ang Hou Fu
#
#  This file is part of Fairest.
#
#  Fairest is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  any later version.
#
#   Fairest is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Fairest.  If not, see <https://www.gnu.org/licenses/>.

from fairest.models import Request, SeverityLevel, RuleType
from fairest.plugins_core import SentenceLengthRule
from fairest.plugins_core.BasicText import BasicTextModel


def test_run_section_rule():
    rule = SentenceLengthRule()
    test = "In the classical theory of gravity, which is based on real space-time, the universe can either have " \
           "existed for an infinite time or else it had a beginning at a singularity at some finite time in the past," \
           " the latter possibility of which, in fact, the singularity theorems indicate, although the quantum theory" \
           " of gravity, on the other hand, suggests a third possibility in which it is possible for space-time to be" \
           " finite in extent and yet to have no singularities that formed a boundary or edge because one is using " \
           "Euclidean space-times, in which the time direction is on the same footing as directions in space. This " \
           "is a sentence that will not be caught by the rule."
    model = BasicTextModel(test)
    reports = rule.run_section_rule(Request(body=test), model, model[0])
    assert len(reports) == 1
    assert reports[0].rule_id == 'SentenceLengthRule'
    assert reports[0].position == f"Paragraph: 0, character: 0"
    request = Request(body=test, SentenceLengthRule={'length': 5})
    rule = SentenceLengthRule(request=request)
    reports = rule.run_section_rule(request, model, model[0])
    assert len(reports) == 2
    request = Request(body=test, SentenceLengthRule={'Severity': SeverityLevel.OTHERS})
    rule = SentenceLengthRule(request=request)
    reports = rule.run_section_rule(request, model, model[0])
    assert reports[0].severity == SeverityLevel.OTHERS


def test_describe():
    assert SentenceLengthRule.describe()
    assert SentenceLengthRule.get_rule_type() == RuleType.SECTION


def test_describe_properties():
    assert SentenceLengthRule.describe_properties()
