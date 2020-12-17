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
