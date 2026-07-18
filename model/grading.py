def get_resume_grade(score):

    if score >= 95:

        return {

            "grade": "A+",

            "performance": "Outstanding",

            "recommendation": "Your resume is highly optimized and has an excellent chance of passing ATS screening.",

            "badge": "success"

        }

    elif score >= 85:

        return {

            "grade": "A",

            "performance": "Excellent",

            "recommendation": "Your resume is well optimized. Only minor improvements may be needed.",

            "badge": "success"

        }

    elif score >= 75:

        return {

            "grade": "B",

            "performance": "Good",

            "recommendation": "Your resume is competitive but adding more relevant keywords and skills can improve your ATS score.",

            "badge": "primary"

        }

    elif score >= 65:

        return {

            "grade": "C",

            "performance": "Average",

            "recommendation": "Your resume needs additional improvements in skills, formatting, and keyword optimization.",

            "badge": "warning"

        }

    elif score >= 50:

        return {

            "grade": "D",

            "performance": "Below Average",

            "recommendation": "Your resume requires significant improvements before applying for most positions.",

            "badge": "warning"

        }

    else:

        return {

            "grade": "F",

            "performance": "Poor",

            "recommendation": "Your resume is not ATS-friendly. Improve the content, structure, and relevant skills before applying.",

            "badge": "danger"

        }