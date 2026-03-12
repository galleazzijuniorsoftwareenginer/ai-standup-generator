from fastapi import APIRouter
from app.services.github_service import get_commits
from app.services.ai_service import generate_standup

router = APIRouter()


@router.get("/generate-standup")
def create_standup(username: str, repo: str):

    commits = get_commits(username, repo)

    standup = generate_standup(commits)

    return {"standup": standup}
