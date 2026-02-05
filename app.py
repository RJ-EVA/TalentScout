import streamlit as st
from resume_parser import extract_text_from_pdf
from llm_service import parse_and_screen_resume

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="TalentScout – AI Resume Screener",
    page_icon="📄",
    layout="centered"
)

# -------------------------------------------------
# BLACK + BLUE THEME
# -------------------------------------------------
st.markdown(
    """
    <style>
    .stApp { background-color: #0e1117; color: #e6edf3; }
    h1, h2, h3 { color: #58a6ff; }

    .stFileUploader {
        background-color: #161b22;
        border: 1px dashed #1f6feb;
        padding: 12px;
        border-radius: 6px;
    }

    .stButton > button {
        background-color: #1f6feb;
        color: white;
        border-radius: 6px;
        border: none;
        padding: 0.5em 1em;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #388bfd;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# UI
# -------------------------------------------------
st.title("📄 TalentScout – AI Resume Screener")
st.write(
    "Upload your resume. "
    "Our AI system will extract candidate details and evaluate suitability automatically."
)

st.divider()

# -------------------------------------------------
# RESUME UPLOAD
# -------------------------------------------------
resume = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

if resume:
    with st.spinner("Reading resume..."):
        resume_text = extract_text_from_pdf(resume)

    with st.spinner("Analyzing resume using AI..."):
        result = parse_and_screen_resume(resume_text)

    st.subheader("📊 Resume Screening Result")
    st.write(result)

    st.success(
        "Resume processed successfully. "
        "If shortlisted, the recruitment team will contact the candidate."
    )
