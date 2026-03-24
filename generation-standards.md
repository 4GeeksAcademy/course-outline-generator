# Course Outline Generation Standards

Comprehensive methodology for generating 4Geeks Academy course outlines.

---

## ⚠️ CRITICAL RULE - READ FIRST ⚠️

### ONE LEARNPACK = ONE `+` BLOCK (NO EXCEPTIONS)

**Each line starting with `+` in syllabus.md is a SEPARATE, INDEPENDENT learnpack.**

**PRE-GENERATION VERIFICATION CHECKLIST:**
- [ ] User specified EXACT `+` block name? (e.g., "HTML" not "Skill 1")
- [ ] Found the specific `+` line in syllabus.md?
- [ ] Extracted ONLY the `-` bullets under THAT `+` block?
- [ ] Stopped at the NEXT `+` line? (Did NOT continue past it)
- [ ] Confirmed ZERO content from other `+` blocks is included?
- [ ] Can quote the EXACT `+` line being used?

**If ANY box is unchecked, STOP and ask user for clarification.**

---

### Bad vs Good Examples

❌ **WRONG - Mixing Multiple `+` Blocks:**
```
User: "Generate Week 1 Skill 1"
Claude: [sees HTML + CSS + Accesibilidad under Skill 1]
Claude: [generates one massive course combining all three]
```

✅ **CORRECT - One `+` Block Only:**
```
User: "Generate Week 1 Skill 1"
Claude: "I found 3 separate learnapacks under Skill 1:"
        "1. + HTML"
        "2. + CSS"  
        "3. + Accesibilidad web"
        "Which ONE should I generate?"
User: "HTML"
Claude: [generates course using ONLY the bullets under + HTML]
```

❌ **WRONG - Assuming Which Block:**
```
User: "Generate the frontend basics course"
Claude: [picks random + block without asking]
```

✅ **CORRECT - Always Confirm:**
```
User: "Generate the frontend basics course"
Claude: "I found several learnapacks that could fit. Please specify the EXACT + block name from syllabus.md"
```

---

## Core Philosophy

**4Geeks Educational Principles:**
- **Vibecoding** (vibemanifesto.org): Iteration over perfection, practical learning over theory
- **Human-in-the-loop**: Collaboration between students and AI/instructors
- **Path of least resistance**: Teach simplest solutions first, add complexity only when needed
- **Autonomous problem-solving**: Develop student self-sufficiency
- **Attention to detail**: Cultivate careful reading and observation

**Target Audience:** Beginner developers (typically 18-35, universally accessible content)

---

## Structure Guidelines

### Lesson Count
**Quality-first principle:** The right number of lessons is the minimum that covers the material without losing depth. Every lesson must earn its place — if two lessons cover tightly related ideas that work better as one, merge them. If a lesson feels thin, it probably should be absorbed into its neighbor.

**Goal:** Match lesson count to actual teaching needs. Never default to a fixed number. Never pad to hit a range.

### Section Count
- **Total:** 5-9 sections (including Section 00 and final outro)
- **Section 00:** Welcome/Introduction (1 lesson)
- **Content sections:** Typically 2-5 lessons each. Sections with 2 lessons are acceptable when those two lessons form a tight, cohesive unit. Avoid sections with only 1 content lesson — that content should merge into an adjacent section.
- **Second-to-last section:** Assessment (includes 🧠 lesson)
- **Final section:** Outro/Conclusion (exactly 1 lesson only)

### Section Cohesion (HARD RULE)
Every section must have a **single teaching goal**. All lessons in that section must serve that goal. Apply this test:
- Can you describe the section's purpose in one sentence? If not, it's doing too much — split it.
- Does every lesson in the section clearly belong? If a lesson serves a different goal, move it to the section where it fits or create a new section.
- Do two adjacent sections cover the same goal? If so, they should be one section.

**This prevents three common problems:**
- Cramming unrelated topics into one section because they're "in the same area" (e.g., "adding skills to an agent" + "testing skills" + "composable architectures" are three different goals, not one section)
- Splitting one topic across two sections, creating artificial thinness in both (e.g., "what is a spec?" and "what is spec driven design?" are the same goal — understanding the concept)
- Creating a section for "Best Practices and Anti-Patterns" — this is not a teaching goal, it's a grab bag of material that belongs distributed across the sections that teach the related concepts

