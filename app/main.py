"""
Main FastAPI Application
AI Job Search Copilot
"""

from fastapi import FastAPI

from api.resume_routes import router as resume_router

app = FastAPI(
    title="AI Job Search Copilot",
    version="1.0.0"
)

app.include_router(resume_router)


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