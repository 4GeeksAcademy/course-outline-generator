# Course Outline Generator

## Quick Setup Steps

### 1. Create New Project
1. Go to claude.ai
2. Click "Projects" → "Create Project"
3. Name it: 
    ```markdown
    Course Outline Generator
    ```
4. Description: 
    ```markdown
    Generates comprehensive course outlines for 4Geeks Academy following vibecoding methodology. Analyzes syllabus context to create structured, beginner-friendly lesson plans with optimized content progression and hands-on practice.
    ```

### 2. Add Custom Instructions
1. Click "Set custom instructions"
2. Copy **entire contents** of `custom-instructions.md`
3. Paste and save

### 3. Add Knowledge Files
1. Click "Add content" or "Project knowledge"
2. Upload `generation-standards.md`
3. Upload `syllabus.md`

### 4. Test It
Type in the project chat:
```markdown
Generate Week 1 Skill 2 Web app layouts
```

**Expected behavior:**
1. Claude finds the learnpack in syllabus
2. Claude examines all previous/upcoming learnapacks
3. Claude shows simple structure outline (with emoji markers)
4. Claude waits for approval
5. After approval, Claude generates full detailed outline

---

## File Roles

| File | Purpose |
|------|---------|
| **Custom Instructions** | Defines Claude's behavior and 5-step workflow |
| **generation-standards.md** | Reference for methodology, structure rules, quality standards |
| **syllabus.md** | Source data - all course learnapacks |

---

## Updating

**Update behavior/workflow:** Edit `custom-instructions.md` → re-paste into project

**Update standards/methodology:** Edit `generation-standards.md` → re-upload to project

**Update syllabus content:** Edit `syllabus.md` → re-upload to project

---

## Note on Emoji Display

The project knowledge preview may show garbled emoji characters (e.g., `ðŸ'»` instead of 💻). This is a display issue only - Claude reads and outputs emojis correctly despite the garbled preview.