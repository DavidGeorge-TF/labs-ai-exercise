from __future__ import annotations

import spacy

nlp = spacy.load("en_core_web_sm")


def tokenize_text(text: str) -> list[str]:
    """Tokenizes the input text into words using spaCy."""
    doc = nlp(text)
    return [token.text for token in doc]


def extract_noun_phrases(text: str) -> list[str]:
    """Extracts noun phrases from the input text."""
    doc = nlp(text)
    return [chunk.text for chunk in doc.noun_chunks]


def extract_entities(text: str):
    """Extracts entities from the input text."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities: list[dict[str, str]] = []
    for ent in doc.ents:
        if ent.label_ == "PERSON" or ent.label_ == "ORG":
            entities.append({ent.text, ent.label_})
    return entities


def average_token_length(text: str) -> float:
    """Returns the average token length in the input text."""
    doc = nlp(text)
    totalLength = 0
    for token in doc:
        totalLength += len(token)
    return totalLength / len(doc)
