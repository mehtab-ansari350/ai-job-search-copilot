"""
Job Skill Extractor Agent

Extracts technical skills
from a job description.
"""

import json
import re

from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY

from utils.skill_normalizer import normalize


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)


def extract_job_skills(job_description: str):
    """
    Extract skills from a job description.
    """

    prompt = f"""
You are an expert AI recruiter.

Extract ONLY explicitly mentioned technical skills.

DO NOT infer skills.

DO NOT summarize.

ONLY include skills that literally appear.

Return JSON only.

Example:

Input:

Python
FastAPI
Docker
AWS
LangChain

Output:

{{
   "skills":[
      "Python",
      "FastAPI",
      "Docker",
      "AWS",
      "LangChain"
   ]
}}

Job Description:

{job_description}

Return ONLY valid JSON.

{{
    "skills":[]
}}
"""

    response = llm.invoke(prompt)

    content = re.sub(
        r"```json|```",
        "",
        response.content
    ).strip()

    result = json.loads(content)

    return normalize(result["skills"])