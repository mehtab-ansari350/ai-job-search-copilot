from typing import TypedDict


class JobSearchState(TypedDict):
    job_description: str

    resume_data: dict

    jobs: list

    ranked_jobs: list

    skill_gap: dict

    ats_report: dict      

    career_plan: dict

    resume_optimization: str

    cover_letter: str 
