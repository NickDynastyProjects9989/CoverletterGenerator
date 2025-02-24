import streamlit as st
import os
from scripts.cover_letter import generate_cover_letter
from scripts.qa_experience import answer_experience_question
from scripts.helpers import load_experience, save_experience, create_word_doc

# Set Page Title
st.set_page_config(page_title="AI Cover Letter & Q&A", layout="wide")

# Load Experience
experience_text = load_experience()

# UI Layout
st.title("📄 AI Cover Letter Generator & Q&A")
st.write("Generate a professional cover letter and ask AI about your experience.")

# Experience Management
st.subheader("📝 Your Experience (Stored)")
st.text_area("Stored Experience", experience_text, height=200, disabled=True)

# Update Experience
with st.expander("🔄 Update Experience"):
    new_experience = st.text_area("Update Your Experience", experience_text, height=200)
    if st.button("Save Experience"):
        save_experience(new_experience)
        st.success("✅ Experience updated! Refresh to see changes.")

# Job Description Input
st.subheader("💼 Enter Job Description")
job_description = st.text_area("Paste the Job Description Here", "")

# Generate Cover Letter
if st.button("🚀 Generate Cover Letter"):
    if job_description:
        cover_letter = generate_cover_letter(job_description)
        st.subheader("📌 Generated Cover Letter:")
        st.write(cover_letter)

        # Download as Word File
        file_path = create_word_doc(cover_letter)
        with open(file_path, "rb") as file:
            st.download_button(
                label="⬇ Download Cover Letter",
                data=file,
                file_name="Cover_Letter.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    else:
        st.warning("⚠ Please enter a job description.")

# Q&A on Experience
st.subheader("💬 Ask AI About Your Experience")
question = st.text_input("Enter your question about your experience")
if st.button("🤖 Get Answer"):
    if question:
        answer = answer_experience_question(question)
        st.write("**AI Answer:**", answer)
    else:
        st.warning("⚠ Please enter a question.")
