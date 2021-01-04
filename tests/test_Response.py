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

from fairest.models import Response, Request, Report


def test_add_report():
    response = Response(Request(body='This is a test string'))
    assert len(response.reports) == 0
    response.add_report(Report('Test report', 'This is test Report', 'Test/Test'))
    assert len(response.reports) == 1
    response.add_report([Report('Test report', 'This is test Report', 'Test/Test')])
    assert len(response.reports) == 2
