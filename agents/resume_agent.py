"""
Resume Agent

Extracts structured information
from resume context.
"""

import json
import re

from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY
from rag.vector_store import search_chunks

from utils.skill_normalizer import normalize 


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)


def extract_resume_data():
    """
    Extract structured resume information.
    """

    docs = search_chunks(
        query="skills projects experience education",
        k=8
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are an expert resume analyzer.

Extract information from the resume.

Resume:
{context}

Return ONLY valid JSON.

{{
    "skills": [],
    "projects": [],
    "experience": [],
    "education": []
}}
"""

    response = llm.invoke(
        prompt
    )

    content = response.content

    content = re.sub(
        r"```json|```",
        "",
        content
    ).strip()

    resume_data = json.loads(content)

    # Normalize resume skills
    resume_data["skills"] = normalize(
        resume_data.get("skills", [])
    )

    return resume_data