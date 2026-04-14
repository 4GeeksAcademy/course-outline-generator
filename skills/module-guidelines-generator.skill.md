---
name: module-guidelines-generator
description: Generates pedagogical guidelines (lineamientos) for the theoretical and practical content of each skill or module in 4Geeks Academy courses. Produces two bilingual texts per skill (Spanish and English): (1) for students — short, motivating header (3–5 lines, plain text); (2) for professors — outcome-focused guide covering what students must learn, reflect on, be aware of, do, and avoid, plus project link and evaluation priorities. Use when asked to "generate guidelines for module X", "create lineamientos for this skill", "haz cabecera para estudiantes y guía para profesor", "lineamientos por skill/día", or "instrucciones del módulo según syllabus". Trigger on "lineamientos", "guidelines for students and teachers", "instrucciones para módulo", "cabecera de módulo", or "guía docente por resultados esperados".
---

# 4Geeks Academy — Module Guidelines Generator

This skill generates **two bilingual guideline texts per skill/module**: one for **students** (short motivating header) and one for **professors** (outcome-focused teaching guide). Both are always delivered in **Spanish and English**. All outputs must be returned in **Markdown**.

---

## Source of Truth: Syllabus

**Before generating any output**, fetch and read the syllabus from its canonical URL:

- <https://raw.githubusercontent.com/4GeeksAcademy/course-outline-generator/refs/heads/main/ai-engineering/syllabus.md>

Use it to extract, for the target skill:

- Exact skill name, day/week position, and scope.
- Theory content (Teoría).
- Thinking Framework sections: **Thinking Development, Best Practices, Patterns, Anti-patterns, Constraints & Limitations**.
- Project(s) or context referenced for that skill.

Do not invent learning objectives or concepts that are not present or clearly implied by the syllabus. If a Thinking Framework section is missing (`_Not introduced in this learnpack_`), infer only from the available theory and avoid adding advanced assumptions.

---

## When to Use This Skill

Use when:

1. Adding or documenting a new skill or module in the syllabus.
2. Creating "lineamientos" or content briefs for theory + practice per skill.
3. Preparing student-facing and professor-facing instructions for a module.
4. A user asks for "guidelines", "lineamientos", "cabecera de módulo", or "guía docente por resultados esperados".

**Do NOT use this skill to:**

- Generate project READMEs (use `project-readme-generator` or `transversal-project-readme-generator`).
- Generate CONTEXT files (use `transversal-project-context-generator`).

---

## Required Inputs

Confirm you have (or ask for) the following. If any are missing, ask for **all missing items at once**.

| Input           | Description                                                                  | Required                     |
| --------------- | ---------------------------------------------------------------------------- | ---------------------------- |
| `skill_name`    | Name of the skill or module                                                  | Required                     |
| `skill_type`    | Category: `web-fundamentals`, `styling-ui`, `programming-logic`, `milestone` | Optional — helps tailor tone |
| `main_concepts` | 3–5 core concepts this skill teaches                                         | Required                     |
| `key_actions`   | 2–4 things the student should be able to do by the end                       | Required                     |
| `project_name`  | Name or short description of the module project                              | Required                     |
| `project_focus` | What the project emphasizes (e.g. KPIs, edge cases, semantic structure)      | Optional but recommended     |

If the syllabus already provides these values, extract them from there; ask the user only for items not found in the syllabus.

---

## Output: Two Bilingual Texts per Skill

Always produce **two distinct texts** for the same skill. Both must be **bilingual (Spanish and English)** regardless of any language preference.

---

### 1. Student Guidelines (Lineamientos para estudiantes)

**Purpose:** A short, motivating header that tells the student what they will learn and what they should be able to do by the end.

**Rules:**

- **Target: 3 lines per language. Maximum: 5 lines**, only if strictly necessary for clarity.
- **Plain text preferred** — avoid bullet lists unless explicitly requested.
- Motivating and clear; use second person (tú/vos or usted, per course convention).
- Must state: what the student will learn + what they should be able to do by the end.
- Encourage steady progress: "Al terminar deberías sentirte capaz de…", "No busques hacerlo perfecto a la primera".
- Both language versions must convey the same meaning.

**Output structure:**

```markdown
### Español

[Texto corto para estudiantes — 3 líneas, máx 5]

---

### English

[Short student header — 3 lines, max 5]
```

---

### 2. Professor Guidelines (Lineamientos para profesor)

**Purpose:** Concrete, outcome-focused teaching guide. Emphasizes what must be achieved **by the end of class**, grounded in the syllabus Thinking Framework.

**Rules:**

- Direct, imperative or neutral third person.
- Dense and scannable (short paragraphs or bullet lists).
- Must explicitly address the following **5 outcome dimensions** (derived from the syllabus Thinking Framework):
  1. **Learn** — Concepts students must understand (theory + Thinking Development).
  2. **Reflect** — Criteria, trade-offs, and decisions students should have thought through.
  3. **Be aware of** — Risks, constraints, and quality criteria students must keep in mind.
  4. **Do** — Observable actions students must complete in exercises or during class.
  5. **Avoid** — Anti-patterns explicitly listed in the syllabus for this skill.
