# agents/job_match_agent.py

"""
Job Match Agent

Compares resume against
a job description.
"""
import json 
import re 
from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY
from rag.vector_store import search_chunks


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)


def analyze_job_match(
    job_description: str
):
    """
    Compare resume against job description.
    """

    retrieved_docs = search_chunks(
        query="technical skills experience projects",
        k=5
    )

    resume_context = "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
    )

    prompt = f"""
You are a senior AI recruiting specialist.

Compare the candidate resume
with the job description.

Resume:
{resume_context}

Job Description:
{job_description}

Return ONLY valid JSON:

{{
  "match_score": 0-100,
  "strengths": [],
  "missing_skills": [],
  "recommendations": []
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

    return json.loads(content)