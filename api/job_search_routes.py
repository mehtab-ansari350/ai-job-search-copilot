from fastapi import APIRouter

from agents.job_search_agent import search_jobs

router = APIRouter()


@router.get("/jobs")
def get_jobs():

    return {
        "jobs": search_jobs()
    }