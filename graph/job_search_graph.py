"""
LangGraph Workflow
"""

from langgraph.graph import(
    StateGraph, END
)

from graph.state import (
    JobSearchState 
)

from agents.resume_agent import (
    extract_resume_data
)

from agents.job_match_agent import (
    analyze_job_match
)

from agents.career_advisor_agent import (
    generate_career_plan
)

def resume_node(
        state: JobSearchState
):
    """
    Resume Agent Node 

    Extract structured resume information.
    """

    resume_data = extract_resume_data()

    return {
        "resume_data": resume_data
    }

def job_match_node(
    state: JobSearchState
):
    """
    Job Match Agent Node
    """

    result = analyze_job_match(
        resume_data=state["resume_data"],
        job_description=state["job_description"]
    )

    return {
        "match_result": result
    }

def career_advisor_node(
    state: JobSearchState
):
    """
    Career Advisor Node

    Generates a roadmap based on
    missing skills from job match.
    """

    missing_skills = state[
        "match_result"
    ]["missing_skills"]

    plan = generate_career_plan(
        missing_skills
    )

    return {
        "career_plan": plan
    }


# LangGraph WorkFlow

builder = StateGraph(
    JobSearchState 
)

builder.add_node(
    "resume_agent",
    resume_node
)

builder.add_node(
    "job_match_agent",
    job_match_node
)

builder.add_node(
    "career_advisor_agent",
    career_advisor_node
)

builder.set_entry_point(
    "resume_agent"
)

builder.add_edge(
    "resume_agent",
    "job_match_agent"
)

builder.add_edge(
    "job_match_agent",
    "career_advisor_agent"
)

builder.add_edge(
    "career_advisor_agent",
    END
)

job_search_graph = builder.compile()