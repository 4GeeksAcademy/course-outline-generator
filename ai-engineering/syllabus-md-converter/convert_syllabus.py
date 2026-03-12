"""
Syllabus XLSX → Markdown Converter
===================================
Usage: python convert_syllabus.py <input.xlsx> <output.md>

Reads the "Planificación del programa" sheet from the Excel file
and produces a clean Markdown syllabus, excluding all projects and HITOs.
"""

import pandas as pd
import re
import sys


def safe_str(val):
    """Return stripped string or None if NaN/empty."""
    if pd.isna(val):
        return None
    s = str(val).strip()
    return s if s else None


def write_thinking_framework(row):
    """Build the Thinking Framework block from a row's columns."""
    sections = [
        ("Desarrollo de pensamiento", "Thinking Development"),
        ("Mejores Prácticas (segun la academia)", "Best Practices"),
        ("Patrones", "Patterns"),
        ("Anti patrones", "Anti-patterns"),
        ("Limitaciones", "Constraints & Limitations"),
    ]
    lines = ["", "### Thinking Framework", ""]
    for col, label in sections:
        val = safe_str(row[col])
        lines.append(f"#### {label}")
        lines.append(val if val else "_Not introduced in this learnpack_")
        lines.append("")
    return "\n".join(lines)


def is_project_only_content(content):
    """Return True if the content is purely project/practice (no theory)."""
    if not content:
        return False
    cl = content.strip().lower()
    skip_prefixes = [
        "> proyecto", "> práctica:", "práctica:", "> sólo práctica",
        "> prácticas:", "ejercicios de js", "se proveerá de una interfaz",
        "proyecto:", "proyecto 1:",
    ]
    if any(cl.startswith(p) for p in skip_prefixes):
        # But keep it if it also contains theory
        if "> teoría" in cl or "teoría" in content.split("\n")[0].lower():
            return False
        return True
    return False


def content_section_header(content):
    """Choose the ### header based on content prefix."""
    ct = content.strip()
    if ct.startswith(("> Teoría", "> Teoria", "Teoría", "Teoria")):
        return "### Teoría"
    if ct.startswith(("> Práctica", "> Practica")):
        return "### Práctica"
    return "### Content"


def determine_status(day_str, current_week):
    """Map the Day column value to a status string."""
    if "En Syllabus" in day_str:
        return "Aprobado" if current_week == 0 else "Approved"
    if "Approved" in day_str:
        return "Approved"
    if "Teoría pendiente" in day_str:
        return "Teoría pendiente aprobación"
    return None


def convert(input_path, output_path):
    df = pd.read_excel(input_path, sheet_name="Planificación del programa")

    # Drop columns that must be ignored entirely (may or may not be present)
    ignore_cols = [
        "Rúbrica (evaluación del proyecto)",
        "URLs de Learnpack",
        "Review Learnpack",
    ]
    df = df.drop(columns=[c for c in ignore_cols if c in df.columns])

    output = ["# Syllabus (Clean Extract)", ""]
    last_heading = None
    current_week = None  # track which week we're in for status mapping

    for i, row in df.iterrows():
        week_raw = row["Week"]
        day_raw = row["Day"]
        content = safe_str(row["Unnamed: 2"])
        day_str = safe_str(day_raw)

        # --- Classify the row ---

        # Detect numeric week
        week_is_number = False
        week_val = 0
        if pd.notna(week_raw):
            try:
                week_val = int(float(week_raw))
                week_is_number = True
            except (ValueError, TypeError):
                pass

        # 7. Empty / trailing rows
        if pd.isna(week_raw) and pd.isna(day_raw) and not content:
            continue
        if week_is_number and not content and pd.isna(day_raw):
            continue

        # 1. Section dividers
        if content and (content.startswith("---") or content.startswith("###")):
            continue

        # 5. HITO rows
        if isinstance(week_raw, str) and "HITO" in str(week_raw):
            continue

        # 4. Project rows (by Day column)
        if day_str and ("Proyecto pendiente" in day_str or "pendiente evaluación" in day_str):
            continue

        # 6. Orphan content rows (no week, no day)
        if pd.isna(week_raw) and pd.isna(day_raw) and content:
            # Attach theory orphans to the last heading if they look like theory
            if content.strip().startswith("> Teoría") or content.strip().startswith("> Teoria"):
                if last_heading:
                    output.append(last_heading)
                    output.append("")
                    output.append(content_section_header(content))
                    output.append("")
                    output.append(content)
                    output.append("")
                    output.append(write_thinking_framework(row))
            # Skip all other orphans
            continue

        # 2. Skill header rows
        if week_is_number and pd.notna(day_raw):
            day_val = str(day_raw)
            current_week = week_val
            heading = f"## Week {week_val} — Day {day_val}"
            last_heading = heading

            output.append(heading)
            output.append("")
            output.append("### Content")
            output.append("")
            if content:
                output.append(content)
            output.append("")
            output.append(write_thinking_framework(row))
            continue

        # 3. Theory / detail rows
        if day_str and ("En Syllabus" in day_str or "Approved" in day_str or "Teoría pendiente" in day_str):
            # Skip project-only content
            if is_project_only_content(content):
                continue
            if not content:
                continue

            status = determine_status(day_str, current_week or 0)

            if last_heading:
                output.append(last_heading)
                output.append("")

            if status:
                output.append(f"**Status:** {status}")
                output.append("")

            output.append(content_section_header(content))
            output.append("")
            output.append(content)
            output.append("")
            output.append(write_thinking_framework(row))
            continue

    # Assemble and clean
    text = "\n".join(output)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    text = text.rstrip() + "\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    # Stats
    section_count = text.count("\n## Week")
    line_count = text.count("\n")
    print(f"Done: {line_count} lines, {section_count} sections → {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} <input.xlsx> <output.md>")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])