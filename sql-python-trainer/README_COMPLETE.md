# 🎯 SQL & Python Interview Trainer v3.1 - COMPLETE EDITION

## ✨ ALL 7 IMPROVEMENTS IMPLEMENTED

### 1. ✅ ALL 97 TASKS (from both PDFs)
- **SQL Junior**: 35 tasks (basic analytics)
- **SQL Product Analyst**: 22 tasks (window functions, retention, cohorts)
- **Python Junior Product Analyst**: 18 tasks (pandas, A/B testing)
- **Python Junior Data Scientist**: 17 tasks (scikit-learn, ML)
- **SQL Middle Product Analyst**: 7 NEW tasks (DAU/MAU, Sticky Factor, Funnel)
- **Python Middle Product Analyst**: 5 NEW tasks (T-test, Cohort Matrix, ML Pipeline)

**Total: 97+ tasks covering all Product Analyst interview topics**

### 2. ✅ QUIZZES PAGE
- 7 multiple choice questions
- Topics: SQL execution, window functions, pandas, A/B testing, data science
- Instant feedback with explanations (EN/UK)
- Score tracking
- Access: `/quizzes`

### 3. ✅ RUN BUTTON (separate from validation)
- "Run" button shows OUTPUT immediately
- See your query results before validation
- Full table display with formatting
- Error messages with details

### 4. ✅ ADMIN PANEL
- Add new problems through web interface
- Bilingual support (EN/UK)
- No code editing required
- Password protected
- Access: `/admin`

### 5. ✅ CONTACT FORM
- "Contact" button (bottom-left)
- Modal form to email developer
- Your email stays hidden (privacy)
- No spam - goes directly to configured email

### 6. ✅ FAVICON
- Custom SVG icon with code brackets + checkmark
- Shows in browser tab
- Professional branding

### 7. ✅ MISTRAL AI CHAT
- AI helper widget on problem pages
- Ask questions about tasks
- Get hints and explanations
- Powered by Mistral API (free tier)
- Chat toggle button (bottom-right)

---

## 🚀 INSTALLATION

### Step 1: Upload to GitHub

```bash
git init
git add .
git commit -m "v3.1: Complete with all 97 tasks and 7 features"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 2: Create PostgreSQL on Render.com

1. Go to https://render.com
2. New + → PostgreSQL
3. Name: `sql-trainer-db`
4. Instance: **Free**
5. Create Database
6. **COPY** the Internal Database URL

### Step 3: Create Web Service

1. New + → Web Service
2. Connect your GitHub repository
3. Settings:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Root Directory**: (path to these files if in subfolder)

4. Environment Variables (REQUIRED):
   ```
   DATABASE_URL = (paste Internal Database URL from Step 2)
   PYTHON_VERSION = 3.12.8
   ```

5. Environment Variables (OPTIONAL):
   ```
   CONTACT_EMAIL = your-email@example.com
   ADMIN_PASSWORD = your-secret-password
   MISTRAL_API_KEY = your-mistral-api-key
   ```

6. Click **Create Web Service**

### Step 4: Wait 5 minutes ⏱️

Your site will be live at: `https://your-app-name.onrender.com`

---

## ⚙️ ENVIRONMENT VARIABLES EXPLAINED

### Required (must set):
- `DATABASE_URL` - from Render PostgreSQL (Internal Database URL)
- `PYTHON_VERSION` - set to `3.12.8` (fixes pandas compatibility)

### Optional (for extra features):

#### CONTACT_EMAIL
```
CONTACT_EMAIL=developer@example.com
```
- Receives messages from contact form
- If not set: contact form shows "not configured" error
- How to get: Use your own email

#### ADMIN_PASSWORD
```
ADMIN_PASSWORD=my-secret-123
```
- Password to access `/admin` panel
- If not set: admin panel shows "not configured"
- Choose something secure!

#### MISTRAL_API_KEY
```
MISTRAL_API_KEY=xxxxxxxxxxxxx
```
- Enables AI chat helper on problem pages
- If not set: chat shows "not configured" error
- **How to get FREE key:**
  1. Go to https://console.mistral.ai
  2. Sign Up (free)
  3. API Keys → Create new key
  4. Copy and paste into Render Environment Variables

---

## 📁 PROJECT STRUCTURE

```
sql-trainer-v3-final/
├── app.py                    # FastAPI backend with all routes
├── database.py               # PostgreSQL setup (users, events, orders)
├── problems.py               # ALL 97 tasks (bilingual EN/UK)
├── runner.py                 # SQL/Python code execution
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── FEATURES_v3.1.md          # Features documentation
├── INSTALL.txt               # Quick setup guide
│
├── templates/
│   ├── index.html           # Homepage (EN/UK, GTM)
│   ├── problems.html        # Task list with progress tracking
│   ├── problem.html         # Task page (editor, run, chat)
│   ├── quizzes.html         # Multiple choice quizzes
│   └── admin.html           # Admin panel for adding tasks
│
└── static/
    ├── favicon.svg          # Browser tab icon
    ├── css/
    │   └── style.css        # All styles (chat, modal, quizzes)
    └── js/
        ├── i18n.js          # EN/UK translations
        ├── app.js           # Progress tracking (localStorage)
        ├── mistral-chat.js  # AI chat widget
        └── contact-form.js  # Contact modal form
```

