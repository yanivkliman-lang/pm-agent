---
description: Export a PRD markdown file as a formatted PDF document, preserving tables, RTL Hebrew, and all sections
argument-hint: "<path-to-PRD> [output-path]"
---

# /prd-pdf — PRD to PDF

Export your PRD markdown file as a clean, formatted PDF.

Supports Hebrew (RTL) and English (LTR) PRDs automatically.

## Usage

```
/prd-pdf PRD-TeacherTask.md
/prd-pdf PRD-TeacherTask.md exports/TeacherTask-PRD.pdf
/prd-pdf PRD-MyProduct-EN.md
```

## What You Get

A PDF file containing the full PRD with:
- Preserved Hebrew RTL or English LTR layout (auto-detected)
- Formatted tables (KPIs, roadmap, risks, pricing)
- Proper headings hierarchy
- Clean typography ready for sharing

## Workflow

### Step 1: Confirm Inputs
- Ask for PRD file path if not provided
- Confirm output path (default: same folder as PRD, `.pdf` extension)

### Step 2: Convert
Try conversion methods in order:
1. **pandoc** (best quality) — uses xelatex for full Unicode/Hebrew support
2. **Python + weasyprint** — generates PDF from HTML
3. **Python + markdown → HTML** (fallback) — generates HTML, user prints to PDF from browser

### Step 3: Report
- Confirm the output file path
- Report file size
- If HTML fallback was used, give clear print-to-PDF instructions

## Notes

- All PRD content is preserved — nothing is truncated
- Tables are rendered as proper HTML tables
- Font: Arial (supports both Hebrew and English)
