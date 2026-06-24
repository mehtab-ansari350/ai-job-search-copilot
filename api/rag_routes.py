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

router = APIRouter()


@router.post("/ask-resume")
def ask_resume_route(
    request: QuestionRequest
):
    """
    Ask questions about resume.
    """

    answer = ask_resume(
        request.question
    )

    return {
        "answer": answer
    }