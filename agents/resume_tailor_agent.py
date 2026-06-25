"""
Resume Tailoring Agent
"""

import json
import re

from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY

from agents.resume_agent import (
    extract_resume_data
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)


def tailor_resume(
    job_description: str
):

    resume_data = extract_resume_data()

    prompt = f"""
You are an ATS Resume Optimization Expert.

Candidate Resume:

{resume_data}

Job Description:

{job_description}

Return ONLY valid JSON:

{{
  "ats_score": 85,
  "matching_keywords": [],
  "missing_keywords": [],
  "strengths": [],
  "resume_recommendations": []
}}
"""

    response = llm.invoke(prompt)

    content = response.content

    content = re.sub(
        r"```json|```",
        "",
        content
    ).strip()

    return json.loads(content)

    