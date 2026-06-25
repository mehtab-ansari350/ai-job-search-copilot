"""
Shared LangGraph State
"""

from typing import TypedDict


class JobSearchState(TypedDict):
    job_description: str

    resume_data: dict

    match_result: dict

    career_plan: dict