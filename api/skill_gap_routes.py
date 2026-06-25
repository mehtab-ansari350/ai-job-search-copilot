from fastapi import APIRouter

from api.schemas import SkillGapRequest
from agents.skill_gap_agent import analyze_skill_gap

router = APIRouter()


@router.post("/skill-gap-analysis")
def skill_gap_route(
    request: SkillGapRequest
):
    return analyze_skill_gap(
        request.job_description
    )