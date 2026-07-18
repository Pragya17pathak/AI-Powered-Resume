# 🚀 AI-Powered Resume Ranker

An intelligent **ATS (Applicant Tracking System) Resume Analyzer** built using **Python, Flask, Scikit-learn, Bootstrap, and Chart.js**. This application compares a resume with a job description, calculates an ATS compatibility score, identifies matched and missing skills, assigns a resume grade, provides improvement suggestions, and generates a professional PDF report.

🌐 **Live Demo:** https://ai-powered-resume-iqhg.onrender.com

---

## ✨ Features

- 📄 Upload Resume (PDF)
- 📝 Analyze Resume Against Job Description
- 🎯 ATS Compatibility Score
- 🏆 Resume Grade (A+ to F)
- 📊 Resume Similarity Analysis
- 🔍 Keyword Matching
- ✅ Matched Skills Detection
- ❌ Missing Skills Identification
- 💡 Resume Improvement Suggestions
- 📈 Interactive Dashboard
- 📋 Resume Statistics
- 📑 PDF Report Generation
- 🌙 Dark Mode Support
- 📱 Responsive User Interface

---

## 🛠️ Tech Stack

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

# 📂 Project Structure

```text
AI-Powered-Resume-Ranker/

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
│   └── uploads/
│
├── templates/
│   ├── components/
│   ├── index.html
│   └── result.html
│
├── app.py
├── requirements.txt
├── render.yaml
├── Procfile
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Pragya17pathak/AI-Powered-Resume.git

cd AI-Powered-Resume
```

---

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv

venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
python app.py
```

---

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

# 🚀 Workflow

```text
Upload Resume
        │
        ▼
Extract Resume Text
        │
        ▼
Preprocess Text
        │
        ▼
Extract Skills
        │
        ▼
Compare with Job Description
        │
        ▼
Calculate ATS Score
        │
        ▼
Identify Missing Skills
        │
        ▼
Generate Suggestions
        │
        ▼
Assign Resume Grade
        │
        ▼
Generate PDF Report
        │
        ▼
Display Interactive Dashboard
```

---

# 📊 ATS Score Components

| Component | Weight |
|-----------|:------:|
| Resume Similarity | 30% |
| Skills Match | 25% |
| Experience | 10% |
| Projects | 10% |
| Education | 10% |
| Certifications | 5% |
| Contact Information | 5% |
| Resume Length | 5% |

---

# 🏅 Resume Grades

| ATS Score | Grade |
|-----------|:-----:|
| 95–100 | A+ |
| 85–94 | A |
| 75–84 | B |
| 65–74 | C |
| 50–64 | D |
| Below 50 | F |

---

# 📄 Generated Report

The application generates a detailed PDF report containing:

- ATS Score
- Resume Grade
- Resume Similarity
- Keyword Match Percentage
- Matched Skills
- Missing Skills
- Resume Statistics
- Improvement Suggestions

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Machine Learning
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Resume Parsing
- PDF Processing
- Flask Web Development
- Interactive Dashboard Design
- Responsive User Interface
- Cloud Deployment using Render

---

# 🚀 Future Improvements

- AI-based Resume Rewriting
- Cover Letter Generator
- LinkedIn Profile Analysis
- Multiple Job Description Comparison
- Interview Question Generator
- Multi-language Resume Analysis
- Resume Ranking Dashboard

---

# 👩‍💻 Author

**Pragya Pathak**

**B.Tech Computer Science and Engineering**

**Lovely Professional University**

---

## 🔗 Connect

**GitHub**

https://github.com/Pragya17pathak

**LinkedIn**

(Add your LinkedIn profile URL here)

---

# 📜 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful, consider giving it a **star** on GitHub.