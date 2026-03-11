---
name: project-solution-file
description: Define and maintain a canonical solution file per project under .learn/ and link it from the project's .learn/learn.json via a solution attribute. Use when creating or updating project solutions so students and LLMs can compare their work against a reference implementation.
---

# Project Solution File

## When to Use This Skill

Use this skill whenever:

- You are creating a new project that will be evaluated (milestones, guided or collaborative projects, etc.).
- You are adding or updating a reference solution for an existing project.
- You are checking that a project has its solution file properly linked in `.learn/learn.json`.

The goal is for **every project to have exactly one canonical solution file**, stored under the `.learn/` folder (together with `learn.json`) and linked from `learn.json` via the `solution` attribute, so that:

- Students can compare their submissions with the key aspects covered by the reference solution.
- An LLM can use the reference to evaluate and contrast a student's submission.

## General Conventions

- **Location of the solution file**: always inside a `.learn/` folder at the project’s root.
  - Example: `projects/ai-engineering-syllabus/ai-eng-milestone-coding-fundamentals/.learn/solution.html`
- **Linking from `learn.json`**: add a `solution` attribute with the path relative to the project root.
  - Example inside the project’s `.learn/learn.json`:
    - `"solution": ".learn/solution.html"`
    - `"solution": ".learn/solution.md"`
    - `"solution": ".learn/solution.py"`
- **One main solution file per project**:
  - If additional context is required (e.g., auxiliary files), keep those in `.learn/` as well and link them from the main file (HTML or MD).
- **Language**: The solution file content (comments, explanatory text, prose in `.md`, visible copy in HTML) must **always be in English**, regardless of the project’s README or UI language. Code identifiers and literals follow the project’s requirements; human-readable text in the solution is English-only.

## Allowed Types of Solution Files

### 1. Solution as an HTML View

**When to use**:

- When the expected output is a web page, landing page, interface, or HTML/CSS structure (with or without JS).

**Requirements**:

- Must be a **well-structured** HTML file, including:
  - Correct semantics (`header`, `main`, `footer`, `section`, `article`, etc.).
  - Optional comments only to clarify non-obvious decisions (don’t narrate every line).
  - The inclusion of all elements/attributes specifically assessed in the project:
    - Example: if the project requires schema.org for `Event`, `CreativeWork`, and `Person`, the solution must mark them accordingly.
- If the project evaluates accessibility or SEO:
  - Include the `lang` attribute in `<html>`, hierarchical headings (`h1`, `h2`, ...), key meta tags, alt text for images, etc.

**Recommended path**:

- `.learn/solution.html`

### 2. Solution as a code (`.py`, `.js`, `.jsx`, `.ts` or `.tsx`)

**When to use**:

- When the expected output is:
  - A script or module in a programming language such as Python, JavaScript, TypeScript or similar.
  - Automation logic, core business logic, data processing, standalone CLI tools, backend modules, or source code for compiled languages.

- _Supported solution file types_ include, but are not limited to:
  - Python: `.py`
  - JavaScript/TypeScript: `.js`, `.jsx`, `.ts`, `.tsx`
  - Bash or Shell: `.sh`
  - Other languages/formats as needed by the project specification.

**Requirements**:

- Must contain a **clear and readable implementation** that:
  - Solves the full target problem.
  - Uses data structures, algorithms, or patterns that serve as “model” examples for students.
  - Includes reasonable error handling or key validations, if required for grading.
- May include helper functions and, if useful, a small usage example (e.g., in Python, under `if __name__ == "__main__":`).

**Recommended path**:

- `.learn/solution.py` or `.learn/solution.ts` accordingly.

### 3. Solution as an Explanatory Document (`.md`)

**When to use**:

- When:
  - The exercise is very open and does not have a single correct implementation.
  - The most important thing is to specify the **aspects to be included** (visual, structural, or code), not provide a literal implementation.
  - You want to show **multiple valid solution alternatives** and explain why they are acceptable.

**What it should contain**:

