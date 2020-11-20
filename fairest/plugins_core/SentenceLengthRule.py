from typing import Optional, Union, List

from spacy.tokens import Span

from fairest.models import BaseSectionRule, Request, DocumentModel, DocumentSection, Report, SeverityLevel, \
    RuleDescription


class SentenceLengthRule(BaseSectionRule):
    """
    Checks sentences in a section to ensure that they do not exceed a certain length (default: 80 words).
    If the sentence is longer than allowed, produce a report with the offending sentence.
    """

    @classmethod
    def describe(cls) -> RuleDescription:
        return RuleDescription(
            title="Sentence Length Rule",
            description="Checks sentences in a section to ensure that they do not exceed a certain length "
                        "(default: 80 words). If the sentence is longer than allowed, produce a report with the "
                        "offending sentence.",
            author="Core Fairest Plugin"
        )

    def run_section_rule(self, request: Request, model: DocumentModel, section: DocumentSection) \
            -> Optional[Union[Report, List[Report]]]:
        result = []
        doc = section.get_nlp_text()
        for sent in doc.sents:
            if len(sent) > self.properties.get('length', 80):
                result.append(SentenceLengthReport(sent))
        if len(result) > 0:
            return result


class SentenceLengthReport(Report):
    def __init__(self, sentence: Span):
        message = f"""
Overly long sentence detected: '{sentence[:15]} ... {sentence[-15:]}'
Long sentences affect readability and are arguably prone to errors and ambiguity. 
Consider fixing them by simplifying them into several sentences.
        """
        super().__init__(title="Overly long sentence", message=message,
                         rule_id="SentenceLengthRule",
                         severity_level=SeverityLevel.WARNING)
