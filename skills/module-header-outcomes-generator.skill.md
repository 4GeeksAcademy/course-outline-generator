---
name: module-header-outcomes-generator
description: Generates module guidelines from the AI Engineering syllabus with two outputs per module in both languages (Spanish and English): (1) short student header (target 3 lines per language, up to 5 only if strictly necessary, preferably plain text) and (2) professor outcomes guide focused on end-of-class evidence based on Thinking Framework, Best Practices, Patterns, and Anti-patterns. Use when asked to generate lineamientos por skill/día, cabeceras para estudiantes, o guía docente por resultados esperados.
---

# 4Geeks Academy - Module Header + Outcomes Guidelines Generator

This skill generates **two outputs per skill/day**:

1. **Student instructions** for module header use.
2. **Professor instructions** focused on **what must be achieved by the end of class**.

All outputs must be returned in **Markdown**.

---

## Mandatory Source of Truth

Before generating any output, you must consult this syllabus URL:

- <https://raw.githubusercontent.com/4GeeksAcademy/course-outline-generator/refs/heads/main/ai-engineering/syllabus.md>

Use it as the canonical source for:

- Skill/day title and scope.
- Theory content.
- Thinking Framework sections:
  - Thinking Development
  - Best Practices
  - Patterns
  - Anti-patterns
  - Constraints & Limitations

Do not invent concepts that are not present or clearly implied by the syllabus.

---

## When to Use This Skill

Use this skill when the user asks:

- "Genera los lineamientos de la skill X"
- "Haz cabecera para estudiantes y guía para profesor"
- "Lineamientos por módulo/día"
- "Instrucciones del módulo según syllabus"

---

## Output Contract

For each requested skill/day, generate exactly these sections:

```markdown
## Lineamientos - Skill X: [Nombre]

### Para estudiantes

### Español

[Texto corto para estudiantes]

---

### English

[Short student header]

### Para profesor

### Español

[Lineamientos]

---

### English

[Guidelines]
```

### 1) Student instructions (strict rules)

- Must be bilingual:
  - `### Español`
  - `### English`
- **Target: 3 lines per language**.
- **Allowed exception:** up to **5 lines per language** only if strictly necessary for clarity.
- Prefer **plain text** (avoid bullet lists unless explicitly requested).
- Must be motivating and clear.
- Must state:
  - What the student will learn.
  - What the student should be able to do by the end.
- Keep language simple and direct.
- Spanish and English versions must keep the same meaning.

### 2) Professor instructions (strict rules)

Must focus on **end-of-class outcomes** and be based on syllabus framework.

Include explicitly:

- **What concepts must be learned** (from theory + thinking development).
- **What the student should have reflected on** (criteria, trade-offs, decision-making).
- **What the student must be conscious of** (risks, constraints, quality criteria).
- **What the student must do** (observable actions in exercises/class).
- **What the student must avoid** (anti-patterns from syllabus).

The professor section must be bilingual:

- `### Español`
- `### English`

Both languages must keep the same meaning.

---

## Generation Workflow

1. Locate the target `Skill X` in the syllabus URL.
2. Extract:
   - Skill title and day/week context.
   - Theory bullets.
   - Thinking Framework content.
3. Draft student header text in Spanish (target 3 lines, plain text; up to 5 only if strictly necessary).
4. Translate student header to English preserving meaning (target 3 lines, up to 5 only if strictly necessary).
5. Draft professor outcome guide in Spanish.
6. Translate professor guide to English preserving meaning.
7. Return the final Markdown block.

---

## Quality Checklist

- [ ] Syllabus URL consulted.
- [ ] Student text includes both Spanish and English.
- [ ] Student text targets 3 lines per language; it may reach up to 5 only if strictly necessary.
- [ ] Student text is plain-text style and motivating.
- [ ] Professor text is outcome-focused (end of class).
- [ ] Professor text explicitly covers: learn, reflect, be aware, do, avoid.
- [ ] Anti-patterns are explicitly mentioned in "avoid".
- [ ] Professor text includes both Spanish and English.
- [ ] Output is valid Markdown.

---

## Notes

- If the syllabus has missing framework sections (`_Not introduced in this learnpack_`), infer only from available theory and explicitly avoid adding advanced assumptions.
- Keep professor guidance concrete and evaluable (observable outcomes).
