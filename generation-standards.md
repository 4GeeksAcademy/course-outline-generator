# Course Outline Generation Standards

Comprehensive methodology for generating 4Geeks Academy course outlines.

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

---

## Lesson Types and Emoji Markers

**CRITICAL: Every content lesson must have one emoji marker.**

### Conceptual Lessons (📖)
- Theory, explanations, principles, concepts
- Includes anti-pattern lessons (just regular conceptual lessons)
- Word count: ~400-600 words
- **Mark with 📖 emoji**

### Hands-On Lessons (💻)
- Practical application and exercises
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

**CRITICAL RULE: One Learnpack Per Generation**

When generating:
1. Find the EXACT `+` line user requests
2. Extract ONLY the `-` lines under that `+`
3. STOP at the next `+` line (different learnpack)
4. Never mix content from multiple `+` blocks

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
1. Learning Objectives (2-4 specific, measurable outcomes)
2. Content Outline (main topics to be covered)
3. Transitions (connection to previous/next lessons)
4. Key Principles (2-4 core concepts)
5. Examples (2-3 concrete illustrations)
6. Hands-On Exercise or Practice Challenge
7. Code examples or Practice scenario
8. Success criteria or Expected outcomes

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

### Word Counts
- [ ] Conceptual (📖): 400-600 words
- [ ] Hands-on (💻): 500-700 words
- [ ] Assessment (🧠): 600-800 words
- [ ] Outro: 400-450 words
- [ ] Total: ±2,000 words from target

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
- Use the same lesson count for every course (optimize each time)
- Create sections with only 1-2 lessons (except intro/outro)
- Place anti-patterns before teaching the correct approach
- Write vague objectives ("understand X", "learn about Y")
- Mix multiple-choice and scenario questions in assessments
- Forget emoji markers on content lessons (📖, 💻, 🧠)
- Add theory or exercises to outro lesson
- Have multiple lessons in final section
- Mix content from different `+` blocks (syllabus mode)
- Continue past the next `+` line (syllabus mode)
- Invent content for framework sections marked as "Not introduced"

### DO:
- Optimize lesson count based on actual content needs
- Vary content section sizes appropriately (3-5 lessons)
- Place anti-patterns after students know the correct approach
- Write specific, measurable learning objectives
- Choose ONE assessment format per lesson (not mixed)
- Include clear practice tasks for all hands-on lessons
- Mark every content lesson with appropriate emoji
- End with single outro lesson only (no content, no exercises)
- Extract from ONE `+` block only (syllabus mode)
- Examine ALL previous learnapacks to avoid repetition
- Examine upcoming learnapacks to avoid premature coverage
- Design optimal structure (don't map 1:1 to bullet points)

---

## Two-Step Generation Process

### Step 1: Simple Structure (Always First)
Present concise overview:
- Course title and source
- Total lessons (optimized number)
- Section breakdown WITH lesson titles and emoji markers
- Lesson distribution percentages
- Word count estimates
- **Wait for approval**

### Step 2: Full Detailed Outline (After Approval)
Generate complete outline with:
- Full lesson details (objectives, content, transitions, principles, examples)
- Hands-on exercises for 💻 lessons
- Assessment questions for 🧠 lesson
- All formatting per template

**Never skip Step 1. Never generate full detail without approval.**

---

## Templates

### Simple Structure Template
```markdown
# Course Outline: [Course Title]

**Source:** Week X, Skill Y
**Total Lessons:** XX (optimized)
**Estimated Words:** ~X,XXX

---

## Proposed Structure

**Section 00: Welcome** (1 lesson, ~450 words)
- 00.0 [Lesson Title] 📖

**Section 01: [Title]** (X lessons, ~X,XXX words)
- 01.0 [Title] 📖
- 01.1 [Title] 💻
- 01.2 [Title] 📖

[... continue for all sections ...]

**Section [X-1]: [Assessment Title]** (X lessons, ~X,XXX words)
- [X].0 [Title] 💻
- [X].1 [Title] 🧠

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
3. **Simple structure first** (with subsections and emoji markers)
4. **Wait for approval** before full generation
5. **Every lesson needs emoji** (📖, 💻, or 🧠) except outro
6. **Final section = 1 lesson only** (outro with no content/exercises)
7. **Examine context** (ALL previous and upcoming learnapacks)
8. **Optimize lesson count** (don't default to fixed numbers)
9. **Guidelines are flexible** (serve educational quality, not arbitrary rules)
