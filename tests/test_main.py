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
