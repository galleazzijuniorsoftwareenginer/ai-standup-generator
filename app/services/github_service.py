import requests


def get_commits(username: str, repo: str):

    url = f"https://api.github.com/repos/{username}/{repo}/commits"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    commits = response.json()

    messages = []

    for commit in commits[:5]:
        messages.append(commit["commit"]["message"])

    return messages

