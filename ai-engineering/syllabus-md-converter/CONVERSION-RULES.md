# CONVERSION-RULES.md — Syllabus Excel → Markdown

This document describes every rule needed to convert the 4Geeks Academy syllabus Excel file into the canonical `syllabus.md` format. Follow these rules exactly.

---

## 1. Excel Structure

**Sheet name:** `Planificación del programa`

**Columns (in order):**

| Column | Internal Name | Purpose |
|--------|--------------|---------|
| A | `Week` | Week number (int), `HITO XX` (string), or empty |
| B | `Day` | Day number (string), status label (string), or empty |
| C | `Unnamed: 2` | Main content: skill descriptions, theory, projects |
| D | `Desarrollo de pensamiento` | Thinking Development text |
| E | `Mejores Prácticas (segun la academia)` | Best Practices text |
| F | `Patrones` | Patterns text |
| G | `Anti patrones` | Anti-patterns text |
| H | `Limitaciones` | Constraints & Limitations text |
| I | `Rúbrica (evaluación del proyecto)` | Rubric (ignore entirely) |

---

## 2. Row Classification

Every row falls into exactly one of these categories. Classify top-down — the first match wins.

### 2.1 Section Dividers → SKIP
- Content starts with `---` (e.g., `--- PREWORK ---`)
- Content starts with `###` (e.g., `### CODING FUNDAMENTALS ###`)

### 2.2 HITO / Milestone Rows → SKIP
- `Week` column contains the substring `HITO` (e.g., `HITO 01`, `HITO 06`)

### 2.3 Project Rows → SKIP
- `Day` column contains `Proyecto pendiente` (any suffix: aprobación, evaluación)
- Content-only rows whose text starts with any of these prefixes (case-insensitive):
  - `> Proyecto`
  - `> Práctica:` or `> Prácticas:`
  - `> Sólo práctica`
  - `> Practica:`
  - `Práctica:` or `Prácticas:`
  - `Proyecto:` or `Proyecto 1:`
  - `Ejercicios de JS`
  - `Se proveerá de una interfaz`
- **Exception:** If a row's content contains BOTH project text AND theory text (e.g., starts with `> Proyecto` but also has `> Teoría` on a later line), keep the entire row — this is rare but possible.

### 2.4 Empty / Trailing Rows → SKIP
- All three key fields (`Week`, `Day`, `Unnamed: 2`) are empty/NaN.
- `Week` = 17 (or any week beyond the last real content) with no content.

### 2.5 Orphan Content Rows → SPECIAL HANDLING
- `Week` and `Day` are both empty, but `Unnamed: 2` has content.
- These are usually theory stubs attached to the **previous skill header row**.
- **Rule:** If the previous emitted section was a Skill Header, emit this as a detail section under the same `## Week N — Day D` heading. Otherwise, skip.

### 2.6 Skill Header Rows → EMIT
- `Week` is a number (int/float) AND `Day` is a number/string (not a status label).
- These define a new skill and produce TWO markdown sections (header + framework).

### 2.7 Detail / Theory Rows → EMIT
- `Day` contains one of: `En Syllabus`, `Approved`, `Teoría pendiente aprobación`
- These are the expanded content for the most recent Skill Header.
- They reuse the same `## Week N — Day D` heading.

---

## 3. Markdown Output Format

The output file starts with:

```
# Syllabus (Clean Extract)
```

### 3.1 Skill Header Section

For each **Skill Header Row** (category 2.6):

```markdown
## Week {week_int} — Day {day_value}

### Content

{content from Unnamed: 2 column}

### Thinking Framework

#### Thinking Development
{value from column D, or "_Not introduced in this learnpack_" if empty}

#### Best Practices
{value from column E, or "_Not introduced in this learnpack_" if empty}

#### Patterns
{value from column F, or "_Not introduced in this learnpack_" if empty}

#### Anti-patterns
{value from column G, or "_Not introduced in this learnpack_" if empty}

#### Constraints & Limitations
{value from column H, or "_Not introduced in this learnpack_" if empty}
```

### 3.2 Detail / Theory Section

For each **Detail Row** (category 2.7):

```markdown
## Week {same_week} — Day {same_day}

**Status:** {status}

### {section_type}

{content from Unnamed: 2 column}

### Thinking Framework

#### Thinking Development
{value or "_Not introduced in this learnpack_"}

#### Best Practices
{value or "_Not introduced in this learnpack_"}

#### Patterns
{value or "_Not introduced in this learnpack_"}

#### Anti-patterns
{value or "_Not introduced in this learnpack_"}

#### Constraints & Limitations
{value or "_Not introduced in this learnpack_"}
```

**Status mapping:**
- `Day` = `"En Syllabus"` → `**Status:** Aprobado`
- `Day` = `"Approved"` → `**Status:** Approved`
- `Day` = `"Teoría pendiente aprobación"` → `**Status:** Teoría pendiente aprobación`

