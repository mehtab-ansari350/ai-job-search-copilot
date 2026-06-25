"""
Career Advisor Agent

Creates a learning roadmap
based on job match analysis.
"""

import json
import re

from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)


def generate_career_plan(
    missing_skills: list
):
    """
    Generate learning roadmap.
    """

    prompt = f"""
You are a senior AI career mentor.

Missing Skills:
{missing_skills}

Create a roadmap.

Return ONLY valid JSON.

{{
    "roadmap": [],
    "estimated_duration": "",
    "interview_focus": []
}}
"""

    response = llm.invoke(prompt)

    content = re.sub(
        r"```json|```",
        "",
        response.content
    ).strip()

    return json.loads(content)