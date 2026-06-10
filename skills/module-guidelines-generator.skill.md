---
name: module-guidelines-generator
description: Generates debate-first pedagogical guidelines (lineamientos) per module/day, **content-first**: theory topics from the syllabus CSV drive every section; the day’s project is referenced only as the application/deliverable hook. Produces two bilingual texts per skill: (1) students — short motivating header (3–5 lines, plain text) + 1–2 preview questions ("before class"); (2) professors — compact hybrid debate kit delivered as plain Markdown (copy-paste ready with headings/lists intact), with concise Summary (ends with class checkpoint), Debate pacing, opening/closing, and 5 dimension subsections (Learn/Reflect/Be aware of/Do/Avoid) with compact representative aspects + 1–2 Socratic reflexive questions per dimension, optional bridge, facilitator probes (Reflect/Avoid only), and Participation criteria. **MANDATORY:** run `syllabus-context-reader` (`parse_syllabus.py` on the planning CSV) before generating — never invent or assume day content. Use when asked to "generate guidelines for module X", "generate lineamientos", "generate guidelines", "student guidelines", "mentor guidelines", "class debate", "reflective questions", or "w8 d22". Trigger on "lineamientos", "teaching guide", "debate", "guidelines".
---

# 4Geeks Academy — Module Guidelines Generator

This skill generates **two bilingual guideline texts per skill/module**: one for **students** (short motivating header) and one for **professors** (outcome-focused teaching guide). Both are always delivered in **Spanish and English**. All outputs must be returned in **Markdown**.

## Content-first principle (mandatory)

Guidelines are **about the class content** — what students learn and discuss that day. The **project names the application context**; it does **not** replace or overshadow the theory plan.

| Priority                 | Source                                                                        | Role in guidelines                                                                                                       |
| ------------------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **1 — Primary**          | `content` **before** `---` (theory topics from CSV)                           | Drives summary, must-discuss, Learn/Reflect/Be aware of/Do/Avoid aspects, preview questions, opening/closing             |
| **2 — Framework**        | `how_to_think`, `best_practices`, `patterns`, `anti_patterns`, `limitaciones` | Shapes dimensions and facilitator probes                                                                                 |
| **3 — Application hook** | `content` **after** `---` (project definition)                                | Referenced in student “by end” line, summary project link, class checkpoint, closing — **not** the main debate narrative |

**Agent rule:** never generate guidelines without running `parse_syllabus.py` for the target week/day. Extract theory topics from parser output; **do not** write project-led guidelines that skip or underweight syllabus theory bullets.

**Bad (project-led):** debate centers on “Voice Agent” wiring while ignoring Pydantic validation, HTTP methods, or API docs listed in theory.

**Good (content-led):** debate centers on CRUD endpoints, Pydantic contracts, and API documentation; Voice Agent is where students apply those concepts.

### Chat delivery format (mandatory)

In the agent chat, **Students** and **Mentors** are delivered as copyable blocks (rendered Markdown in chat is not suitable for copying).

**Block titles (outside the fence)**

- Put a **visible heading before each copy block** so the user can identify what they are copying.
- Use these exact headings:
  - `#### Students — English`
  - `#### Students — Español`
  - `#### Mentors — English`
  - `#### Mentors — Español`
- Headings stay **outside** the code fence — never inside the copyable content.

**Students — plain text**

- After each Students heading, open a ` ```text ` fence containing **only** the student guideline text to copy (3–5 lines).
- No bullet lists or Markdown headings inside; natural Spanish (not literal).

**Mentors — plain Markdown**

**Mentor instructions must be delivered as plain Markdown**, ready to paste into CMS, Notion, Google Docs, or any platform **preserving formatting** (headings, lists, bold).

- Deliver the **Mentors** section inside a ` ```markdown ` fence containing **only** the teaching kit to copy — summary, debate pacing, dimensions, closing (e.g. starts with the summary paragraph or `### Debate pacing`).
- The fence must contain guideline content only: no block titles, no agent commentary, no copy instructions.
- Use only standard Markdown syntax: `#`–`####`, `-` lists / numbered lists, `**bold**` where applicable.
- The professor should be able to select **Mentors → English** or **Mentors → Spanish** and paste directly with visible formatting.
- **In agent chat (Cursor):** mandatory to deliver **four blocks** (or two if the user requests only one language/audience), each with its heading **before** the fence:
  - `#### Students — English` → ` ```text ` …
  - `#### Students — Español` → ` ```text ` …
  - `#### Mentors — English` → ` ```markdown ` …
  - `#### Mentors — Español` → ` ```markdown ` …
