from fastapi import APIRouter

from api.schemas import InterviewRequest
from agents.interview_agent import (
    generate_interview_questions
)

router = APIRouter()


@router.post("/generate-interview")
def generate_interview_route(
    request: InterviewRequest
):
    return generate_interview_questions(
        request.job_description
    )