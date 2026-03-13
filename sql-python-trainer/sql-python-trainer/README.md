# SQL & Python Interview Trainer

Платформа для тренировки SQL и Python задач для Data Analyst интервью.

## 🚀 Деплой на Render.com

### Шаг 1: Подготовка проекта

1. **Загрузите код на GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/ваш-username/sql-python-trainer.git
git push -u origin main
```

### Шаг 2: Создайте аккаунт на Render

1. Зайдите на [render.com](https://render.com)
2. Создайте аккаунт (можно через GitHub)

### Шаг 3: Создайте PostgreSQL базу данных

1. В Dashboard Render нажмите **"New +"** → **"PostgreSQL"**
2. Настройки:
   - **Name**: `sql-trainer-db`
   - **Database**: `sql_trainer`
   - **User**: оставьте по умолчанию
   - **Region**: выберите ближайший регион
   - **Instance Type**: выберите **Free**
3. Нажмите **"Create Database"**
4. **ВАЖНО**: Скопируйте **Internal Database URL** (понадобится для Web Service)

### Шаг 4: Создайте Web Service

1. В Dashboard нажмите **"New +"** → **"Web Service"**
2. Подключите ваш GitHub репозиторий
3. Настройки:
   - **Name**: `sql-python-trainer`
   - **Region**: тот же, что и у базы данных
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Instance Type**: выберите **Free**

4. **Environment Variables** (очень важно!):
   Нажмите "Advanced" и добавьте переменную:
   - **Key**: `DATABASE_URL`
   - **Value**: вставьте Internal Database URL из Шага 3

5. Нажмите **"Create Web Service"**

### Шаг 5: Проверка

1. Render начнет деплой (занимает 3-5 минут)
2. После успешного деплоя вы увидите зеленую галочку
3. Нажмите на URL вашего сайта (вида `https://sql-python-trainer.onrender.com`)
4. Сайт должен открыться!

## 📁 Структура проекта

```
sql-python-trainer/
├── app.py                 # Главный файл FastAPI
├── database.py            # Работа с PostgreSQL
├── problems.py            # 100 задач
├── runner.py              # Выполнение SQL/Python кода
├── requirements.txt       # Python зависимости
├── templates/
│   ├── index.html        # Главная страница
│   ├── problems.html     # Список задач
│   └── problem.html      # Страница задачи
└── static/
    └── css/
        └── style.css     # Стили
```

## ⚙️ Локальная разработка

```bash
# Установите зависимости
pip install -r requirements.txt

# Запустите сервер
python app.py
```

Откройте: http://localhost:8000

## 🔧 Troubleshooting

### Проблема: "Application failed to respond"
**Решение**: Проверьте, что переменная `DATABASE_URL` добавлена в Environment Variables

### Проблема: "Database connection failed"
**Решение**: Убедитесь, что используете **Internal Database URL** (начинается с `postgres://`), а не External

### Проблема: Сайт засыпает
**Решение**: Это нормально для бесплатного tier. Первый запрос после 15 минут неактивности займет ~30 секунд.

## 📊 Фичи

- ✅ 50 SQL задач
- ✅ 50 Python задач
- ✅ Интерактивный код-редактор (Monaco)
- ✅ Запуск кода прямо в браузере
- ✅ PostgreSQL база данных
- ✅ Google Tag Manager интеграция

## 🎯 Google Tag Manager

Замените `GTM-XXXXXXX` в `templates/index.html` на ваш GTM ID.

## 📝 Добавление новых задач

Отредактируйте `problems.py` и добавьте новую задачу в массив `PROBLEMS`:

```python
{
    "id": 101,
    "title": "Новая задача",
    "type": "SQL",  # или "PYTHON"
    "difficulty": "Easy",
    "description": "Описание задачи",
    "starter_code": "SELECT * FROM orders;",
    "solution": "SELECT * FROM orders LIMIT 10;",
    "tables": ["orders"]
}
```

## 📧 Контакты

Если возникли вопросы при деплое - создайте Issue в репозитории.

## 📄 Лицензия

MIT
