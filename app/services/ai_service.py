from google import genai
import os


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_standup(commits):

    prompt = f"""
Based on these GitHub commit messages, generate a developer daily standup.

Commits:
{commits}

Format:

Yesterday:
- ...

Today:
- ...

Blockers:
- ...
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
