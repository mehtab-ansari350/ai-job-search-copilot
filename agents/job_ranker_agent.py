"""
Job Ranker Agent

Ranks jobs based on resume skills.
"""

from utils.skill_normalizer import normalize


def rank_jobs(resume: dict, jobs: list):
    """
    Rank jobs according to resume skills.
    """

    # Normalize resume skills
    resume_skills = set(
        normalize(
            resume.get("skills", [])
        )
    )

    ranked = []

    for job in jobs:

        # Get job skills safely
        job_skills = job.get("skills", [])

        # If provider accidentally returns a string
        if isinstance(job_skills, str):
            job_skills = []

        # Normalize job skills
        job_skills = set(
            normalize(job_skills)
        )

        # No extracted skills
        if len(job_skills) == 0:

            ranked.append(
                {
                    "title": job.get("title"),
                    "company": job.get("company"),
                    "location": job.get("location"),
                    "match_score": 0,
                    "matched_skills": []
                }
            )

            continue

        # Find common skills
        matched = resume_skills & job_skills

        score = int(
            (len(matched) / len(job_skills)) * 100
        )

        ranked.append(
            {
                "title": job.get("title"),
                "company": job.get("company"),
                "location": job.get("location"),
                "match_score": score,
                "matched_skills": sorted(list(matched))
            }
        )

    ranked.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return ranked