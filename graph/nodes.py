"""
LangGraph Nodes

Each node wraps one AI agent.
Nodes read from the shared state
and return updated state.
"""

from graph.state import JobSearchState

from agents.resume_agent import extract_resume_data
from agents.job_search_agent import search_jobs
from agents.job_ranker_agent import rank_jobs
from agents.skill_gap_agent import analyze_skill_gap
from agents.career_advisor_agent import generate_career_plan
from agents.ats_agent import analyze_ats 


def resume_node(state: JobSearchState):

    resume = extract_resume_data()

    return {
        "resume_data": resume
    }

def job_search_node(state: JobSearchState):

    jobs = search_jobs()

    return {
        "jobs": jobs
    }

from agents.job_ranker_agent import rank_jobs


def job_ranker_node(state):

    ranked_jobs = rank_jobs(
        state["resume_data"],
        state["jobs"]
    )

    return {
        "ranked_jobs": ranked_jobs
    }


from agents.skill_gap_agent import analyze_skill_gap


def skill_gap_node(state):

    skill_gap = analyze_skill_gap(
        state["job_description"]
    )

    return {
        "skill_gap": skill_gap
    }

def career_advisor_node(state):

    career_plan = generate_career_plan(
        state["skill_gap"]["missing_skills"]
    )

    return {
        "career_plan": career_plan
    }

def ats_node(state):

    report = analyze_ats(
        state["resume_data"],
        state["job_description"]
    )

    return {
        "ats_report": report
    }