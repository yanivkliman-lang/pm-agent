---
description: Convert a PRD into a visual slide deck using Gamma — all sections, structured for stakeholders
argument-hint: "<path-to-PRD> [audience] [language: he|en]"
---

# /prd-slides — PRD to Slide Deck

Convert your PRD into a professional slide presentation using Gamma.

Supports Hebrew (RTL) and English (LTR) PRDs.

## Usage

```
/prd-slides PRD-TeacherTask.md
/prd-slides PRD-TeacherTask.md investors
/prd-slides PRD-MyProduct.md "engineering team" en
```

## What You Get

A Gamma presentation with slides covering:
- Problem & goals
- Target audience & personas
- Key features (one slide per category)
- Success metrics (KPIs)
- Roadmap
- Risks (for internal audiences)
- Open questions

## Workflow

### Step 1: Clarify
- Ask for the PRD file path if not provided
- Ask who the audience is (default: general stakeholders)
- Ask for language preference if not clear from PRD content (Hebrew / English)

### Step 2: Parse PRD
- Read the PRD file
- Extract all relevant sections
- Map each section to the appropriate slide

### Step 3: Generate
- Build the slide structure
- Call Gamma MCP to generate the presentation
- Return the Gamma link + slide summary

### Step 4: Confirm
- Ask if any slide needs adjustment
- Offer to regenerate specific slides with different depth or focus
