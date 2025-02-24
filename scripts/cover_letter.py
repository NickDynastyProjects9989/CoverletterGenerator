import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from scripts.helpers import load_experience

# Load API key securely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key=GROQ_API_KEY)

# Cover letter prompt template
cover_letter_prompt = PromptTemplate(
    input_variables=["experience", "job_description"],
    template="""
    Generate a professional cover letter for the following job description:
    {job_description}

    The candidate's experience includes:
    {experience}

    The letter should be well-structured, formal, and tailored to the role.
    """
)

# Generate Cover Letter
def generate_cover_letter(job_description):
    experience = load_experience()
    prompt = cover_letter_prompt.format(experience=experience, job_description=job_description)
    return llm.predict(prompt)
