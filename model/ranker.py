# model/ranker.py
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from model.skills import extract_skills


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"www\S+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def calculate_document_similarity(resume_text, job_description):
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        sublinear_tf=True,
        max_features=5000
    )

    vectors = vectorizer.fit_transform([resume_text, job_description])

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return round(similarity * 100, 2)


def calculate_skill_similarity(resume_skills, jd_skills):
    if not resume_skills or not jd_skills:
        return 0

    resume_string = " ".join(sorted(resume_skills))
    jd_string = " ".join(sorted(jd_skills))

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_string, jd_string])

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return round(similarity * 100, 2)


def calculate_ats_score(resume_text, job_description):

    resume_text = preprocess_text(resume_text)
    job_description = preprocess_text(job_description)

    resume_skills = {s.lower() for s in extract_skills(resume_text)}
    jd_skills = {s.lower() for s in extract_skills(job_description)}

    matched_skills = sorted(list(resume_skills & jd_skills))
    missing_skills = sorted(list(jd_skills - resume_skills))

    if len(jd_skills) == 0:
        keyword_match = 0
    else:
        keyword_match = round(
            len(matched_skills) / len(jd_skills) * 100,
            2
        )

    document_similarity = calculate_document_similarity(
        resume_text,
        job_description
    )

    skill_similarity = calculate_skill_similarity(
        resume_skills,
        jd_skills
    )

    similarity_percentage = round(
        (document_similarity * 0.40) +
        (skill_similarity * 0.60),
        2
    )

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
        similarity_score = round(similarity_percentage / 2, 2)

    skill_score = round((keyword_match / 100) * 25, 2)

    experience_keywords = [
        "experience", "intern", "internship",
        "developer", "engineer", "software",
        "worked", "employment", "freelance"
    ]
    experience_score = min(
        sum(1 for k in experience_keywords if k in resume_text) * 2,
        10
    )

    project_keywords = [
        "project", "projects", "developed",
        "implemented", "designed", "built", "created"
    ]
    project_score = min(
        sum(1 for k in project_keywords if k in resume_text) * 2,
        10
    )

    education_keywords = [
        "b.tech", "btech", "bachelor",
        "engineering", "university",
        "college", "degree"
    ]
    education_score = min(
        sum(1 for k in education_keywords if k in resume_text) * 2,
        10
    )

    certification_keywords = [
        "certificate",
        "certification",
        "certifications",
        "certificates"
    ]
    certification_score = min(
        sum(1 for k in certification_keywords if k in resume_text) * 2,
        5
    )

    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume_text
    )
    phone = re.search(
        r"(\+?\d{1,3}[-.\s]?)?(\d{10})",
        resume_text
    )

    contact_score = 0
    if email:
        contact_score += 2
    if phone:
        contact_score += 2
    if "github.com" in resume_text:
        contact_score += 0.5
    if "linkedin.com" in resume_text:
        contact_score += 0.5
    contact_score = min(contact_score, 5)

    word_count = len(resume_text.split())

    if word_count >= 350:
        length_score = 5
    elif word_count >= 250:
        length_score = 4
    elif word_count >= 150:
        length_score = 3
    elif word_count >= 80:
        length_score = 2
    else:
        length_score = 1

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
        "similarity_percentage": similarity_percentage,
        "document_similarity": document_similarity,
        "skill_similarity": skill_similarity
    }

    return (
        final_score,
        matched_skills,
        missing_skills,
        breakdown
    )