### 💻 Lesson Placement (HARD RULE)
**💻 lessons are always the last lesson in their section** — no lesson of any type follows a 💻 within the same section.

---

## Lesson Types and Emoji Markers

**CRITICAL: Every content lesson must have one emoji marker.**

### Conceptual Lessons (📖)
- Theory, explanations, principles, concepts
- Anti-patterns are woven into relevant conceptual lessons (not standalone lessons — see Anti-Patterns section)
- **Mark with 📖 emoji**

### Hands-On Lessons (💻)
- Pure code challenges — no theory, no explanation of any kind
- Every 💻 lesson consists exclusively of three components:
  1. **Challenge prompt** — instructions telling the student what to do
  2. **Solution code** — the complete working answer
  3. **Challenge code** — the starter file the student receives (with stubs or `// your code here` markers)
- These three components are converted to files when Learnpack generates them
- **💻 lessons never teach** — if a topic needs both teaching and practice, the teaching goes in a 📖 lesson and the practice goes in a separate 💻 lesson added after it in the same section
- **Single-task challenge prompts (HARD RULE):** Each 💻 challenge prompt must describe ONE focused task in 1-2 sentences. NEVER use numbered sub-tasks, multi-step lists, or multiple objectives inside a single challenge prompt. If a challenge naturally has multiple parts, describe it as one cohesive goal (e.g., "Build a complete CRUD API for a contacts resource" NOT "1. Create GET, 2. Create POST, 3. Create DELETE"). Numbered lists and multi-step prompts cause downstream tools (Rigobot) to split one challenge into many, breaking the course structure.
- **Code block length:** Both the solution code and challenge code should be concise and readable — aim for under 30 lines each. If the code is getting longer, the challenge scope is too broad.
- **Mark with 💻 emoji**

**When to include 💻 lessons (decision test):**
Ask: "Does the student write code that **produces output when executed?**" If yes → 💻 is appropriate. If no → don't force it. A file that configures, instructs, or is read by an agent is not code that runs — it's a document. Structured format (JSON, YAML, markdown with fields) does not make something executable code.

**💻 lessons make sense when:**
- The skill is writing functional code (functions, APIs, components, queries, scripts)
- The code can be executed in the IDE and **produces observable output** (a return value, a rendered component, a server response, a test result)
- Auto-testing or self-verification is meaningful (the student can see if it works)

**💻 lessons do NOT make sense when:**
- The student's deliverable is natural language (writing specs, prompts, documentation, communication strategies)
- The topic is about methodology, planning, or thinking frameworks
- The student writes structured documents that an agent *reads* but that don't *execute* — even if they use JSON, YAML, or markdown with structured fields
- The practice would be better served by the assessment (🧠) or by examples within a 📖 lesson
- You'd have to invent an artificial coding exercise just to have a 💻 — if it feels forced, it is

**Common 4Geeks topics that are NOT 💻 material** (these are frequently misidentified as code because they involve structured formats):
- Agent skills, agent rules, agent memory banks — these are natural-language configuration documents, not executable code
- Specifications (specs) — structured descriptions of what to build, not code that runs
- Implementation plans — project planning documents
- Context engineering — writing effective context for AI, not code

**Zero 💻 lessons is a valid course structure.** Many topics (strategy, design methodology, communication, project planning) produce better learning with strong conceptual lessons and a good assessment than with shoehorned code challenges.

### Assessment Lessons (🧠)
- 5-7 questions (multiple choice OR scenario-based, not mixed)
- Include in second-to-last section
- **Mark with 🧠 emoji**

### Welcome Lessons (00.0)
The Welcome lesson introduces the core problem this course solves, previews what students will be able to do by the end, and gives a brief overview of the course sections. It does NOT teach content — it motivates and orients. Think of it as the "why should I care?" lesson.

### Outro Lessons
- Final section only (exactly 1 lesson)
- No emoji marker needed
- No theory, no exercises, no assessment
- Content: Course recap, next steps, resources, encouragement

