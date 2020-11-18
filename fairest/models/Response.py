from enum import Enum, auto
from typing import List, Union

from fairest.models import Report
from fairest.models.Request import Request


class ResponseCode(Enum):
    """
    Provides the final status of the processing.

    * OK: Fairest went over its rounds and completed its reporting.
    * Bad Request: Fairest could not process the request and gave up.
    * Forbidden: Fairest was not able to complete its reporting even though
      there was no error with the request.
    * With Error: Fairest completed its processing, but there was errors.
    """
    OK = auto
    BAD_REQUEST = auto
    FORBIDDEN = auto
    WITH_ERROR = auto


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

    def add_report(self, report: Union[Report, List[Report]]):
        """Short cut for adding a report to the list."""
        if type(report) is list:
            self.reports.extend(report)
        else:
            self.reports.append(report)
