"""
RAG Routes
"""

from fastapi import APIRouter

from app.schemas import (
    QuestionRequest
)

from rag.rag_service import (
    ask_resume
)

from app.schemas import (
    QuestionRequest,
    JobDescriptionRequest
)

from agents.job_match_agent import (
    analyze_job_match
)

router = APIRouter()


@router.post("/ask-resume")
def ask_resume_route(
    request: QuestionRequest
):
    """
    Ask questions about resume.
    """

    result = ask_resume(
    request.question
    )
    return result 

@router.post("/match-job")
def match_job(
    request: JobDescriptionRequest
):
    """
    Compare resume against job description.
    """

    result = analyze_job_match(
        request.job_description
    )

    return result 