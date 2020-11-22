from abc import abstractmethod
from typing import Optional, Union, List, Type

from fairest.models import Request, DocumentModel, Report, DocumentSection


class RuleDescription:
    def __init__(self, title, author="", contact="", description="A Fairest Plugin"):
        f"""
        This class describes a rule for information. For use with BaseRule.describe()

        :param title: The name of the rule.
        :param author: The person/organisation which wrote the rule.
        :param contact: A method to contact the author.
        :param description: A general description of what the Rule does.
        """
        self.title = title
        self.author = author
        self.description = description
        self.contact = contact


class RuleProperty:
    def __init__(self, property_name: str, description="", property_default=None, friendly_name=""):
        """
        This class describes information on a property which can be set for a rule to customise its behavior.
        For use with BaseRule.describe_properties()

        :param property_name: Name of property in the code.
        :param description: A description of what the property does.
        :param property_default: A description of what the default value of the property is.
        :param friendly_name: A user friendly name of the property
        """
        self.property_name = property_name
        self.description = description
        self.property_default = property_default
        self.friendly_name = friendly_name if friendly_name else self.property_name


class BaseRule:
    def __init__(self, properties=None, request: Request = None):
        self._properties = properties if properties is not None else {}
        if request is not None:
            if self.get_rule_name() in request.options:
                self._properties.update(request.options[self.get_rule_name()])

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
        self._properties.update(properties)

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

    @classmethod
    def describe_properties(cls) -> List[RuleProperty]:
        """
        Returns a description of the properties which are available to be set in properties.
        This is used for helping the user to set properties.

        :return: A dictionary of keys being the key of the property and the value being a tuple of
        the description of the property and an optional default value.
        """
        return []


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
SectionRuleType = Type[BaseSectionRule]
