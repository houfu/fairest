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

import logging

import spacy
from spacy.tokens import Doc

nlp_logger = logging.getLogger('fairest.nlp')


def get_nlp(model="en_core_web_sm"):
    nlp_logger.info(f'Starting NLP with model: {model}')
    return spacy.load(model)


nlp = get_nlp()


def get_nlp_doc(text: str) -> Doc:
    nlp_logger.info(f'Running NLP on text: {text[0:25]}')
    return nlp(text)
