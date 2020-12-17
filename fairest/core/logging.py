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

import logging
from io import StringIO

from fairest.models import Response, Report


def init_logger(level=logging.DEBUG) -> logging.StreamHandler:
    ch = logging.StreamHandler(StringIO())
    fairest_logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fairest_logger.addHandler(ch)
    return ch


def close_logger(log_stream: logging.StreamHandler, response: Response):
    log_stream.flush()
    response.debug_log = log_stream.stream.getvalue()
    if response.source_request.options.get('development', False):
        response.add_report(DebugReport(response.debug_log))
    log_stream.close()


class DebugReport(Report):
    def __init__(self, log: str):
        message = "Output of Debug Log \n" + log
        super().__init__(title="Debug Log", message=message, rule_id="Core.DebugReport")


fairest_logger = logging.getLogger('fairest')
