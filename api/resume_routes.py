"""
Resume Upload Routes
"""

import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from rag.resume_parser import extract_text_from_pdf
from rag.ingestion_service import ingest_resume 

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