---

## Anti-Patterns and Best Practices

Anti-patterns and best practices are NOT standalone lessons or sections. They are woven into the conceptual lessons (📖) where the related concept is taught, so students learn the correct approach, the best practices that reinforce it, and the anti-patterns that violate it — all in the same context.

**Never create a section or lesson called "Best Practices" or "Anti-Patterns."** These are not teaching goals — they are material that enriches lessons with real teaching goals. A lesson about "Test Planning" should include TDD best practices and the anti-pattern of only testing happy paths. A lesson about "Skill Structure" should include the best practice of small composable skills and the anti-pattern of the God Skill. The material goes where the concept lives.

**How to integrate:**
- When a 📖 lesson teaches a concept, include the relevant best practice(s) and anti-pattern(s) as natural complements within that same lesson
- Present the correct approach first, then the best practice that reinforces it, then the anti-pattern as a "what NOT to do" with consequences
- This means best practices and anti-patterns appear organically where they're most useful — not collected into a separate lesson or section the student reads out of context

**Content per anti-pattern (within its host lesson):**
- Clear anti-pattern example
- Why it's tempting
- What goes wrong
- The correct approach (already taught earlier in the same lesson)

---

## Syllabus-Based Generation Rules

### Understanding the Syllabus Structure

**Learnpack blocks:** Lines starting with `+` (e.g., `+ HTML Basics`)
- Each `+` block is a separate, independent learnpack
- Content: Indented `-` lines following the `+` block
- Boundary: Stops at the next `+` line (new learnpack starts)

### ⚠️ MANDATORY RULE: One Learnpack Per Generation

**THE PROCESS:**

1. **User requests a course** (e.g., "Generate Week 1 Skill 1")

2. **YOU MUST:**
   - Locate the Skill section in syllabus.md
   - List ALL `+` blocks found under that Skill
   - Ask: "I found these learnapacks: [list all + blocks]. Which ONE should I generate?"
   - Wait for user to specify the EXACT `+` block name

3. **Find the EXACT `+` line user requests**
   - Example: User says "HTML" → Find `+ HTML` line

4. **Extract ONLY the `-` lines under that `+`**
   - Start: First `-` after the `+` line
   - Stop: Immediately when you hit the NEXT `+` line
   - Result: A list of required topics for THIS learnpack only

5. **VERIFY before proceeding:**
   ```
   ✓ Extracted from one `+` block only?
   ✓ Stopped at next `+` line?
   ✓ Zero content from other `+` blocks?
   ```

**NEVER:**
- Combine multiple `+` blocks into one generation
- Continue past the next `+` line
- Assume which `+` block user wants
- Generate without explicit `+` block confirmation

### Example Extraction

```markdown
Skill 1: Frontend Basics

+ HTML
    - Main tags
    - Semantic HTML
    - Best practices
+ CSS
    - Flexbox
    - DRY in CSS
    - Selectors
```

**User:** "Generate Week 1 Skill 1"

**YOU RESPOND:**
"I found 2 learnapacks under Skill 1:
1. + HTML
2. + CSS

Which ONE should I generate?"

**User:** "HTML"

**YOU EXTRACT:**
```
+ HTML
    - Main tags
    - Semantic HTML  
    - Best practices
[STOP HERE - next line is + CSS]
```

**YOU GENERATE:** A complete course covering these 3 topics only.

---

### Understanding Coverage Requirements

**The `-` bullet points are REQUIRED TOPICS, not structural templates.**

**Correct approach:** Design the optimal course structure ensuring these topics are covered. Let the content determine how many sections and lessons are needed.

**Wrong approach:** Create one section per bullet point.

**Example:**
```
+ HTML
    - Main tags
    - Semantic HTML
    - Best practices
```

✅ Design optimal HTML course covering these 3 required topics — as many sections and lessons as quality demands
❌ Create exactly 3 sections matching the bullets

### Using the Thinking Framework

The `-` bullets under the `+` block define the **required topics**. The **Thinking Framework** section for that day (Thinking Development, Best Practices, Patterns, Anti-patterns) provides additional material that must be woven into the lessons where relevant:

