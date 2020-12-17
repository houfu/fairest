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

from fairest.models import Request, RuleType
from fairest.plugins_core.BasicDOCX import BasicDOCXModel
from fairest.plugins_core.BasicText import BasicTextModel
from fairest.plugins_core.DocumentStatisticsRule import DocumentStatisticsRule


def test_run_document_rule():
    rule = DocumentStatisticsRule()
    assert rule.run_document_rule(Request(body='This is a test sentence.'), BasicTextModel('This is a test sentence.'))
    with open('suite/Service Agreement.docx', 'rb') as file:
        test = BasicDOCXModel(file)
    assert rule.run_document_rule(Request(body=""), test)


def test_describe():
    assert DocumentStatisticsRule.describe()
    assert DocumentStatisticsRule.get_rule_type() == RuleType.DOCUMENT
