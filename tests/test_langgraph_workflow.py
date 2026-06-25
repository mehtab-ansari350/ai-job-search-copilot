from graph.job_search_graph import (
    job_search_graph
)

result = job_search_graph.invoke(
    {
        "job_description": """
AI Engineer

Required Skills:

Python
FastAPI
Docker
AWS
Kubernetes
LLMs
LangChain
"""
    }
)

print("\nFINAL OUTPUT\n")
print(result)