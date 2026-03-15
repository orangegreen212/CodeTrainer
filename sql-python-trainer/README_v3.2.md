# 🎯 SQL & Python Trainer v3.2 - FINAL EDITION

## ✨ NEW IN v3.2 (6 Improvements)

### 1. ✅ Quizzes Button in Filters
- Added "Quizzes" button next to All/SQL/Python
- Quick access from problems page
- Styled with purple accent

### 2. ✅ Solutions Fixed & Verified
- Corrected SQL syntax in all 97 tasks
- Verified Python code examples
- All solutions tested

### 3. ✅ "What to Find" Brief Description
**NEW FIELD** in each problem:
```
📋 What to Find: Average endorsements per user for TECHNICAL skills in Aug 2024
Tables: fct_skill_endorsements, dim_skills, dim_users
```
Shows above main description - gives quick context.

### 4. ✅ Admin: Add Quiz Questions
- Extended admin panel with Quiz tab
- Add multiple choice questions (4 options)
- Set correct answer + explanations
- Bilingual (EN/UK)

### 5. ✅ Export Tasks to CSV
- New "Export CSV" button on problems page
- Downloads all 97 tasks
- Edit in Excel/Google Sheets
- Columns: id, title_en, title_uk, what_to_find, description, solution, etc.
- **Use this to fix all task descriptions!**

### 6. ✅ Patterns Page (`/patterns`)
- Learn how to solve common SQL/Python patterns
- 5 sections: Aggregations, Window Functions, JOINs, CTEs, Pandas
- Step-by-step explanations
- Real examples with solutions
- Interactive tabs

### 7. ✅ Mistral Code Formatting
- Multi-line code responses
- Proper SQL/Python formatting
- Code blocks with syntax highlighting
- Better readability in chat

---

## 🚀 QUICK START

Same as v3.1:

1. Upload to GitHub
2. Render.com → PostgreSQL (free)
3. Render.com → Web Service + Environment Variables:
   - `DATABASE_URL` (required)
   - `PYTHON_VERSION=3.12.8` (required)
   - `CONTACT_EMAIL=your@email.com` (optional)
   - `ADMIN_PASSWORD=secret` (optional)
   - `MISTRAL_API_KEY=xxx` (optional)

---

## 📦 v3.2 FILE CHANGES

### New Files:
- `templates/patterns.html` - Patterns learning page
- `CHANGELOG_v3.2.md` - Version changes
- `UPDATE_PROBLEM_HTML.txt` - Instructions for what_to_find display

### Updated Files:
- `app.py` - Added `/patterns`, `/api/export/tasks`, `/admin/add-quiz`
- `problems.py` - Added `add_quiz()` function
- `templates/admin.html` - Quiz form tab
- `templates/problems.html` - Quizzes/Patterns buttons, Export CSV
- `static/js/mistral-chat.js` - Code formatting
- `static/css/style.css` - New styles for patterns, admin tabs, code blocks

---

## 🔗 NEW ROUTES

- `GET /patterns` - Patterns learning page
- `GET /api/export/tasks` - Download CSV with all tasks
- `POST /admin/add-quiz` - Add quiz question (admin only)

---

## 📝 HOW TO FIX TASK DESCRIPTIONS

1. Go to `/problems`
2. Click "Export CSV" button
3. Open `tasks-export.csv` in Excel/Google Sheets
4. Edit columns:
   - `what_to_find_en` - Brief "What to find"
   - `what_to_find_uk` - Ukrainian version
   - `description_en` - Full description
   - `description_uk` - Ukrainian description
   - `solution` - Correct SQL/Python code
5. Save CSV
6. Use Admin panel to add corrected tasks
7. OR update `problems.py` directly and redeploy

---

## 🎨 PATTERNS PAGE SECTIONS

1. **Aggregations** - COUNT, SUM, AVG patterns
2. **Window Functions** - ROW_NUMBER, RANK, DENSE_RANK
3. **JOINs** - When to use INNER/LEFT/RIGHT/FULL
4. **CTEs** - WITH clause patterns
5. **Pandas** - GroupBy → Aggregate patterns

Each section has:
- Step-by-step guide
- Real code examples
- Explanations

---

## 💾 DATA STRUCTURE

All problems now support `what_to_find` field:

```python
{
    "id": 1,
    "title": {"en": "...", "uk": "..."},
    "what_to_find": {
        "en": "Average endorsements per user",
        "uk": "Середня кількість endorsements"
    },
    "description": {...},
    "tables": ["table1", "table2"],
    "solution": "SELECT...",
    ...
}
```

---

## 🐛 TROUBLESHOOTING

Same as v3.1 - no new environment variables needed.

---

## 📊 STATISTICS

- **Total Tasks**: 97
- **Quizzes**: 7
- **Patterns**: 5 sections
- **Languages**: EN/UK
- **Features**: 13 total

---

## 🔄 UPDATING FROM v3.1

1. Replace all files with v3.2
2. No database migration needed
3. No new env variables
4. Git push → Render auto-deploys

---

**Version**: 3.2
**Date**: March 2026
**Status**: Production Ready ✅

Built for Product Analysts & Data Scientists 💚
