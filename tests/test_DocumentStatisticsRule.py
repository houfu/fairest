from fairest.models import Request, RuleType
from fairest.plugins_core.BasicDOCX import BasicDOCXModel
from fairest.plugins_core.BasicText import BasicTextModel
from fairest.plugins_core.DocumentStatisticsRule import DocumentStatisticsRule


def test_run_document_rule():
    rule = DocumentStatisticsRule()
    assert rule.run_document_rule(Request(body='This is a test sentence.'), BasicTextModel('This is a test sentence.'))
    with open('Service Agreement.docx', 'rb') as file:
        test = BasicDOCXModel(file)
    assert rule.run_document_rule(Request(body=""), test)


def test_describe():
    assert DocumentStatisticsRule.describe()
    assert DocumentStatisticsRule.get_rule_type() == RuleType.DOCUMENT
