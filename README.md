# 🤖 AI-Powered Resume Ranker

An AI-powered Resume Ranking and ATS (Applicant Tracking System) Analyzer built using **Flask**, **Python**, **Machine Learning**, **spaCy**, **Scikit-learn**, and **Chart.js**. The application evaluates resumes against a job description, calculates an ATS score, assigns a resume grade, provides hiring recommendations, extracts skills, generates AI-powered suggestions, visualizes analytics, and allows users to download a professional PDF report.

---

## 🚀 Features

### Resume Analysis

- 📄 Upload Resume (PDF)
- 📝 Analyze Resume against Job Description
- 🎯 ATS Score Calculation
- 🏆 Resume Grade (A+, A, B, C, D, F)
- 💼 Hiring Recommendation
- 📊 Resume Quality Assessment

### Skill Analysis

- ✅ Skill Extraction
- ✔️ Matched Skills Detection
- ❌ Missing Skills Detection
- 🤖 AI Resume Analysis
- 💡 AI Improvement Suggestions

### Dashboard

- 📈 ATS Score Dashboard
- 🍩 Doughnut Chart Visualization
- 📊 Score Breakdown Bar Chart
- 📉 Progress Indicators
- 📱 Responsive Interface

### Report Generation

- 📄 Resume Preview
- 📥 Download PDF Report
- 🖨 Print Report
- 📋 Copy Report Summary

### User Experience

- 🌙 Light/Dark Theme
- 📱 Fully Responsive Bootstrap UI
- ⚡ Fast Resume Processing

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

### Data Visualization

- Chart.js

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

---

## 📂 Project Structure

```
AI-Powered Resume Ranker/
│
├── app.py
│
├── model/
│   ├── analyzer.py
│   ├── grading.py
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
│       ├── grading.html
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

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser:

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

## 🏆 Resume Evaluation

Every analyzed resume receives:

- ATS Score
- Resume Grade
- Performance Level
- Hiring Recommendation

Example:

```
ATS Score: 88%

Grade: A

Performance: Excellent

Recommendation: Highly Recommended
```

---

## 📈 Dashboard

Interactive dashboard includes:

- ATS Score Doughnut Chart
- Score Breakdown Bar Chart
- Progress Bars
- Resume Analytics
- Resume Evaluation Card

---

## 📄 Downloadable PDF Report

The generated report includes:

- ATS Score
- Resume Grade
- Hiring Recommendation
- Score Breakdown
- Matched Skills
- Missing Skills
- Resume Strengths
- Areas for Improvement
- AI Suggestions

---

## 📸 Workflow

1. Upload Resume
2. Enter Job Description
3. Resume Parsing
4. ATS Analysis
5. Resume Evaluation
6. Dashboard Visualization
7. AI Suggestions
8. Download Professional PDF Report

---

## 🔮 Future Enhancements

- Keyword Match Percentage
- Resume Section Rating
- Resume Comparison
- AI Resume Rewriter
- Resume History
- User Authentication
- Database Integration
- Cloud Deployment
- Email Report Sharing

---

## 👩‍💻 Author

**Pragya Pathak**

GitHub

https://github.com/Pragya17pathak

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.