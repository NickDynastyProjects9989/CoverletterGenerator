import os
from langchain_groq import ChatGroq
from scripts.helpers import load_experience

# Load API key securely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="deepseek-r1-distill-llama-70b",api_key=GROQ_API_KEY)

# Function to answer experience-based questions
def answer_experience_question(question):
    experience = load_experience()
    prompt = f"Based on this experience: {experience}\nAnswer this question very briefly in 3 to 5 lines it has to be professional from my experience and after think give me side heading final answer: {question}"
    return llm.predict(prompt)
