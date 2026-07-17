import re

import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

# Load skills dataset

skills_df = pd.read_csv("dataset/skills.csv")

SKILLS = (

    skills_df["Skill"]

    .dropna()

    .astype(str)

    .str.strip()

    .str.lower()

    .unique()

    .tolist()

)


def extract_skills(text):
    # Return empty list for invalid input

    if not text:

        return []

    # Normalize resume text

    text = text.lower()

    text = re.sub(r"[^\w\s#+.-]", " ", text)

    doc = nlp(text)

    found_skills = set()

    # Match complete skills

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.add(skill.title())

    # Match single-word skills

    tokens = {

        token.text.lower()

        for token in doc

        if not token.is_space

    }

    for skill in SKILLS:

        if " " not in skill and skill in tokens:

            found_skills.add(skill.title())

    # Return sorted skills

    return sorted(found_skills)