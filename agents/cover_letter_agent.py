"""
Cover Letter Generator Agent
"""

import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"


def generate_cover_letter(resume_data, job):

    prompt = f"""
You are an expert HR recruiter and professional resume writer.

Write a professional cover letter.

Candidate Skills:
{resume_data.get("skills", [])}

Experience:
{resume_data.get("experience", [])}

Projects:
{resume_data.get("projects", [])}

Job Title:
{job.get("title", "")}

Company:
{job.get("company", "")}

Job Description:
{job.get("description", "")}

Instructions:
- Keep it under 300 words.
- Make it ATS-friendly.
- Mention matching skills.
- Explain why the candidate is a strong fit.
- Sound confident and professional.
- End politely.
"""

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.4,
        messages=[
            {
                "role": "system",
                "content": "You are an expert cover letter writer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content