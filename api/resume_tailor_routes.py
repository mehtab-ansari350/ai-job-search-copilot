from fastapi import APIRouter

from api.schemas import (
    TailorResumeRequest
)

from agents.resume_tailor_agent import (
    tailor_resume
)

router = APIRouter()


@router.post("/tailor-resume")
def tailor_resume_route(
    request: TailorResumeRequest
):

    result = tailor_resume(
        request.job_description
    )

    return result