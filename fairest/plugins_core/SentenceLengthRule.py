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

from typing import Optional, Union, List

from spacy.tokens import Span

from fairest.models import BaseSectionRule, Request, DocumentModel, DocumentSection, Report, SeverityLevel, \
    RuleDescription, RuleProperty


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
                        "If the sentence is longer than allowed, produce a report with the offending sentence.",
            author="Core Fairest Plugin"
        )

    @classmethod
    def describe_properties(cls) -> List[RuleProperty]:
        return [
            RuleProperty('length',
                         'The threshold for making a report. '
                         'Any sentence longer than this value is considered too long.',
                         80),
            RuleProperty('Severity', "Reports are marked with this level of severity.", SeverityLevel.WARNING)
        ]

    def run_section_rule(self, request: Request, model: DocumentModel, section: DocumentSection) \
            -> Optional[Union[Report, List[Report]]]:
        result = []
        doc = section.get_nlp_text()
        severity = self.properties.get('Severity', SeverityLevel.WARNING)
        for sent in doc.sents:
            if len(sent) > self.properties.get('length', 80):
                result.append(SentenceLengthReport(sent, section.get_position(), severity))
        if len(result) > 0:
            return result


class SentenceLengthReport(Report):
    def __init__(self, sentence: Span, position: str, severity: SeverityLevel):
        message = f"""
Overly long sentence detected: '{sentence[:15]} ... {sentence[-15:]}'
Long sentences affect readability and are arguably prone to errors and ambiguity. 
Consider fixing them by simplifying them into several sentences.
        """
        super().__init__(title="Overly long sentence", message=message,
                         rule_id="SentenceLengthRule",
                         severity_level=severity,
                         position=f"Paragraph: {position}, character: {sentence.start}")
