def generate_suggestions(missing_skills, resume_text):
    # Initialize suggestions list

    suggestions = []

    # Convert resume to lowercase

    resume_lower = resume_text.lower()

    # Suggest missing skills

    for skill in missing_skills:

        suggestions.append(
            f"Add {skill} to your resume if you have practical experience with it."
        )

    # Suggest GitHub profile

    if "github" not in resume_lower:

        suggestions.append(
            "Add your GitHub profile to showcase your projects."
        )

    # Suggest LinkedIn profile

    if "linkedin" not in resume_lower:

        suggestions.append(
            "Include your LinkedIn profile to strengthen your professional presence."
        )

    # Suggest experience

    if not any(word in resume_lower for word in [
        "experience",
        "intern",
        "internship"
    ]):

        suggestions.append(
            "Mention internships, freelance work, or relevant experience."
        )

    # Suggest certifications

    if not any(word in resume_lower for word in [
        "certification",
        "certificate"
    ]):

        suggestions.append(
            "Add relevant certifications to improve your ATS score."
        )

    # Suggest projects

    if "project" not in resume_lower:

        suggestions.append(
            "Include at least two technical projects with clear outcomes."
        )

    # Suggest achievements

    if not any(word in resume_lower for word in [
        "achievement",
        "award"
    ]):

        suggestions.append(
            "Include measurable achievements using numbers or percentages."
        )

    # Suggest education

    if not any(word in resume_lower for word in [
        "b.tech",
        "btech",
        "bachelor",
        "college",
        "university"
    ]):

        suggestions.append(
            "Include complete educational qualifications."
        )

    # Suggest contact information

    if "@" not in resume_lower:

        suggestions.append(
            "Add a professional email address."
        )

    # Suggest resume summary

    if "summary" not in resume_lower and "objective" not in resume_lower:

        suggestions.append(
            "Add a professional summary at the beginning of your resume."
        )

    # Suggest technical skills

    if "skills" not in resume_lower:

        suggestions.append(
            "Create a dedicated technical skills section."
        )

    # Return suggestions

    return suggestions