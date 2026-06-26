from graph.nodes import (
    resume_node,
    job_search_node,
    job_rank_node,
    skill_gap_node,
    career_plan_node
)

state = {
    "job_description": (
        "AI Engineer with Python, FastAPI, Docker, "
        "AWS, Kubernetes and LangChain"
    )
}

state.update(resume_node(state))
state.update(job_search_node(state))
state.update(job_rank_node(state))
state.update(skill_gap_node(state))
state.update(career_plan_node(state))

print("\nFINAL STATE\n")
print(state)