- Do not repeat Students or Mentors as rendered chat text only.
- Do not use disk files unless the user explicitly requests it.

**Example (agent chat layout):**

````markdown
#### Students — English

```text
You will learn...
```

#### Students — Español

```text
Aprenderás...
```

#### Mentors — English

```markdown
Students cover theory on...
**Class checkpoint:** ...
```

#### Mentors — Español

```markdown
Los estudiantes cubren teoría sobre...
**Checkpoint de la clase:** ...
```
````

---

## Source of Truth: Syllabus (via `syllabus-context-reader`)

**MANDATORY — before generating any output**, load syllabus context using the **`syllabus-context-reader`** skill:

- Skill path: `course-outline-generator/skills/syllabus-context-reader/SKILL.md`
- Follow its workflow end-to-end (run `scripts/parse_syllabus.py`; do **not** read the planning by hand).
- Cross-ref: use the parser workflow exactly as defined there (see its `scripts/parse_syllabus.py` extraction + `--include-prior` guidance). Do not re-implement JSON extraction inside this skill.

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
  --week <week> \
  --day <day> \
  --include-prior
```

Use the **AI Native Full Stack** CSV only when the user explicitly names that program.

### Map JSON output → guideline inputs

From `current` in the parser JSON:

| Parser field     | Use in guidelines as                                                                                                                                                                                                                                                          |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `skill`          | Skill name, scope, `skill_name`                                                                                                                                                                                                                                               |
| `content`        | **Split on `---`:** (1) **before** → `theory_topics`, `main_concepts`, `key_actions` — **primary** source for all debate dimensions; (2) **after** → `project_name`, `project_focus` — application hook only. Never let the project section override missing theory coverage. |
| `how_to_think`   | Thinking development → **Learn**, **Reflect**                                                                                                                                                                                                                                 |
| `best_practices` | **Be aware of**, evaluation priorities                                                                                                                                                                                                                                        |
| `patterns`       | **Do**, patterns to reinforce                                                                                                                                                                                                                                                 |
| `anti_patterns`  | **Avoid** (required; do not omit)                                                                                                                                                                                                                                             |
| `limitaciones`   | **Be aware of**, constraints in class and project                                                                                                                                                                                                                             |
| `week` + `day`   | Position in course (e.g. Week 8 — Day 22)                                                                                                                                                                                                                                     |

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

| Input           | Description                                                                                                                                            | Required                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| `skill_name`    | Name of the skill or module                                                                                                                            | Required                     |
| `skill_type`    | Category: `web-fundamentals`, `styling-ui`, `programming-logic`, `milestone`                                                                           | Optional — helps tailor tone |
| `theory_topics` | Core theory topics covered in class (extracted from `content`, before the `---` separator) — **primary input**; must be parsed from CSV before writing | Required                     |
| `main_concepts` | 3–5 core concepts this skill teaches                                                                                                                   | Required                     |
| `key_actions`   | 2–4 things the student should be able to do by the end                                                                                                 | Required                     |
| `project_name`  | Name or short description of the module project(s) — **application hook only**                                                                         | Required                     |
| `project_focus` | What the project emphasizes — used to link theory to deliverable, not to replace theory                                                                | Optional but recommended     |

If the parser output already provides these values, extract them from `current` (theory topics and project details both live in `content`); ask the user only for items still missing after the CSV extraction.

---

## Output: Two Bilingual Texts per Skill

Always produce **two distinct texts** for the same skill. Both must be **bilingual (Spanish and English)** regardless of any language preference.

---

### 1. Student Guidelines (Lineamientos para estudiantes)

**Purpose:** A short, motivating class opener in natural language that tells students **what theory content they will cover**, what they should be able to do by the end **applied in the day’s project**, and includes 1–2 preview questions grounded in **syllabus theory topics** (not project mechanics alone).

**Rules:**

- **Content-first:** lead with theory topics from `content` (before `---`); name the project as the place to apply them — not as the sole subject of the opener.
- **Target: 3–5 lines per language. Maximum: 5 lines total**, including preview questions (inline, not bullet lists).
- **Plain text preferred** — avoid bullet lists unless explicitly requested.
- Motivating and clear; use second person (tú/vos or usted, per course convention).
- **Forward-looking tone** — students read this **before or at the start of class**; describe what they **will do/learn that day**, not what they are doing now. **Do not** require "Today you will…" / "Hoy vas a…" every time.
  - EN: use **"You will…"** (e.g. "You will create…", "You will learn…") and/or direct imperative (**"Create…"**, **"Build…"**). Optional: "By the end you will be able to…". Avoid present for the main action (not "You create…" / "You are building…").
  - ES: use **"Vas a…"** / **"Crearás…"** / **"Aprenderás…"** and/or imperative (**"Crea…"**, **"Construye…"**). Optional: "Al final podrás…". Avoid present for the main action (not "Creas…" / "Estás construyendo…").
- Must state: what the student **will** learn (**theory topics from syllabus**) + what they **will** be able to do by the end (applied in the project).
- Include **1–2 preview questions** students can reflect on before class — at least one must reference a **theory topic** from the CSV content plan, not only the project name.
- Encourage steady progress: "By the end you should feel capable of...", "Don't aim for perfection on the first try."
- Both language versions must convey the same meaning.
- Spanish must read as native classroom Spanish (not literal translation from English). Adapt phrasing and rhythm while preserving intent.

**Output structure:**

```markdown
### English

