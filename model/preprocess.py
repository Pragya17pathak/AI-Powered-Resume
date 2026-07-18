import re
import spacy

# Load spaCy English model

nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):

    if not text:

        return ""

    # Convert to lowercase

    text = text.lower()

    # Remove URLs

    text = re.sub(
        r"http\S+|www\S+",
        " ",
        text
    )

    # Remove email addresses

    text = re.sub(
        r"\S+@\S+",
        " ",
        text
    )

    # Remove phone numbers

    text = re.sub(
        r"\+?\d[\d\s\-]{8,}",
        " ",
        text
    )

    # Remove punctuation and numbers

    text = re.sub(
        r"[^a-z\s]",
        " ",
        text
    )

    # Remove extra spaces

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    # Process using spaCy

    doc = nlp(text)

    cleaned_words = []

    for token in doc:

        if token.is_stop:

            continue

        if token.is_space:

            continue

        if len(token.text) <= 1:

            continue

        cleaned_words.append(
            token.lemma_
        )

    cleaned_text = " ".join(cleaned_words)

    return cleaned_text