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

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Sequence
from typing import overload, List


class DocumentSection:
    """
    Abstract representation of a unit in the Document model.
    Document interpreters should implement the get_text method to return its plain string representation,
    which is used to process full and short texts.
    """

    @abstractmethod
    def get_text(self) -> str: ...

    @abstractmethod
    def get_position(self) -> str: ...

    def get_nlp_text(self):
        from fairest.core.nlp import get_nlp_doc
        return get_nlp_doc(self.get_text())


class DocumentModel(Sequence):
    """
    Abstract representation of the document model in Fairest.
    Document interpreters should implement the abstract sequence methods.
    These methods are used for processing full and short texts.
    """

    @overload
    @abstractmethod
    def __getitem__(self, i: int) -> DocumentSection: ...

    @overload
    @abstractmethod
    def __getitem__(self, s: slice) -> Sequence[DocumentSection]: ...

    @abstractmethod
    def __getitem__(self, i: int) -> DocumentSection: ...

    @abstractmethod
    def __len__(self) -> int: ...

    def __init__(self, document_type: str = None):
        """
        Abstract representation of the document model in Fairest.

        :param document_type: Implementations should use this namespace for determining what
          kind of model this is. By default, it uses the name of the class.
        """
        self.document_type = document_type if document_type else self.__class__.__name__

    @abstractmethod
    def get_full_text(self) -> List[str]: ...

    def get_nlp_text(self):
        from fairest.core.nlp import get_nlp_doc
        document = "\n ".join(self.get_full_text())
        return get_nlp_doc(document)
