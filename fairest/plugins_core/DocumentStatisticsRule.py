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

from typing import Optional, Union, List

from textstat import textstat

from fairest.models import BaseDocumentRule, Request, DocumentModel, Report, RuleDescription


class DocumentStatisticsRule(BaseDocumentRule):
    """
    Produces a report of some useful statistics of the document. Uses textstat.
    """

    @classmethod
    def describe(cls) -> RuleDescription:
        return RuleDescription(
            title="Document Statistics Rule",
            description="Produces a report of some useful statistics of the document. Uses textstat.",
            author="Core Fairest Plugin"
        )

    def run_document_rule(self, request: Request, model: DocumentModel) -> Optional[Union[Report, List[Report]]]:
        doc = model.get_nlp_text()
        text = doc.text
        return Report(
            title="Document Statistics",
            message=
            f"""
Word count: {textstat.lexicon_count(text)}
Sentence count: {textstat.sentence_count(text)}
Average sentence length: {textstat.avg_sentence_length(text)}
Readability: {textstat.text_standard(text)}
Reading time: {textstat.reading_time(text)}s
            """,
            rule_id=self.get_rule_name()
        )