- Include:
  - **Project link:** how theory and practice connect to the module project; what "good" looks like (clarity, structure, accessibility, correctness, etc.).
  - **Evaluation priorities:** understanding over memorization; application in the project over ticking checklists; good practices and meaningful intent.
- **~120–180 words per language.**
- Both language versions must convey the same content.

**Output structure:**

```markdown
### Español

[Lineamientos para profesor — ~120–180 palabras]

---

### English

[Professor guidelines — ~120–180 words]
```

---

## Workflow

1. **Fetch the syllabus** — Read the canonical URL above. Locate the target skill. Extract: title, theory, Thinking Framework (Thinking Development, Best Practices, Patterns, Anti-patterns, Constraints).
2. **Gather inputs** — Confirm `skill_name`, `main_concepts`, `key_actions`, `project_name`. Use syllabus values where available; ask only for missing items.
3. **Choose skill type** — If `skill_type` or project name matches a known pattern, apply the corresponding focus (see Skill-Type Examples below).
4. **Generate student guidelines** — 3 lines per language (max 5), plain text, motivating. Same meaning in both languages. Deliver with `### Español` / `### English` structure.
5. **Generate professor guidelines** — Cover all 5 outcome dimensions + project link + evaluation priorities. ~120–180 words per language. Same content in both languages. Deliver with `### Español` / `### English` structure.
6. **Deliver both texts** — Present clearly labeled: "Para estudiantes" and "Para profesor". Follow the output format below.

---

## Skill-Type Examples (Reference)

Use these to tailor tone and focus; do not copy verbatim.

### Web fundamentals (HTML, CSS, SEO, accessibility)

- **Student:** Landing profesional, HTML semántico, CSS, accesibilidad y SEO; estructura clara, jerarquía visual, encontrable en buscadores y usable por todas las personas; práctica con etiquetas, títulos, contraste, alt text; proyecto: landing para artista.
- **Professor:** Enfatizar HTML semántico, accesibilidad (alt, contraste, teclado, ARIA solo si hace falta), SEO on-page (títulos, descripciones, estructura). Validar con DOM y herramientas básicas; justificar decisiones; evaluar semántica, accesibilidad mínima y SEO básico en el proyecto.

### Tailwind and dashboards

- **Student:** Interfaces limpias con Tailwind, dashboard con KPIs, drivers y detalles operativos; pensar en componentes y layouts; diseño responsivo; jerarquía visual, espaciado, tipografía.
- **Professor:** Utility-first, estructura de dashboards (KPI arriba, drivers en medio, operativo abajo); diseño de información. Que expliquen decisiones ("este color resalta KPIs"); revisar mobile/responsive; evaluar "se entiende rápido y es usable".

### Programming / TypeScript (logic, algorithms)

- **Student:** Lógica y pensamiento algorítmico con TypeScript; arrays, objetos, control de flujo, funciones; código predecible y testeable; casos borde; proyecto tipo Cinema Seat Manager o fundamentos de código.
- **Professor:** Tipos básicos, control de flujo y casos borde; funciones pequeñas y testeables. TDD ligero; que expliquen el algoritmo en voz alta; evaluar correctitud, casos límite y claridad del código en el proyecto.

---

## Output Format

Present the result in a single block:

```markdown
## Lineamientos — [Nombre del skill]

### Para estudiantes

#### Español

[Lineamientos para estudiantes en español.]

---

#### English

[Student guidelines in English.]

### Para profesor

#### Español

[Lineamientos para profesor en español.]

---

#### English

[Professor guidelines in English.]
```

If the user needs integration into a platform (e.g. CMS fields or `learn.json`), offer a compact key-value structure (`guidelines_student_es`, `guidelines_student_en`, `guidelines_professor_es`, `guidelines_professor_en`) upon request.

---

## Quality Self-Check Before Delivering

- [ ] Syllabus URL consulted; guidelines align with the skill's theory and Thinking Framework.
- [ ] Both texts generated (student + professor) for the same skill.
- [ ] Student text: 3 lines per language (max 5), plain text, motivating.
- [ ] Student text states what the student will learn and what they should be able to do.
- [ ] Student text is bilingual (### Español and ### English) with the same meaning.
- [ ] Professor text covers all 5 outcome dimensions: learn, reflect, be aware, do, avoid.
- [ ] Anti-patterns explicitly mentioned under "avoid".
- [ ] Professor text includes project link and evaluation priorities.
- [ ] Professor text is bilingual (### Español and ### English) with the same content.
- [ ] Professor text is ~120–180 words per language.
- [ ] No mixed audiences: one text is clearly "para estudiantes", the other "para profesor".
- [ ] Skill name, project name, and main concepts reflected correctly in both texts.
- [ ] Output is valid Markdown.
