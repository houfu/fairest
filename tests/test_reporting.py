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

from fairest.core.reporting import add_report, run_reporting
from fairest.models import Response, Request, Report
from fairest.plugins_core import DocumentStatisticsRule, SentenceLengthRule
from fairest.plugins_core.BasicText import BasicTextModel


def test_add_report():
    response = Response(request=Request(body=''))
    add_report(None, response)
    assert len(response.reports) == 0
    add_report(Report(message='Test', title='Test', rule_id='Test'), response)
    assert len(response.reports) == 1
    reports = [Report(message='Test', title='Test', rule_id='Test'),
               Report(message='Test', title='Test', rule_id='Test')]
    add_report(reports, response)
    assert len(response.reports) == 3


def test_disable_rule():
    request = Request(body="This is a test string.",
                      disable=[DocumentStatisticsRule, SentenceLengthRule])
    model = BasicTextModel('This is a test string.')
    response = run_reporting(model, request, Response(request))
    assert len(response.reports) == 0
