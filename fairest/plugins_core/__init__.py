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

import fairest
from fairest.plugins_core.BasicDOCX import BasicDocxModelRule
from fairest.plugins_core.BasicText import BasicTextModelRule
from fairest.plugins_core.DocumentStatisticsRule import DocumentStatisticsRule
from fairest.plugins_core.SentenceLengthRule import SentenceLengthRule


@fairest.hook_impl(trylast=True)
def get_document_model_rules():
    return [BasicTextModelRule, BasicDocxModelRule]


@fairest.hook_impl
def get_document_rules():
    return [DocumentStatisticsRule]


@fairest.hook_impl
def get_section_rules():
    return [SentenceLengthRule]
