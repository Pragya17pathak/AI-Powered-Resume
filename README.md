# 🤖 AI-Powered Resume Ranker

An AI-powered Resume Ranking and ATS (Applicant Tracking System) Analyzer built using **Flask**, **Python**, **Machine Learning**, **spaCy**, and **Scikit-learn**. The application analyzes resumes against a job description, calculates an ATS score, identifies matched and missing skills, provides AI-based improvement suggestions, visualizes results with interactive charts, and generates downloadable PDF reports.

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 📝 Analyze Resume against Job Description
- 🎯 ATS Score Calculation
- 📊 Interactive Dashboard
- 📈 Doughnut Chart for ATS Score
- 📉 Bar Chart for Score Breakdown
- ✅ Skill Extraction
- ✔️ Matched Skills Detection
- ❌ Missing Skills Detection
- 🤖 AI Resume Analysis
- 💡 AI Improvement Suggestions
- 📋 Resume Assessment
- 👀 Resume Preview
- 📥 Download Professional PDF Report
- 🖨 Print Report
- 📋 Copy Report Summary
- 🌙 Light/Dark Theme Support
- 📱 Responsive Bootstrap UI

---

## 🛠 Tech Stack

### Backend

- Python
- Flask

### Machine Learning & NLP

- Scikit-learn
- spaCy

### PDF Processing

- pdfplumber
- ReportLab

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chart.js

---

## 📂 Project Structure

```
AI-Powered Resume Ranker/
│
├── app.py
│
├── model/
│   ├── analyzer.py
│   ├── parser.py
│   ├── pdf_report.py
│   ├── preprocess.py
│   ├── ranker.py
│   ├── report.py
│   ├── skills.py
│   └── suggestions.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── uploads/
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── components/
│       ├── dashboard.html
│       ├── charts.html
│       ├── breakdown.html
│       ├── skills.html
│       ├── analysis.html
│       ├── assessment.html
│       ├── preview.html
│       └── actions.html
│
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/Pragya17pathak/AI-Powered-Resume.git

cd AI-Powered-Resume
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 📊 ATS Scoring Parameters

| Parameter | Weight |
|-----------|-------:|
| Resume Similarity | 30 |
| Skills Match | 25 |
| Experience | 10 |
| Projects | 10 |
| Education | 10 |
| Certifications | 5 |
| Contact Information | 5 |
| Resume Length | 5 |

---

## 📈 Dashboard

The application provides interactive visualizations including:

- ATS Score Doughnut Chart
- Score Breakdown Bar Chart
- Progress Bars
- Resume Analysis Dashboard

---

## 📄 PDF Report

Users can download a professional report containing:

- ATS Score
- Score Breakdown
- Matched Skills
- Missing Skills
- Resume Strengths
- Areas for Improvement
- AI Suggestions

---

## 📸 Application Workflow

1. Upload Resume
2. Enter Job Description
3. ATS Analysis
4. Resume Evaluation
5. Dashboard Visualization
6. AI Suggestions
7. Download PDF Report

---

## 🔮 Future Enhancements

- Resume Grade (A+, A, B...)
- Hiring Recommendation
- Keyword Match Percentage
- Multiple Resume Comparison
- User Authentication
- Resume History
- Database Integration
- Cloud Deployment
- Email Report Sharing

---

## 👩‍💻 Author

**Pragya Pathak**

GitHub:
https://github.com/Pragya17pathak

LinkedIn:
https://www.linkedin.com/

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.