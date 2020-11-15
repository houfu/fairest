import spacy
from spacy.tokens import Doc


def get_nlp():
    return spacy.load("en_core_web_sm")


nlp = get_nlp()


def get_nlp_doc(text: str) -> Doc:
    return nlp(text)
