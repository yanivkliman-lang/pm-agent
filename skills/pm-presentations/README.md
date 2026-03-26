# pm-presentations

Presentation skills for Product Managers: convert PRDs into slides and PDFs with one command.

Supports **Hebrew (RTL)** and **English (LTR)** automatically.

## Skills (3)

- **prd-to-slides** — Convert a PRD into a full slide deck using Gamma, covering problem, solution, features, roadmap, and KPIs.
- **prd-to-pdf** — Export a PRD markdown file as a formatted PDF, preserving tables, RTL Hebrew, and all sections.
- **kickoff-presentation** — Build a focused 9-slide Kickoff presentation from a PRD: executive summary of the problem, solution space, and main tasks.

## Commands (3)

- `/prd-slides` — Convert a PRD into a Gamma slide deck for stakeholders.
- `/prd-pdf` — Export a PRD as a formatted PDF file.
- `/kickoff-deck` — Build a Kickoff meeting presentation from a PRD.

## Requirements

- **Gamma MCP** — must be installed and authorized for `/prd-slides` and `/kickoff-deck`
- **Python** — required for `/prd-pdf` (pandoc optional but preferred)

## Usage Examples

```
/prd-slides PRD-TeacherTask.md
/prd-slides PRD-MyProduct-EN.md investors en

/prd-pdf PRD-TeacherTask.md
/prd-pdf PRD-MyProduct-EN.md exports/product-prd.pdf

/kickoff-deck PRD-TeacherTask.md
/kickoff-deck PRD-TeacherTask.md "engineering team"
```

## Language Support

All three skills auto-detect the PRD language:
- Hebrew characters detected → RTL layout, Hebrew output
- English PRD → LTR layout, English output
- Override with explicit `language: he` or `language: en` argument
