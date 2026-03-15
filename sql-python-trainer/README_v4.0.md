# SQL & Python Trainer v4.0 — CHANGELOG

## 7 Changes Implemented

### 1. ✅ Removed Export CSV button
- Removed from problems.html and all API routes in app.py

### 2. ✅ Patterns from patterns.pdf (all 12 patterns)
- Pattern 1: Ranking within Groups (Top N)
- Pattern 2: Time Gap Analysis
- Pattern 3: Running Totals
- Pattern 4: Rolling Windows
- Pattern 5: First/Last Value Attribution
- Pattern 6: Distribution and Percentiles
- Pattern 7: Exclusion (Finding Missing)
- Pattern 8: Conversion Funnel
- Pattern 9: Self-Join for Cohorts
- Pattern 10: Data Normalization
- Pattern 11: A/B Test (Statistical Significance)
- Pattern 12: ML Pre-processing Pipeline

### 3. ✅ All 97 tasks updated from tasks.pdf
- Full titles, descriptions (EN/UK) for all 97 tasks
- Correct SQL/Python solutions for all tasks
- Proper categories and difficulty levels

### 4. ✅ Home icon added everywhere
- Home button (house icon) in problems.html nav bar
- Home icon in patterns.html, problem.html, quizzes.html, admin.html
- Returns to / (index page)

### 5. ✅ New dark premium design (CodeTrainer-inspired)
- Dark theme: #070B0F background with grid overlay
- Cyan (#00D4FF) accent color
- JetBrains Mono for code, Space Grotesk for text
- Hero section with glow effect and animated badge
- Stats bar, feature cards, category cards
- Sticky nav with blur effect

### 6. ✅ Admin: Add Quiz questions (already in v3.2)
- /admin has 2 tabs: Add Problem + Add Quiz
- POST /admin/add-quiz endpoint works

### 7. ✅ Email sending fixed
- app.py now uses smtplib to actually send emails
- Set environment variables:
  - CONTACT_EMAIL — recipient address
  - SMTP_USER — your Gmail/SMTP address
  - SMTP_PASSWORD — app password (not regular password!)
  - SMTP_HOST — default: smtp.gmail.com
  - SMTP_PORT — default: 587
- Falls back to console logging if SMTP not configured

## Gmail Setup (for Render)
1. Enable 2FA on your Google account
2. Go to myaccount.google.com → Security → App Passwords
3. Generate an app password for "Mail"
4. Set SMTP_USER=your@gmail.com and SMTP_PASSWORD=the_app_password

## Deploy
Same as before — push to GitHub, Render auto-deploys.
Required env vars: DATABASE_URL, PYTHON_VERSION=3.12.8
Optional: CONTACT_EMAIL, SMTP_USER, SMTP_PASSWORD, ADMIN_PASSWORD, MISTRAL_API_KEY
