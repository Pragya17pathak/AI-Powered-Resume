def get_resume_grade(score):

    if score >= 95:

        return {

            "grade": "A+",

            "performance": "Outstanding",

            "recommendation": "Highly Recommended",

            "badge": "success"

        }

    elif score >= 85:

        return {

            "grade": "A",

            "performance": "Excellent",

            "recommendation": "Highly Recommended",

            "badge": "success"

        }

    elif score >= 75:

        return {

            "grade": "B",

            "performance": "Good",

            "recommendation": "Recommended",

            "badge": "primary"

        }

    elif score >= 65:

        return {

            "grade": "C",

            "performance": "Average",

            "recommendation": "Consider Improvements",

            "badge": "warning"

        }

    elif score >= 50:

        return {

            "grade": "D",

            "performance": "Below Average",

            "recommendation": "Needs Improvement",

            "badge": "warning"

        }

    else:

        return {

            "grade": "F",

            "performance": "Poor",

            "recommendation": "Not Recommended",

            "badge": "danger"

        }