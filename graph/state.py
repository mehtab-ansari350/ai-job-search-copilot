from typing import TypedDict


class JobSearchState(TypedDict):
    job_description: str

    resume_data: dict

    jobs: list

    ranked_jobs: list

    skill_gap: dict

    career_plan: dict

    match_result: dict