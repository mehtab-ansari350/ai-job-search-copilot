import json
import re

from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY
from rag.vector_store import search_chunks


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)


def generate_cover_letter(
    job_description: str
):
    
    docs = search_chunks(
        query="skills projects experience",
        k=5
    )

    resume_context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are a professional recruiter.

Write a professional cover letter.

Resume:
{resume_context}

Job Description:
{job_description}

Return ONLY JSON:

{{
  "cover_letter":"..."
}}
"""

    response = llm.invoke(prompt)

    content = re.sub(
        r"```json|```",
        "",
        response.content
    ).strip()

    return json.loads(content)