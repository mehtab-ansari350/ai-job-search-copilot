"""
API Schemas
"""

from pydantic import BaseModel 

class JobDescriptionRequest(
    BaseModel 
):
    job_description: str 


class TailorResumeRequest(BaseModel):
    job_description: str


class CoverLetterRequest(BaseModel):
    job_description: str

class InterviewRequest(BaseModel):
    job_description: str

class SkillGapRequest(BaseModel):
    job_description: str