from fastapi import APIRouter

from api.schemas import CareerAdvisorRequest
from agents.career_advisor_agent import generate_career_plan

router = APIRouter()


@router.post("/career-advisor")
def career_advisor(request: CareerAdvisorRequest):

    career_plan = generate_career_plan(
        request.missing_skills
    )

    return career_plan