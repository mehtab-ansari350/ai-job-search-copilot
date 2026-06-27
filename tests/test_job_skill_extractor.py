from agents.job_skill_extractor_agent import (
    extract_job_skills
)

description = """
We are hiring an AI Engineer.

Requirements

Python

FastAPI

Docker

AWS

Kubernetes

LangChain

LLMs

RAG

Vector Databases

REST APIs
"""

skills = extract_job_skills(description)

print(skills)