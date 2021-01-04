#  Copyright (c) 2021.  Ang Hou Fu
#
#  This software is licensed under the The MIT License.
#  You should have received a copy of the license terms with the software.
#  Otherwise, you can find the text here: https://opensource.org/licenses/MIT
#
#
#  This software is licensed under the The MIT License.
#  You should have received a copy of the license terms with the software.
#  Otherwise, you can find the text here: https://opensource.org/licenses/MIT
#

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
