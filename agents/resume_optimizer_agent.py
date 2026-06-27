"""
Resume Optimizer Agent
"""

import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def optimize_resume(resume_data, job_description):

    prompt = f"""
You are a Senior Technical Recruiter and Resume Expert.

Candidate Resume

Skills:
{resume_data.get("skills", [])}

Experience:
{resume_data.get("experience", [])}

Projects:
{resume_data.get("projects", [])}

Target Job Description

{job_description}

Your task is to improve this resume.

Return in markdown.

## Professional Summary

## Improved Skills

## Improved Experience

## Improved Projects

## ATS Keywords to Add

## Final Suggestions
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content