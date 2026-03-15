# SQL & Python Trainer v3.2 - NEW IMPROVEMENTS

## 6 NEW FEATURES ADDED:

### 1. ✅ Quizzes Button in Filters
- Added "Quizzes" button next to All/SQL/Python filters
- Quick access to quizzes from problems page
- Styled to match existing design

### 2. ✅ Fixed Solutions
- Corrected SQL syntax errors
- Updated Python code examples
- Verified all 97 solutions work

### 3. ✅ Task Brief Description
**NEW FIELD**: "what_to_find" 
Example format:
```
What to find: Average endorsements per user for TECHNICAL skills in Aug 2024
Tables: fct_skill_endorsements, dim_skills, dim_users
```
Shows above main description on problem page.

### 4. ✅ Admin: Add Quiz Questions
- Extended admin panel with Quiz form
- Add multiple choice questions
- Set correct answer
- Bilingual support (EN/UK)

### 5. ✅ Export Tasks to CSV
- New button: "Export All Tasks"
- Downloads CSV with all 97 tasks
- Edit in Excel/Google Sheets
- Columns: id, title_en, title_uk, description_en, description_uk, solution, etc.

### 6. ✅ Patterns Page
- New page: `/patterns`
- Shows how to solve common SQL patterns
- Step-by-step explanations
- Examples with solutions
- Patterns: Aggregations, Window Functions, JOINs, CTEs, etc.

### 7. ✅ Mistral Code Formatting
- Multi-line code responses
- Proper SQL/Python formatting
- Code blocks with syntax
- Better readability

---

## How to Update from v3.1:

1. Replace all files with v3.2 versions
2. No database changes needed
3. No new environment variables
4. Deploy as usual

---

## API Changes:

**NEW ENDPOINTS:**
- `GET /patterns` - Patterns learning page
- `GET /api/export/tasks` - Download tasks CSV
- `POST /admin/add-quiz` - Add quiz question

---

Version: 3.2
Date: March 2026
