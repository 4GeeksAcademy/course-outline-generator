---
name: 4geeks-module-guidelines-generator
description: Generates pedagogical guidelines (lineamientos) for the theoretical and practical content of each skill or module in 4Geeks Academy courses. Produces two texts per skill: (1) for students — friendly, motivating, with main learning aspects; (2) for professors — concrete, with emphasis on key concepts and the module project. Use when asked to "generate guidelines for module X", "create lineamientos for this skill", "write student and professor instructions for the module", "add pedagogical guidelines to the syllabus", or when preparing content briefs for each skill's theory and practice. Trigger on "lineamientos", "guidelines for students and teachers", "instrucciones para módulo", or "contenido teórico y práctico por skill".
---

# 4Geeks Academy — Module Guidelines (Lineamientos) Generator

This skill generates **two guideline texts per skill/module** for 4Geeks Academy: one aimed at **students** and one at **professors**. They frame the theoretical and practical content of each skill and connect it to the module project.

---

## Required Reference: Syllabus

**Before generating any guidelines**, you must read and use the syllabus as the source of truth for the program structure and for each skill:

- **Path:** `course-outline-generator/ai-engineering/syllabus.md` (relative to the project root) or `ai-engineering/syllabus.md` from within the course-outline-generator repo.
- **Purpose:** Use the syllabus to understand:
  - The exact name and position of each skill/milestone in the program.
  - The theory (Teoría) and thinking framework (Thinking Development, Best Practices, Patterns, Anti-patterns, Constraints) associated with that skill.
  - The sequence of topics and how the skill connects to previous and next content.
  - The project(s) or context referenced for that week/skill.
- **Usage:** When generating lineamientos for a given skill, locate that skill in the syllabus, extract its theory and framework, and align the student and professor guidelines with that content. Do not invent learning objectives or concepts that are not present or implied in the syllabus.

---

## When to Use This Skill

Use this skill when:

1. Adding or documenting a new skill or module in the syllabus
2. Creating "lineamientos" or content briefs for theory + practice per skill
3. Preparing student-facing and professor-facing instructions for a module
4. Standardizing how each skill explains its focus, main concepts, and project link
5. A user asks for "guidelines", "lineamientos", or "instrucciones para estudiantes y profesor" for a skill/module

**Do NOT use this skill to:**

- Generate project READMEs (use `4geeks-project-readme-generator` or `4geeks-transversal-project-readme-generator`)
- Generate CONTEXT files (use `4geeks-transversal-project-context-generator`)

---

## Required Inputs

Before generating, confirm you have (or ask for) the following. If any are missing, ask for **all missing items at once**.

- **`skill_name`** — Name of the skill or module. _Required._
- **`skill_type`** — Category: web-fundamentals, styling-ui, programming-logic, milestone. _Optional; helps tailor tone and focus._
- **`main_concepts`** — 3–5 core concepts this skill teaches. _Required._
- **`key_actions`** — 2–4 things the student should be able to do by the end (e.g. "maquetar una landing accesible", "escribir funciones TypeScript testeables"). _Required._
- **`project_name`** — Name or short description of the module project (e.g. "Artist landing", "Simple dashboard with Tailwind", "Cinema Seat Manager"). _Required._
- **`project_focus`** — What the project emphasizes (e.g. semantic structure, KPIs, edge cases). _Optional but recommended._
- **`language`** — `es` or `en` for the output language. _Default: `es`._

---

## Output: Two Texts per Skill

Always produce **two distinct texts** for the same skill.

### 1. Guidelines for Students (Lineamientos para estudiantes)

**Purpose:** Friendly, motivating, and clear. Highlight what they will learn and why it matters.

**Tone and style:**

- Second person (tú/vos or usted, according to course convention)
- Encouraging: "Al terminar deberías sentirte capaz de…", "No busques hacerlo perfecto a la primera"
- Emphasize understanding and steady progress over perfection
- Connect theory → small exercises → project in simple terms

**Required elements:**

1. **Opening:** What this skill is and what they will work on in the module.
2. **Goal:** What they should be able to do by the end (use `key_actions`).
3. **Flow:** Brief description of the path: concepts → guided practice → project application.
4. **Recommendations (optional but recommended):**
   - Take notes in their own words
   - Experiment beyond minimum instructions
   - Ask for feedback early (from instructor and peers) on clarity and good practices

**Length:** Short version ~80–120 words; extended version ~150–220 words. Prefer the short version unless the user asks for "extended" or "detailed" student guidelines.

**Template (Spanish — adapt to English if `language: en`):**

```markdown
En este módulo vas a trabajar la skill de **[NOMBRE DEL SKILL]**. El objetivo es que entiendas **para qué sirve en el mundo real**, practiques con **ejercicios guiados** y lo apliques en un **proyecto concreto**. Al terminar, deberías sentirte capaz de **[2–3 acciones clave]**. No busques hacerlo perfecto a la primera: **prioriza entender los conceptos, preguntar tus dudas y avanzar de forma constante**. El proyecto te ayudará a conectar la teoría con casos reales.
```

