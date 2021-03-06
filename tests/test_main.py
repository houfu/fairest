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

from fairest.main import fairest
from fairest.models import ResponseCode


def test_main():
    assert fairest(body='').response_code == ResponseCode.BAD_REQUEST
    assert fairest(body='This is a test string').response_code == ResponseCode.OK
    assert fairest(body=b"ABCD").response_code == ResponseCode.BAD_REQUEST


def test_logging():
    assert fairest(body='').debug_log
    response = fairest(body="This is a test string.", disable_rules=['DocumentStatisticsRule', 'SentenceLengthRule'],
                       development=True)
    assert len(response.reports) == 1
