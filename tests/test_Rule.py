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
