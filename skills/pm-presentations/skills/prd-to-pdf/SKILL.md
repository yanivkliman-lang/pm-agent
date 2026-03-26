---
name: prd-to-pdf
description: "Convert a PRD markdown file into a formatted PDF document. Use when the user wants to export or share the PRD as a PDF file."
---

# PRD to PDF

You are a document formatting specialist. Your job is to convert a PRD markdown file into a clean, professional PDF document.

## Purpose

Export the PRD as a PDF file, preserving all formatting, tables, and Hebrew RTL text — ready to share with stakeholders who don't have access to markdown viewers.

## Input

- `$PRD_FILE`: Path to the PRD markdown file (e.g., `PRD-TeacherTask.md`)
- `$OUTPUT_PATH`: Optional — where to save the PDF. Default: same folder as the PRD file, with `.pdf` extension
- `$LANGUAGE`: Optional — `he` for Hebrew (RTL), `en` for English (LTR). Default: auto-detect from PRD content

## Language Detection

Before converting, detect the PRD language:
- If the PRD contains Hebrew characters (א-ת) → apply RTL CSS (`direction: rtl`), use a font with Hebrew support (Arial)
- If the PRD is in English → apply LTR CSS (`direction: ltr`), standard font
- If `$LANGUAGE` is explicitly provided → use that

## Process

### Step 1: Determine Output Path

If `$OUTPUT_PATH` is not provided, derive it from `$PRD_FILE`:
- Example: `PRD-TeacherTask.md` → `PRD-TeacherTask.pdf`
- Save in the same directory as the source file

### Step 2: Try Conversion Methods (in order)

Try each method below until one succeeds:

#### Method A: Pandoc (preferred)

For Hebrew PRDs:
```bash
pandoc "$PRD_FILE" -o "$OUTPUT_PATH" \
  --pdf-engine=xelatex \
  -V mainfont="Arial" \
  -V lang=he \
  -V dir=rtl \
  -V geometry:margin=2cm
```

For English PRDs:
```bash
pandoc "$PRD_FILE" -o "$OUTPUT_PATH" \
  --pdf-engine=xelatex \
  -V mainfont="Arial" \
  -V lang=en \
  -V geometry:margin=2cm
```

If pandoc is not available, try Method B.

#### Method B: Python with markdown + weasyprint
```python
import markdown
from weasyprint import HTML
import sys

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    content = f.read()

lang_dir = "rtl" if is_hebrew else "ltr"
lang_code = "he" if is_hebrew else "en"

html_content = f"""<!DOCTYPE html>
<html dir="{lang_dir}" lang="{lang_code}">
<head>
<meta charset="utf-8">
<style>
  body {{ font-family: Arial, sans-serif; direction: {lang_dir}; margin: 2cm; line-height: 1.6; }}
  h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 8px; }}
  h2, h3 {{ color: #34495e; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
  th, td {{ border: 1px solid #bdc3c7; padding: 8px 12px; text-align: {("right" if is_hebrew else "left")}; }}
  th {{ background-color: #ecf0f1; font-weight: bold; }}
  code {{ background: #f8f9fa; padding: 2px 4px; border-radius: 3px; }}
  blockquote {{ border-right: 4px solid #3498db; padding-right: 1em; color: #555; }}
</style>
</head>
<body>
{markdown.markdown(content, extensions=['tables', 'fenced_code'])}
</body>
</html>"""

HTML(string=html_content).write_pdf(sys.argv[2])
print(f"PDF saved to: {{sys.argv[2]}}")
```

Run:
```bash
python convert_prd.py "$PRD_FILE" "$OUTPUT_PATH"
```

#### Method C: Python with markdown to HTML (fallback — user prints to PDF)
If neither pandoc nor weasyprint is available:
```python
import markdown
import sys

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    content = f.read()

html_output = sys.argv[2].replace('.pdf', '.html')
html_content = f"""<!DOCTYPE html>
<html dir="rtl" lang="he">
<head>
<meta charset="utf-8">
<title>PRD</title>
<style>
  body {{ font-family: Arial, sans-serif; direction: rtl; max-width: 900px; margin: 2cm auto; line-height: 1.6; }}
  h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 8px; }}
  h2, h3 {{ color: #34495e; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
  th, td {{ border: 1px solid #bdc3c7; padding: 8px 12px; text-align: right; }}
  th {{ background-color: #ecf0f1; font-weight: bold; }}
</style>
</head>
<body>
{markdown.markdown(content, extensions=['tables', 'fenced_code'])}
</body>
</html>"""

with open(html_output, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML saved to: {{html_output}}")
print("To convert to PDF: open the file in Chrome and use File → Print → Save as PDF")
```

### Step 3: Verify and Report

After conversion:
- Confirm the output file exists and report its path
- Report the file size
- If Method C was used (HTML fallback), give the user clear instructions to print to PDF from the browser

## Output

Tell the user:
1. The full path to the generated PDF (or HTML if fallback)
2. Which method was used
3. Any warnings (e.g., fonts, RTL rendering notes)

## Important Notes

- Always preserve Hebrew text and RTL direction
- Tables must be preserved — they contain critical data (KPIs, roadmap, risks)
- Never truncate content — include all sections of the PRD
