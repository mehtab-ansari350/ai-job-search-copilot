from fastapi import APIRouter

from api.schemas import CoverLetterRequest
from agents.resume_agent import extract_resume_data
from agents.cover_letter_agent import generate_cover_letter

router = APIRouter()


@router.post("/generate-cover-letter")
def generate_cover_letter_route(request: CoverLetterRequest):

    resume_data = extract_resume_data()

    job = {
        "title": "",
        "company": "",
        "description": request.job_description,
    }

    cover_letter = generate_cover_letter(
        resume_data,
        job
    )

    return {
        "cover_letter": cover_letter
    }