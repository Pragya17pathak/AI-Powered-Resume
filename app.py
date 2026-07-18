from flask import Flask, render_template, request, send_file
import os

from model.parser import extract_text_from_pdf
from model.preprocess import preprocess_text
from model.skills import extract_skills
from model.ranker import calculate_ats_score
from model.suggestions import generate_suggestions
from model.analyzer import analyze_resume
from model.report import generate_report
from model.pdf_report import generate_pdf
from model.grading import get_resume_grade

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

latest_result = {}


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_resume():

    global latest_result

    if "resume" not in request.files:

        return "No file uploaded."

    file = request.files["resume"]

    if file.filename == "":

        return "No file selected."

    filepath = os.path.join(

        app.config["UPLOAD_FOLDER"],

        file.filename

    )

    file.save(filepath)

    extracted_text = extract_text_from_pdf(filepath)

    clean_text = preprocess_text(extracted_text)

    skills = extract_skills(clean_text)

    job_description = request.form["job_description"]

    ats_score, matched_skills, missing_skills, breakdown = calculate_ats_score(

        clean_text,

        job_description

    )

    grade_data = get_resume_grade(ats_score)

    breakdown_percent = {

        "similarity": round((breakdown["similarity"] / 30) * 100),

        "skills": round((breakdown["skills"] / 25) * 100),

        "experience": round((breakdown["experience"] / 10) * 100),

        "projects": round((breakdown["projects"] / 10) * 100),

        "education": round((breakdown["education"] / 10) * 100),

        "certifications": round((breakdown["certifications"] / 5) * 100),

        "contact": round((breakdown["contact"] / 5) * 100),

        "length": round((breakdown["length"] / 5) * 100)

    }

    keyword_match = breakdown.get("keyword_match", 0)

    similarity_percentage = breakdown.get("similarity_percentage", 0)

    suggestions = generate_suggestions(

        missing_skills,

        extracted_text

    )

    strengths, improvements = analyze_resume(

        ats_score,

        matched_skills,

        missing_skills,

        extracted_text

    )

    report, report_strengths, recommendations = generate_report(

        ats_score,

        matched_skills,

        missing_skills,

        extracted_text

    )

    latest_result = {

        "score": ats_score,

        "grade": grade_data["grade"],

        "performance": grade_data["performance"],

        "recommendation": grade_data["recommendation"],

        "badge": grade_data["badge"],

        "breakdown": breakdown,

        "matched": matched_skills,

        "missing": missing_skills,

        "strengths": strengths,

        "improvements": improvements,

        "suggestions": suggestions,

        "keyword_match": keyword_match,

        "similarity_percentage": similarity_percentage

    }

    return render_template(

        "result.html",

        text=extracted_text,

        skills=skills,

        score=ats_score,

        grade=grade_data["grade"],

        performance=grade_data["performance"],

        recommendation=grade_data["recommendation"],

        badge=grade_data["badge"],

        matched=matched_skills,

        missing=missing_skills,

        suggestions=suggestions,

        breakdown=breakdown,

        breakdown_percent=breakdown_percent,

        strengths=strengths,

        improvements=improvements,

        report=report,

        report_strengths=report_strengths,

        recommendations=recommendations,

        keyword_match=keyword_match,

        similarity_percentage=similarity_percentage

    )


@app.route("/download-report")
def download_report():

    if not latest_result:

        return "No report available."

    filename = "Resume_Report.pdf"

    generate_pdf(

        filename,

        latest_result["score"],

        latest_result["breakdown"],

        latest_result["matched"],

        latest_result["missing"],

        latest_result["strengths"],

        latest_result["improvements"],

        latest_result["suggestions"]

    )

    return send_file(

        filename,

        as_attachment=True

    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )