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
