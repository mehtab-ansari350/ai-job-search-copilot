"""
Resume Upload Routes 
"""

import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File 

router = APIRouter()

UPLOAD_DIRECTORY = "data/resumes"

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):
    """
    Upload resume PDF
    """

    file_path = os.path.join(
        UPLOAD_DIRECTORY,
        file.filename
    )

    with open(file_path, "wb") as f :
        content = await file.read()
        f.write(content)

        return {
            "message": "Resume upload successfully",
            "file_name": file.filename 
        }