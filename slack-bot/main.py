import os
import hmac
import hashlib
import time
import httpx
from fastapi import FastAPI, Request, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

from pm_agent import ask_pm_agent
from jira_client import create_jira_ticket

load_dotenv()

app = FastAPI()

SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]

VALID_COMMANDS = {"prd", "sprint", "competitive", "ask", "jira"}
SLACK_MAX_LENGTH = 3900


def verify_slack_signature(body: bytes, timestamp: str, signature: str) -> bool:
    if abs(time.time() - int(timestamp)) > 300:
        return False
    sig_basestring = f"v0:{timestamp}:{body.decode()}"
    expected = "v0=" + hmac.new(
        SLACK_SIGNING_SECRET.encode(),
        sig_basestring.encode(),
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(expected, signature)


async def post_to_slack(response_url: str, text: str, in_channel: bool = True):
    chunks = [text[i : i + SLACK_MAX_LENGTH] for i in range(0, len(text), SLACK_MAX_LENGTH)]
    async with httpx.AsyncClient() as client:
        for chunk in chunks:
            await client.post(
                response_url,
                json={"response_type": "in_channel" if in_channel else "ephemeral", "text": chunk},
            )


async def process_command(command: str, text: str, user_name: str, response_url: str):
    try:
        result = await ask_pm_agent(command, text, user_name)
        await post_to_slack(response_url, result)
    except Exception as e:
        await post_to_slack(response_url, f":x: שגיאה בעיבוד הפקודה: {e}", in_channel=False)


async def process_jira(text: str, user_name: str, response_url: str):
    try:
        structured = await ask_pm_agent("jira", text, user_name)
        ticket_url = create_jira_ticket(text, structured)
        await post_to_slack(response_url, f":white_check_mark: טיקט נוצר: {ticket_url}\n\n{structured}")
    except Exception as e:
        await post_to_slack(response_url, f":x: שגיאה ביצירת טיקט ב-Jira: {e}", in_channel=False)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/slack/{command}")
async def handle_command(command: str, request: Request, background_tasks: BackgroundTasks):
    body = await request.body()
    timestamp = request.headers.get("X-Slack-Request-Timestamp", "")
    signature = request.headers.get("X-Slack-Signature", "")

    if not verify_slack_signature(body, timestamp, signature):
        raise HTTPException(status_code=401, detail="Invalid Slack signature")

    if command not in VALID_COMMANDS:
        return JSONResponse({"text": f":x: פקודה לא מוכרת: `/{command}`"})

    form = await request.form()
    text = form.get("text", "").strip()
    user_name = form.get("user_name", "someone")
    response_url = form.get("response_url", "")

    if not text:
        usage = {
            "prd": "`/prd <תיאור הפיצ'ר>`",
            "sprint": "`/sprint <פריטי הבקלוג>`",
            "competitive": "`/competitive <שם החברה>`",
            "ask": "`/ask <שאלה>`",
            "jira": "`/jira <תיאור הטיקט>`",
        }
        return JSONResponse({"text": f":information_source: שימוש: {usage[command]}"})

    if command == "jira":
        background_tasks.add_task(process_jira, text, user_name, response_url)
    else:
        background_tasks.add_task(process_command, command, text, user_name, response_url)

    labels = {
        "prd": "כותב PRD",
        "sprint": "מתכנן ספרינט",
        "competitive": "מנתח מתחרים",
        "ask": "חושב",
        "jira": "יוצר טיקט ב-Jira",
    }
    return JSONResponse({"text": f":hourglass_flowing_sand: {labels[command]}... (/{command} {text})"})
