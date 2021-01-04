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

import pytest

from fairest.models import Request, RuleType
from fairest.plugins_core.BasicText import BasicTextSection, BasicTextModel, BasicTextModelRule


def test_BasicTextSection():
    section = BasicTextSection('Paragraph 1', '1')
    assert section.get_text() == 'Paragraph 1'
    assert section.get_position() == '1'


def test_BasicTextModel():
    test_text = "3.4	The Service Provider shall perform the Services in accordance with all " \
                "codes, laws, statutes, ordinances, rules, regulations, standards and orders " \
                "(including without limitation any anti-corruption related regulation of Japanese and " \
                "foreign federal, state, and local governments and governmental agencies applicable " \
                "to the Services) (collectively, “Laws”). \n" \
                "3.5	The Service Provider represents and warrants that it is familiar with any anti-corruption " \
                "related regulation of Japanese and foreign federal, state, and local governments and governmental " \
                "agencies applicable to the Services (the “Anti-Corruption Law”) and its purposes."
    clauses = test_text.split('\n')
    model = BasicTextModel(clauses)
    assert model.document_type == 'BasicTextModel'
    doc_1 = model.get_nlp_text()
    assert doc_1.has_annotation("DEP")
    assert len(model) == 2
    assert model[
               1].get_text() == "3.5	The Service Provider represents and warrants that it is familiar with " \
                                "any anti-corruption related regulation of Japanese and foreign federal, state, " \
                                "and local governments and governmental agencies applicable to the Services " \
                                "(the “Anti-Corruption Law”) and its purposes."
    doc_2 = model[1].get_nlp_text()
    assert doc_2.has_annotation("DEP")
    assert model.get_full_text() == clauses
    model2 = BasicTextModel(test_text)
    assert len(model2) == len(model)


@pytest.mark.parametrize("test_document, test_current,expected", [
    (b"Test bytes", None, False),
    ("Test string", None, True),
    ("Test string", "Some other plugin has already constructed a document model.", False),
])
def test_check_document(test_document, test_current, expected):
    rule = BasicTextModelRule()
    assert rule.check_document(test_document, test_current) == expected


def test_describe():
    assert BasicTextModelRule.describe()
    assert BasicTextModelRule.get_rule_type() == RuleType.DOCUMENT_MODEL


@pytest.mark.parametrize("test_request, expected", [
    (Request('This is a test string'), True),
])
def test_run_document_model_rule(test_request, expected):
    rule = BasicTextModelRule()
    assert bool(rule.run_document_model_rule(test_request)) == expected
