from fastapi import FastAPI
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
    "name": "AI Standup Generator API",
    "description": "Generate developer daily standup reports from GitHub commits using AI.",
    "documentation": "/docs",
    "example_request": "/generate-standup?username=torvalds&repo=linux",
    "status": "API running"
}
