import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from model.skills import extract_skills


def calculate_ats_score(resume_text, job_description):
    # Convert text to lowercase

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    # Calculate resume similarity

    vectorizer = TfidfVectorizer()

    tfidf = vectorizer.fit_transform(
        [resume_text, job_description]
    )

    similarity = cosine_similarity(
        tfidf[0:1],
        tfidf[1:2]
    )[0][0]

    similarity_score = round(similarity * 30, 2)

    # Extract resume and job skills

    resume_skills = extract_skills(resume_text)

    jd_skills = extract_skills(job_description)

    matched_skills = list(
        set(resume_skills) &
        set(jd_skills)
    )

    missing_skills = list(
        set(jd_skills) -
        set(resume_skills)
    )

    if len(jd_skills) == 0:

        skill_score = 0

    else:

        skill_score = round(
            (len(matched_skills) / len(jd_skills)) * 25,
            2
        )

    # Detect experience section

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

    experience_score = 0

    for word in experience_keywords:

        if word in resume_text:

            experience_score = 10

            break

    # Detect projects section

    project_keywords = [

        "project",
        "projects",
        "developed",
        "implemented",
        "built"

    ]

    project_score = 0

    for word in project_keywords:

        if word in resume_text:

            project_score = 10

            break

    # Detect education section

    education_keywords = [

        "b.tech",
        "btech",
        "bachelor",
        "college",
        "university",
        "engineering",
        "degree"

    ]

    education_score = 0

    for word in education_keywords:

        if word in resume_text:

            education_score = 10

            break

    # Detect certifications

    certification_keywords = [

        "certification",
        "certifications",
        "certificate",
        "certificates"

    ]

    certification_score = 0

    for word in certification_keywords:

        if word in resume_text:

            certification_score = 5

            break

    # Detect email address

    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume_text
    )

    # Detect phone number

    phone = re.search(
        r"(\+?\d{1,3}[-.\s]?)?(\d{10})",
        resume_text
    )

    if email and phone:

        contact_score = 5

    else:

        contact_score = 0

    # Evaluate resume length

    word_count = len(resume_text.split())

    if word_count >= 250:

        length_score = 5

    elif word_count >= 150:

        length_score = 3

    else:

        length_score = 1

    # Calculate final ATS score

    final_score = round(

        similarity_score +

        skill_score +

        experience_score +

        project_score +

        education_score +

        certification_score +

        contact_score +

        length_score,

        2

    )

    final_score = min(final_score, 100)

    # Store score breakdown

    breakdown = {

        "similarity": similarity_score,

        "skills": skill_score,

        "experience": experience_score,

        "projects": project_score,

        "education": education_score,

        "certifications": certification_score,

        "contact": contact_score,

        "length": length_score

    }

    # Return ATS results

    return (

        final_score,

        matched_skills,

        missing_skills,

        breakdown

    )