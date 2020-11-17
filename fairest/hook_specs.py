from typing import Union, List

import pluggy

from fairest.models.Rule import SectionRuleType, DocumentRuleType, DocumentModelRuleType

hook_specs = pluggy.HookspecMarker('fairest')


@hook_specs
def get_DocumentModelRules() -> Union[DocumentModelRuleType, List[DocumentModelRuleType]]:
    """
    Gets a list of DocumentModelRule classes or a DocumentModelRule class from a package.

    DocumentModelRules reads a Request and returns a DocumentModel.

    """


@hook_specs
def get_DocumentRules() -> Union[DocumentRuleType, List[DocumentRuleType]]:
    """
    Gets a list of DocumentRule classes or a DocumentRule class from a package.

    DocumentRule reads a DocumentModel and produces reports.
    In most cases, they are specific to a file format.

    :return:
    """


@hook_specs
def get_SectionRules() -> Union[SectionRuleType, List[SectionRuleType]]:
    """
    Gets a list of SectionRule classes or a SectionRule class from a package.

    SectionRule reads a short section of a document in plain text and produces reports.

    :return:
    """