**Section type detection** (from the content's first line):
- Starts with `> Teoría`, `> Teoria`, `Teoría`, or `Teoria` → `### Teoría`
- Starts with `> Práctica` or `> Practica` → `### Práctica`
- Anything else → `### Content`

### 3.3 Orphan Content Section

For **Orphan Rows** (category 2.5) that follow a Skill Header:

```markdown
## Week {previous_week} — Day {previous_day}

### Content

{content from Unnamed: 2 column}

### Thinking Framework

{...same sub-sections...}
```

---

## 4. Content Formatting Rules

- **Preserve newlines** inside cell content exactly as they appear. Excel stores them as `\n` within the cell.
- **Do NOT add `> Teoría:` prefix** if it already exists in the content. Output the content verbatim.
- **Do NOT wrap or reflow** long lines. Keep them as-is.
- **Blank lines:** Keep at most two consecutive blank lines. Collapse three or more into two.
- **No trailing empty sections.** If the last row produces a section with no meaningful content, omit it.

---

## 5. What to Ignore Entirely

- Column I (`Rúbrica`) — never read or output.
- All HITO rows — these are milestone/project markers.
- All project/práctica-only rows (see section 2.3).
- Section divider rows (see section 2.1).
- Any row with `Week` = 17 and no content (trailing placeholder).

---

## 6. Python Reference Implementation

Below is a tested Python script that performs this conversion. Use it as a reference or run it directly.

```python
import pandas as pd
import re

def convert_syllabus(excel_path, output_path):
    df = pd.read_excel(excel_path, sheet_name='Planificación del programa')

    def safe_str(val):
        if pd.isna(val):
            return None
        return str(val).strip()

    def write_tf(row):
        lines = []
        lines.append("")
        lines.append("### Thinking Framework")
        lines.append("")
        cols = [
            ('Desarrollo de pensamiento', 'Thinking Development'),
            ('Mejores Prácticas (segun la academia)', 'Best Practices'),
            ('Patrones', 'Patterns'),
            ('Anti patrones', 'Anti-patterns'),
            ('Limitaciones', 'Constraints & Limitations'),
        ]
        for col, label in cols:
            val = safe_str(row[col])
            lines.append(f"#### {label}")
            lines.append(val if val else "_Not introduced in this learnpack_")
            lines.append("")
        return "\n".join(lines)

    output = []
    output.append("# Syllabus (Clean Extract)")
    output.append("")

    last_heading = None
    last_skill_row_index = -1

    for i, row in df.iterrows():
        week = row['Week']
        day = row['Day']
        content = safe_str(row['Unnamed: 2'])
        day_str = safe_str(day)

        # 2.1 Skip empty rows
        if pd.isna(week) and pd.isna(day) and not content:
            continue

        # 2.1 Skip section dividers
        if content and (content.startswith('---') or content.startswith('###')):
            continue

        # 2.2 Skip HITO rows
        if isinstance(week, str) and 'HITO' in str(week):
            continue

        # 2.3 Skip project rows by Day column
        if day_str and ('Proyecto pendiente' in day_str or 'pendiente evaluación' in day_str):
            continue

        # 2.5 Handle orphan content rows
        if pd.isna(week) and pd.isna(day) and content:
            if last_skill_row_index == i - 1 or last_skill_row_index == i - 2:
                # Attach to previous skill header
                output.append(last_heading)
                output.append("")
                output.append("### Content")
                output.append("")
                output.append(content)
                output.append("")
                output.append(write_tf(row))
            continue

        # 2.4 Skip trailing rows
        week_is_number = False
        week_val = 0
        if pd.notna(week):
            try:
                week_val = int(float(week))
                week_is_number = True
            except (ValueError, TypeError):
                pass

        if week_is_number and week_val == 17 and not content:
            continue

        # 2.6 Skill header rows
        if week_is_number and pd.notna(day):
            day_val = str(day)
            heading = f"## Week {week_val} — Day {day_val}"
            last_heading = heading
            last_skill_row_index = i

            output.append(heading)
            output.append("")
            output.append("### Content")
            output.append("")
            if content:
                output.append(content)
            output.append("")
            output.append(write_tf(row))
            continue

        # 2.7 Detail / theory rows
        if day_str and ('En Syllabus' in day_str or 'Approved' in day_str or 'Teoría pendiente' in day_str):
            # 2.3 Skip project-only content
            if content:
                cl = content.strip().lower()
                skip_prefixes = [
                    '> proyecto', '> práctica:', 'práctica:', '> sólo práctica',
                    '> prácticas:', 'ejercicios de js', 'se proveerá de una interfaz',
                    'proyecto:', 'proyecto 1:'
                ]
                should_skip = any(cl.startswith(p) for p in skip_prefixes)
                if should_skip and '> Teoría' not in content and 'Teoría' not in content.split('\n')[0]:
                    continue

            if not content:
                continue

            # Status mapping
            if 'En Syllabus' in day_str:
                status = "Aprobado"
            elif 'Approved' in day_str:
                status = "Approved"
            elif 'Teoría pendiente' in day_str:
                status = "Teoría pendiente aprobación"
            else:
                status = None

            if last_heading:
                output.append(last_heading)
                output.append("")

            if status:
                output.append(f"**Status:** {status}")
                output.append("")

            # Section type
            ct = content.strip()
            if ct.startswith('> Teoría') or ct.startswith('> Teoria') or ct.startswith('Teoría') or ct.startswith('Teoria'):
                output.append("### Teoría")
            elif ct.startswith('> Práctica') or ct.startswith('> Practica'):
                output.append("### Práctica")
            else:
                output.append("### Content")
            output.append("")
            output.append(content)
            output.append("")
            output.append(write_tf(row))
            continue

    text = "\n".join(output)
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    text = text.rstrip() + '\n'

    with open(output_path, 'w') as f:
        f.write(text)

    return output_path
```

---

## 7. Verification Checklist

After generating the Markdown, verify:

- [ ] No `HITO` or milestone sections appear
- [ ] No project descriptions appear (no `> Proyecto`, no `Práctica:` standalone sections)
- [ ] No `#REF!` errors from Excel
- [ ] Week and Day numbers match the Excel exactly
- [ ] Skill numbers match the Excel exactly
- [ ] All theory content is present with its Thinking Framework
- [ ] The `_Not introduced in this learnpack_` placeholder appears for every empty framework sub-section
- [ ] No trailing empty sections at the end of the file
