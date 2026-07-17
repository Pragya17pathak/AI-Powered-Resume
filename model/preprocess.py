import re
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    """
    Cleans and preprocesses resume text.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove special characters except +, # and .
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)

    # Process with spaCy
    doc = nlp(text)

    cleaned_words = []

    for token in doc:

        # Remove stopwords
        if token.is_stop:
            continue

        # Remove punctuation
        if token.is_punct:
            continue

        # Remove spaces
        if token.is_space:
            continue

        # Lemmatization
        cleaned_words.append(token.lemma_)

    return " ".join(cleaned_words)