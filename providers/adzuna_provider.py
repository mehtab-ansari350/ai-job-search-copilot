"""
Adzuna Job Provider
"""

import requests

from providers.base_provider import BaseJobProvider
from app.config import (
    ADZUNA_APP_ID,
    ADZUNA_APP_KEY
)
from agents.job_skill_extractor_agent import extract_job_skills


class AdzunaProvider(BaseJobProvider):

    BASE_URL = (
        "https://api.adzuna.com/v1/api/jobs/in/search/1"
    )

    def get_jobs(
        self,
        keyword="AI Engineer",
        location="India"
    ):

        params = {
            "app_id": ADZUNA_APP_ID,
            "app_key": ADZUNA_APP_KEY,
            "results_per_page": 20,
            "what": keyword,
            "where": location,
            "content-type": "application/json"
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        jobs = []

        for job in data.get("results", []):

            description = job.get(
                "description",
                ""
            )

            skills = extract_job_skills(
                description
            )

            #Fallback if the LLM extracts too few skills
            if len(skills) < 3:
                skills = [
                    "Python",
                    "Machine Learning",
                    "LLMs"
                ]

            jobs.append(
                {
                    "title": job.get("title"),
                    "company": job.get(
                        "company",
                        {}
                    ).get(
                        "display_name",
                        "Unknown"
                    ),
                    "location": job.get(
                        "location",
                        {}
                    ).get(
                        "display_name",
                        "Unknown"
                    ),
                    "description": description,
                    "skills": skills
                }
            )

        return jobs