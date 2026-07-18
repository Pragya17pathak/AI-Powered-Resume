# 🚀 AI-Powered Resume Ranker

An intelligent **ATS (Applicant Tracking System) Resume Analyzer** built with **Python, Flask, Machine Learning, and Chart.js**. The application compares a resume with a job description, calculates an ATS compatibility score, identifies matched and missing skills, provides personalized suggestions, assigns a resume grade, and generates a professional PDF report.

---

## 📌 Features

- 📄 Upload Resume (PDF)
- 📝 Job Description Matching
- 🎯 ATS Score Calculation
- 🏆 Resume Grade (A+ to F)
- 📊 Interactive Charts
- ✅ Matched Skills Detection
- ❌ Missing Skills Detection
- 💡 AI Resume Improvement Suggestions
- 📈 Resume Similarity Score
- 📚 Resume Statistics Dashboard
- 📑 Professional PDF Report
- 🌙 Dark Mode Support
- 📱 Responsive Modern UI
- 🎨 Glassmorphism Dashboard
- ⚡ Animated Charts & Progress Bars

---

## 🖥️ Screenshots

### 🏠 Home Page

> Add screenshot here

```
static/screenshots/home.png
```

---

### 📊 Dashboard

> Add screenshot here

```
static/screenshots/dashboard.png
```

---

### 📈 Charts

> Add screenshot here

```
static/screenshots/charts.png
```

---

### 💡 Suggestions

> Add screenshot here

```
static/screenshots/suggestions.png
```

---

### 📄 Resume Preview

> Add screenshot here

```
static/screenshots/preview.png
```

---

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chart.js

### Backend

- Python
- Flask

### Machine Learning

- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

### Libraries

- PyPDF2
- ReportLab
- NumPy
- Pandas

---

## 📂 Project Structure

```
AI-Powered-Resume-Ranker/

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

│   │

│   ├── js/

│   │   └── script.js

│   │

│   ├── uploads/

│   │

│   └── screenshots/

│

├── templates/

│   ├── components/

│   │

│   ├── index.html

│   └── result.html

│

├── app.py

├── requirements.txt

├── README.md

└── Resume_Report.pdf

```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Pragya17pathak/AI-Powered-Resume.git

cd AI-Powered-Resume
```

---

## 2️⃣ Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
python app.py
```

---

## 5️⃣ Open Browser

```
http://127.0.0.1:5000
```

---

# 🚀 How It Works

```
Upload Resume

↓

Extract Resume Text

↓

Clean & Preprocess Text

↓

Extract Skills

↓

Compare With Job Description

↓

Calculate ATS Score

↓

Find Missing Skills

↓

Generate Suggestions

↓

Assign Resume Grade

↓

Generate PDF Report

↓

Display Interactive Dashboard
```

---

# 📊 ATS Score Breakdown

| Category | Weight |
|-----------|--------|
| Resume Similarity | 30 |
| Skills Match | 25 |
| Experience | 10 |
| Projects | 10 |
| Education | 10 |
| Certifications | 5 |
| Contact Information | 5 |
| Resume Length | 5 |

---

# 🎯 Resume Grades

| ATS Score | Grade |
|-----------|-------|
| 95 - 100 | A+ |
| 85 - 94 | A |
| 75 - 84 | B |
| 65 - 74 | C |
| 50 - 64 | D |
| Below 50 | F |

---

# 📄 Generated Report Includes

- ATS Score
- Resume Grade
- Resume Similarity
- Keyword Match
- Matched Skills
- Missing Skills
- Strengths
- Weaknesses
- Resume Suggestions
- Resume Statistics

---

# 💡 Future Enhancements

- AI Resume Rewriting
- Cover Letter Generator
- Resume Ranking Against Multiple Jobs
- LinkedIn Profile Analyzer
- Resume Keyword Optimizer
- AI Career Recommendation System
- Interview Question Generator
- Multi-language Resume Analysis
- Resume Templates
- Cloud Deployment

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Machine Learning
- Natural Language Processing
- Text Similarity
- Resume Parsing
- PDF Processing
- Flask Web Development
- Interactive Data Visualization
- Responsive UI Design

---

# 👩‍💻 Author

**Pragya Pathak**

B.Tech Computer Science Engineering

Lovely Professional University

---

## 🔗 Connect With Me

**GitHub**

https://github.com/Pragya17pathak

**LinkedIn**

Add your LinkedIn profile here

---

# ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub.

It motivates me to build more open-source projects.

---

# 📜 License

This project is licensed under the MIT License.

Feel free to use and modify it for learning purposes.