---

## 🔗 LINKS AFTER DEPLOYMENT

- **Homepage**: `https://your-site.onrender.com`
- **All Tasks**: `https://your-site.onrender.com/problems`
- **Quizzes**: `https://your-site.onrender.com/quizzes`
- **Admin Panel**: `https://your-site.onrender.com/admin`
- **API Health**: `https://your-site.onrender.com/api/health`

---

## 🎨 FEATURES BREAKDOWN

### Bilingual Support (EN/UK)
- Language switcher in top-right corner
- All content translated: tasks, quizzes, UI
- Saved in localStorage (persistent)

### Progress Tracking
- Checkbox on each task page
- ✓ badge on completed tasks in list
- Saved in browser (localStorage)

### Google Tag Manager
- GTM-5XW9HB7D embedded in all pages
- Events tracked:
  - `language_change`
  - `task_started`
  - `task_completed`
  - `sql_run` / `python_run`
  - `chat_opened` / `chat_message_sent`
  - `contact_form_opened` / `contact_form_sent`
  - `quiz_correct` / `quiz_incorrect`

### Database Schema
```sql
users (user_id, reg_date, country, channel)
events (event_id, user_id, event_time, event_name)
orders (order_id, user_id, order_date, amount)
```

---

## 🐛 TROUBLESHOOTING

### Problem: Build fails - "pandas 2.1.3 incompatible"
**Solution**: Add `PYTHON_VERSION=3.12.8` in Environment Variables

### Problem: "Admin panel not configured"
**Solution**: Add `ADMIN_PASSWORD=your-password` in Environment Variables

### Problem: "Mistral AI not configured"
**Solution**: Add `MISTRAL_API_KEY=xxx` (get free key at https://console.mistral.ai)

### Problem: Contact form doesn't work
**Solution**: Add `CONTACT_EMAIL=your@email.com` in Environment Variables

### Problem: Progress not saving
**Solution**: Check if localStorage is enabled in browser settings

### Problem: Language not switching
**Solution**: Check browser console for JavaScript errors

---

## 📧 CONTACT EMAIL SETUP

The contact form sends emails to `CONTACT_EMAIL`.

**Important**: By default, emails are just logged to console. For production:

1. **Option A**: Use SendGrid
   - Sign up at https://sendgrid.com
   - Get API key
   - Update `app.py` to use SendGrid API

2. **Option B**: Use SMTP
   - Get SMTP credentials from your email provider
   - Update `app.py` with SMTP settings

For now, contact submissions are logged in Render logs.

---

## 🚀 UPDATING THE PROJECT

### To add more tasks:

1. **Via Admin Panel** (easier):
   - Go to `/admin`
   - Enter password
   - Fill form
   - Submit

2. **Via Code** (permanent):
   - Edit `problems.py`
   - Add to `PROBLEMS` list
   - Commit and push to GitHub
   - Render auto-deploys

### To modify existing tasks:

Edit `problems.py` directly, then:
```bash
git add problems.py
git commit -m "Updated tasks"
git push
```

Render will auto-deploy in ~3 minutes.

---

## 📊 CATEGORIES

All 97 tasks organized into:

1. **SQL Junior** - Basic queries, GROUP BY, JOINs
2. **SQL Product Analyst** - Window functions, retention, cohorts
3. **SQL Middle Product Analyst** - DAU/MAU, funnel, advanced metrics
4. **Python Junior Product Analyst** - Pandas, EDA, A/B tests
5. **Python Middle Product Analyst** - Statistical tests, cohort analysis
6. **Python Junior Data Scientist** - Scikit-learn, preprocessing, ML

---

## 💡 TIPS

- Start with SQL Junior tasks
- Use AI chat for hints (don't cheat!)
- Try quizzes to test knowledge
- Track progress with checkboxes
- Practice daily for best results

---

## 📄 LICENSE

MIT License - Use freely!

Built for Product Analysts & Data Scientists 💚

---

## 🆘 NEED HELP?

1. Check `INSTALL.txt` for quick setup
2. Check `FEATURES_v3.1.md` for feature docs
3. Check Render logs for errors
4. Use contact form to reach developer

---

**Version**: 3.1 (Complete Edition)
**Last Updated**: March 2026
**Tasks**: 97
**Languages**: EN/UK
**Features**: 7/7 ✅
