import os
from docx import Document
import tempfile

EXPERIENCE_FILE = "experience.txt"

# Load experience from file
def load_experience():
    if os.path.exists(EXPERIENCE_FILE):
        with open(EXPERIENCE_FILE, "r", encoding="utf-8") as file:
            return file.read()
    return ""

# Save experience to file
def save_experience(experience):
    with open(EXPERIENCE_FILE, "w", encoding="utf-8") as file:
        file.write(experience)

# Create Word document
def create_word_doc(text):
    doc = Document()
    doc.add_paragraph(text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmpfile:
        doc.save(tmpfile.name)
        return tmpfile.name
