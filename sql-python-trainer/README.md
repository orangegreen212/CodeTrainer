# 🎯 SQL & Python Interview Trainer v2.0

Платформа для подготовки к Product Analyst интервью с 85 реальными задачами.

## ✨ Что нового в v2.0

### 🐛 Исправлено
- ✅ Ошибка `Decimal is not JSON serializable`
- ✅ Пустой Code Editor (раньше был pre-filled)
- ✅ Показ примеров данных из таблиц

### 📊 Новая схема данных
```sql
users (user_id, reg_date, platform, country, utm_source)
events (event_id, user_id, event_time, event_name, item_id)
purchases (purchase_id, user_id, purchase_date, amount, status)
```

### 📝 85 новых задач

**SQL Junior (35 задач)**
- DAU, MAU, ARPU
- Конверсия, воронки
- GROUP BY, JOINs

**SQL Middle (15 задач)**
- ROW_NUMBER, RANK, PARTITION BY
- Cohort Analysis
- LTV, Churn Rate, Retention

**Python Junior (18 задач)**
- Pandas: groupby, merge, pivot
- A/B тесты (t-test)
- Визуализация (seaborn)

**Python ML (17 задач)**
- Train/Test Split
- Logistic Regression
- ROC-AUC, Feature Engineering

### 🎨 Улучшенный дизайн
- Градиентные цвета
- Анимации при наведении
- Категории задач
- Подсказки

### 🤖 AI проверка решений
- Интеграция с Mistral API
- Автоматическая валидация кода
- Фидбэк по решениям

---

## 🚀 Быстрый старт

### 1. Загрузите на GitHub

```bash
git init
git add .
git commit -m "Initial commit: SQL & Python Trainer v2"
git remote add origin https://github.com/ваш-username/репозиторий.git
git push -u origin main
```

### 2. Создайте PostgreSQL на Render

1. https://render.com → New + → PostgreSQL
2. Name: `sql-trainer-db`
3. Instance Type: **Free**
4. Create Database
5. **Скопируйте Internal Database URL**

### 3. Создайте Web Service

1. New + → Web Service
2. Connect GitHub repository
3. Settings:
   - Runtime: **Python 3**
   - Build: `pip install -r requirements.txt`
   - Start: `python app.py`
   - Root Directory: `sql-python-trainer/sql-python-trainer`
4. Environment:
   - `DATABASE_URL`: вставьте Internal Database URL
   - `PYTHON_VERSION`: `3.12.8`
   - `MISTRAL_API_KEY`: ваш ключ (опционально)
5. Create Web Service

**Готово!** Через 5 минут сайт будет работать.

---

## 🔑 Mistral API (опционально)

Для проверки решений через AI:

1. https://mistral.ai → Sign Up
2. Dashboard → API Keys → Create
3. Render → Environment → Add:
   - Key: `MISTRAL_API_KEY`
   - Value: ваш ключ

**Без этого все работает, кроме кнопки "Проверить решение"**

---

## 📁 Структура проекта

```
├── app.py                  # FastAPI сервер
├── database.py             # PostgreSQL + новая схема
├── problems.py             # 85 задач
├── runner.py               # Выполнение SQL/Python + Mistral
├── requirements.txt        # Dependencies
├── templates/
│   ├── index.html         # Главная
│   ├── problems.html      # Список задач
│   └── problem.html       # Страница задачи
└── static/css/
    └── style.css          # Стили
```

---

## 🎯 Фичи

- ✅ 85 задач Product Analytics
- ✅ Интерактивный Code Editor (Monaco)
- ✅ Запуск SQL и Python прямо в браузере
- ✅ Примеры данных из таблиц
- ✅ AI проверка решений (Mistral)
- ✅ Категории и фильтры
- ✅ Подсказки для задач
- ✅ Адаптивный дизайн

---

## 🐛 Troubleshooting

**Ошибка "Decimal is not JSON serializable":**
→ Убедитесь, что используете новый `database.py`

**Code Editor не пустой:**
→ В `problem.html` должно быть `value: ''` в Monaco Editor

**Нет примеров данных:**
→ Проверьте, что `table_samples` передаются в template

**Build failed (pandas):**
→ Добавьте `PYTHON_VERSION = 3.12.8` в Environment Variables

---

## 📧 Контакты

Вопросы? Создайте Issue в репозитории!

---

## 📄 Лицензия

MIT - используйте как хотите! 💚
