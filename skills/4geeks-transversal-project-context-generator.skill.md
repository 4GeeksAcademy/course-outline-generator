---
name: 4geeks-transversal-project-context-generator
description: Generates CONTEXT.md files for one or more company scenarios for a 4Geeks Academy transversal project milestone. A CONTEXT file is the company-specific document a student reads before implementing their milestone — it provides the real-world domain data (event schemas, KPIs, entity tables, seed instructions, restrictions) that turns a generic README into a concrete assignment. Requires an existing README for the milestone as input. Use this skill when adding a new company scenario to an existing milestone, when onboarding a new sector into the transversal project, or when generating context files after a README has already been written. Trigger on phrases like "generate the context for [company]", "add a new company to milestone N", "create CONTEXT files for this README", "generate CONTEXT for [sector] scenario", or when a user provides a README and one or more company descriptions. Do NOT use this skill to generate READMEs — use 4geeks-transversal-readme-generator for that.
---

# 4Geeks Academy — Transversal Context Generator

Generates `CONTEXT-[slug].md` files for one or more company scenarios against an existing milestone README. Each CONTEXT file is a self-contained operational document the student reads before writing any code — it translates the generic requirements of the README into the specific domain language of their assigned company.

---

## Step 1 — Collect Required Inputs

Confirm all inputs before generating. If any are missing, ask for all of them at once.

| Input                 | Description                                                                                                                                                                                                                                                                       | Default                           |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| `existing_readme`     | The milestone README to generate context for — **must be read in full**                                                                                                                                                                                                           | — Must ask —                      |
| `company_description` | The canonical company profile document for this scenario — **must be read in full** before writing any section. Every CONTEXT file for every milestone of this company must derive from this single source of truth: name, departments, personnel, tone, and operational details. | — Must ask —                      |
| `company_scenarios`   | One or more company descriptions to generate CONTEXT files for                                                                                                                                                                                                                    | — Must ask —                      |
| `reference_context`   | An existing CONTEXT file from the same milestone, for parity calibration                                                                                                                                                                                                          | Optional but strongly recommended |

> When `reference_context` is provided, use it to calibrate section count, table density, bullet counts, and tone. The goal is that a student assigned to the new scenario has a structurally identical experience to one assigned to the reference.

---

## Step 2 — Read the README First

Before generating any CONTEXT file, read the provided README in full and extract:

1. **Domain-sensitive requirements** — anything the student needs company-specific data to implement (field names, entity types, KPI definitions, alert thresholds, seed schema).
2. **Implied CONTEXT structure** — how many event types does the README expect? How many KPIs? Does it mention an alert? A comparative view? A seed script? A restriction?
3. **The CONTEXT anchor text** — the exact warning in the README that tells students to use their CONTEXT file. Confirm it is present; if not, note it for the README author.

The README's implied structure is the authoritative template for all CONTEXT files generated in this session. It overrides the default CONTEXT structure below wherever they differ. A CONTEXT file that invents sections the README never references, or omits sections the README depends on, is broken.

---

## Step 3 — Parity Rules

Every CONTEXT file generated for the same milestone must be **structurally identical** to every other CONTEXT file for that milestone. Parity is not about identical content — it is about identical structure, density, and cognitive load.

| Element                          | Rule                                                            |
| -------------------------------- | --------------------------------------------------------------- |
| Section count and order          | Identical across all variants                                   |
| Event type count                 | Same in every variant                                           |
| Reference entity table row count | Same in every variant (±0)                                      |
| KPI count                        | Same in every variant                                           |
| KPI table columns                | Identical structure: KPI name, description, calculation formula |
| Alert count                      | One per variant                                                 |
| Alert JSON field names           | Identical across all variants                                   |
| Seed instruction bullet count    | Same in every variant                                           |
| Stakeholder message length       | Comparable across variants (3–4 sentences)                      |
| Specific restriction             | One per variant, comparable paragraph length                    |

### When an extra table is structurally necessary

Some domains require a lookup table others do not (e.g., SLA thresholds by service type, pipeline stage definitions, currency exchange reference). This is permitted only when the table is **functionally required** to implement a KPI or alert — meaning without it, the student would have to invent values. In that case, the exception is acceptable and does not need to be compensated with filler tables in other variants.

### Verifying parity

After generating all CONTEXT files, run this check before delivering:

- [ ] Same number of `##` sections across all variants
- [ ] Same number of event type rows
- [ ] Same number of reference entity rows
- [ ] Same number of KPI rows
- [ ] Same number of seed instruction bullets
- [ ] Stakeholder messages are comparable in length
- [ ] Restrictions are comparable in length and specificity

If any check fails, rewrite the offending section before delivering.

---

## Step 4 — CONTEXT File Structure

Every CONTEXT file follows this structure exactly, in this order. Section names and the intro block are fixed — do not rename or reorder them.

