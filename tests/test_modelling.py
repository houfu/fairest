import pytest

from fairest.core.modelling import get_model
from fairest.models import Request


@pytest.mark.parametrize('test_request, expected_name', [
    (Request('This is a test string'), 'BasicTextModel')
])
def test_get_model(test_request, expected_name):
    if result := get_model(test_request):
        assert result.document_type == expected_name
    else:
        assert False
