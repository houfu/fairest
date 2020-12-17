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

import pytest

from fairest.models import Request, RuleType
from fairest.plugins_core.BasicDOCX import BasicDOCXModel, BasicDocxModelRule


def test_BasicDOCXModel():
    with open('suite/Service Agreement.docx', 'rb') as file:
        test = BasicDOCXModel(file)
    assert test
    assert test[0].get_text() == 'SERVICE AGREEMENT'
    assert test[1].get_position() == '1'
    assert test.get_full_text()


@pytest.mark.parametrize("test_document, test_current,expected", [
    (b"Test bytes", None, True),
    ("Test string", None, False),
    (b"Test bytes", "Some other plugin has already constructed a document model.", False),
])
def test_check_document(test_document, test_current, expected):
    rule = BasicDocxModelRule()
    assert rule.check_document(test_document, test_current) == expected


def test_run_document_model_rule():
    rule = BasicDocxModelRule()
    assert rule.get_rule_type() == RuleType.DOCUMENT_MODEL
    with open('suite/Service Agreement.docx', 'rb') as file:
        request_2 = Request(file.read())
    assert rule.run_document_model_rule(request_2)
    with open('test_BasicText.py', 'rb') as file:
        request_3 = Request(file.read())
    assert rule.run_document_model_rule(request_3) is None


def test_describe():
    assert BasicDocxModelRule.describe()
