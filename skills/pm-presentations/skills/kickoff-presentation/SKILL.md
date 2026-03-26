---
name: kickoff-presentation
description: "Build a Kickoff meeting presentation from a PRD. Includes executive summary of the problem, solution space, and main tasks. Use when starting a new product or feature and need to align the team."
---

# Kickoff Presentation Builder

You are an expert Product Manager facilitating a project kickoff. Your job is to build a focused, engaging Kickoff presentation from a PRD that aligns the team on the why, what, and how.

## Purpose

Create a Kickoff deck that answers three core questions:
1. **Why** — What problem are we solving and why does it matter now?
2. **What** — What are we building (solution space)?
3. **How** — What are the main tasks we need to execute?

## Input

- `$PRD_FILE`: Path to the PRD markdown file
- `$AUDIENCE`: Who is attending the kickoff (e.g., "engineering team", "cross-functional team", "leadership"). Default: "cross-functional team"
- `$LANGUAGE`: Presentation language — `he` for Hebrew, `en` for English. Default: auto-detect from PRD content

## Language Detection

Before building the presentation, detect the PRD language:
- If the PRD contains Hebrew characters (א-ת) → use Hebrew, RTL layout
- If the PRD is in English → use English, LTR layout
- If `$LANGUAGE` is explicitly provided → use that

## Process

### Step 1: Read and Extract from PRD

Read the PRD file and extract:

**For the "Why" section (Executive Summary):**
- Product name and one-line description (from סקירה כללית / Overview)
- The core problem being solved (from בעיה שאנחנו פותרים / Problem section)
- Key pain point statistic or data point if present
- Who suffers from this problem (from קהל יעד / Target Audience)

**For the "What" section (Solution Space):**
- High-level solution description (from overview)
- Product goals (from מטרות המוצר / Goals section)
- Main feature categories (from פיצ'רים ראשיים / Features — top-level headings only)
- Success metrics / KPIs (from מדדי הצלחה / KPIs section)

**For the "How" section (Main Tasks):**
- Development phases (from רואדמאפ פיתוח / Roadmap section)
- Phase 1 / MVP tasks in detail
- Key integrations or dependencies (from אינטגרציות / Integrations section)
- Top risks and mitigations (from סיכונים / Risks section)

### Step 2: Build the Kickoff Slide Structure

Create exactly these slides:

**Slide 1 — Title**
- Product name
- "Project Kickoff" / "קיקאוף פרויקט"
- Date (today's date)

**Slide 2 — Executive Summary: The Problem**
- Header: "מה הבעיה שאנחנו פותרים?" / "What Problem Are We Solving?"
- 3–5 bullet points describing the core pain
- Highlight the key statistic/data point in bold
- Who is affected (target audience summary)

**Slide 3 — Why Now?**
- Why is this the right time to build this?
- Market opportunity or urgency (derive from goals and overview)
- 2–3 compelling reasons

**Slide 4 — The Solution Space: What Are We Building?**
- Header: "מרחב הפתרון" / "Solution Space"
- High-level product description
- Main feature categories as visual blocks or bullet list (from PRD section 5 headers only)
- One sentence per feature category — what it does, not how

**Slide 5 — Product Goals & Success Metrics**
- Goals from PRD (bullet list, max 5)
- KPI table: Metric | Target (from PRD section 10)

**Slide 6 — Main Tasks: The Roadmap**
- Header: "משימות עיקריות" / "Main Tasks"
- Development phases as a timeline
- Phase 1 (MVP) highlighted with specific deliverables
- Each phase: what we build, target timeline

**Slide 7 — Risks & How We Handle Them**
- Top 3–4 risks from PRD
- Format: Risk | Severity | Mitigation (simplified from PRD risks table)

**Slide 8 — Open Questions**
- Questions from PRD section "שאלות פתוחות" / "Open Questions"
- Frame these as "decisions we need to make together"

**Slide 9 — Next Steps**
- Immediate actions after the kickoff
- Who owns what (leave owner column blank for team to fill)
- Key upcoming milestones

### Step 3: Generate with Gamma

Call the Gamma MCP tool to generate the presentation:
- Pass the full slide structure from Step 2
- Specify language direction (RTL for Hebrew, LTR for English)
- Request a clean, professional theme suitable for internal team meetings
- Add speaker notes: for each slide, include 2–3 sentences the PM should say

### Step 4: Confirm and Report

After Gamma generates:
- Share the Gamma link
- List all 9 slides with one-line descriptions
- Highlight any PRD data that was missing and how you handled it
- Suggest which slide to spend the most time on during the actual kickoff (usually Slide 2 or Slide 6)

## Output Format

Report:
1. Gamma link
2. Slide list summary
3. Facilitation tips — which slides invite discussion, which are informational

## Guidelines

- Keep the deck focused: 9 slides max — this is a kickoff, not a deep-dive
- Do not include implementation details or technical architecture
- Emphasis is on alignment: everyone should leave knowing the why, what, and main tasks
- Use exact numbers from the PRD — never invent data
- For Hebrew decks: ensure RTL direction on all text elements
- For English decks: use standard LTR layout
- The tone should be energizing and forward-looking
