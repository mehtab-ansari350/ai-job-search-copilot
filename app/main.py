"""
Main FastAPI Application
AI Job Search Copilot
"""

from fastapi import FastAPI

from api.resume_routes import router as resume_router

from api.rag_routes import (
    router as rag_router
)

from api.graph_routes import (
    router as graph_router
)

from api.job_search_routes import (
    router as job_router
)

from api.job_ranker_routes import (
    router as rank_router
)

from api.resume_tailor_routes import (
    router as tailor_router
)

from api.cover_letter_routes import router as cover_letter_router

from api.interview_routes import (
    router as interview_router
)

from api.skill_gap_routes import router as skill_gap_router

app = FastAPI(
    title="AI Job Search Copilot",
    version="1.0.0"
)

app.include_router(
    resume_router
)

app.include_router(
    rag_router
)

app.include_router(
    graph_router
)

app.include_router(
    job_router
)

app.include_router(
    rank_router
)

app.include_router(
    tailor_router
)

app.include_router(
    cover_letter_router
)

app.include_router(
    interview_router
)

app.include_router(
    skill_gap_router,
    tags=["Skill Gap Analyzer"]
)

@app.get("/")
def home():
    return {
        "message": "AI Job Search Copilot is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }