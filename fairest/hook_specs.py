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
