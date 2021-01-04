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
