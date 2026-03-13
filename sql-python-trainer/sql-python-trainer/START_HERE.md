# 🚀 НАЧНИТЕ ЗДЕСЬ!

## Что вы получили

✅ Полностью рабочий проект "SQL & Python Interview Trainer"
✅ 100 задач (50 SQL + 50 Python)
✅ Интерактивный код-редактор Monaco
✅ Готово к деплою на Render.com (бесплатно!)

---

## ⚡ Быстрый старт (3 шага)

### Шаг 1: Загрузите на GitHub

```bash
cd sql-python-trainer
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/ваш-username/ваш-репозиторий.git
git push -u origin main
```

### Шаг 2: Создайте PostgreSQL на Render

1. Зайдите на https://render.com
2. New + → PostgreSQL
3. Name: `sql-trainer-db`
4. Plan: **Free**
5. Create Database
6. **Скопируйте Internal Database URL!**

### Шаг 3: Создайте Web Service

1. New + → Web Service
2. Подключите GitHub репозиторий
3. Settings:
   - Runtime: **Python 3**
   - Build: `pip install -r requirements.txt`
   - Start: `python app.py`
   - **Environment Variable:**
     - Key: `DATABASE_URL`
     - Value: вставьте Internal Database URL из Шага 2
4. Create Web Service

**Готово!** Через 5 минут ваш сайт будет работать.

---

## 📚 Подробные инструкции

Если застряли - читайте:
- **DEPLOY_GUIDE.md** - пошаговая инструкция с картинками (текст)
- **README.md** - документация проекта

---

## 📁 Структура файлов

```
sql-python-trainer/
├── app.py              ← Главный файл (FastAPI)
├── database.py         ← Подключение к PostgreSQL
├── problems.py         ← 100 задач
├── runner.py           ← Выполнение SQL/Python
├── requirements.txt    ← Python зависимости
├── templates/          ← HTML страницы
│   ├── index.html
│   ├── problems.html
│   └── problem.html
└── static/css/         ← Стили
    └── style.css
```

---

## 🔥 Что дальше?

1. ✅ Задеплойте сайт (см. выше)
2. 📝 Добавьте больше задач в `problems.py`
3. 🎨 Измените дизайн в `static/css/style.css`
4. 📊 Подключите Google Tag Manager (инструкция в DEPLOY_GUIDE.md)

---

## ❓ Проблемы?

**Сайт не открывается:**
→ Проверьте, что добавили DATABASE_URL в Environment Variables

**Build failed:**
→ Проверьте логи деплоя в Render Dashboard

**Долго грузится:**
→ Это нормально для Free tier (первый запрос ~30 сек после сна)

**Другие вопросы:**
→ Читайте DEPLOY_GUIDE.md (там всё подробно!)

---

## 🎉 Успехов!

Теперь у вас есть собственная платформа для тренировки SQL и Python!

**URL вашего сайта будет:**
https://ваше-имя.onrender.com

Поделитесь с друзьями! 🚀
