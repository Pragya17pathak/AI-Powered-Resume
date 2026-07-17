def generate_report(score, matched, missing, resume_text):
    # Initialize report sections

    report = []
    strengths = []
    recommendations = []

    # Convert resume to lowercase

    text = resume_text.lower()

    # Generate overall evaluation

    if score >= 90:

        report.append("Excellent ATS score with outstanding job compatibility.")

    elif score >= 75:

        report.append("Good ATS score with a strong match for the job role.")

    elif score >= 60:

        report.append("Average ATS score with scope for improvement.")

    else:

        report.append("Low ATS score. Tailor your resume to the job description.")

    # Evaluate matched skills

    if matched:

        strengths.append(
            f"Matched {len(matched)} required skills."
        )

    else:

        recommendations.append(
            "Include more technical skills related to the job description."
        )

    # Check projects section

    if "project" in text:

        strengths.append("Projects section detected.")

    else:

        recommendations.append(
            "Add at least two technical projects with measurable outcomes."
        )

    # Check GitHub profile

    if "github" in text:

        strengths.append("GitHub profile detected.")

    else:

        recommendations.append(
            "Add your GitHub profile to showcase your work."
        )

    # Check LinkedIn profile

    if "linkedin" in text:

        strengths.append("LinkedIn profile detected.")

    else:

        recommendations.append(
            "Add your LinkedIn profile."
        )

    # Check certifications

    if "certification" in text or "certificate" in text:

        strengths.append("Certifications section detected.")

    else:

        recommendations.append(
            "Include relevant certifications."
        )

    # Check achievements

    if "achievement" in text or "award" in text:

        strengths.append("Achievements section detected.")

    else:

        recommendations.append(
            "Include measurable achievements using numbers or percentages."
        )

    # Check experience

    if any(word in text for word in [
        "experience",
        "intern",
        "internship",
        "developer",
        "engineer"
    ]):

        strengths.append("Experience section detected.")

    else:

        recommendations.append(
            "Mention internships, freelance work, or professional experience."
        )

    # Check education

    if any(word in text for word in [
        "b.tech",
        "btech",
        "bachelor",
        "college",
        "university"
    ]):

        strengths.append("Education section detected.")

    else:

        recommendations.append(
            "Include complete educational qualifications."
        )

    # Recommend missing skills

    for skill in missing:

        recommendations.append(
            f"Consider adding {skill} if you have practical experience."
        )

    # Remove duplicate recommendations

    recommendations = list(dict.fromkeys(recommendations))

    # Return report

    return report, strengths, recommendations