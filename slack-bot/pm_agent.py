import os
import anthropic

client = anthropic.AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

SYSTEM_PROMPT = """You are an expert Product Manager agent with deep experience in product strategy, discovery, and execution.

Your expertise covers:
- Product discovery and user research
- Writing PRDs and user stories
- Competitive analysis
- Prioritization frameworks (RICE, MoSCoW, ICE)
- Roadmap planning
- Breaking features into tasks
- Writing structured Jira tickets

How you work:
- Be structured and methodical
- Respond in the same language the user wrote in — Hebrew if they write in Hebrew, English if they write in English
- Use PM frameworks and best practices
- Be concise but comprehensive
- Use Slack formatting: *bold*, _italic_, bullet lists with •
"""

COMMAND_PROMPTS = {
    "prd": (
        "Write a comprehensive PRD for the following feature or product:\n{text}\n\n"
        "Structure:\n"
        "• *Executive Summary*\n"
        "• *Problem Statement*\n"
        "• *Goals & Success Metrics*\n"
        "• *User Stories*\n"
        "• *Functional Requirements*\n"
        "• *Out of Scope*\n"
        "• *Open Questions*"
    ),
    "sprint": (
        "Create a detailed sprint plan for the following backlog items:\n{text}\n\n"
        "Structure:\n"
        "• *Sprint Goal*\n"
        "• *User Stories* (with story point estimates)\n"
        "• *Definition of Done*\n"
        "• *Risks & Dependencies*"
    ),
    "competitive": (
        "Perform a competitive analysis for: {text}\n\n"
        "Structure:\n"
        "• *Market Overview*\n"
        "• *Key Competitors* (features, pricing, positioning)\n"
        "• *Strengths & Weaknesses*\n"
        "• *Strategic Recommendations*"
    ),
    "ask": "{text}",
    "jira": (
        "Create a structured Jira ticket for the following:\n{text}\n\n"
        "Provide exactly in this format:\n"
        "Summary: (one clear line)\n"
        "Description: (2-3 sentences with context and goal)\n"
        "Acceptance Criteria:\n"
        "- [ ] criterion 1\n"
        "- [ ] criterion 2\n"
        "- [ ] criterion 3\n"
        "Story Points: (1 / 2 / 3 / 5 / 8)\n"
        "Labels: (comma separated relevant labels)\n"
        "Priority: (Highest / High / Medium / Low)"
    ),
}


async def ask_pm_agent(command: str, text: str, user_name: str) -> str:
    prompt_template = COMMAND_PROMPTS.get(command, "{text}")
    prompt = prompt_template.format(text=text)

    message = await client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"@{user_name}: {prompt}"}],
    )
    return message.content[0].text
