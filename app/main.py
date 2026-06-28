"""
Main FastAPI Application
AI Job Search Copilot
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    graph_router,
    prefix="/api",
    tags=["LangGraph"]
)

app.include_router(
    resume_router,
    prefix="/api",
    tags=["Resume"]
)

app.include_router(
    rag_router,
    prefix="/api",
    tags=["RAG"]
)

app.include_router(
    job_router,
    prefix="/api",
    tags=["Jobs"]
)

app.include_router(
    rank_router,
    prefix="/api",
    tags=["Ranking"]
)

app.include_router(
    tailor_router,
    prefix="/api",
    tags=["Resume Tailor"]
)

app.include_router(
    cover_letter_router,
    prefix="/api",
    tags=["Cover Letter"]
)

app.include_router(
    interview_router,
    prefix="/api",
    tags=["Interview"]
)

app.include_router(
    skill_gap_router,
    prefix="/api",
    tags=["Skill Gap"]
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