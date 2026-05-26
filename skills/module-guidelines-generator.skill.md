---
name: module-guidelines-generator
description: Generates pedagogical guidelines (lineamientos) for the theoretical and practical content of each skill or module in 4Geeks Academy courses. Produces two bilingual texts per skill (Spanish and English): (1) for students — short, motivating header (3–5 lines, plain text); (2) for professors — outcome-focused guide covering what students must learn, reflect on, be aware of, do, and avoid, plus project link and evaluation priorities. ALWAYS loads syllabus context via the syllabus-context-reader skill (CSV parser) before generating. Use when asked to "generate guidelines for module X", "create lineamientos for this skill", "haz cabecera para estudiantes y guía para profesor", "lineamientos por skill/día", "w8 d22", or "instrucciones del módulo según syllabus". Trigger on "lineamientos", "guidelines for students and teachers", "instrucciones para módulo", "cabecera de módulo", or "guía docente por resultados esperados".
---

# 4Geeks Academy — Module Guidelines Generator

This skill generates **two bilingual guideline texts per skill/module**: one for **students** (short motivating header) and one for **professors** (outcome-focused teaching guide). Both are always delivered in **Spanish and English**. All outputs must be returned in **Markdown**.

---

## Source of Truth: Syllabus (via `syllabus-context-reader`)

**MANDATORY — before generating any output**, load syllabus context using the **`syllabus-context-reader`** skill:

- Skill path: `course-outline-generator/skills/syllabus-context-reader/SKILL.md`
- Follow its workflow end-to-end (run `scripts/parse_syllabus.py`; do **not** read `syllabus.md`, a GitHub raw URL, or the CSV by hand).

**Do NOT** use these as primary sources:

- `course-outline-generator/ai-engineering/syllabus.md`
- <https://raw.githubusercontent.com/4GeeksAcademy/course-outline-generator/refs/heads/main/ai-engineering/syllabus.md>

**Official source:** `New Syllabus AI Engineer - Planificación del programa.csv` (or the AI Native Full Stack CSV when that program applies). `syllabus.md` is a derived export only — if it disagrees with the CSV, the CSV wins.

The parser normalizes week/day, merges multi-row content, and exposes prior skills.

### Required parser invocation

1. If week/day are unknown, run `--list` or `--search` (see `syllabus-context-reader`).
2. Always extract the target day with **`--include-prior`**:

```bash
python3 course-outline-generator/skills/syllabus-context-reader/scripts/parse_syllabus.py \
  --csv "course-outline-generator/ai-engineering/New Syllabus AI Engineer - Planificación del programa.csv" \
  --week <semana> \
  --day <día> \
  --include-prior
```

Use the **AI Native Full Stack** CSV only when the user explicitly names that program.

### Map JSON output → guideline inputs

From `current` in the parser JSON:

| Parser field     | Use in guidelines as                                                |
| ---------------- | ------------------------------------------------------------------- |
| `skill`          | Skill name, scope, `skill_name`                                     |
| `content`        | Theory, projects (`main_concepts`, `project_name`, `project_focus`) |
| `how_to_think`   | Thinking Development → **Learn**, **Reflect**                       |
| `best_practices` | **Be aware of**, evaluation priorities                              |
| `patterns`       | **Do**, patterns to reinforce                                       |
| `anti_patterns`  | **Avoid** (required; do not omit)                                   |
| `limitaciones`   | **Be aware of**, constraints in class and project                   |
| `week` + `day`   | Position in course (e.g. Week 8 — Day 22)                           |

From `prior_skills`: calibrate tone and prerequisites only — **do not** teach content from future days; **do not** assume knowledge beyond what `prior_skills` lists. Default parser mode is **smart** (prior milestones + last 15 regular lessons). If you need the full course history, re-run with `--prior-full`. Check `prior_skills_meta.total_prior` vs `returned`.

Do not invent learning objectives or concepts absent from the parser output. If a framework field is `null` or empty, infer only from `content` and `skill`; avoid advanced assumptions.

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

If the parser output already provides these values, extract them from `current` (and `content` for project details); ask the user only for items still missing after the CSV extraction.

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

1. **Load syllabus context (mandatory)** — Invoke **`syllabus-context-reader`**: read `SKILL.md`, run `parse_syllabus.py` with `--week`, `--day`, and **`--include-prior`**. Resolve week/day from the user request (e.g. `w8 d22` → `--week 8 --day 22`). If ambiguous, run `--list` or `--search` first; never guess from `syllabus.md`.
2. **Map parser JSON** — Populate `skill_name`, `main_concepts`, `key_actions`, `project_name`, `project_focus` from `current` and `prior_skills` (see table above).
3. **Gather inputs** — Ask only for fields still missing after step 2.
4. **Choose skill type** — If `skill_type` or project name matches a known pattern, apply the corresponding focus (see Skill-Type Examples below).
5. **Generate student guidelines** — 3 lines per language (max 5), plain text, motivating. Same meaning in both languages.
6. **Generate professor guidelines** — Cover all 5 outcome dimensions + project link + evaluation priorities. ~120–180 words per language. Ground **Avoid** in `anti_patterns` from the parser.
7. **Deliver both texts** — Present clearly labeled: "Para estudiantes" and "Para profesor". Follow the output format below.

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

- [ ] **`syllabus-context-reader` used**: `parse_syllabus.py` ran with `--include-prior`; `syllabus.md` / GitHub URL **not** used as source.
- [ ] Guidelines align with parser `current` (`skill`, `content`, `how_to_think`, `best_practices`, `patterns`, `anti_patterns`, `limitaciones`).
- [ ] No content from days after the target day; tone matches `prior_skills`.
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
