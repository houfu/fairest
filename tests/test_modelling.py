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

from fairest.core.modelling import get_model
from fairest.models import Request


@pytest.mark.parametrize('test_request, expected_name', [
    (Request('This is a test string'), 'BasicTextModel')
])
def test_get_model(test_request, expected_name):
    result = get_model(test_request)
    if result:
        assert result.document_type == expected_name
    else:
        assert False
