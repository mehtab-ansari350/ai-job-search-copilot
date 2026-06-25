from agents.resume_agent import extract_resume_data
from agents.job_search_agent import search_jobs


def rank_jobs():

    resume = extract_resume_data()

    resume_skills = set(
        skill.lower()
        for skill in resume["skills"]
    )

    jobs = search_jobs()

    ranked = []

    for job in jobs:

        job_skills = set(
            skill.lower()
            for skill in job["skills"]
        )

        matched = (
            resume_skills.intersection(
                job_skills
            )
        )

        score = int(
            len(matched)
            / len(job_skills)
            * 100
        )

        ranked.append({
            "title": job["title"],
            "company": job["company"],
            "location": job["location"],
            "match_score": score,
            "matched_skills": list(matched)
        })

    ranked.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return ranked