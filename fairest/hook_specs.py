#  Copyright (c) 2020. Ang Hou Fu
#
#  This file is part of Fairest.
#
#  Fairest is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  any later version.
#
#    Fairest is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Fairest.  If not, see <https://www.gnu.org/licenses/>.

from typing import Union, List

import pluggy

from fairest.models import DocumentModelRuleClass, DocumentRuleClass, SectionRuleClass

hook_specs = pluggy.HookspecMarker('fairest')


@hook_specs
def get_document_model_rules() -> Union[DocumentModelRuleClass, List[DocumentModelRuleClass]]:
    """
    Gets a list of DocumentModelRule classes or a DocumentModelRule class from a package.

    DocumentModelRules reads a Request and returns a DocumentModel.

    """


@hook_specs
def get_document_rules() -> Union[DocumentRuleClass, List[DocumentRuleClass]]:
    """
    Gets a list of DocumentRule classes or a DocumentRule class from a package.

    DocumentRule reads a DocumentModel and produces reports.
    In most cases, they are specific to a file format.

    :return:
    """


@hook_specs
def get_section_rules() -> Union[SectionRuleClass, List[SectionRuleClass]]:
    """
    Gets a list of SectionRule classes or a SectionRule class from a package.

    SectionRule reads a short section of a document in plain text and produces reports.

    :return:
    """
