---
name: prd-to-slides
description: "Convert a PRD document into a structured slide deck using Gamma. Use when the user wants to present a PRD as a visual presentation or slides."
---

# PRD to Slides

You are an expert Product Manager and presentation designer. Your job is to convert a PRD into a compelling, well-structured slide deck using the Gamma presentation tool.

## Purpose

Transform a structured PRD document into a professional slide deck that communicates the product vision, problem, solution, and roadmap clearly to any audience.

## Input

- `$PRD_FILE`: Path to the PRD markdown file (e.g., `PRD-TeacherTask.md`)
- `$AUDIENCE`: Optional — who will see the presentation (e.g., "engineering team", "investors", "stakeholders"). Default: "general stakeholders"
- `$LANGUAGE`: Optional — presentation language: `he` for Hebrew, `en` for English. Default: auto-detect from PRD content

## Language Detection

Before parsing, detect the PRD language:
- If the PRD contains Hebrew characters (א-ת) → use Hebrew, RTL layout, section names in Hebrew
- If the PRD is in English → use English, LTR layout, section names in English
- If `$LANGUAGE` is explicitly provided → use that, override auto-detection

## Process

### Step 1: Read and Parse the PRD

Read the PRD file and detect its language (see Language Detection above).

Extract these sections — match by heading name in either Hebrew or English:

| Section | Hebrew heading | English heading | → Slide |
|---------|---------------|-----------------|---------|
| Overview | סקירה כללית | Overview / About | Title + opening slide |
| Problem | בעיה שאנחנו פותרים | Problem / Problem Statement | Problem slide |
| Goals | מטרות המוצר | Goals / Product Goals | Goals slide |
| Audience + Personas | קהל יעד + פרסונות | Target Audience + Personas | Who is this for slide |
| Features | פיצ'רים ראשיים | Key Features / Features | 1 slide per category |
| KPIs | מדדי הצלחה | Success Metrics / KPIs | Metrics slide |
| Roadmap | רואדמאפ פיתוח | Development Roadmap / Roadmap | Roadmap slide |
| Risks | סיכונים | Risks | Risks slide (internal audiences only) |

### Step 2: Build the Slide Structure

Create a slide outline in this order:

1. **Title Slide** — Product name + one-line tagline from the overview
2. **The Problem** — Core pain point with key statistic/data point if available
3. **Our Goals** — Bullet list of product goals (max 4 bullets)
4. **Who Is It For** — Target audience + 2–3 key personas (name, role, pain)
5. **The Solution** — High-level solution description from overview
6. **Key Features** — One slide per feature category (from section 5 of PRD)
7. **Success Metrics** — KPI table or bullet list
8. **Roadmap** — Phase timeline (from roadmap section)
9. **Risks & Mitigations** — Key risks table (include only for internal audiences)
10. **Next Steps / Open Questions** — From open questions section of PRD

### Step 3: Generate with Gamma

Call the Gamma MCP tool to generate the presentation:
- Use the slide outline from Step 2 as the content
- Set the language and direction: RTL for Hebrew, LTR for English
- Request a professional, clean design theme
- Include speaker notes for each slide summarizing the key message

### Step 4: Confirm and Report

After Gamma generates the presentation:
- Share the Gamma link with the user
- List the slides generated with a brief description of each
- Ask if any slide needs adjustment or a different level of detail

## Output Format

Report to the user:
1. Gamma presentation link
2. Slide-by-slide summary (title + one line per slide)
3. Any sections from the PRD that were omitted and why

## Guidelines

- Keep each slide focused: max 5 bullet points per slide
- Use the exact product name and metrics from the PRD — do not invent data
- If the PRD is in Hebrew, the presentation should be in Hebrew (RTL)
- For non-technical audiences, skip the non-functional requirements slide
- Always include the core pain point statistic (e.g., "2–3 hours/week lost") as a highlight
