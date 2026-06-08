import os
import re
import requests
from requests.auth import HTTPBasicAuth

JIRA_URL = os.environ["JIRA_URL"].rstrip("/")
JIRA_EMAIL = os.environ["JIRA_EMAIL"]
JIRA_API_TOKEN = os.environ["JIRA_API_TOKEN"]
JIRA_PROJECT_KEY = os.environ["JIRA_PROJECT_KEY"]


def _extract_field(text: str, field: str) -> str:
    match = re.search(rf"{field}:\s*(.+)", text)
    return match.group(1).strip() if match else ""


def _extract_story_points(text: str) -> int | None:
    sp = _extract_field(text, "Story Points")
    try:
        return int(sp)
    except (ValueError, TypeError):
        return None


def create_jira_ticket(original_text: str, structured_content: str) -> str:
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    summary = _extract_field(structured_content, "Summary") or original_text[:100]
    priority = _extract_field(structured_content, "Priority") or "Medium"
    labels_raw = _extract_field(structured_content, "Labels")
    labels = [l.strip() for l in labels_raw.split(",") if l.strip()] if labels_raw else []

    payload: dict = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": structured_content}],
                    }
                ],
            },
            "issuetype": {"name": "Story"},
            "priority": {"name": priority},
        }
    }

    if labels:
        payload["fields"]["labels"] = labels

    sp = _extract_story_points(structured_content)
    if sp is not None:
        payload["fields"]["story_points"] = sp

    response = requests.post(
        f"{JIRA_URL}/rest/api/3/issue",
        json=payload,
        headers=headers,
        auth=auth,
        timeout=15,
    )
    response.raise_for_status()

    issue_key = response.json()["key"]
    return f"{JIRA_URL}/browse/{issue_key}"
