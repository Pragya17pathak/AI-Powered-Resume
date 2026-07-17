def analyze_resume(score, matched_skills, missing_skills, resume_text):
    # Initialize result lists

    strengths = []
    improvements = []

    # Convert resume to lowercase

    text = resume_text.lower()

    # Evaluate ATS score

    if score >= 90:

        strengths.append("Excellent ATS score with strong job compatibility.")

    elif score >= 75:

        strengths.append("Good ATS score with a competitive profile.")

    elif score >= 60:

        strengths.append("Average ATS score with room for improvement.")

    else:

        improvements.append("Increase keyword relevance to improve ATS compatibility.")

    # Evaluate matched skills

    if matched_skills:

        strengths.append(
            f"Matched {len(matched_skills)} required skills."
        )

    else:

        improvements.append(
            "Add more technical skills related to the job description."
        )

    # Evaluate missing skills

    if missing_skills:

        improvements.append(
            "Consider adding these skills if applicable: " +
            ", ".join(missing_skills)
        )

    # Check contact information

    if "@" in text:

        strengths.append("Professional email address detected.")

    else:

        improvements.append("Add a professional email address.")

    # Check LinkedIn profile

    if "linkedin" in text:

        strengths.append("LinkedIn profile detected.")

    else:

        improvements.append("Add your LinkedIn profile URL.")

    # Check GitHub profile

    if "github" in text:

        strengths.append("GitHub profile detected.")

    else:

        improvements.append("Add your GitHub profile URL.")

    # Check projects section

    if "project" in text:

        strengths.append("Projects section detected.")

    else:

        improvements.append("Include academic or personal projects.")

    # Check experience section

    if any(word in text for word in [
        "experience",
        "intern",
        "internship",
        "developer",
        "engineer"
    ]):

        strengths.append("Experience section detected.")

    else:

        improvements.append("Add internship or work experience if available.")

    # Check education section

    if any(word in text for word in [
        "b.tech",
        "btech",
        "bachelor",
        "college",
        "university"
    ]):

        strengths.append("Education section detected.")

    else:

        improvements.append("Include your educational qualifications.")

    # Check certifications

    if any(word in text for word in [
        "certification",
        "certificate"
    ]):

        strengths.append("Certifications section detected.")

    else:

        improvements.append("Add relevant certifications to strengthen your resume.")

    # Check achievements

    if "achievement" in text or "award" in text:

        strengths.append("Achievements section detected.")

    else:

        improvements.append("Include measurable achievements and awards.")

    # Check resume length

    word_count = len(text.split())

    if word_count >= 250:

        strengths.append("Resume length is appropriate.")

    else:

        improvements.append("Expand your resume with relevant experience and projects.")

    # Return analysis

    return strengths, improvements