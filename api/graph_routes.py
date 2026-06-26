"""
LangGraph API Routes
"""

from fastapi import APIRouter 

from api.schemas import (
    JobDescriptionRequest
)

from graph.builder import graph

router = APIRouter()

@router.post("/analyze-job")
def analyze_job(request: JobDescriptionRequest):

    result = graph.invoke(
        {
            "job_description": request.job_description
        }
    )

    return result