# 📋 Пошаговая инструкция: Деплой на Render.com

## Часть 1: Загрузка кода на GitHub

### 1.1 Откройте терминал в папке проекта

**Windows:**
- Откройте папку `sql-python-trainer`
- Кликните правой кнопкой → "Open in Terminal" (или "Git Bash Here")

**Mac/Linux:**
- Откройте Terminal
- Перейдите в папку: `cd /путь/к/sql-python-trainer`

### 1.2 Инициализируйте Git

```bash
git init
```

### 1.3 Добавьте все файлы

```bash
git add .
```

### 1.4 Сделайте первый коммит

```bash
git commit -m "Initial commit: SQL & Python Interview Trainer"
```

### 1.5 Подключите GitHub репозиторий

**Замените `ваш-username` и `ваш-репозиторий` на ваши данные:**

```bash
git branch -M main
git remote add origin https://github.com/ваш-username/ваш-репозиторий.git
git push -u origin main
```

✅ **Готово!** Код теперь на GitHub.

---

## Часть 2: Регистрация на Render

### 2.1 Зайдите на Render.com

1. Откройте: https://render.com
2. Нажмите **"Get Started"** или **"Sign Up"**

### 2.2 Создайте аккаунт

**Способ 1: Через GitHub (рекомендуется)**
- Нажмите **"GitHub"**
- Авторизуйтесь через GitHub
- Разрешите доступ Render к вашим репозиториям

**Способ 2: По email**
- Введите email и пароль
- Подтвердите email

✅ **Готово!** Вы в Dashboard Render.

---

## Часть 3: Создание PostgreSQL базы данных

### 3.1 Откройте создание новой базы

1. В Dashboard нажмите **"New +"** (синяя кнопка справа вверху)
2. Выберите **"PostgreSQL"**

### 3.2 Заполните настройки

**Name:** `sql-trainer-db` (или любое имя)

**Database:** `sql_trainer` (оставьте по умолчанию)

**User:** оставьте как есть

**Region:** 
- Для Украины выбирайте **"Frankfurt (Europe)"**
- Для других стран выбирайте ближайший регион

**PostgreSQL Version:** оставьте последнюю

**Datadog API Key:** оставьте пустым

**Instance Type:** выберите **"Free"**

### 3.3 Создайте базу

1. Нажмите **"Create Database"** (внизу)
2. Подождите 1-2 минуты (база создается)

### 3.4 ВАЖНО: Скопируйте Database URL

1. После создания откроется страница базы
2. Найдите раздел **"Connections"**
3. Скопируйте **"Internal Database URL"** 
   - Формат: `postgres://user:pass@host/dbname`
   - НЕ копируйте "External Database URL"!

**Куда скопировать:** 
- Сохраните в Notepad/TextEdit
- Понадобится в Шаге 4.4

✅ **База создана!** Переходим к Web Service.

---

## Часть 4: Создание Web Service (сайт)

### 4.1 Откройте создание Web Service

1. Вернитесь в Dashboard (нажмите "Render" логотип вверху слева)
2. Нажмите **"New +"**
3. Выберите **"Web Service"**

### 4.2 Подключите GitHub репозиторий

**Если это ваш первый проект:**
- Нажмите **"Connect a repository"**
- Выберите **"GitHub"**
- Авторизуйте Render (если еще не сделали)

**Найдите репозиторий:**
- В списке найдите `sql-python-trainer`
- Нажмите **"Connect"**

### 4.3 Заполните настройки Web Service

**Name:** `sql-python-trainer` (или любое имя, будет в URL)

**Region:** **ВЫБЕРИТЕ ТОТ ЖЕ РЕГИОН, что и для базы данных!**
- Если база во Frankfurt → выберите Frankfurt

**Branch:** `main`

**Root Directory:** оставьте пустым

**Runtime:** выберите **"Python 3"**

**Build Command:** 
```
pip install -r requirements.txt
```

**Start Command:**
```
python app.py
```

### 4.4 Настройте Environment Variables (КРИТИЧНО!)

1. Прокрутите вниз до раздела **"Environment Variables"**
2. Нажмите **"Add Environment Variable"**
3. Заполните:
   - **Key:** `DATABASE_URL`
   - **Value:** вставьте Internal Database URL из Шага 3.4
     (тот, который вы скопировали в Notepad)

