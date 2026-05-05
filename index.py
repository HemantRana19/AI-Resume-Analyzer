import streamlit as st
import pdfplumber
import matplotlib.pyplot as plt

st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: #f5f7fb;
}

/* Bigger input fields */
.stFileUploader {
    padding: 20px;
    font-size: 18px;
}

.stTextArea textarea {
    height: 150px !important;
    font-size: 16px;
}

/* Labels bigger */
label {
    font-size: 18px !important;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------- Page Config ----------
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #f5f7fb;
    font-family: 'Segoe UI', sans-serif;
}

.block-container {
    padding-top: 2rem;
}

h1 {
    color: #1e293b;
    font-size: 40px;
    font-weight: 700;
}

h3 {
    color: #475569;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
}

.stTextArea textarea {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Load Skills ----------
def load_skills():
    with open("data/skills_list.txt", "r") as f:
        return [line.strip().lower() for line in f]

# ---------- Extract Text ----------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# ---------- Header ----------
# st.title("🤖 AI Resume Analyzer")
st.markdown("<h1 style='text-align: center;'>🤖 AI Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("### 🚀 Analyze your resume and boost your chances of getting hired")
# st.markdown("---")

# ---------- Input Card ----------
# st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📄 Upload Resume", type=["pdf"])

with col2:
    jd_text = st.text_area("📋 Job Description")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Main Logic ----------
if uploaded_file and jd_text:

    resume_text = extract_text_from_pdf(uploaded_file)

    # ---------- Similarity ----------
    texts = [resume_text, jd_text]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    ats_score = round(score * 100, 2)

    skills = load_skills()

    resume_lower = resume_text.lower()
    jd_lower = jd_text.lower()

    matched = [s for s in skills if s in resume_lower and s in jd_lower]
    missing = [s for s in skills if s in jd_lower and s not in resume_lower]

    # ---------- ATS Score Card ----------
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 ATS Score")
    st.metric("Match Score", f"{ats_score}%")
    st.progress(int(ats_score))

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Skills ----------
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matched Skills")
        st.write(matched if matched else "No matching skills")

    with col2:
        st.subheader("❌ Missing Skills")
        st.write(missing if missing else "No missing skills")

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Chart ----------
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Skills Analysis")

    labels = ['Matched', 'Missing']
    sizes = [len(matched), len(missing)]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Feedback ----------
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🧠 Detailed Feedback")

    if ats_score < 40:
        st.error("❌ Your resume is not aligned with the job. Add more relevant skills and projects.")
    elif ats_score < 70:
        st.warning("⚠️ Moderate match. Improve missing skills and optimize keywords.")
    else:
        st.success("✅ Great match! Your resume is well aligned with the job.")

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Suggestions ----------
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("💡 Improvement Suggestions")

    if missing:
        for skill in missing:
            st.write(f"👉 Add {skill} in your resume")
    else:
        st.write("🔥 Excellent! No major skill gaps found")

    st.markdown('</div>', unsafe_allow_html=True) 
    