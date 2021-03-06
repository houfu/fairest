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
