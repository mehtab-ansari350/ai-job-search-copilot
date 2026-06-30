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
You are an expert ATS resume parser.

Extract ALL information from the resume.

Return ONLY valid JSON.

Rules:

- Extract ALL technical skills.
- Extract EVERY project.
- Extract EVERY work experience.
- Extract EVERY education entry.
- Extract certifications if present.
- Extract achievements if present.
- Extract GitHub, LinkedIn and Portfolio links if available.
- Never leave projects empty unless there are absolutely none.
- Never invent information.

Resume:

{context}

Return this JSON format:

{{
    "skills": [],

    "projects": [
        {{
            "title":"",
            "description":"",
            "technologies":[]
        }}
    ],

    "experience":[
        {{
            "position":"",
            "organization":"",
            "duration":"",
            "description":""
        }}
    ],

    "education":[
        {{
            "degree":"",
            "field":"",
            "university":"",
            "duration":"",
            "cgpa":""
        }}
    ],

    "certifications":[],

    "achievements":[],

    "links": {{
        "github":"",
        "linkedin":"",
        "portfolio":""
    }}
}}
"""

    response = llm.invoke(prompt)

    content = response.content

    print("\n================ LLM OUTPUT ================\n")
    print(content)
    print("\n============================================\n")

    content = re.sub(
    r"```json|```",
    "",
    content
    )

    # Remove comments
    content = re.sub(r"#.*", "", content)

    # Find the first JSON object
    start = content.find("{")

    if start != -1:
        content = content[start:]

    # Remove everything after the last }
    end = content.rfind("}")

    if end != -1:
        content = content[:end + 1]

    content = content.strip()

    try:
        resume_data = json.loads(content)
    except Exception as e:
        print("\n========= INVALID JSON =========")
        print(content)
        print("================================")
        raise Exception(f"Invalid JSON returned by LLM: {e}")

    # Normalize resume skills
    resume_data["skills"] = normalize(
        resume_data.get("skills", [])
    )

    return resume_data