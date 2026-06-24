from pydantic import BaseModel
from typing import List 


class QuestionRequest(
    BaseModel
):
    question: str

class JobDescriptionRequest(
    BaseModel
):
    job_description: str

class JobMatchResponse(BaseModel):
    match_score: int
    strengths: List[str]
    missing_skills: List[str]
    recommendations: List[str]