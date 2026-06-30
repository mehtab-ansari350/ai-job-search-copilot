"""
Resume Storage Service
"""

import json
import os

RESUME_JSON_PATH = "data/resumes/latest_resume.json"


def save_resume(text: str):
    """
    Save latest uploaded resume.
    """

    os.makedirs("data/resumes", exist_ok=True)

    data = {
        "text": text
    }

    with open(RESUME_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_resume():
    """
    Load latest uploaded resume.
    """

    if not os.path.exists(RESUME_JSON_PATH):
        return None

    with open(RESUME_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)