---

### 2. Guidelines for Professors (Lineamientos para profesor)

**Purpose:** Concrete and actionable. Emphasize what to stress in theory, how to run practice, and how everything ties to the project.

**Tone and style:**

- Direct, imperative or neutral third person
- Focus on: key concepts, common mistakes, evaluation priorities, and the project as the main application

**Required elements:**

1. **Theory focus:** List 3–4 **core concepts** to emphasize; avoid scattering attention.
2. **Real-world link:** Explicitly connect the skill to AI Engineering or professional use when relevant.
3. **Practice:** Start with small, observable exercises where typical errors can be spotted and corrected in group.
4. **Project link:** All practice should point toward the module project; state what "good" looks like (clarity, structure, naming, accessibility, performance, or logical correctness, as appropriate).
5. **Evaluation priorities:**
   - Understanding of key concepts over memorization
   - Ability to apply the skill in the project (not only ticking a technical checklist)
   - Use of good practices and meaningful comments where they add intent

**Length:** ~120–180 words per language. Dense and scannable (short paragraphs or bullet lists).

**Output structure — always deliver professor guidelines in both languages**, using this exact structure:

```markdown
### Español

<Lineamientos en español>

---

### English

<Lineamientos en inglés>
```

Generate the Spanish version first, then the English version. Both must convey the same content (same concepts, practice approach, project link, evaluation priorities); only the language changes.

---

## Workflow

1. **Consult the syllabus** — Read `course-outline-generator/ai-engineering/syllabus.md` (or `ai-engineering/syllabus.md` from the repo root). Locate the skill or module for which you are generating guidelines. Extract the relevant theory (Teoría), thinking framework, and any project or context mentioned for that skill. Use this to align and ground the lineamientos.
2. **Gather inputs** — Confirm `skill_name`, `main_concepts`, `key_actions`, `project_name`, and optionally `skill_type`, `project_focus`, `language`. If the syllabus already defines these, use it; otherwise ask the user for missing items.
3. **Choose skill type** — If `skill_type` or project name suggests a known pattern, use the corresponding example focus:
   - **Web (HTML/CSS/SEO/accessibility):** semantics, accessibility basics, on-page SEO; justify structural and UX decisions.
   - **Tailwind / dashboards:** utility-first, dashboard structure (KPI / drivers / operational), information design; mobile/responsive.
   - **Programming / TypeScript:** types, control flow, edge cases, small testable functions; TDD-light, tracing algorithms, clarity and correctness.
4. **Generate student guidelines** — Apply the student template; fill in skill name, key actions, and optional recommendations. Keep tone friendly and motivating. Ensure alignment with the theory and framework from the syllabus.
5. **Generate professor guidelines** — Apply the professor template; fill in core concepts, practice approach, project link, and evaluation priorities. Base these on the syllabus content for this skill. **Always output professor guidelines in the bilingual structure:** first "### Español" with the Spanish text, then "---", then "### English" with the English text. Both versions must convey the same content.
6. **Deliver both texts** — Present clearly labeled: "Para estudiantes" and "Para profesor". For "Para profesor", use the structure with ### Español, separator, ### English. If the user requested a specific format (e.g. Markdown section, JSON, copy-paste block), follow it.

---

## Skill-Type Examples (Reference)

Use these as reference when tailoring guidelines; do not copy verbatim unless the skill matches exactly.

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

## Quality Self-Check Before Delivering

- [ ] Syllabus (`ai-engineering/syllabus.md`) was consulted; guidelines align with the skill’s theory and thinking framework as defined there
- [ ] Both texts generated (student + professor) for the same skill
- [ ] Student text: friendly, motivating, includes goal and key actions
- [ ] Professor text: concrete, includes theory focus, practice approach, project link, evaluation priorities
- [ ] Professor guidelines delivered in the bilingual structure: ### Español, content, ---, ### English, content (same content in both languages)
- [ ] No mixed audience: one text is clearly "para estudiantes", the other "para profesor"
- [ ] Skill name, project name, and main concepts reflected correctly in both texts
- [ ] If language was specified for student guidelines, that language is used; professor guidelines are always in both Spanish and English
- [ ] Length within suggested ranges (student short ~80–120 words unless extended requested; professor ~120–180 words per language)

---

## Output Format Suggestion

Present the result in a single block. For **Para profesor**, always use the bilingual structure (Español first, then English):

```markdown
## Lineamientos — [Nombre del skill]

### Para estudiantes

[Texto generado en el idioma solicitado.]

### Para profesor

### Español

[Lineamientos en español.]

---

### English

[Lineamientos en inglés.]
```

If the user needs integration into a platform (e.g. fields in a CMS or learn.json), offer a compact version or key-value structure (e.g. `guidelines_student`, `guidelines_professor_es`, `guidelines_professor_en`) upon request.