**Проверьте:**
- URL должен начинаться с `postgres://` или `postgresql://`
- Должны быть username, password, host, database name

### 4.5 Выберите Plan

**Instance Type:** выберите **"Free"**
- 750 часов в месяц (достаточно для одного сайта)
- Засыпает после 15 минут неактивности

### 4.6 Создайте Web Service

1. Нажмите **"Create Web Service"** (внизу)
2. Начнется деплой (зеленый индикатор прогресса)

✅ **Деплой запущен!**

---

## Часть 5: Ожидание деплоя

### 5.1 Процесс деплоя

**Вы увидите логи в реальном времени:**

```
==> Downloading buildpack...
==> Installing dependencies
==> Building...
==> Starting service
```

**Время деплоя:** 3-7 минут

### 5.2 Успешный деплой

**Когда деплой завершится, вы увидите:**
- ✅ Зеленая галочка "Live"
- URL вашего сайта (вида `https://sql-python-trainer.onrender.com`)

### 5.3 Проверка работы

1. Нажмите на URL сайта
2. Должна открыться главная страница
3. Нажмите "Start Practicing"
4. Откройте любую задачу
5. Напишите код и нажмите "Run Code"

✅ **Сайт работает!**

---

## Часть 6: Частые ошибки и их решение

### ❌ Ошибка: "Application failed to respond"

**Причина:** Не указана переменная DATABASE_URL

**Решение:**
1. Откройте ваш Web Service в Render
2. Перейдите в "Environment"
3. Добавьте переменную `DATABASE_URL`
4. Нажмите "Save Changes"
5. Render автоматически передеплоит

---

### ❌ Ошибка: "Database connection refused"

**Причина:** Неправильный Database URL

**Решение:**
1. Откройте вашу PostgreSQL базу в Render
2. Убедитесь, что копируете **"Internal Database URL"**
3. НЕ используйте "External Database URL"
4. URL должен быть вида: `postgres://user:pass@hostname/dbname`

---

### ❌ Сайт открывается долго (30+ секунд)

**Причина:** Бесплатный tier засыпает после 15 минут неактивности

**Это нормально!** 
- Первый запрос "будит" сайт (~30 секунд)
- Последующие запросы работают быстро
- Для постоянной работы нужен платный план ($7/месяц)

---

### ❌ Ошибка: "Build failed"

**Причина:** Проблемы с requirements.txt

**Решение:**
1. Проверьте, что файл `requirements.txt` есть в корне репозитория
2. Убедитесь, что Build Command: `pip install -r requirements.txt`
3. Проверьте логи деплоя на ошибки

---

## Часть 7: Обновление сайта

### Когда вы внесли изменения в код:

```bash
git add .
git commit -m "Описание изменений"
git push
```

**Render автоматически:**
- Заметит изменения в GitHub
- Запустит новый деплой
- Обновит сайт

✅ **Автоматический деплой работает!**

---

## Часть 8: Настройка Google Tag Manager

### 8.1 Создайте GTM аккаунт

1. Зайдите на https://tagmanager.google.com
2. Создайте аккаунт и контейнер
3. Скопируйте GTM ID (формат: `GTM-XXXXXXX`)

### 8.2 Добавьте GTM в код

1. Откройте файл `templates/index.html`
2. Найдите `GTM-XXXXXXX` (два раза в файле)
3. Замените на ваш GTM ID
4. Сохраните и запушьте в GitHub:

```bash
git add .
git commit -m "Add Google Tag Manager"
git push
```

✅ **GTM подключен!**

---

## 🎉 Готово!

Ваш сайт работает на:
- **URL:** https://ваш-сайт.onrender.com
- **База:** PostgreSQL на Render
- **Деплой:** Автоматический через GitHub

**Что дальше:**
- Добавьте больше задач в `problems.py`
- Настройте дизайн в `static/css/style.css`
- Подключите Google Analytics через GTM
- Поделитесь сайтом с друзьями!

---

## 💡 Полезные ссылки

- **Render Dashboard:** https://dashboard.render.com
- **Render Docs:** https://render.com/docs
- **GitHub репозиторий:** https://github.com/ваш-username/ваш-репозиторий

---

## 📧 Нужна помощь?

Если что-то не получается:
1. Проверьте логи деплоя в Render (раздел "Logs")
2. Убедитесь, что все файлы на GitHub
3. Перечитайте инструкцию с самого начала
4. Создайте Issue в GitHub репозитории
