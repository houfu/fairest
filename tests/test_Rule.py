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

from fairest.models import BaseRule


def test_describe():
    assert BaseRule.describe()
    assert len(BaseRule.describe_properties()) == 0


def test_properties():
    rule = BaseRule()
    # Empty properties update to something
    rule.properties = {'Test': False}
    assert 'Test' in rule.properties
    rule.properties = {'Test_2': False}
    assert 'Test' in rule.properties
    assert 'Test_2' in rule.properties
    rule.properties = {'Test_2': True}
    assert rule.properties['Test_2']
