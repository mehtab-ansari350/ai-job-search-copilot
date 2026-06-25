from fastapi import APIRouter

from agents.job_ranker_agent import (
    rank_jobs
)

router = APIRouter()


@router.get("/rank-jobs")
def get_ranked_jobs():

    return {
        "ranked_jobs": rank_jobs()
    }