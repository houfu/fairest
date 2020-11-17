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
