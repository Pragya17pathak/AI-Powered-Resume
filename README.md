# 🤖 AI-Powered Resume Ranker

An AI-powered Resume Ranking System built with **Python** and **Flask** that evaluates resumes against a job description using Natural Language Processing (NLP). The system calculates an ATS (Applicant Tracking System) score, identifies matched and missing skills, provides AI-based suggestions, and generates a detailed resume analysis report.

---

## 📌 Project Overview

Recruiters often receive hundreds of resumes for a single job opening. This project automates the resume screening process by comparing a resume with a job description and generating an ATS score along with detailed insights.

The system helps candidates improve their resumes while assisting recruiters in identifying the most suitable applicants efficiently.

---

## 🚀 Features

- 📄 PDF Resume Parsing
- 🧹 Resume Text Preprocessing
- 🎯 ATS Score Calculation
- 🔍 Resume & Job Description Similarity
- 💻 Skill Extraction
- ✅ Matched Skills Detection
- ❌ Missing Skills Detection
- 📊 ATS Score Breakdown
- 🤖 AI Resume Analysis
- 💡 Personalized Resume Improvement Suggestions
- 📝 AI Hiring Assessment
- 📑 Resume Preview
- 📱 Responsive Bootstrap Dashboard
- 🧩 Modular Flask Templates

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend

- Python
- Flask

### Machine Learning & NLP

- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- Regular Expressions (Regex)

### Libraries

- pdfplumber
- pandas
- spaCy
- scikit-learn

---

## 📂 Project Structure

```
AI-Powered-Resume/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/
│   └── skills.csv
│
├── model/
│   ├── analyzer.py
│   ├── parser.py
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
└── templates/
    ├── index.html
    ├── result.html
    └── components/
        ├── dashboard.html
        ├── breakdown.html
        ├── skills.html
        ├── analysis.html
        ├── assessment.html
        ├── preview.html
        └── actions.html
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Pragya17pathak/AI-Powered-Resume.git
```

### Navigate to Project Folder

```bash
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

---

## ▶️ Run the Project

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📖 How It Works

### Step 1

Upload a PDF resume.

### Step 2

Paste the Job Description.

### Step 3

The system extracts the resume text.

### Step 4

The resume is preprocessed using NLP techniques.

### Step 5

Skills are extracted from the resume and job description.

### Step 6

TF-IDF Vectorization and Cosine Similarity are used to calculate resume-job similarity.

### Step 7

The ATS score is generated.

### Step 8

The application displays:

- ATS Score
- Score Breakdown
- Matched Skills
- Missing Skills
- Resume Analysis
- Resume Assessment
- Resume Preview
- AI Suggestions

---

## 📊 ATS Score Components

| Component | Maximum Score |
|------------|--------------:|
| Resume Similarity | 30 |
| Skill Match | 25 |
| Experience | 10 |
| Projects | 10 |
| Education | 10 |
| Certifications | 5 |
| Contact Information | 5 |
| Resume Length | 5 |
| **Total** | **100** |

---

## 🧠 Machine Learning Techniques

- TF-IDF Vectorization
- Cosine Similarity
- Keyword Matching
- Regex Pattern Matching
- Rule-Based Resume Evaluation

---

## 📸 Output

The application provides:

- ATS Score Dashboard
- Resume Score Breakdown
- Matched Skills
- Missing Skills
- Resume Strengths
- Improvement Suggestions
- Hiring Assessment
- Resume Preview

---

## 🔮 Future Enhancements

- 📊 Chart.js Dashboard
- 📄 PDF Report Download
- 🌙 Dark Mode
- 🎤 Voice-Based Resume Analysis
- ☁️ Cloud Deployment
- 📈 Resume Ranking for Multiple Candidates
- 🤖 LLM-Based Resume Review
- 📧 Email Report Generation

---

## 📚 Learning Outcomes

This project demonstrates:

- Flask Web Development
- Natural Language Processing
- Machine Learning Basics
- TF-IDF Vectorization
- Cosine Similarity
- Resume Parsing
- Modular Project Architecture
- Bootstrap UI Development

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Create a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Pragya Pathak**

GitHub: https://github.com/Pragya17pathak

---

⭐ If you found this project helpful, consider giving it a star on GitHub!