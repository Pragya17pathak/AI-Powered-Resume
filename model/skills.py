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

    .str.lower()

    .str.strip()

    .unique()

    .tolist()

)

# Skill synonyms

SYNONYMS = {

    "ai": "artificial intelligence",

    "artificial intelligence": "artificial intelligence",

    "machine learning": "machine learning",

    "ml": "machine learning",

    "deep learning": "deep learning",

    "dl": "deep learning",

    "nlp": "natural language processing",

    "natural language processing": "natural language processing",

    "javascript": "javascript",

    "js": "javascript",

    "reactjs": "react",

    "react": "react",

    "nodejs": "node",

    "node.js": "node",

    "node": "node",

    "postgres": "postgresql",

    "postgresql": "postgresql",

    "mysql": "mysql",

    "sql": "sql",

    "rest": "rest api",

    "restful api": "rest api",

    "rest api": "rest api",

    "oop": "object oriented programming",

    "object oriented programming": "object oriented programming",

    "aws": "amazon web services",

    "amazon web services": "amazon web services",

    "azure": "microsoft azure",

    "microsoft azure": "microsoft azure",

    "github": "github",

    "git": "git",

    "docker": "docker",

    "kubernetes": "kubernetes",

    "tensorflow": "tensorflow",

    "pytorch": "pytorch",

    "numpy": "numpy",

    "pandas": "pandas",

    "scikit learn": "scikit-learn",

    "scikit-learn": "scikit-learn",

    "flask": "flask",

    "django": "django",

    "html": "html",

    "css": "css",

    "bootstrap": "bootstrap",

    "linux": "linux",

    "c++": "c++",

    "cpp": "c++",

    "c#": "c#",

    "java": "java",

    "python": "python"

}


def normalize_skill(skill):

    skill = skill.lower().strip()

    return SYNONYMS.get(

        skill,

        skill

    )


def extract_skills(text):

    if not text:

        return []

    text = text.lower()

    text = re.sub(

        r"[^\w\s#+.-]",

        " ",

        text

    )

    doc = nlp(text)

    found = set()

    # Match multi-word skills

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(

            pattern,

            text

        ):

            found.add(

                normalize_skill(skill)

            )

    # Match token skills

    tokens = {

        token.text.lower()

        for token in doc

        if not token.is_space

    }

    for token in tokens:

        token = normalize_skill(token)

        if token in SKILLS or token in SYNONYMS.values():

            found.add(token)

    return sorted(

        {

            skill.title()

            for skill in found

        }

    )