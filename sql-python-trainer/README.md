# SQL & Python Interview Trainer v3.0 - FINAL

## ✨ What's New in v3.0

### 1. 🌍 Bilingual Support (EN/UK)
- Language switcher in top-right corner
- All content translated to Ukrainian
- Language preference saved in localStorage

### 2. ✓ Progress Tracking
- Mark tasks as completed
- Progress saved in browser (localStorage)
- Visual checkmarks on completed tasks

### 3. 📊 Google Tag Manager
- GTM ID: GTM-5XW9HB7D
- Tracks: task_started, task_completed, language_change

### 4. 📝 NEW Tasks from PDF
- 7 SQL Product Analyst tasks (DAU, Cohorts, Funnel, etc.)
- 5 Python tasks (A/B Test, ML Pipeline, Feature Engineering)
- 3 Multiple Choice Quizzes

### 5. 🎨 Modern Design
- SVG icons instead of emojis
- Neumorphism design style
- Smooth animations
- Professional color scheme

### 6. 🗄️ Updated Schema
```sql
users (user_id, reg_date, country, channel)
events (event_id, user_id, event_time, event_name)
orders (order_id, user_id, order_date, amount)
```

## 🚀 Quick Start

### Deploy to Render.com

1. **Create PostgreSQL Database**
   - Render → New + → PostgreSQL
   - Name: `sql-trainer-db`
   - Instance: Free
   - Copy Internal Database URL

2. **Create Web Service**
   - New + → Web Service
   - Connect GitHub repo
   - Settings:
     - Runtime: Python 3
     - Build: `pip install -r requirements.txt`
     - Start: `python app.py`
     - Root Directory: (path to these files)
   - Environment Variables:
     - `DATABASE_URL`: your Internal DB URL
     - `PYTHON_VERSION`: `3.12.8`

## 📁 File Structure

```
├── app.py                    # FastAPI backend
├── database.py               # PostgreSQL setup
├── problems.py               # 12 bilingual tasks
├── runner.py                 # SQL/Python execution
├── requirements.txt
├── templates/
│   ├── index.html           # Homepage with GTM
│   ├── problems.html        # Task list with progress
│   └── problem.html         # Task page with checkboxes
└── static/
    ├── css/style.css        # Modern design
    └── js/
        ├── i18n.js          # EN/UK translations
        └── app.js           # Progress tracking
```

## 🌍 Language Support

Default language: English
Switch to Ukrainian: Click "UK" button in top-right

Translations stored in: `/static/js/i18n.js`

## ✓ Progress Tracking

- Checkbox on each task page
- Progress saved in browser localStorage
- Completed tasks show ✓ badge on problems list

## 📊 GTM Events Tracked

- `language_change` - when user switches language
- `task_started` - when user opens a task
- `task_completed` - when user marks task as done
- `sql_run` - when user runs SQL code
- `python_run` - when user runs Python code

## 🎨 Design Features

- No emojis (replaced with SVG icons)
- Neumorphism card style
- Gradient backgrounds
- Smooth hover animations
- Responsive layout

## 📝 Tasks Included

**SQL:**
1. DAU & Sticky Factor
2. Second Highest Value
3. Top 2 per Country
4. New vs Returning Users
5. 3 Consecutive Days
6. Cumulative & Rolling Revenue
7. Strict Funnel Analysis

**Python:**
8. A/B Test (T-test)
9. Cohort Retention Matrix
10. ML Pipeline
11. Class Imbalance (SMOTE)
12. Feature Importance

**Quizzes:**
- SQL Execution Order
- WHERE vs HAVING
- Window Functions

## 🔧 Troubleshooting

**Language not switching:**
→ Check browser console for JavaScript errors

**Progress not saving:**
→ Ensure localStorage is enabled in browser

**GTM not tracking:**
→ Verify GTM-5XW9HB7D is active in Tag Manager

## 📄 License

MIT - Use freely!

Built for Product Analysts & Data Scientists 💚
