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
**Optimize based on content complexity:**
- Simple topics: 15-22 lessons
- Moderate topics: 23-28 lessons
- Complex topics: 29-35 lessons

**Goal:** Match lesson count to actual teaching needs. Never default to a fixed number.

### Section Count
- **Total:** 7-9 sections (including Section 00 and final outro)
- **Section 00:** Welcome/Introduction (1 lesson)
- **Content sections:** 5-7 sections (3-5 lessons each)
- **Second-to-last section:** Assessment (includes 🧠 lesson)
- **Final section:** Outro/Conclusion (exactly 1 lesson only)

### 💻 Lesson Placement (HARD RULE)
- **💻 lessons are always the last lesson in their section** — no lesson of any type follows a 💻 within the same section.

---

## Lesson Types and Emoji Markers

**CRITICAL: Every content lesson must have one emoji marker.**

### Conceptual Lessons (📖)
- Theory, explanations, principles, concepts
- Includes anti-pattern lessons (just regular conceptual lessons)
- Word count: ~400-600 words
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
- Word count: ~500-700 words
- **Mark with 💻 emoji**

**Distribution guidelines:**
- Practical courses (coding, tools): 40-50% hands-on
- Conceptual courses (theory, strategy): 20-30% hands-on
- Mixed courses: 30-40% hands-on

**Flexibility:** These are guidelines. Some subjects naturally need more/less practice. Ask: "Does this % make sense for THIS topic?"

### Assessment Lessons (🧠)
- 5-7 questions (multiple choice OR scenario-based, not mixed)
- Include in second-to-last section
- Word count: ~600-800 words
- **Mark with 🧠 emoji**

### Outro Lessons
- Final section only (exactly 1 lesson)
- No emoji marker needed
- No theory, no exercises, no assessment
- Word count: ~400-450 words
- Content: Course recap, next steps, resources, encouragement

---

## Anti-Pattern Lessons

Anti-patterns are regular conceptual lessons (📖) that teach what NOT to do.

**Distribution:**
- Short courses (15-22 lessons): 1 anti-pattern
- Medium courses (23-28 lessons): 2 anti-patterns
- Long courses (29+ lessons): 2-3 anti-patterns

**Placement:** Always AFTER teaching the correct approach

**Content:**
- Clear anti-pattern examples
- Consequences of each anti-pattern
- Correct approach shown side-by-side
- Explanation of why the anti-pattern is common/tempting

---

## Word Count Guidelines

| Lesson Type | Word Count | Purpose |
|-------------|------------|---------|
| Conceptual (📖) | 400-600 | Understanding principles |
| Hands-on (💻) | 500-700 | Practical application |
| Assessment (🧠) | 600-800 | Testing comprehension |
| Outro | 400-450 | Reflection and next steps |

**Total Course:** Lesson count × 500 (e.g., 26 lessons = ~13,000 words)

**Acceptable variance:** ±2,000 words from target

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

**Correct approach:** Design the optimal course structure (maybe 6-8 sections) ensuring these topics are covered within it.

**Wrong approach:** Create one section per bullet point.

**Example:**
```
+ HTML
    - Main tags
    - Semantic HTML
    - Best practices
```

✅ Design optimal HTML course (6-8 sections) covering these 3 required topics
❌ Create exactly 3 sections matching the bullets

### Examining Context

**Always check:**
- **ALL previous learnapacks:** What has been taught so far in the syllabus? (avoid repetition)
- **Upcoming learnapacks:** What's coming later in the curriculum? (avoid premature coverage)
- **Learning progression:** Where does this learnpack fit in the complete journey?

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

## Quality Checklist

### Structure
- [ ] Lesson count optimized for content (15-35 range, not default)
- [ ] 7-9 total sections
- [ ] Logical progression (simple → complex)
- [ ] Each content section has 3-5 lessons
- [ ] Anti-patterns (📖) placed AFTER teaching correct approach
- [ ] Hands-on percentage matches course type
- [ ] Assessment (🧠) in second-to-last section
- [ ] Final section has exactly 1 lesson (outro only)
- [ ] Every content lesson marked with emoji (📖, 💻, or 🧠)
- [ ] Every 💻 lesson is the last lesson in its section

### Content
- [ ] Specific learning objectives (not vague)
- [ ] Concrete, relevant examples
- [ ] Logical transitions between lessons
- [ ] Key principles aligned with 4Geeks philosophy
- [ ] No repetition from ANY previous learnapacks in syllabus (full context examined)
- [ ] No premature coverage of topics scheduled for later learnapacks

