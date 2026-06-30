from fastapi import APIRouter, HTTPException
import traceback

from api.schemas import JobDescriptionRequest
from graph.builder import graph

router = APIRouter()


@router.post("/analyze-job")
def analyze_job(request: JobDescriptionRequest):
    try:
        result = graph.invoke(
            {
                "job_description": request.job_description
            }
        )
        return result

    except Exception as e:
        print("\n========== GRAPH ERROR ==========")
        traceback.print_exc()
        print("=================================\n")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )