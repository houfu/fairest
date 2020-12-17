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

from enum import Enum, auto
from typing import List, Union

from fairest.models import Report, Request


class ResponseCode(Enum):
    """
    Provides the final status of the processing.

    * OK: Fairest went over its rounds and completed its reporting.
    * Bad Request: Fairest could not process the request and gave up.
    * Forbidden: Fairest was not able to complete its reporting even though
      there was no error with the request.
    * With Error: Fairest completed its processing, but there was errors.
    """
    OK = auto()
    BAD_REQUEST = auto()
    FORBIDDEN = auto()
    WITH_ERROR = auto()


class Response:

    def __init__(self, request: Request):
        """
        Response is the output object of the fairest system

        :param request: The original request is stored for reference.
        """
        self.source_request = request
        self.reports: List[Report] = []
        self.response_code = ResponseCode.OK
        self.debug_log = ""

    def add_report(self, report: Union[Report, List[Report], None]):
        """Short cut for adding a report to the list."""
        if report:
            if type(report) is list:
                self.reports.extend(report)
            else:
                self.reports.append(report)
