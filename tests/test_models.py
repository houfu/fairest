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

from fairest.models import Report, Request, Response, SeverityLevel
from fairest.plugins_core import SentenceLengthRule


def test_request():
    request = Request(body='', custom_param=True)
    assert request
    assert request.options['custom_param']
    request = Request(body='', disable=[SentenceLengthRule])
    assert request.is_rule_disabled(SentenceLengthRule)
    assert request.is_rule_disabled('SentenceLengthRule')


def test_report():
    assert Report('Test report title', 'Test report content', 'Test/Test-rule', severity_level=SeverityLevel.HINT)


def test_response_add_report():
    response = Response(Request(body=''))
    assert len(response.reports) == 0
    response.add_report(
        Report('Test report title', 'Test report content', 'Test/Test-rule', severity_level=SeverityLevel.HINT))
    assert len(response.reports) == 1


def test_is_string():
    test_request_1 = Request(body='String')
    assert test_request_1.is_string()
    test_request_2 = Request(body=b'Bytes')
    assert not test_request_2.is_string()
