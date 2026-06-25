"""
Skill Gap Analyzer Agent
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


def analyze_skill_gap(job_description: str):

    retrieved_docs = search_chunks(
        query="skills experience projects",
        k=5
    )

    resume_context = "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
    )

    prompt = f"""
You are a senior AI career advisor.

Resume:
{resume_context}

Job Description:
{job_description}

Compare the resume with the job description.

Return ONLY valid JSON:

{{
  "existing_skills": [],
  "missing_skills": [],
  "learning_priority": []
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