### Lesson Balance
- [ ] Appropriate mix of conceptual/hands-on for subject matter
- [ ] 1-3 anti-pattern lessons (📖) properly placed
- [ ] One assessment lesson (🧠) in second-to-last section
- [ ] Single outro lesson concludes course

### 💻 Lesson Integrity
- [ ] Every 💻 lesson contains only: challenge prompt, solution code, challenge code
- [ ] No theory or explanation inside any 💻 lesson
- [ ] Every 💻 lesson is the last lesson in its section
- [ ] Teaching content preceding a 💻 is covered in a 📖 lesson in the same section
- [ ] Every challenge prompt is ONE focused task in 1-2 sentences (no numbered sub-tasks or multi-step lists)
- [ ] Solution code and challenge code are each under 30 lines

### Word Counts
- [ ] Conceptual (📖): 400-600 words
- [ ] Hands-on (💻): 500-700 words
- [ ] Assessment (🧠): 600-800 words
- [ ] Outro: 400-450 words
- [ ] Total: ±2,000 words from target

### Syllabus Compliance
- [ ] Extracted from ONE `+` block only
- [ ] Stopped at next `+` line
- [ ] User confirmed which `+` block to use
- [ ] All `-` bullets from that block covered
- [ ] No content from other `+` blocks included

---

## Assessment Approach

**Good Review = Educational Quality Assessment**
- Does content flow naturally?
- Will students retain this information?
- Is practice placed effectively?
- Does the structure serve the subject matter?

**Bad Review = Rigid Compliance Checking**
- Are percentages exact?
- Do numbers match arbitrary rules?
- Does it check all boxes regardless of context?

**Remember:** Guidelines exist to promote quality, not restrict it. If something breaks a guideline but improves learning, it's good design.

---

## Common Mistakes to Avoid

### DON'T:
- Mix content from multiple `+` blocks in syllabus mode
- Generate without confirming which `+` block user wants
- Continue past the next `+` line in syllabus
- Use the same lesson count for every course (optimize each time)
- Create sections with only 1-2 lessons (except intro/outro)
- Place anti-patterns before teaching the correct approach
- Write vague objectives ("understand X", "learn about Y")
- Mix multiple-choice and scenario questions in assessments
- Forget emoji markers on content lessons (📖, 💻, 🧠)
- Add theory or exercises to outro lesson
- Have multiple lessons in final section
- Invent content for framework sections marked as "Not introduced"
- Include any theory or explanation inside a 💻 lesson
- Place a 💻 lesson anywhere other than last in its section
- Use numbered sub-tasks or multi-step lists in 💻 challenge prompts (causes Rigobot to split one challenge into many)
- Write solution or challenge code blocks longer than 30 lines

