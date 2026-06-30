"""
Resume Optimizer Agent
"""

from groq import Groq

from app.config import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)


def optimize_resume(resume_data, job_description):

    prompt = f"""
You are a Senior FAANG Recruiter, ATS Expert, and Professional Resume Writer.

Your ONLY job is to improve the candidate's existing resume.

Candidate Resume

Skills:
{resume_data.get("skills", "")}

Experience:
{resume_data.get("experience", "")}

Projects:
{resume_data.get("projects", "")}

Target Job Description

{job_description}

STRICT RULES

1. NEVER invent any company.
2. NEVER invent any project.
3. NEVER invent any certification.
4. NEVER invent any experience.
5. NEVER invent any achievement.
6. NEVER invent any metric.
7. NEVER invent any technology.
8. NEVER add AWS, Kubernetes, MongoDB, etc. unless they already exist in the resume.
9. If something is missing, recommend it instead of pretending the candidate has it.
10. Only rewrite existing content professionally.

Your goal is to:

• Improve grammar
• Improve ATS score
• Improve readability
• Improve action verbs
• Improve bullet points
• Add ATS keywords naturally
• Keep everything truthful

Return ONLY these sections.

# Professional Summary

# Improved Skills

# Improved Experience

# Improved Projects

# ATS Keywords Found

# ATS Keywords Missing

# Suggested Improvements

For "ATS Keywords Missing", recommend skills from the job description that are NOT in the resume.

Never claim the candidate has those skills.

Instead write:

"Consider learning Docker."

"Consider learning Kubernetes."

"Consider learning AWS."

instead of adding them to the resume.

Output should be professional.

No explanations.

No markdown code blocks.

No fake information.
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