- **Anti-patterns** → woven into the 📖 lessons that teach the correct approach they violate
- **Patterns** → woven into the 📖 lessons that cover the related concept
- **Best Practices** → woven into the 📖 lessons where the practice applies
- **Thinking Development** → shapes the overall course philosophy and learning objectives

Do not ignore the Thinking Framework. Do not create separate lessons for individual framework items unless the content genuinely warrants a standalone lesson. The framework enriches the required topics — it does not replace or expand the topic list.

**Important:** Some Thinking Framework items belong to the overall Day/Skill and span multiple `+` blocks. Only use framework items that are relevant to THIS `+` block's topics. If a framework item clearly belongs to a different `+` block (e.g., a rule about "globs" when you're generating the "Spec Driven Design" block, not the "Rules" block), do not include it.

### Examining Context

**Always check:**
- **ALL previous learnapacks:** What has been taught so far in the syllabus? (avoid repetition)
- **Upcoming learnapacks:** What's coming later in the curriculum? (avoid premature coverage)
- **Learning progression:** Where does this learnpack fit in the complete journey?
- **Same-topic prerequisite:** If a previous learnpack already introduced this same concept at a surface level, this learnpack must NOT re-introduce it. Assume students already know the basics and start where the previous learnpack stopped. (e.g., if a prior learnpack covered "What are skills?" and "How do they work?", this learnpack should skip those questions and begin with the deeper material.)

