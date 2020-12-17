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
from typing import Optional


class SeverityLevel(Enum):
    """
    The SeverityLevel enum provides information on the severity of the report
    to give more context to the information given.

    * Error: This report is used for information which must be fixed.
    * Warning: This report is used for information which is serious, but can
      be ignored.
    * Hint: This report is used for useful information which the user is encouraged
      to adopt.
    * Others: A catch-all. (Try not to use it!)
    """
    ERROR = auto()
    WARNING = auto()
    HINT = auto()
    OTHERS = auto()


class Report:
    def __init__(self, title: str, message: str, rule_id: str, severity_level: SeverityLevel = SeverityLevel.OTHERS,
                 example: Optional[str] = None, attribution: Optional[str] = None, position: str = None):
        """
        An individual report.

        :param rule_id:
        :param position:
        :param title: A short title to summarise the action recommended by report.
        :param message: The full content of the report in Markdown for the report.
        :param severity_level:
        :param example:
        :param attribution:
        """
        self.title = title
        self.message = message
        self.rule_id = rule_id
        self.severity = severity_level
        self.example = example
        self.attribution = attribution
        self.position = position
