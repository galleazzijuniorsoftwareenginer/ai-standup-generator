from fastapi import FastAPI
from datetime import datetime
from app.api.standup_routes import router as standup_router
app = FastAPI(
    title="AI Standup Generator",
    description="Generate standups using GitHub activity and AI",
    version="0.1"
)

app.include_router(standup_router)


@app.get("/")
def root():
    return {
        "project": "AI Standup Generator",
        "description": "AI-powered API that generates developer daily standup reports from GitHub commits.",
        "author": "galleazzijuniorsoftwareenginer",
        "version": "0.1",
        "tech_stack": [
            "Python",
            "FastAPI",
            "GitHub API",
            "Gemini AI",
            "Docker",
            "Railway"
        ],
        "endpoints": {
            "generate_standup": "/generate-standup?username=torvalds&repo=linux",
            "docs": "/docs"
        },
        "status": "running",
        "timestamp": datetime.utcnow()
    }
