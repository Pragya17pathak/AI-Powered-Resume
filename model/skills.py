import re

SKILLS = ['python', 'java', 'c', 'c++', 'c#', 'html', 'css', 'javascript', 'typescript', 'react', 'angular', 'vue', 'node.js', 'express', 'flask', 'django', 'fastapi', 'spring boot', 'php', 'sql', 'mysql', 'postgresql', 'mongodb', 'sqlite', 'oracle', 'git', 'github', 'docker', 'kubernetes', 'aws', 'amazon web services', 'azure', 'microsoft azure', 'google cloud', 'machine learning', 'deep learning', 'artificial intelligence', 'natural language processing', 'computer vision', 'tensorflow', 'keras', 'pytorch', 'scikit-learn', 'pandas', 'numpy', 'scipy', 'matplotlib', 'seaborn', 'opencv', 'feature engineering', 'data preprocessing', 'data analysis', 'data visualization', 'model evaluation', 'classification', 'regression', 'linear regression', 'logistic regression', 'decision tree', 'random forest', 'naive bayes', 'support vector machine', 'svm', 'knn', 'k-nearest neighbors', 'clustering', 'pca', 'lda', 'tf-idf', 'bag of words', 'word2vec', 'cosine similarity', 'llm', 'generative ai', 'prompt engineering', 'langchain', 'rag', 'rest api', 'json', 'xml', 'jwt', 'oauth', 'linux', 'bash', 'shell scripting', 'object oriented programming', 'oop', 'data structures', 'algorithms', 'dsa', 'operating systems', 'computer networks', 'dbms', 'database management system', 'software engineering', 'jupyter notebook', 'visual studio code', 'vs code', 'pycharm', 'excel', 'power bi', 'tableau', 'chart.js', 'bootstrap', 'tailwind css', 'jquery', 'ajax', 'pypdf2', 'pdfplumber', 'reportlab', 'streamlit', 'render', 'vercel', 'firebase', 'debugging', 'problem solving']

SYNONYMS = {'ml': 'machine learning', 'ai': 'artificial intelligence', 'nlp': 'natural language processing', 'js': 'javascript', 'ts': 'typescript', 'cpp': 'c++', 'scikit learn': 'scikit-learn', 'tfidf': 'tf-idf', 'tf idf': 'tf-idf', 'restful api': 'rest api', 'chartjs': 'chart.js', 'jupyter': 'jupyter notebook', 'vs code': 'visual studio code', 'gcp': 'google cloud', 'aws': 'amazon web services', 'os': 'operating systems', 'cn': 'computer networks', 'dbms': 'database management system', 'dsa': 'data structures', 'reactjs': 'react'}

def normalize_skill(skill):
    skill = skill.lower().strip()
    return SYNONYMS.get(skill, skill)

def extract_skills(text):
    if not text:
        return []
    text = text.lower()
    text = re.sub(r"[^a-z0-9#+.\-\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    found = set()

    for skill in SKILLS:
        escaped = re.escape(skill)
        escaped = escaped.replace(r"\ ", r"[\s\-]+")
        pattern = rf"\b{escaped}\b"
        if re.search(pattern, text):
            found.add(normalize_skill(skill))

    words = set(text.split())
    for w in words:
        n = normalize_skill(w)
        if n in SKILLS:
            found.add(n)

    return sorted([s.title() for s in found])
