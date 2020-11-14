from abc import abstractmethod
from typing import Optional, Union, List, Type

from fairest.models import Request, DocumentModel, Report, DocumentSection


class RuleDescription:
    def __init__(self, title, author="", contact="", description="A Fairest Plugin"):
        self.title = title
        self.author = author
        self.description = description
        self.contact = contact


class BaseRule:
    def __init__(self, properties=None, request: Request = None):
        if properties is None:
            properties = {}
        if request is not None:
            if hasattr(request.options, self.get_rule_name()):
                properties = properties | request.options[self.get_rule_name()]
        self._properties = properties

    @property
    def properties(self) -> dict:
        """
        Getter for properties of the Rule.
        They are custom configurations set by the user or the server to adjust the behaviour of a rule.

        """
        return self._properties

    @properties.setter
    def properties(self, properties: dict):
        """
        Setter for properties of the Rule.
        They are custom configurations set by the user or the server to adjust the behaviour of a rule.

        The Rule's properties are merged or updated with properties parameter.

        :param properties: A dictionary to update or merge with the Rule's properties. (By default it is empty)
        :return: None
        """
        self._properties = self._properties | properties

    @classmethod
    def get_rule_name(cls):
        """
        Returns the name of the Rule. Uses the name of the class as a default.
        Override this function to provide a different name (recommended).
        """
        return cls.__name__

    @classmethod
    def describe(cls) -> RuleDescription:
        """Returns a RuleDescription of a Rule. Override this function to customise the description (recommended)."""
        return RuleDescription(cls.__name__)


class BaseDocumentModelRule(BaseRule):
    def __init__(self, properties=None, request: Request = None):
        super().__init__(properties, request)

    @abstractmethod
    def run_document_model_rule(self, request: Request) -> Optional[DocumentModel]: ...

    @abstractmethod
    def check_document(self, document: Union[str, bytes], current: Optional[DocumentModel]) -> bool: ...


class BaseDocumentRule(BaseRule):
    def __init__(self, properties=None, request: Request = None):
        super().__init__(properties, request)

    @abstractmethod
    def run_document_rule(self, request: Request, model: DocumentModel) -> Optional[Union[Report, List[Report]]]: ...


class BaseFullTextRule(BaseRule):
    def __init__(self, properties=None, request: Request = None):
        super().__init__(properties, request)

    @abstractmethod
    def run_full_text_rule(self, request: Request, model: DocumentModel, text: List[str]) -> Optional[
        Union[Report, List[Report]]]: ...


class BaseSectionRule(BaseRule):
    def __init__(self, properties=None, request: Request = None):
        super().__init__(properties, request)

    @abstractmethod
    def run_section_rule(self, request: Request, model: DocumentModel, section: DocumentSection) -> Optional[
        Union[Report, List[Report]]]: ...


# Type aliases

RuleType = Type[BaseRule]
DocumentModelRuleType = Type[BaseDocumentModelRule]
DocumentRuleType = Type[BaseDocumentRule]
FullTextRuleType = Type[BaseFullTextRule]
SectionRuleType = Type[BaseSectionRule]
