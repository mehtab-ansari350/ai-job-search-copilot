from graph.job_search_graph import (
    resume_node,
    job_match_node 
)

state = {
    "job_description": """
AI Engineer 

Requried Skills:

python
Fast API
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

print(state["match_result"])