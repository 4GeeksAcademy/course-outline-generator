# Syllabus Converter — Claude Project Setup

## What This Does

Converts the 4Geeks Academy syllabus Excel file (`syllabus.xlsx`) into a clean Markdown file (`syllabus.md`), excluding all projects and milestones (HITOs).

## Files in This Package

| File | Purpose | Where it goes in Claude |
|------|---------|------------------------|
| `system-prompt.md` | Custom instructions for Claude | Paste into **Project Instructions** |
| `CONVERSION-RULES.md` | Detailed conversion logic and rules reference | Upload as **Project Knowledge** |
| `convert_syllabus.py` | Standalone Python conversion script | Upload as **Project Knowledge** |
| `syllabus.md` | Current output (reference / baseline) | Upload as **Project Knowledge** |

## How to Set Up the Claude Project

1. **Go to** [claude.ai](https://claude.ai) → Projects → Create Project
2. **Set the project name** to something like `Syllabus XLSX→MD Converter`
3. **Open `system-prompt.md`**, copy its full contents, and paste them into the **Project Instructions** (system prompt) field.
4. **Upload these three files** as **Project Knowledge**:
   - `CONVERSION-RULES.md` — the conversion rules and row classification logic.
   - `convert_syllabus.py` — the tested Python script Claude will run.
   - `syllabus.md` — a concrete example of the expected output format.
5. **Done.**

## How to Use

1. Open a new conversation inside the project.
2. Upload your updated `syllabus.xlsx`.
3. Claude will produce and deliver the updated `syllabus.md` file — no extra prompting needed.
