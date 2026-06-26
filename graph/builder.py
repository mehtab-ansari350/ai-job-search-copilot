"""
LangGraph Builder
"""

from langgraph.graph import StateGraph, END

from graph.state import JobSearchState

from graph.nodes import (
    resume_node,
    job_search_node,
    job_ranker_node,
    skill_gap_node,
    career_advisor_node,
)

workflow = StateGraph(JobSearchState)

workflow.add_node("resume", resume_node)
workflow.add_node("job_search", job_search_node)
workflow.add_node("job_ranker", job_ranker_node)
workflow.add_node("skill_gap", skill_gap_node)
workflow.add_node("career_advisor", career_advisor_node)

workflow.set_entry_point("resume")

workflow.add_edge("resume", "job_search")
workflow.add_edge("job_search", "job_ranker")
workflow.add_edge("job_ranker", "skill_gap")
workflow.add_edge("skill_gap", "career_advisor")
workflow.add_edge("career_advisor", END)

graph = workflow.compile()