[Short student header — 3–5 lines, max 5]

---

### Spanish

[Short student text in Spanish — 3–5 lines, max 5, natural phrasing]
```

---

### 2. Professor Guidelines (Lineamientos para profesor)

**Purpose:** Debate-first teaching kit centered on **that day’s syllabus content**. Turn the 5 Thinking Framework dimensions into a reflexive discussion so students internalize _why_ each **theory concept** matters for excelling as an AI Engineer — with the project as proof of application.

**Rules:**

- **Content-first:** summary, must-discuss, dimension aspects, and reflective questions must trace to **theory bullets** in `content` (before `---`). Reference the project to show application and in the class checkpoint — do not make the project the only subject of debate.
- Direct, imperative or neutral third person.
- Structured debate flow (not one dense paragraph).
- Must explicitly address the following **5 outcome dimensions** as their own `####` subsections:
  1. **Learn**
  2. **Reflect**
  3. **Be aware of**
  4. **Do**
  5. **Avoid**
- Include (inside the kit):
  - **Content plan + project link / what good looks like:** enumerate or summarize **theory topics from the syllabus** first; then how those topics connect to the module project(s) and what applying both well looks like.
  - **Evaluation priorities:** understanding over memorization; application in the project over ticking checklists; meaningful intent.
  - **Class checkpoint line (#7):** the last line inside **Summary** tying debate outputs to both theory coverage and a concrete project deliverable.
- Questions must be **open-ended, Socratic** (no answer keys embedded).
- Keep it concise: **Summary ~45–60 words**; avoid long paragraphs.
- Per dimension, include aspects **inline in one compact paragraph** (no subsection title), using 1–3 short phrases/cases.
- Per dimension, include **1–2 reflective questions** (regular and milestone days).
- Under **Reflect** and **Avoid** only, add **facilitator probes (#3)** (1–2 bullets like `If they say X, ask Y`, `How could we use...`, `What if...`), grounded in `how_to_think` trade-offs and/or `anti_patterns`.
- **Milestone behavior:** when parser `current.is_milestone` is true, keep **1 question (max 2) per dimension** and emphasize demo/evaluation conversation over theory drill.
- Both language versions must convey the same content (Spanish/English parity).
- Spanish mentor text must sound natural for a real instructor (not literal translation); adapt syntax/idioms while preserving structure and intent.
- **Spanish mentor headings must be in Spanish** — do not leave English section titles in the Spanish kit. Use this mapping:

| English                                | Español                              |
| -------------------------------------- | ------------------------------------ |
| A summary                              | Un resumen                           |
| **Class checkpoint:**                  | **Checkpoint de la clase:**          |
| Debate pacing                          | Ritmo del debate                     |
| Bridge within the module (if applies)  | Puente dentro del módulo (si aplica) |
| Participation criteria                 | Criterios de participación           |
| Debate                                 | Debate                               |
| Opening — professional impact          | Apertura — impacto profesional       |
| Learn                                  | Aprender                             |
| Reflect                                | Reflexionar                          |
| Be aware of                            | Tener en cuenta                      |
| Do                                     | Hacer                                |
| Avoid                                  | Evitar                               |
| **Reflective questions:**              | **Preguntas reflexivas:**            |
| Facilitator probes:                    | Sondeos del facilitador:             |
| Closing — Excellence as an AI Engineer | Cierre — Excelencia como AI Engineer |

- **Mandatory plain Markdown delivery (mentor):** the teaching kit is returned as renderable Markdown when copy-pasted; not as agent prose or code block.
- Mentor output must be **plain Markdown copy-ready**: clean headings + lists only, no meta commentary, no decorative prefixes, no escaped formatting artifacts.

**Bridge — rules**

- Include **Bridge within the module** only when today's skill **directly continues** a lesson from the **same module** (same CSV module block, e.g. between `### MODULE NAME ###` markers or equivalent section in `content`).
- **Do not** bridge across modules or hitos (e.g. do not link "Working with AI coding agents" to "Next.js APIs" unless they share the same module block).
- If there is no same-module continuity, **omit the Bridge section entirely** (do not leave an empty "if applies").
- When bridging, reference the **prior topic/skill in natural language** — never cite week/day (`w7 d21`, "day 21", "semana 8").
- Good EN: "From connecting frontend and data with APIs, now you govern how AI behaves across iterations."
- Good ES: "Tras conectar frontend y datos con APIs, ahora gobiernas cómo se comporta la IA en cada iteración."
- Bad: "From `w7 d21`…" / "Desde la semana 7 día 21…"

**Output structure (professor — paste as-is):**

```markdown
## English

[Summary (~45–60 words, covering theory topics + project link + evaluation priorities)]

**Class checkpoint:** [...]

### Debate pacing

[Suggested order, must-discuss, if-time, time guide]

### Bridge within the module (if applies)

[One bullet: prior topic → today's skill. Omit this whole section if not same module. No week/day references.]

### Participation criteria

- ... (3 bullets)

### Debate

#### Opening — professional impact

1. [...]

#### Learn

[Inline aspects sentence: 1–3 compact phrases/cases, no "Representative aspects" label]
**Reflective questions:**

1. ... (1–2)

#### Reflect

[Inline aspects sentence: 1–3 compact phrases/cases, no "Representative aspects" label]
**Reflective questions:**

1. ...
   Facilitator probes:

- If they say X, ask Y

#### Be aware of

...

#### Do

...

#### Avoid

...
Facilitator probes:

- If they say X, ask Y

### Closing — Excellence as an AI Engineer

1. [...]

---

### Spanish

... (Resumen)

**Checkpoint de la clase:** [...]

### Ritmo del debate

[...]

### Puente dentro del módulo (si aplica)

[Un bullet: tema previo → skill de hoy. Omitir sección entera si no es el mismo módulo. Sin referencias a semana/día.]

### Criterios de participación

- ... (3 bullets)

### Debate

#### Apertura — impacto profesional

1. [...]

#### Aprender

[Frase de aspectos en línea]
**Preguntas reflexivas:**

1. ...

#### Reflexionar

[...]
**Preguntas reflexivas:**

1. ...
   Sondeos del facilitador:

- Si dicen X, pregunta Y

#### Tener en cuenta

...

#### Hacer

...

#### Evitar

...
Sondeos del facilitador:

- ...

### Cierre — Excelencia como AI Engineer

1. [...]
```

---

## Workflow

1. **Load syllabus context (mandatory)** — Invoke **`syllabus-context-reader`**: read `SKILL.md`, run `parse_syllabus.py` with `--week`, `--day`, and **`--include-prior`**. Resolve week/day from the user request (e.g. `w8 d22` → `--week 8 --day 22`). If ambiguous, run `--list` or `--search` first; never guess from `syllabus.md`.
2. **Map parser JSON (content-first)** — Populate inputs from `current` (see table above). **First:** parse `content` before `---` into an explicit `theory_topics` list (every `+` / `-` bullet in the CSV theory block). **Second:** extract `project_name` / `project_focus` from after `---`. Derive `main_concepts` and `key_actions` from theory topics + `how_to_think`/`patterns`, not from project title alone. Treat `prior_skills` as prerequisites only (tone/expectations). Do not teach content from future days. **Stop** if parser was not run — do not generate from memory or `syllabus.md`.
3. **Internal: representative aspects per dimension** _(process-visible, result-hidden)_ — For each dimension (Learn/Reflect/Be aware of/Do/Avoid) derive **1–3 compact** aspects/cases from **theory topics first**, then render them as **one inline sentence** in final output (no subsection title):
   - Learn/Reflect: `content` (**theory topics before `---`**), `how_to_think`, `skill`
   - Be aware: `best_practices`, `limitaciones`, theory constraints in `content`
   - Do: `patterns` + **theory activities** in `content`; project application only as supporting example
   - Avoid: `anti_patterns` (**required; never omit**)
   - If a field is `null`, infer only from `content` + `skill`.
     Also run **Bridge check**: scan `prior_skills` + CSV module boundaries (`### … ###` in planning). Bridge **only** if the immediately relevant prior lesson is in the **same module** as today and sets up today's skill. Extract **topic label** from that prior `skill` (not week/day). If no same-module link, set bridge = omit.
   - **Hidden internal rule:** do not include this "Phase 2 analysis" in the final student/professor text; only carry the _selected_ aspects and resulting questions forward.
4. **Internal: debate questions kit** _(process-visible, result-hidden)_ —
   - Create **open-ended Socratic questions** from the representative aspects.
   - Regular days: **1–2 questions per dimension**.
   - Milestone days (`current.is_milestone` true): target **1 question (max 2) per dimension** (keep total questions small; emphasize "what good looks like").
   - Add exactly **1 opening** career-impact question (whole class).
   - Add exactly **1 closing** question tied to how decisions show up in both the theory content and the module project / next milestone.
   - **Quality bar:** prefer concrete scenarios from **syllabus theory topics** first, then project application or anti-patterns; avoid yes/no unless followed by "why"; questions must be discussable (trade-offs, "what if", production impact). At least **3 of 5** dimension aspect sentences must name a theory topic from the CSV content plan.
   - **Bilingual parity:** same intent in ES/EN.
   - **Translation quality bar:** do not perform literal ES<->EN translation; rewrite Spanish naturally for teaching context while preserving semantic intent.
5. **Generate student guidelines** — 3–5 lines per language, plain text, motivating, **forward-looking** ("You will…" / imperative; no mandatory "Today you will"). **Lead with theory topics from syllabus**; mention project as application. Add **1–2 preview questions** (inline, not bullet lists) grounded in content plan. Spanish must sound natural, not literal. In agent chat: heading `#### Students — English` / `#### Students — Español` **before** each ` ```text ` fence; fence contains only the student guideline text to copy.
6. **Generate professor guidelines (debate-first hybrid kit)** —
   - **Expected outcomes summary**: concise (**~45–60 words**), **name or summarize theory topics first**, then project link + evaluation priorities; end with **class checkpoint line** tying **content mastery** to a concrete project deliverable.
   - **Debate pacing (#1)**: order + must-discuss (**2–3 items from theory plan**, not project steps alone) + if-time + time guide (~45–60 min debate + practice).
   - **Bridge within the module** (from Bridge check): include section only when same-module continuity exists; one bullet referencing **prior topic** in natural language (EN/ES); never week/day codes.
   - **Participation criteria (#13)**: exactly 3 bullets.
   - **Opening**: opening career-impact question.
   - For each dimension: `####` section with **inline aspects sentence** (1-3 compact phrases/cases, no title) + **Reflective questions** (1-2). Under **Reflect** and **Avoid** add **Facilitator probes (#3)** (1-2 "If they say X, ask Y" probes; no answer keys).
   - Spanish mentor version must be adapted, fluent, and non-literal; **all section headings in Spanish** (see mapping table).
   - In agent chat: deliver with headings `#### Mentors — English` / `#### Mentors — Español` **before** each ` ```markdown ` fence; fence contains only the mentor kit to copy. Default; no disk files unless user asks.
   - For CMS paste: user copies block interior; headings, bullets, bold preserved on paste.
7. **Dedup pass (#5)** — Ensure no two questions across dimensions share the same intent. If overlap, merge, rephrase, or drop the weaker one.
8. **Deliver both texts** — Return a single Markdown block in the required output format with both languages and clear audience separation.

---

## Skill-Type Examples (Reference)

Use these to tailor tone and focus; do not copy verbatim. Each example is **content-led** (theory topics named first) with the project as application — match that pattern, not project-only narratives.

### Web fundamentals (HTML, CSS, SEO, accessibility)

- **Student:** You will build a professional landing page with HTML and CSS, focusing on semantic structure, visual hierarchy, accessibility, and SEO. By the end, you should be able to review structure, contrast, and headings with clear criteria, and apply correct tags in your project. Before class, reflect on this: which part of your HTML helps AI understand your page instead of just copying it?

- **Professor (mini kit):**
  - **Learn:** semantics + hierarchy. Question: what changes when you replace `div` with semantic tags for both humans and assistants?
  - **Reflect:** speed vs semantic quality trade-off. Question: when does "moving fast" create debt, and how would you justify slowing down?
  - **Be aware of:** contrast/alt text/headings. Question: what minimum criteria define "accessible enough" for this class stage?
  - **Do:** review structure via DOM/inspection tools. Question: what would you verify first before asking AI to rewrite markup?
  - **Avoid:** anti-patterns like "layout without semantics." Question: what would AI do if you let it pick tags by intuition without rules?
  - **Facilitator probes (Reflect/Avoid):** "If they say 'it doesn't matter,' ask about real accessibility/SEO impact"; "If they reduce SEO to keywords, ask about document structure."

### Tailwind and dashboards

- **Student:** You will design a Tailwind dashboard that organizes KPIs, drivers, and operational details so information becomes immediately clear. By the end, you should be able to justify your visual hierarchy and ensure responsive behavior in your project. Before class, reflect on this: which visual decision changes dashboard comprehension the fastest?

- **Professor (mini kit):**
  - **Learn:** information design (KPI/driver/operational layers). Question: why should layout follow decisions, not just components?
  - **Reflect:** density vs readability trade-off. Question: what would you cut first if the dashboard becomes unreadable on mobile?
  - **Be aware of:** contrast, spacing, and scanability. Question: which human metric would you use (time to understand, clarity, navigation quality)?
  - **Do:** repeatable component structure. Question: what rule would you write so AI does not alter layout "randomly"?
  - **Avoid:** style copy/paste without intent. Question: how do you detect when AI optimizes aesthetics but harms usability?
  - **Facilitator probes (Reflect/Avoid):** "If they only discuss colors, ask how quickly users can read KPIs (e.g., in 5 seconds)."

### Programming / TypeScript (logic, algorithms)

- **Student:** In this session, you will practice logic and algorithmic thinking with TypeScript to solve problems clearly and predictably. By the end, you should be able to implement small functions, cover edge cases, and explain why your data flow is correct. Before class, reflect on this: which edge case breaks your solution if ignored?

- **Professor (mini kit):**
  - **Learn:** control flow + types + data. Question: what minimum input/output information makes the algorithm deterministic?
  - **Reflect:** simplification vs edge-case coverage trade-off. Question: what would you decide if AI suggests a shortcut that reduces correctness?
  - **Be aware of:** edge cases and validation. Question: which business rule is hidden inside this edge case?
  - **Do:** testable, readable implementation. Question: what would you verify before accepting a PR?
  - **Avoid:** imperative coding without plan / ambiguous logic. Question: which anti-pattern appears when code "works" but is not maintainable?
  - **Facilitator probes (Reflect/Avoid):** "If they say 'it works,' ask for the smallest failing test"; "If they justify by intuition, ask for invariants."

### Working with coding agents (context, rules, memory bank)

- **Student:** You will prepare a project so a coding agent can work with real context: review the repo, create `.agents/rules`, and maintain a useful memory-bank so AI does not improvise blindly. By the end, you should be able to convert good and bad code patterns into clear working rules. Before class, reflect on this: which part of your current code would teach bad habits to a coding agent if undocumented?

- **Professor (mini kit):**
  - **Learn:** context engineering, rules (user vs project, globs, alwaysApply), and memory-bank. Question: when do many small contexts outperform one large context, and how does that affect cost and quality?
  - **Reflect:** implementation plan vs imperative prompt-by-prompt commands. Question: at what point does "moving fast with AI" break the plan, and how would you detect it in the repo?
  - **Be aware of:** file references, project structure, and business context (not only technical context). Question: what minimum information must live in `memory-bank` so a new agent does not hallucinate the product?
  - **Do:** fork project, commit by meaningful step, write `.agents/rules`, maintain `memory-bank`. Question: what would you validate in an agent summary against real code before trusting it?
  - **Avoid:** planless imperative development, "Global Dictator" rule overrides, ambiguous rules, blind trust in proactivity, dumping huge chat logs. Question: what happens when your rules are vague or leave too much autonomy to AI?
  - **Facilitator probes (Reflect/Avoid):** "If they say 'AI already knows,' ask which file proves it"; "If they want to override team rules, ask who pays that production cost."

### OpenClaw modules (personal assistants, integrations, security)

- **Student:** You will configure your first OpenClaw assistant on a VPS, set up `openclaw.json`, and connect it to Telegram to operate it safely. By the end, you should be able to assign concrete tasks without exposing secrets or giving full system access. Before class, reflect on this: what capability would you allow by default, and what would you deny by default?

- **Professor (mini kit):**
  - **Learn:** OpenClaw as an assistant that "knows nothing until taught"; model selection by task; API → skills/workflows. Question: why is installing OpenClaw not enough to get a useful agent without architecture?
  - **Reflect:** automation speed vs attack surface (MCP/integrations). Question: which integration should be connected first, and which should wait for stronger policies?
  - **Be aware of:** security risks, secrets handling, minimum permissions, and installation discipline. Question: which sensitive data must never remain in agent workspace/context?
  - **Do:** configure Telegram/MCP with bounded scope; transform an API into a reproducible skill. Question: how would you prove a correct execution without "trusting the chat transcript"?
  - **Avoid:** exposed keys, sensitive data access, full access permissions, assuming Zapier-MCP is the only path. Question: what happens if the agent gets write access to systems it should not touch?
  - **Facilitator probes (Reflect/Avoid):** "If they say 'connect everything,' ask for a tool allowlist"; "If they downplay security, ask for worst-case impact of one leaked key."

### Agent loop (Python, LLM + tools, observe-decide-act)

- **Student:** You will build a basic Python agent loop where the LLM decides, code executes, and tools act inside a controlled cycle. By the end, you should define objective, stop condition, and conversation logging (for example, CSV) to verify the agent actually solved the task. Before class, reflect on this: how do you know your loop ended by success and not because the model simply stopped trying?

- **Professor (mini kit):**
  - **Learn:** observe → decide → act → observe cycle; LLM/code/tool/loop roles. Question: which part of the flow must live in code instead of prompt?
  - **Reflect:** tool count vs agent clarity trade-off. Question: how many tools are too many for a class loop, and how would you measure that?
  - **Be aware of:** explicit objective, observable state, and finish condition. Question: which objective signal would you use to stop the loop without relying on "looks done"?
  - **Do:** build `.py` calling API via tools; persist CSV log (`actor`, `message`, `tool_call`, `timestamp`). Question: which CSV pattern would alert you to infinite looping or poorly defined tools?
  - **Avoid:** heavy logic inside tools, ambiguous tools, monolithic prompt, no stop condition. Question: what anti-pattern appears when one tool does everything and the LLM only "approves" it?
  - **Facilitator probes (Reflect/Avoid):** "If the prompt is 3 pages long, ask what should move to code"; "If there is no stop condition, ask for the test proving termination."

---

## Output Format

Present the result in a single block:

```markdown
# Guidelines — [Skill]

## Students

### English

[Student guidelines in English: header (3–5 lines, max 5) + 1–2 "before class" preview questions.]

---

### Spanish

[Student guidelines in Spanish: opener (3–5 lines, max 5), natural phrasing + 1–2 "before class" preview questions.]

## Mentors

> **Delivery rule:** everything under `## Mentors` must be **plain copyable Markdown** (not wrapped in code fences). The user pastes directly into their tool and headings/lists are preserved.

### English

[Professor guidelines in English — plain Markdown only: Summary (with class checkpoint) + Debate pacing + Opening + Learn/Reflect/Be aware of/Do/Avoid (inline aspects + questions, probes in Reflect/Avoid) + Bridge within module only if same module (topic-based, no w/d) + Closing + Participation criteria. No code fence around this block.]

---

### Spanish

[Professor guidelines in Spanish — same plain copyable Markdown format; **section headings in Spanish**; natural Spanish, not literal translation.]
```

**Chat delivery (default):** four copy blocks with visible headings **before** each fence — `#### Students — English`, `#### Students — Español`, `#### Mentors — English`, `#### Mentors — Español`. Each fence contains **only** the guideline content to copy. Do not rely on rendered chat text alone. Disk files only if user requests.

If the user needs integration into a platform (e.g. CMS fields or `learn.json`), offer a compact key-value structure (`guidelines_student_es`, `guidelines_student_en`, `guidelines_professor_es`, `guidelines_professor_en`) upon request — values still in plain Markdown for professor fields.

---

## Quality Self-Check Before Delivering

- [ ] **`syllabus-context-reader` used**: `parse_syllabus.py` ran with `--include-prior`; `syllabus.md` / GitHub URL **not** used as source; guidelines **not** generated from memory or guesswork.
- [ ] **Content-first**: theory topics from `content` (before `---`) drive summary, must-discuss, dimensions, and preview questions; project referenced as application hook, not sole narrative.
- [ ] Guidelines align with parser `current` (`skill`, `content`, `how_to_think`, `best_practices`, `patterns`, `anti_patterns`, `limitaciones`).
- [ ] Theory topics extracted from `content` (before `---`) and project details extracted from `content` (after `---`) — theory leads; project supports.
- [ ] At least **3 of 5** dimension aspect sentences and **2 of 3** must-discuss items name concrete theory topics from the CSV content plan.
- [ ] No content from days after the target day; tone matches `prior_skills`.
- [ ] Both texts generated (student + professor) for the same skill.
- [ ] Student text: 3–5 lines per language (max 5), plain text, motivating, **forward-looking** (EN: "You will…" and/or imperative; ES: "Vas a…" / "-arás" / imperative; no required "Today/Hoy").
- [ ] Student text states what the student **will** learn (theory topics) and what they **will** be able to do by end of class (applied in project).
- [ ] Student text is bilingual (### Español and ### English) with the same meaning and natural Spanish (non-literal).
- [ ] Professor text includes the summary (ending with class checkpoint line covering both content and project), Debate pacing, and Participation criteria (exactly 3 bullets).
- [ ] Professor text covers all 5 outcome dimensions as `####` subsections: Learn, Reflect, Be aware of, Do, Avoid.
- [ ] Anti-patterns explicitly mentioned under "avoid".
- [ ] Professor text includes content plan coverage + project link / what good looks like and evaluation priorities inside the summary.
- [ ] Professor text is bilingual (### Español and ### English) with the same content and natural Spanish adaptation (non-literal).
- [ ] Spanish mentor kit uses **Spanish section headings** (Resumen, Ritmo del debate, Aprender, Preguntas reflexivas, etc.) — no English titles in ES version.
- [ ] Bridge included **only** for same-module continuity; omitted when not applicable (no empty bridge).
- [ ] Bridge references **prior topic/skill**, never week/day (`w7 d21`, "día 21", etc.).
- [ ] Each copy block has a visible heading **before** the fence: `#### Students — English`, `#### Students — Español`, `#### Mentors — English`, `#### Mentors — Español`.
- [ ] Student content in chat: ` ```text ` fences per language contain **only** the student guideline text to copy.
- [ ] Mentor content in chat: ` ```markdown ` fences per language contain **only** the mentor kit to copy (no block titles, agent commentary, or copy instructions inside the fence).
- [ ] Student preview questions exist (1–2) inline in each language.
- [ ] Facilitator probes appear only under Reflect and Avoid, and never as full answer keys.
- [ ] Per dimension limits respected: aspects written inline (no title) with 1–3 compact phrases/cases; reflective questions 1–2.
- [ ] Milestone days (`is_milestone`) keep per-dimension questions to 1 (max 2) and emphasize demo/evaluation.
- [ ] No internal analysis / "Phase 2 analysis" appears in final student/professor text.
- [ ] No duplicate question intent across dimensions (dedup rule #5).
- [ ] No mixed audiences: one text is clearly for "Students", the other for "Mentors".
- [ ] Skill name, theory topics, project name, and main concepts reflected correctly in both texts.
- [ ] Output is valid Markdown.

---

## Manual spot-check (before committing this skill)

- Run the generator for **Week 8 Day 22**: verify `Debate pacing` exists, `Facilitator probes` appears under Reflect/Avoid, the summary ends with class checkpoint; **no Bridge** to week 7 (different module: "Working with AI coding agents" starts at w8); if bridging w8 d23 from d22, use topic labels only.
- Pick a **sparse day** from the CSV (null/empty `anti_patterns` or `limitaciones`): verify questions still exist, and Avoid/Be aware degrade gracefully without inventing concepts.
- Pick an **HITO / milestone day**: verify reduced per-dimension questions (target 1–2) and deliverable-focused Summary/opening/closing.