```
1. Title:  "CONTEXT.md — [Company Name]"
           "Milestone N: [Topic]"

2. Intro notice block  (identical in all variants — see template below)

3. ## Tu empresa
   2–3 sentences: what the company does, where it operates, size.

4. ## Tu departamento y el problema que debes resolver
   2–3 sentences: which department, what the current problem is, why it matters.

5. ## Tu stakeholder
   Name and role on a line, then their message in a blockquote (3–4 sentences).

   **Stakeholder naming rule:** Names must reflect international diversity across the full set of CONTEXT files for a given course. Do not cluster names by region. A reasonable distribution across a set of three scenarios might include names from the US, Spain, Portugal, Venezuela, and Argentina — but the exact mix should feel natural, not mechanical. Each individual file gets one stakeholder; the diversity is achieved across the collection.

6. ## Esquema de eventos
   Base JSON structure, then event type table, then reference entity table.

7. ## KPIs que debe mostrar tu dashboard
   Table: KPI name | Description | How to calculate

8. ## Alerta que debes implementar
   One paragraph describing the trigger condition, then the exact JSON structure.

9. ## Vista comparativa del dashboard
   One paragraph describing what dimension to break down and why it matters operationally.

10. ## Instrucciones para el seed
    Exactly N bullets — match count across all variants.
    Each bullet specifies a count, a distribution, or an edge case.

11. ## Restricción específica
    One paragraph describing a domain constraint that affects how data is displayed or stored.
```

### Intro notice block template

This block is word-for-word identical in every CONTEXT file for every milestone:

```markdown
> Este documento describe tu empresa y la situación concreta para la que estás construyendo este hito. Léelo completo antes de escribir ningún código. Todo lo que construyas debe reflejar este contexto.
```

### Event type table format

```markdown
| `event_type` | Descripción                | Campos en `metadata`                   |
| ------------ | -------------------------- | -------------------------------------- |
| `event_name` | What this event represents | `field1`, `field2 (value_a / value_b)` |
```

List valid enum values inline within the `metadata` column. Do not create a separate table for enums unless the list exceeds 5 values.

### KPI table format

```markdown
| KPI          | Descripción                        | Cómo calcularlo                          |
| ------------ | ---------------------------------- | ---------------------------------------- |
| **KPI name** | What it measures in plain language | Formula or data source in concrete terms |
```

### Alert JSON format

Always present the alert as a code block with exact field names. Field names must be identical across all variants for the same milestone.

````markdown
```json
{
  "alert_type": "snake_case_name",
  "entity_id": "string",
  "field_name": "value type and example",
  "threshold": value
}
```
````

```

### Seed instruction format

Each bullet must specify at least one concrete number, distribution, or boundary condition. Vague bullets like "add some events" are not acceptable.

✅ `Crea 25 procesos distintos con fechas de apertura en los últimos 90 días`
❌ `Añade varios procesos de selección`

The last bullet or second-to-last must always specify the edge case that triggers the alert, so the evaluator can confirm it fires.

---

## Step 5 — Bilingual Output

CONTEXT files are delivered in two stages:

**Stage 1 — Primary document (working language):** Generate the primary language version first and deliver it for review. Do not generate the translation until the primary document has been explicitly approved. The primary language is the working language of the course — typically Spanish, unless the user specifies otherwise.

**Stage 2 — Translation (after approval):** Once the primary document is approved, generate the translation. The translation must be a faithful, consistent rendering — same structure, same section order, same data. Do not add, remove, or reword content between versions.

Each file must include a translation notice written **in the language of the target document** — so a reader who does not understand the current document can still find the other version:

- In `CONTEXT-[slug].md` (English): `_Estas instrucciones están [disponibles en español](./CONTEXT-[slug].es.md)._`
- In `CONTEXT-[slug].es.md` (Spanish): `_These instructions are [available in English](./CONTEXT-[slug].md)._`

Place the translation notice immediately after the title block, before the intro notice block.

Name files using lowercase slugs with hyphens: `CONTEXT-nexova.md` / `CONTEXT-nexova.es.md`, `CONTEXT-trackflow.md` / `CONTEXT-trackflow.es.md`.

---

## Quality Self-Check Before Delivering

- [ ] Existing README was read in full before generating any CONTEXT file
- [ ] CONTEXT structure matches what the README implies — no invented sections, no missing sections
- [ ] All variants have the same number of sections, event types, entity rows, KPI rows, seed bullets
- [ ] Stakeholder messages are comparable in length across all variants
- [ ] Restrictions are comparable in length and specificity across all variants
- [ ] Every seed instruction bullet contains at least one concrete number, distribution, or boundary condition
- [ ] At least one seed bullet specifies the edge case that triggers the alert
- [ ] Alert JSON field names are identical across all variants
- [ ] Intro notice block is word-for-word identical in all variants
- [ ] Primary language document generated and delivered for review before translation begins
- [ ] Translation generated only after explicit approval of the primary document
- [ ] Translation is structurally identical to the approved primary — no added, removed, or reworded content
- [ ] Translation notice in `CONTEXT-[slug].md` is written in Spanish: `_Estas instrucciones están disponibles en español…_`
- [ ] Translation notice in `CONTEXT-[slug].es.md` is written in English: `_These instructions are available in English…_`
- [ ] Files named using lowercase slugs with hyphens
- [ ] Stakeholder names across all CONTEXT files for the course reflect international diversity — not clustered by region
- [ ] Every detail in the stakeholder section (name, role, message tone) is consistent with the provided `company_description`
```
