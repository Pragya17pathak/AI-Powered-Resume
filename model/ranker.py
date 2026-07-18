import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from model.skills import extract_skills


def calculate_ats_score(resume_text, job_description):

    resume_text = resume_text.lower()

    job_description = job_description.lower()

    # Calculate TF-IDF similarity

    vectorizer = TfidfVectorizer(

        stop_words="english",

        ngram_range=(1, 2),

        sublinear_tf=True

    )

    tfidf = vectorizer.fit_transform(

        [

            resume_text,

            job_description

        ]

    )

    similarity = cosine_similarity(

        tfidf[0],

        tfidf[1]

    )[0][0]

    similarity_percentage = round(

        similarity * 100,

        2

    )

    # Convert similarity into ATS points (0-30)

    if similarity_percentage >= 90:

        similarity_score = 30

    elif similarity_percentage >= 80:

        similarity_score = 28

    elif similarity_percentage >= 70:

        similarity_score = 25

    elif similarity_percentage >= 60:

        similarity_score = 22

    elif similarity_percentage >= 50:

        similarity_score = 18

    elif similarity_percentage >= 40:

        similarity_score = 15

    elif similarity_percentage >= 30:

        similarity_score = 12

    elif similarity_percentage >= 20:

        similarity_score = 8

    elif similarity_percentage >= 10:

        similarity_score = 5

    else:

        similarity_score = round(

            similarity_percentage / 2,

            2

        )

    # Extract skills

    resume_skills = {

        skill.lower()

        for skill in extract_skills(

            resume_text

        )

    }

    jd_skills = {

        skill.lower()

        for skill in extract_skills(

            job_description

        )

    }

    matched_skills = sorted(

        list(

            resume_skills &

            jd_skills

        )

    )

    missing_skills = sorted(

        list(

            jd_skills -

            resume_skills

        )

    )

    if len(jd_skills) == 0:

        skill_score = 0

        keyword_match = 0

    else:

        keyword_match = round(

            (

                len(matched_skills)

                /

                len(jd_skills)

            )

            *

            100,

            2

        )

        skill_score = round(

            (

                keyword_match

                /

                100

            )

            *

            25,

            2

        )

    # Experience

    experience_keywords = [

        "experience",

        "intern",

        "internship",

        "developer",

        "engineer",

        "worked",

        "software",

        "employee"

    ]

    experience_score = 10 if any(

        word in resume_text

        for word in experience_keywords

    ) else 0

    # Projects

    project_keywords = [

        "project",

        "projects",

        "developed",

        "implemented",

        "built"

    ]

    project_score = 10 if any(

        word in resume_text

        for word in project_keywords

    ) else 0

    # Education

    education_keywords = [

        "b.tech",

        "btech",

        "bachelor",

        "college",

        "university",

        "engineering",

        "degree"

    ]

    education_score = 10 if any(

        word in resume_text

        for word in education_keywords

    ) else 0

    # Certifications

    certification_keywords = [

        "certificate",

        "certification",

        "certifications",

        "certificates"

    ]

    certification_score = 5 if any(

        word in resume_text

        for word in certification_keywords

    ) else 0

    # Contact

    email = re.search(

        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

        resume_text

    )

    phone = re.search(

        r"(\+?\d{1,3}[-.\s]?)?(\d{10})",

        resume_text

    )

    linkedin = "linkedin.com" in resume_text

    github = "github.com" in resume_text

    contact_score = 0

    if email:

        contact_score += 2

    if phone:

        contact_score += 2

    if linkedin or github:

        contact_score += 1

    contact_score = min(

        contact_score,

        5

    )

    # Resume length

    word_count = len(

        resume_text.split()

    )

    if word_count >= 500:

        length_score = 5

    elif word_count >= 300:

        length_score = 4

    elif word_count >= 200:

        length_score = 3

    elif word_count >= 100:

        length_score = 2

    else:

        length_score = 1

    # Final ATS Score

    final_score = round(

        similarity_score

        +

        skill_score

        +

        experience_score

        +

        project_score

        +

        education_score

        +

        certification_score

        +

        contact_score

        +

        length_score,

        2

    )

    final_score = min(

        final_score,

        100

    )

    breakdown = {

        "similarity": similarity_score,

        "skills": skill_score,

        "experience": experience_score,

        "projects": project_score,

        "education": education_score,

        "certifications": certification_score,

        "contact": contact_score,

        "length": length_score,

        "keyword_match": keyword_match,

        "similarity_percentage": similarity_percentage

    }

    return (

        final_score,

        matched_skills,

        missing_skills,

        breakdown

    )