import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import anthropic

load_dotenv()

app = App(token=os.environ["SLACK_BOT_TOKEN"])
claude = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

SYSTEM_PROMPT = """You are PM Agent — an expert Product Manager embedded in the team's Slack.

Rules:
- NEVER introduce yourself or list your capabilities. Just answer.
- Be concise and direct — this is Slack, not a document editor
- Respond in the same language the user wrote in (Hebrew → Hebrew, English → English)
- Use Slack formatting: *bold*, bullet points with •
- For long outputs (PRD, analysis), use clear sections with *Title*
- Ask clarifying questions only when truly necessary
"""


def ask_claude(user_message: str) -> str:
    response = claude.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )
    return response.content[0].text


def split_message(text: str, limit: int = 3900) -> list[str]:
    return [text[i : i + limit] for i in range(0, len(text), limit)]


@app.event("app_mention")
def handle_mention(event, say):
    user = event.get("user", "")
    text = event.get("text", "")
    thread_ts = event.get("thread_ts") or event.get("ts")

    # Remove the @PM Agent mention from the text
    clean_text = " ".join(
        word for word in text.split() if not word.startswith("<@")
    ).strip()

    if not clean_text:
        say(text="היי! שאל אותי כל שאלה בנושא Product Management 🚀", thread_ts=thread_ts)
        return

    reply = ask_claude(f"<@{user}> שאל: {clean_text}")

    for chunk in split_message(reply):
        say(text=chunk, thread_ts=thread_ts)


@app.event("message")
def handle_dm(event, say):
    # Only handle DMs (channel_type = "im"), ignore bot messages
    if event.get("channel_type") != "im" or event.get("bot_id"):
        return

    text = event.get("text", "").strip()
    if not text:
        return

    reply = ask_claude(text)

    for chunk in split_message(reply):
        say(text=chunk)


if __name__ == "__main__":
    print("PM Agent connecting to Slack...")
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
