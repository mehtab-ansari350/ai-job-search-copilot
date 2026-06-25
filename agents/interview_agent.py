import json
import re

from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY
from rag.vector_store import search_chunks


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)


def generate_interview_questions(
    job_description: str
):

    docs = search_chunks(
        query="skills experience projects",
        k=5
    )

    resume_context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are a Senior AI Engineering Interviewer.

Candidate Resume:
{resume_context}

Job Description:
{job_description}

Generate:

- 5 Technical Questions
- 3 Behavioral Questions
- Sample Answers
- Interview Tips

Return ONLY valid JSON.

{{
  "technical_questions":[
    {{
      "question":"",
      "sample_answer":""
    }}
  ],
  "behavioral_questions":[
    {{
      "question":"",
      "sample_answer":""
    }}
  ],
  "tips":[]
}}
"""

    response = llm.invoke(prompt)

    content = re.sub(
        r"```json|```",
        "",
        response.content
    ).strip()

    return json.loads(content)