### DO:
- Ask user to specify EXACT `+` block name from syllabus
- Extract from ONE `+` block only (verify before proceeding)
- Stop immediately at the next `+` line
- List all available `+` blocks if user request is ambiguous
- Optimize lesson count based on actual content needs
- Vary content section sizes appropriately (3-5 lessons)
- Place anti-patterns after students know the correct approach
- Write specific, measurable learning objectives
- Choose ONE assessment format per lesson (not mixed)
- Keep 💻 lessons as pure code challenges (prompt + solution code + challenge code)
- Write each 💻 challenge prompt as ONE focused task in 1-2 sentences (e.g., "Build a complete CRUD API for a contacts resource" NOT "1. Create GET, 2. Create POST, 3. Create DELETE")
- Keep solution and challenge code under 30 lines each
- Ensure all teaching for a 💻 challenge is covered in a preceding 📖 in the same section
- Mark every content lesson with appropriate emoji
- End with single outro lesson only (no content, no exercises)
- Examine ALL previous learnapacks to avoid repetition
- Examine upcoming learnapacks to avoid premature coverage
- Design optimal structure (don't map 1:1 to bullet points)

---

## Two-Step Generation Process

### Step 1: Identify and Confirm the Learnpack (MANDATORY)

**When user requests generation:**

1. **Locate the section** in syllabus.md
2. **List ALL `+` blocks** found in that section
3. **Ask user:** "I found these learnapacks: [list]. Which ONE should I generate?"
4. **Wait for user** to specify EXACT `+` block name
5. **Confirm extraction:**
   - "Generating [+block name] only"
   - "Topics to cover: [list - bullets]"
   - "Proceed with simple structure?"

**NEVER skip this confirmation step, even if only one `+` block exists.**

### Step 2: Simple Structure (Always Before Detail)

Present concise overview:
- Course title and source
- Total lessons (optimized number)
- Section breakdown WITH lesson titles and emoji markers
- Lesson distribution percentages
- Word count estimates
- **Wait for approval**

**Template:**
```markdown
# Course Outline: [Course Title]

**Source:** Week X, Skill Y - [+ Block Name]
**Learnpack:** + [Exact name from syllabus]
**Total Lessons:** XX (optimized)
**Estimated Words:** ~X,XXX

---

## Proposed Structure

**Section 00: Welcome** (1 lesson, ~450 words)
- 00.0 [Lesson Title] 📖

**Section 01: [Title]** (X lessons, ~X,XXX words)
- 01.0 [Title] 📖
- 01.1 [Title] 📖
- 01.2 [Title] 💻

[... continue for all sections ...]

**Section [X-1]: [Assessment Title]** (X lessons, ~X,XXX words)
- [X].0 [Title] 📖
- [X].1 [Title] 💻
- [X].2 [Title] 🧠

**Section [X]: [Outro Title]** (1 lesson, ~450 words)
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

### Step 3: Wait for Approval

- User reviews the structure
- User approves OR requests modifications
- Do NOT generate full detail until approved

### Step 4: Full Detailed Outline (After Approval Only)

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
**Total Lessons:** XX (optimized)
**Estimated Words:** ~X,XXX

---

## Proposed Structure

**Section 00: Welcome** (1 lesson, ~450 words)
- 00.0 [Lesson Title] 📖

**Section 01: [Title]** (X lessons, ~X,XXX words)
- 01.0 [Title] 📖
- 01.1 [Title] 📖
- 01.2 [Title] 💻

[... continue for all sections ...]

**Section [X-1]: [Assessment Title]** (X lessons, ~X,XXX words)
- [X].0 [Title] 📖
- [X].1 [Title] 💻
- [X].2 [Title] 🧠

**Section [X]: [Outro Title]** (1 lesson, ~450 words)
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
**Estimated Total Length:** ~X,XXX words
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

| Section | Lessons | Estimated Words |
|---------|---------|----------------|
| 00 - Welcome | 1 | ~400 |
| 01 - [Title] | X | ~X,XXX |
| ... | ... | ... |
| [X] - Outro | 1 | ~450 |
| **Total** | **XX** | **~X,XXX** |

---

## Section 00: [Welcome Title]

### 00.0 [Lesson Title] 📖 (XXX words)

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

### 01.0 [Lesson Title] 📖 (XXX words)

[... same structure as above ...]

---

### 01.X [Challenge Title] 💻 (XXX words)

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

### [X].0 [Outro Lesson Title] (~450 words)

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

## Final Reminders

1. **Always generate in English only** (translate Spanish topics)
2. **One learnpack = one generation** (never mix `+` blocks)
3. **Ask user which `+` block** if request is ambiguous
4. **Simple structure first** (with subsections and emoji markers)
5. **Wait for approval** before full generation
6. **Every lesson needs emoji** (📖, 💻, or 🧠) except outro
7. **Final section = 1 lesson only** (outro with no content/exercises)
8. **Examine context** (ALL previous and upcoming learnapacks)
9. **Optimize lesson count** (don't default to fixed numbers)
10. **Guidelines are flexible** (serve educational quality, not arbitrary rules)
11. **💻 lessons are pure code challenges only** (prompt + solution code + challenge code — no theory)
12. **💻 lessons are always last in their section** (no lesson follows a 💻 in the same section)
13. **💻 challenge prompts = ONE task, 1-2 sentences** (never numbered sub-tasks — Rigobot splits them into multiple lessons)

---

## Pre-Generation Final Verification

**Before presenting ANY structure, answer:**

1. ✓ Did user specify which `+` block? (If no → ASK)
2. ✓ Am I extracting from ONE `+` block only? (Count = 1)
3. ✓ Did I stop at the next `+` line? (No content beyond it)
4. ✓ Can I quote the EXACT `+` line I'm using? (Be specific)
5. ✓ Examined previous learnapacks for context? (Avoid repetition)
6. ✓ Examined upcoming learnapacks for context? (Avoid premature topics)
7. ✓ Are all 💻 lessons placed last in their section?
8. ✓ Do all 💻 lessons contain only challenge prompt, solution code, and challenge code?
9. ✓ Is every 💻 challenge prompt ONE focused task in 1-2 sentences? (No numbered sub-tasks)

**If any answer is NO, STOP and resolve before proceeding.**
