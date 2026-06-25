"""
Job Match Agent

Compares resume against
a job description.
"""
import json 
import re 
from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)


def analyze_job_match(
    resume_data: dict,
    job_description: str
):
    """
    Compare structured resume data
    against a job description.
    """

    prompt = f"""
You are a senior AI recruiting specialist.

Candidate Resume Data:

{json.dumps(resume_data, indent=2)}

Job Description:

{job_description}

Instructions:

1. Compare candidate skills against required skills.
2. Calculate match score logically.
3. Match score should be between 0 and 100.
4. If candidate satisfies most requirements,
   score should be above 70.
5. Explain missing skills accurately.

Return ONLY valid JSON.

{{
    "match_score": 0,
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