- A clear description of:
  - **Expected visual aspects**:
    - Important CSS classes.
    - Required layouts (e.g., use of grid, flexbox, columns, responsive, dark mode, etc.).
  - **Code aspects**:
    - Recommended data structures.
    - Main algorithms or key logical steps.
    - Relevant design patterns (if applicable).
  - **Structural aspects**:
    - Proper organization of HTML.
    - Separation of concerns (files, modules, components).
    - Correct hierarchy and semantics.
- Where possible, include **small code snippets** highlighting key points, but a full line-by-line solution is not necessary.

**Recommended path**:

- `.learn/solution.md`

## Steps to Create or Update a Project Solution

Always follow this workflow:

1. **Identify the project**
   - Locate the project’s root folder (e.g., `projects/ai-engineering-syllabus/ai-eng-milestone-coding-fundamentals/`).

2. **Check or create `.learn/`**
   - If it doesn’t exist, create a `.learn/` folder at the root of the project (this is where `learn.json` and the solution file live).

3. **Choose the solution file type**
   - If the main deliverable is a web page or UI → **`solution.html`**.
   - If a concrete script (Python/TypeScript) is required → **`solution.py`** or **`solution.ts`**.
   - If the key is to describe criteria, patterns, or aspects → **`solution.md`**.
   - If unsure, prefer **`solution.md`** so you can:
     - Describe evaluation criteria.
     - Include partial examples (HTML, Python, or TypeScript) as sections.

4. **Create the solution file**
   - Place the file in `.learn/` with one of these names:
     - `solution.html`
     - `solution.md`
     - `solution.py`
     - `solution.ts`
   - Ensure that:
     - It covers all **aspects to be evaluated** in the README and/or project context.
     - It is readable and sufficiently complete as a reference for students and LLMs.

5. **Link the solution in `learn.json`**
   - Open the project’s `.learn/learn.json`.
   - Add or update the `"solution"` attribute in the root object, or wherever project content metadata is located.
   - Use a **path relative to the project root**, for example:
     - `"solution": ".learn/solution.html"`
     - `"solution": ".learn/solution.md"`
   - Check that there aren’t multiple `solution` attributes with different paths for the same project; if so, unify them.

6. **Review consistency**
   - Make sure that:
     - The `README` and milestone context describe the same elements that the solution implements.
     - There are no contradictions between requirements and the solution (e.g., README requires schema.org and the solution doesn’t include it).
     - If the project has multiple language versions (`README.md`, `README.es.md`), the solution is valid for all.

## Use by Students and LLMs

- **For students**:
  - The solution is **not for copy-paste**, but a reference:
    - To check if all assessed elements have been considered.
    - To see examples of recommended data structures, algorithms, or layouts.
  - Encourage comparing their submission with the solution and ask:
    - “Am I covering all the key points included in the solution?”
    - “Is my structure reasonably similar, even if the code isn’t identical?”

- **For LLMs**:
  - The solution serves as the **golden reference**:
    - To check if a student’s submission meets the minimal criteria.
    - To provide feedback based on the reference (without requiring exact text match).
  - When using this skill as an agent:
    - Read the `README`, milestone context, and `.learn/learn.json` first.
    - Use the `.learn/solution.*` file as the main reference for:
      - Validating the submission covers key aspects.
      - Suggesting improvements aligned with that solution.

## Quick Checklist

Before considering the project’s solution configuration as complete, check:

- [ ] Is there a `.learn/` folder at the project root (with `learn.json` inside)?
- [ ] Is there exactly one main solution file (`solution.html`, `solution.md`, `solution.py`, or `solution.ts`) inside `.learn/`?
- [ ] Does the solution file cover all aspects to be evaluated as described in the README/context?
- [ ] Does `.learn/learn.json` have a `"solution"` attribute pointing to `.learn/solution.*`?
- [ ] Is the `solution` attribute’s path correct and relative to the project root?
- [ ] Is the solution clear and useful as a reference for students and LLMs?
- [ ] Is all human-readable content in the solution (comments, prose, copy) in English?
