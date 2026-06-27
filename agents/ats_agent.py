import re

from utils.skill_normalizer import normalize


def analyze_ats(resume_data: dict, job_description: str):
    """
    Analyze ATS compatibility between resume and job description.

    Returns:
    {
        ats_score,
        matched_keywords,
        missing_keywords,
        strengths,
        weaknesses,
        suggestions
    }
    """

    
    # Resume Skills

    resume_skills = set(
        normalize(
            resume_data.get("skills", [])
        )
    )

  
    # Extract keywords from JD

    words = re.findall(
        r"[A-Za-z0-9+#./-]+",
        job_description.lower()
    )

    stop_words = {
        "and", "or", "with", "for", "the", "to",
        "of", "in", "on", "at", "using", "use",
        "experience", "years", "year", "developer",
        "engineer", "required", "preferred",
        "knowledge", "ability"
    }

    job_keywords = set()

    for word in words:

        word = word.strip()

        if len(word) < 3:
            continue

        if word in stop_words:
            continue

        job_keywords.add(word)

    job_keywords = set(
        normalize(list(job_keywords))
    )

  
    # Skill Match
   
    matched = resume_skills & job_keywords

    missing = job_keywords - resume_skills

    if len(job_keywords) == 0:
        skill_score = 0
    else:
        skill_score = len(matched) / len(job_keywords) * 50

  
    # Experience Score
   
    experience = resume_data.get("experience", [])

    experience_score = 20 if experience else 0

    # -----------------------------
    # Projects Score
    # -----------------------------
    projects = resume_data.get("projects", [])

    if len(projects) >= 2:
        project_score = 15
    elif len(projects) == 1:
        project_score = 8
    else:
        project_score = 0

    # -----------------------------
    # Education Score
    # -----------------------------
    education = resume_data.get("education", [])

    education_score = 10 if education else 0

    # -----------------------------
    # Completeness
    # -----------------------------
    completeness = 0

    if resume_data.get("skills"):
        completeness += 1

    if resume_data.get("experience"):
        completeness += 1

    if resume_data.get("projects"):
        completeness += 1

    if resume_data.get("education"):
        completeness += 1

    if resume_data.get("links"):
        completeness += 1

    completeness_score = completeness

    # -----------------------------
    # Final Score
    # -----------------------------
    ats_score = int(
        skill_score
        + experience_score
        + project_score
        + education_score
        + completeness_score
    )

    ats_score = min(100, ats_score)

    # -----------------------------
    # Strengths
    # -----------------------------
    strengths = []

    if experience:
        strengths.append("Relevant work experience")

    if len(projects) >= 2:
        strengths.append("Strong project portfolio")

    if len(matched) >= 5:
        strengths.append("Excellent keyword coverage")

    if "python" in resume_skills:
        strengths.append("Strong Python background")

    # -----------------------------
    # Weaknesses
    # -----------------------------
    weaknesses = []

    if len(missing) > 0:
        weaknesses.append("Missing important job keywords")

    if len(projects) == 0:
        weaknesses.append("Projects section is weak")

    # -----------------------------
    # Suggestions
    # -----------------------------
    suggestions = []

    for skill in list(missing)[:5]:
        suggestions.append(f"Add {skill} to your resume if you have experience.")

    if len(projects) < 2:
        suggestions.append("Include more production-level AI projects.")

    suggestions.append("Quantify achievements using metrics.")

    suggestions.append("Use action verbs like Built, Designed, Improved, Optimized.")

    return {

        "ats_score": ats_score,

        "matched_keywords": sorted(list(matched)),

        "missing_keywords": sorted(list(missing)),

        "strengths": strengths,

        "weaknesses": weaknesses,

        "suggestions": suggestions
    }