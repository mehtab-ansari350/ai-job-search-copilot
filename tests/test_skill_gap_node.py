from agents.skill_gap_agent import (
    analyze_skill_gap
)

job_description = """
AI Engineer

Skills:
Python
FastAPI
Docker
AWS
Kubernetes
LangChain
LLMs
"""

result = analyze_skill_gap(
    job_description
)

print(result)