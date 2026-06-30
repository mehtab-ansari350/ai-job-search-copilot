"""
Resume Upload Routes
"""

import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from rag.resume_parser import extract_text_from_pdf
from rag.ingestion_service import ingest_resume 
from api.schemas import JobDescriptionRequest
from agents.resume_optimizer_agent import optimize_resume
from rag.resume_storage import load_resume

router = APIRouter()

UPLOAD_DIRECTORY = "data/resumes"

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):
    """
    Upload resume and ingest into vector database.
    """

    file_path = os.path.join(
        UPLOAD_DIRECTORY,
        file.filename
    )

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    result = ingest_resume(file_path)

    return {
        "message": "Resume uploaded and indexed successfully",
        "file_name": file.filename,
        "chunks_stored": result["chunks_stored"],
        "text_length": result["text_length"]
    }

@router.post("/optimize-resume")
async def optimize_resume_route(request: JobDescriptionRequest):
    """
    Optimize the latest uploaded resume.
    """

    resume = load_resume()

    if resume is None:
        return {
            "error": "Please upload a resume first."
        }

    resume_data = {
        "skills": resume["text"],
        "experience": resume["text"],
        "projects": resume["text"],
    }

    optimized_resume = optimize_resume(
        resume_data,
        request.job_description
    )

    return {
        "optimized_resume": optimized_resume
    }