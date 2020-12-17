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

from typing import List, Union, Optional

from fairest.models import Request, DocumentSection, DocumentModel, BaseDocumentModelRule, RuleDescription


class BasicTextSection(DocumentSection):
    """
    A unit of the BasicTextModel.
    """

    def get_position(self) -> str:
        return self.position

    def __init__(self, text: str, position: str):
        """
        A unit of the BasicTextModel.

        :param text: The text of this section.
        :param position: The position of this section in the document.
          Can be a paragraph number or the index of the text in a list.
        """
        self.text = text
        self.position = position

    def get_text(self) -> str:
        return self.text


class BasicTextModel(DocumentModel):
    def get_full_text(self) -> List[str]:
        return [section.get_text() for section in self.paragraphs]

    def __init__(self, text: Union[List[str], str]):
        """
        The BasicTextModel accepts a string or a list of strings and transforms it into a model
        for fairest processing.

        :param text: A string or a list of strings. If a string, newlines are split into a list.
          If a list is created or provided, the `position` of each BasicTextSection is its index
          in the list.
        """
        super().__init__()
        if type(text) == str:
            self.paragraphs = [BasicTextSection(content, str(index)) for index, content in enumerate(text.split('\n'))]
        else:
            self.paragraphs = [BasicTextSection(content, str(index)) for index, content in enumerate(text)]

    def __getitem__(self, i: int) -> BasicTextSection:
        return self.paragraphs[i]

    def __len__(self) -> int:
        return len(self.paragraphs)


class BasicTextModelRule(BaseDocumentModelRule):

    def check_document(self, document: Union[str, bytes], current: Optional[DocumentModel]) -> bool:
        return document != "" and isinstance(document, str) and current is None

    @classmethod
    def describe(cls) -> RuleDescription:
        return RuleDescription(
            title="Basic Text Model Rule",
            description="The BasicTextModel accepts a string or a list of strings and "
                        "transforms it into a model for fairest processing.",
            author="Core Fairest Plugin"
        )

    def run_document_model_rule(self, request: Request) -> Optional[DocumentModel]:
        return BasicTextModel(request.request_body)
