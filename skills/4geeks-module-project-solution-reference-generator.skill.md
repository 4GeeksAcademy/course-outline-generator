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

The goal is for **every project to have exactly one canonical solution**, stored under the `.learn/solution/` folder (together with its README) and linked from `learn.json` via the `solution` attribute, so that:

- Students can compare their submissions with the key aspects covered by the reference solution.
- An LLM can use the reference to evaluate and contrast a student's submission.

## General Conventions

- **Location of the solution**: always inside a `.learn/solution/` folder at the project’s root.
  - Example: `projects/ai-engineering-syllabus/ai-eng-milestone-coding-fundamentals/.learn/solution/`
  - All solution files (TypeScript, HTML, CSS, etc.) must live inside this folder.
- **Mandatory README in the solution folder**:
  - Always create a **README** inside `.learn/solution/` that explains the reference solution.
  - The README must be `.md`.
  - The README must describe the structure of the solution, key decisions, and how the files inside `.learn/solution/` work together.
- **Linking from `learn.json`**: add a `solution` attribute whose value is the **full URL in the repository** of the main README of the solution (not a relative path).
  - Example inside the project’s `.learn/learn.json`:
    - `"solution": "https://github.com/ORG/REPO/blob/BRANCH/path/to/project/.learn/solution/README.md"`
- **One main solution entry point per project**:
  - The README in `.learn/solution/` acts as the canonical entry point and should link to any auxiliary files in the same folder (HTML, TS, CSS, etc.).
- **Language**: The solution README and any explanatory content (comments, prose in `.md`, visible copy in HTML) must **always be in English**, regardless of the project’s README or UI language. Code identifiers and literals follow the project’s requirements; human-readable text in the solution is English-only.

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

**Recommended paths inside `.learn/solution/`**:

- Main explanation: `.learn/solution/README.md` or `.learn/solution/README.html`
- HTML implementation (if applicable): `.learn/solution/solution.html`

### 2. Solution as code files (`.py`, `.js`, `.jsx`, `.ts`, `.tsx`, etc.)

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

**Recommended paths inside `.learn/solution/`**:

- Main explanation (mandatory): `.learn/solution/README.md`
- Code files (one or more): for example
  - `.learn/solution/solution.py`
  - `.learn/solution/solution.ts`
  - `.learn/solution/solution.js`
  - or more granular filenames like `.learn/solution/main.ts`, `.learn/solution/utils.ts`, etc.

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

**Recommended path inside `.learn/solution/`**:

- Main explanation: `.learn/solution/README.md`

## Steps to Create or Update a Project Solution

Always follow this workflow:

1. **Identify the project**
   - Locate the project’s root folder (e.g., `projects/ai-engineering-syllabus/ai-eng-milestone-coding-fundamentals/`).

2. **Check or create `.learn/` and `.learn/solution/`**
   - If `.learn/` doesn’t exist, create it at the root of the project (this is where `learn.json` lives).
   - Inside `.learn/`, create a `solution/` folder if it doesn’t exist.

3. **Choose the solution file types**
   - There must **always** be a README inside `.learn/solution/`:
     - Prefer `README.md` unless the project requires an HTML explanation (`README.html`).
   - For implementation files:
     - If the main deliverable is a web page or UI → create e.g. **`solution.html`** (and any CSS/JS files needed) inside `.learn/solution/`.
     - If a concrete script (Python/TypeScript) is required → create e.g. **`solution.py`** or **`solution.ts`** inside `.learn/solution/`.
     - If the key is to describe criteria, patterns, or aspects, this goes in `README.md` and you may include additional partial examples as separate files or snippets inside the README.

4. **Create the solution files**
   - Place **all solution-related files** in `.learn/solution/`, for example:
     - `.learn/solution/README.md` (mandatory)
     - `.learn/solution/solution.html`
     - `.learn/solution/styles.css`
     - `.learn/solution/solution.ts`
   - Ensure that:
     - The README explains the overall structure, key decisions, and how to interpret the implementation files.
     - The implementation files cover all **aspects to be evaluated** in the README and/or project context.
     - Everything is readable and sufficiently complete as a reference for students and LLMs.

5. **Link the solution in `learn.json`**
   - Open the project’s `.learn/learn.json`.
   - Add or update the `"solution"` attribute in the root object, or wherever project content metadata is located.
   - Use the **full URL to the README file in the repository** (no relative paths), for example:
     - `"solution": "https://github.com/ORG/REPO/blob/BRANCH/path/to/project/.learn/solution/README.md"`
     - `"solution": "https://github.com/ORG/REPO/blob/BRANCH/path/to/project/.learn/solution/README.html"`
   - Check that there aren’t multiple `solution` attributes with different URLs for the same project; if so, unify them.

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
- [ ] Is there a `.learn/solution/` folder at the project root?
- [ ] Is there a **README** inside `.learn/solution/` (preferably `README.md`) that explains the solution?
- [ ] Do all implementation files for the reference solution live inside `.learn/solution/` (e.g., `.ts`, `.html`, `.css`, etc.)?
- [ ] Does the README cover all aspects to be evaluated as described in the README/context?
- [ ] Does `.learn/learn.json` have a `"solution"` attribute pointing to `.learn/solution/README.*`?
- [ ] Is the `solution` attribute’s path correct and relative to the project root?
- [ ] Is the solution (README + files) clear and useful as a reference for students and LLMs?
- [ ] Is all human-readable content in the solution (comments, prose, copy) in English?
