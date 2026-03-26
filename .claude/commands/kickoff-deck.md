---
description: Build a Kickoff meeting presentation from a PRD — problem, solution space, and main tasks
argument-hint: "<path-to-PRD> [audience] [language: he|en]"
---

# /kickoff-deck — Kickoff Presentation Builder

Build a focused Kickoff presentation from your PRD that aligns the team on why, what, and how.

Supports Hebrew (RTL) and English (LTR) PRDs automatically.

## Usage

```
/kickoff-deck PRD-TeacherTask.md
/kickoff-deck PRD-TeacherTask.md "engineering team"
/kickoff-deck PRD-MyProduct-EN.md "cross-functional team" en
```

## What You Get

A 9-slide Gamma presentation covering:
1. Title slide
2. The Problem (executive summary)
3. Why Now?
4. Solution Space — what we're building
5. Goals & Success Metrics
6. Main Tasks — Roadmap
7. Risks & Mitigations
8. Open Questions
9. Next Steps

## Workflow

### Step 1: Clarify
- Ask for the PRD file if not provided
- Ask who will attend the kickoff (default: cross-functional team)
- Detect language from PRD content (Hebrew / English) — ask only if unclear

### Step 2: Extract from PRD
- Pull the problem, solution, goals, features, roadmap, risks, open questions
- Identify key statistics and data points to highlight

### Step 3: Generate
- Build the slide structure (exactly 9 slides)
- Call Gamma MCP to create the presentation
- Return the Gamma link + slide list

### Step 4: Facilitation Tips
- Indicate which slides are discussion-oriented vs. informational
- Suggest how much time to spend on each section

## Design Principles

- **Focused**: 9 slides max — this is a kickoff, not a deep-dive
- **Energizing**: forward-looking tone
- **Aligned**: everyone leaves knowing the why, what, and main tasks
- **Honest**: real data from PRD only — no invented numbers
