from fastapi import APIRouter

from api.schemas import CoverLetterRequest
from agents.cover_letter_agent import generate_cover_letter

router = APIRouter()


@router.post("/generate-cover-letter")
def generate_cover_letter_route(
    request: CoverLetterRequest
):
    return generate_cover_letter(
        request.job_description
    )