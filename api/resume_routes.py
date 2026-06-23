"""
Resume Upload Routes
"""

import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from rag.resume_parser import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIRECTORY = "data/resumes"

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):
    """
    Upload resume and extract text
    """

    file_path = os.path.join(
        UPLOAD_DIRECTORY,
        file.filename
    )

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    extracted_text = extract_text_from_pdf(
        file_path
    )

    return {
        "message": "Resume uploaded successfully",
        "file_name": file.filename,
        "text_preview": extracted_text[:1000]
    }