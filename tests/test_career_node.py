from graph.job_search_graph import (
    resume_node,
    job_match_node,
    career_advisor_node 
)

state = {
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

state.update(
    resume_node(state)
)

state.update(
    job_match_node(state)
)

state.update(
    career_advisor_node(state)
)

print(state["career_plan"])
