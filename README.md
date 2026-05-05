# 🤖 AI Resume Analyzer (NLP + Machine Learning)

## 📌 Overview

AI Resume Analyzer is a web-based application that evaluates a candidate’s resume against a given Job Description (JD).
It calculates an ATS (Applicant Tracking System) score, identifies missing skills, and provides actionable suggestions to improve resume quality.

---

## 🚀 Features

* 📄 Resume parsing (PDF format)
* 🧠 NLP-based text processing
* 📊 ATS score calculation using TF-IDF & Cosine Similarity
* ✅ Matched skills detection
* ❌ Missing skills identification
* 💡 Smart improvement suggestions
* 📈 Visual insights using charts
* 🌐 Interactive UI with Streamlit

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Streamlit, Scikit-learn, PDFPlumber, Matplotlib
* **Concepts:** NLP, TF-IDF, Cosine Similarity

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/resume-analyzer-ai.git
cd resume-analyzer-ai
```

### 2. Create virtual environment (optional)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run resume.py
```

---

## 📊 How It Works

1. Upload your resume (PDF)
2. Paste the job description
3. System extracts skills from both inputs
4. Calculates ATS score using similarity measures
5. Displays:

   * Match score
   * Matched skills
   * Missing skills
   * Suggestions for improvement

---

## 📁 Project Structure

```
resume-analyzer-ai/
│
├── resume.py
├── requirements.txt
├── README.md
└── data/
    └── skills_list.txt
```

---

## 🎯 Future Improvements

* 🔥 BERT-based semantic matching
* 🌐 Deployment with public URL
* 📊 Advanced analytics dashboard
* 👤 User authentication system

---

## 👨‍💻 Author

Hemant Rana



