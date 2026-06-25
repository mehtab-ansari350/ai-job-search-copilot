"""
LangGraph API Routes
"""

from fastapi import APIRouter 

from api.schemas import (
    JobDescriptionRequest
)

from graph.job_search_graph import(
    job_search_graph 
)

router = APIRouter()

@router.post(
    "/analyze-job"
)
def analyze_job(
    request: JobDescriptionRequest
):
    """
    Run LangGraph workflow.
    """

    result = job_search_graph.invoke(
        {
            "job_description":
            request.job_description
        }
    )

    return result