**How to examine:**
- Review all `+` blocks from Week 1 up to the current learnpack
- Review `+` blocks coming after the current learnpack
- Note specific topics and concepts that have been covered
- Note topics that are scheduled for later (don't teach them prematurely)

---

## Lesson Design Requirements

### Every Conceptual Lesson (📖) Must Include:
1. Learning Objectives (2-4 specific, measurable outcomes)
2. Content Outline (main topics to be covered)
3. Transitions (connection to previous/next lessons)
4. Key Principles (2-4 core concepts)
5. Examples (2-3 concrete illustrations)

### Every Hands-On Lesson (💻) Must Include:
1. Challenge Prompt — ONE focused task described in 1-2 sentences (never numbered sub-tasks or multi-step lists)
2. Solution Code — complete working answer, under 30 lines
3. Challenge Code — starter file with stubs or `// your code here` markers, under 30 lines

### Every Assessment Lesson (🧠) Must Include:
1. Learning Objectives (2-4 specific, measurable outcomes)
2. Question format (multiple choice OR scenario-based, not mixed)
3. 5-7 questions covering full course
4. Evaluation criteria
5. Score interpretation

### Every Outro Lesson Must Include:
- Course recap (what students accomplished)
- Connection to bigger picture
- Next steps and continued learning
- Resources for further exploration
- Encouragement and celebration

**Note:** Outro has NO learning objectives, NO exercises, NO theory, NO assessment.

---

## Hard Rules vs Flexible Guidelines

Some rules in this document are labeled **(HARD RULE)** — these are structural constraints that exist for technical or downstream-tool reasons and must always be followed:
- Section Cohesion
- 💻 Lesson Placement (last in section)
- 💻 Single-task challenge prompts (Rigobot splits multi-step prompts)
- One learnpack per generation
- 💻 Declaration Gate (must declare before structuring)

Everything else is a **guideline** that serves educational quality. If something breaks a guideline but genuinely improves learning, it's good design. But "I didn't feel like following it" is not a valid reason to break a guideline — there should be a concrete pedagogical justification.

---

## Generation Process

### Step 1: Identify and Confirm the Learnpack (MANDATORY)

**When user requests generation:**

1. **Locate the section** in syllabus.md
2. **List ALL `+` blocks** found in that section
3. **Ask user:** "I found these learnapacks: [list]. Which ONE should I generate?"
4. **Wait for user** to specify EXACT `+` block name
5. **💻 Declaration Gate (HARD RULE):** Before proposing any structure, declare whether this course will include 💻 lessons.
   - State **yes** or **no**
   - If yes: describe specifically what code the student will write and what **observable output** it produces when executed in the IDE (a return value, rendered component, server response, test result)
   - If the student's deliverable is a document that an agent or tool *reads* rather than code that *executes and produces output* — the answer is **no**, even if the document uses structured formats like JSON, YAML, or markdown
   - This decision must be made NOW, before Step 2. Do not decide later while building the structure.
6. **Confirm extraction:**
   - "Generating [+block name] only"
   - "Topics to cover: [list - bullets]"
   - "💻 lessons: [yes — what they'll code] or [no — reason]"
   - "Proceed with simple structure?"

**NEVER skip this confirmation step, even if only one `+` block exists.**

### Step 2: Simple Structure (Always Before Detail)

Present concise overview:
- Course title and source
- Total lessons (optimized for quality)
- Section breakdown WITH lesson titles and emoji markers
- Lesson distribution
- **Wait for approval**

**Template:**
```markdown
# Course Outline: [Course Title]

**Source:** Week X, Skill Y - [+ Block Name]
**Learnpack:** + [Exact name from syllabus]
**Total Lessons:** XX (optimized for quality)

---

## Proposed Structure

**Section 00: Welcome** (1 lesson)
- 00.0 [Lesson Title] 📖

**Section 01: [Title]** (X lessons)
- 01.0 [Title] 📖
- 01.1 [Title] 📖
- 01.2 [Title] 💻

[... continue for all sections ...]

**Section [X-1]: [Assessment Title]** (X lessons)
- [X].0 [Title] 📖
- [X].1 [Title] 💻
- [X].2 [Title] 🧠

**Section [X]: [Outro Title]** (1 lesson)
- [X].0 [Outro Lesson]

---

**Course Format:** [Mixed/Practical/Conceptual] (X% hands-on = X lessons)

**Lesson Distribution:**
- Conceptual (📖): X lessons
- Hands-on (💻): X lessons
- Assessment (🧠): 1 lesson

---

**Confirm to proceed with full detailed outline?**
```

### Step 3: Quality Analysis (Before Approval)

Before asking for approval, run a quality analysis on the proposed structure. Check:

**Content Flow & Pedagogical Quality:**
- Are any sections artificially split? (Two thin sections covering tightly related ideas should be one.)
- Are any sections overloaded with loosely related topics? (A section mixing a pattern, a thinking style, and unrelated concepts may need restructuring.)
- Does every section have a single teaching goal? Can you describe it in one sentence? (If not, split or restructure.)
- Does every lesson have a clear, distinct purpose? (If you can't explain why a lesson is separate from its neighbor, merge them.)
- Do pre-assessment lessons have a sharp identity? (Vague "putting it all together" lessons should be replaced with concrete synthesis activities.)

**Context Overlap:**
- Does any lesson drift into territory covered by the previous learnpack?
- If a previous learnpack introduced this same topic, does this course skip the introduction and start where the previous one stopped?
- Does any lesson teach content reserved for the next learnpack?
- Are boundary topics scoped tightly enough? (A pattern that exists in both this and the next learnpack must be taught only in the context relevant to THIS learnpack.)

If the analysis reveals issues, fix the structure before presenting it. If you present and the user requests the analysis, show the full results.

### Step 4: Wait for Approval

- User reviews the structure
- User approves OR requests modifications
- Do NOT generate full detail until approved

**Structural re-run rule:** If user feedback results in removing or adding 💻 lessons, or any other significant change to lesson composition (merging sections, dropping lessons, changing the hands-on ratio), **re-run Step 2 from scratch.** Do not patch the existing structure by simply deleting or inserting lessons — rebuild the section structure to reflect the actual course shape. Sections that existed to set up a code challenge may no longer need to exist, topics that were split to make room for practice may now belong together, and the overall pacing should be re-optimized.

### Step 5: Full Detailed Outline (After Approval Only)

Generate complete outline with:
- Full lesson details (objectives, content, transitions, principles, examples) for 📖 lessons
- Challenge prompt, solution code, and challenge code for 💻 lessons
- Assessment questions for 🧠 lesson
- All formatting per template below

**Never skip the simple structure step. Never generate full detail without approval.**

---

## Templates

### Simple Structure Template
```markdown
# Course Outline: [Course Title]

**Source:** Week X, Skill Y - [+ Block Name]
**Learnpack:** + [Exact name from syllabus]
**Total Lessons:** XX (optimized for quality)

---

## Proposed Structure

**Section 00: Welcome** (1 lesson)
- 00.0 [Lesson Title] 📖

**Section 01: [Title]** (X lessons)
- 01.0 [Title] 📖
- 01.1 [Title] 📖
- 01.2 [Title] 💻

[... continue for all sections ...]

**Section [X-1]: [Assessment Title]** (X lessons)
- [X].0 [Title] 📖
- [X].1 [Title] 💻
- [X].2 [Title] 🧠

**Section [X]: [Outro Title]** (1 lesson)
- [X].0 [Outro Lesson]

---

**Course Format:** [Mixed/Practical/Conceptual] (X% hands-on = X lessons)

**Lesson Distribution:**
- Conceptual (📖): X lessons
- Hands-on (💻): X lessons
- Assessment (🧠): 1 lesson

---

**Confirm to proceed with full detailed outline?**
```

### Full Detailed Outline Template
```markdown
# Course Outline: [Course Title]

**Title:** [Full Course Title]
**Learnpack:** + [Exact name from syllabus]
**Prerequisite:** [Previous course or "None"]
**Target Audience:** [Specific description]
**Total Lessons:** XX
**Format:** [Mixed/Practical/Conceptual] (X% hands-on)

---

## Course Description

[2-3 paragraphs: what students learn, why it matters, connections]

---

## Course Philosophy

This course emphasizes:
- [Key principle 1]
- [Key principle 2]
- [Key principle 3]

---

## Course Statistics Summary

| Section | Lessons |
|---------|---------|
| 00 - Welcome | 1 |
| 01 - [Title] | X |
| ... | ... |
| [X] - Outro | 1 |
| **Total** | **XX** |

---

## Section 00: [Welcome Title]

### 00.0 [Lesson Title] 📖

**Learning Objectives:**
- [Specific outcome 1]
- [Specific outcome 2]

**Content Outline:**
- [Main topic 1]
- [Main topic 2]

**Transitions:**
[Connection to next lesson]

**Key Principles:**
- [Core concept 1]
- [Core concept 2]

**Examples:**
- [Concrete example 1]
- [Concrete example 2]

---

## Section 01: [Section Title]

### 01.0 [Lesson Title] 📖

[... same structure as above ...]

---

### 01.X [Challenge Title] 💻

**Challenge Prompt:**
[Clear instructions telling the student what to do]

**Solution Code:**
```[language]
[Complete working solution]
```

**Challenge Code:**
```[language]
[Starter file with stubs or // your code here markers]
```

---

[REPEAT FOR ALL CONTENT LESSONS]

---

## Section [X]: [Outro Title]

### [X].0 [Outro Lesson Title]

**Content Outline:**
- Course recap: what students accomplished
- Connection to bigger picture
- Next steps and continued learning
- Resources for further exploration
- Encouragement and celebration

**Note:** This is conclusion only - no theory, exercises, or assessment.

---
```

---

## Pre-Generation Checklist

**Before presenting ANY structure, answer every item. If any answer is NO, STOP and resolve before proceeding.**

### Syllabus Extraction
- [ ] User specified which `+` block
- [ ] Extracting from ONE `+` block only (count = 1)
- [ ] Stopped at the next `+` line (no content beyond it)
- [ ] Can quote the EXACT `+` line being used

### Context
- [ ] Examined previous learnapacks for overlap
- [ ] Examined upcoming learnapacks for premature coverage
- [ ] If a previous learnpack introduced this topic, starting where it stopped (no re-introducing)

### 💻 Gate
- [ ] Declared 💻 yes/no with justification (before structuring)
- [ ] If 💻 = yes: student writes code that **produces observable output when executed** (not documents an agent reads)

### Structure Quality
- [ ] Every section has a single teaching goal (cohesion test)
- [ ] Every lesson earns its place (no artificial splits, no padding)
- [ ] Anti-patterns and best practices woven into relevant 📖 lessons (no standalone lessons or sections for these)
- [ ] Thinking Framework material integrated where relevant
- [ ] Ran quality analysis on content flow and context overlap
- [ ] Generated in English only
