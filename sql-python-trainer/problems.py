"""
85 Product Analyst Interview Problems
Based on new schema: users, events, purchases
"""

PROBLEMS = [
    # SQL JUNIOR PRODUCT ANALYST (1-35)
    {
        "id": 1,
        "title": "Всего пользователей",
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Junior",
        "description": "Подсчитайте общее количество пользователей в таблице users.",
        "tables": ["users"],
        "starter_code": "",
        "solution": "SELECT COUNT(user_id) FROM users;",
        "hint": "Используйте функцию COUNT() для подсчета записей."
    },
    {
        "id": 2,
        "title": "DAU (Daily Active Users)",
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Junior",
        "description": "Посчитайте количество уникальных активных пользователей по дням на основе таблицы events.",
        "tables": ["events"],
        "starter_code": "",
        "solution": "SELECT DATE(event_time), COUNT(DISTINCT user_id) FROM events GROUP BY 1;",
        "hint": "Используйте DATE() для извлечения даты и COUNT(DISTINCT user_id)."
    },
    {
        "id": 3,
        "title": "Регистрации по платформам",
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Junior",
        "description": "Посчитайте количество пользователей по каждой платформе (iOS, Android, Web).",
        "tables": ["users"],
        "starter_code": "",
        "solution": "SELECT platform, COUNT(user_id) FROM users GROUP BY 1;",
        "hint": "Группируйте по полю platform и используйте COUNT()."
    },
    {
        "id": 4,
        "title": "Топ-5 стран по юзерам",
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Junior",
        "description": "Найдите топ-5 стран по количеству зарегистрированных пользователей.",
        "tables": ["users"],
        "starter_code": "",
        "solution": "SELECT country, COUNT(user_id) FROM users GROUP BY 1 ORDER BY 2 DESC LIMIT 5;",
        "hint": "Группируйте по country, сортируйте по COUNT DESC, используйте LIMIT 5."
    },
    {
        "id": 5,
        "title": "Общая выручка",
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Junior",
        "description": "Посчитайте общую выручку из успешных покупок (status = 'success').",
        "tables": ["purchases"],
        "starter_code": "",
        "solution": "SELECT SUM(amount) FROM purchases WHERE status = 'success';",
        "hint": "Используйте SUM(amount) с фильтром WHERE status = 'success'."
    },
    {
        "id": 6,
        "title": "ARPU (Средний доход на юзера)",
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Junior",
        "description": "Посчитайте ARPU (Average Revenue Per User) - средний доход на одного пользователя.",
        "tables": ["purchases", "users"],
        "starter_code": "",
        "solution": "SELECT SUM(amount)/COUNT(DISTINCT user_id) FROM purchases;",
        "hint": "Разделите общую выручку на количество уникальных пользователей."
    },
    {
        "id": 7,
        "title": "Средний чек",
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Junior",
        "description": "Посчитайте средний размер успешной покупки.",
        "tables": ["purchases"],
        "starter_code": "",
        "solution": "SELECT AVG(amount) FROM purchases WHERE status = 'success';",
        "hint": "Используйте AVG(amount) с фильтром по status."
    },
    {
        "id": 8,
        "title": "Пользователи без покупок",
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Junior",
        "description": "Найдите пользователей, которые зарегистрировались, но ни разу не совершили покупку.",
        "tables": ["users", "purchases"],
        "starter_code": "",
        "solution": "SELECT u.user_id FROM users u LEFT JOIN purchases p ON u.user_id = p.user_id WHERE p.purchase_id IS NULL;",
        "hint": "Используйте LEFT JOIN и проверьте WHERE purchase_id IS NULL."
    },
    {
        "id": 9,
        "title": "Первая покупка юзера",
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Junior",
        "description": "Для каждого пользователя найдите дату его первой покупки.",
        "tables": ["purchases"],
        "starter_code": "",
        "solution": "SELECT user_id, MIN(purchase_date) FROM purchases GROUP BY 1;",
        "hint": "Используйте MIN(purchase_date) с группировкой по user_id."
    },
    {
        "id": 10,
        "title": "Количество покупок у каждого",
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Junior",
        "description": "Посчитайте количество покупок для каждого пользователя.",
        "tables": ["purchases"],
        "starter_code": "",
        "solution": "SELECT user_id, COUNT(purchase_id) FROM purchases GROUP BY 1;",
        "hint": "Группируйте по user_id и считайте COUNT(purchase_id)."
    },
    {
        "id": 11,
        "title": "Топ-10 'китов' по выручке",
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Junior",
        "description": "Найдите топ-10 пользователей с наибольшей суммарной выручкой.",
        "tables": ["purchases"],
        "starter_code": "",
        "solution": "SELECT user_id, SUM(amount) FROM purchases GROUP BY 1 ORDER BY 2 DESC LIMIT 10;",
        "hint": "Группируйте по user_id, суммируйте amount, сортируйте DESC, LIMIT 10."
    },
    {
        "id": 12,
        "title": "Конверсия Регистрация → Покупка",
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Junior",
        "description": "Посчитайте процент пользователей, которые совершили хотя бы одну покупку после регистрации.",
        "tables": ["users", "purchases"],
        "starter_code": "",
        "solution": "SELECT COUNT(DISTINCT p.user_id)*100.0 / COUNT(DISTINCT u.user_id) FROM users u LEFT JOIN purchases p ON u.user_id = p.user_id;",
        "hint": "Разделите количество уникальных покупателей на общее количество пользователей и умножьте на 100."
    },
    {
        "id": 13,
        "title": "Самое частое событие",
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Junior",
        "description": "Найдите самое частое событие (event_name) в таблице events.",
        "tables": ["events"],
        "starter_code": "",
        "solution": "SELECT event_name, COUNT(*) FROM events GROUP BY 1 ORDER BY 2 DESC LIMIT 1;",
        "hint": "Группируйте по event_name, считайте и сортируйте по количеству DESC."
    },
    {
        "id": 14,
        "title": "Выручка по каналам привлечения",
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Junior",
        "description": "Посчитайте суммарную выручку по каждому UTM-источнику (utm_source).",
        "tables": ["users", "purchases"],
        "starter_code": "",
        "solution": "SELECT u.utm_source, SUM(p.amount) FROM users u JOIN purchases p ON u.user_id = p.user_id GROUP BY 1;",
        "hint": "JOIN таблицы users и purchases, группируйте по utm_source."
    },
    {
        "id": 15,
        "title": "Пользователи с 2+ покупками",
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Junior",
        "description": "Найдите пользователей, которые совершили более одной покупки.",
        "tables": ["purchases"],
        "starter_code": "",
        "solution": "SELECT user_id FROM purchases GROUP BY 1 HAVING COUNT(purchase_id) > 1;",
        "hint": "Используйте HAVING COUNT(purchase_id) > 1 после группировки."
    },
    {
        "id": 16,
        "title": "Дней от регистрации до покупки",
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Junior",
        "description": "Посчитайте количество дней между регистрацией пользователя и его покупкой.",
        "tables": ["users", "purchases"],
        "starter_code": "",
        "solution": "SELECT p.user_id, p.purchase_date - u.reg_date FROM purchases p JOIN users u ON p.user_id=u.user_id;",
        "hint": "Вычтите reg_date из purchase_date используя JOIN."
    },
    {
        "id": 17,
        "title": "Доля iOS юзеров",
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Junior",
        "description": "Посчитайте процент пользователей платформы iOS от общего количества пользователей.",
        "tables": ["users"],
        "starter_code": "",
        "solution": "SELECT COUNT(CASE WHEN platform='iOS' THEN 1 END)*100.0/COUNT(*) FROM users;",
        "hint": "Используйте CASE WHEN для подсчета iOS пользователей и разделите на COUNT(*)."
    },
    {
        "id": 18,
        "title": "Успешные покупки vs Отказы",
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Junior",
        "description": "Посчитайте количество успешных и неуспешных покупок по статусу.",
        "tables": ["purchases"],
        "starter_code": "",
        "solution": "SELECT status, COUNT(*) FROM purchases GROUP BY 1;",
        "hint": "Группируйте по полю status."
    },
    {
        "id": 19,
        "title": "Покупки в день регистрации",
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Junior",
        "description": "Найдите количество пользователей, совершивших покупку в день регистрации.",
        "tables": ["users", "purchases"],
        "starter_code": "",
        "solution": "SELECT COUNT(DISTINCT p.user_id) FROM users u JOIN purchases p ON u.user_id=p.user_id WHERE u.reg_date = p.purchase_date;",
        "hint": "JOIN таблицы и сравните reg_date с purchase_date."
    },
    {
        "id": 20,
        "title": "Последняя активность юзера",
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Junior",
        "description": "Для каждого пользователя найдите время его последней активности (event_time).",
        "tables": ["events"],
        "starter_code": "",
        "solution": "SELECT user_id, MAX(event_time) FROM events GROUP BY 1;",
        "hint": "Используйте MAX(event_time) с группировкой по user_id."
    },
    
    # PYTHON JUNIOR (51-68)
    {
        "id": 51,
        "title": "Очистка NaN",
        "type": "PYTHON",
        "difficulty": "Easy",
        "category": "Python Junior",
        "description": "Заполните пропущенные значения в колонке utm_source значением 'organic'.",
        "tables": ["users"],
        "starter_code": "",
        "solution": "df_users['utm_source'] = df_users['utm_source'].fillna('organic')\nprint(df_users['utm_source'].head())",
        "hint": "Используйте метод fillna() на колонке utm_source."
    },
    {
        "id": 52,
        "title": "Расчет DAU",
        "type": "PYTHON",
        "difficulty": "Easy",
        "category": "Python Junior",
        "description": "Посчитайте Daily Active Users используя pandas.",
        "tables": ["events"],
        "starter_code": "",
        "solution": "dau = df_events.groupby(df_events['event_time'].dt.date)['user_id'].nunique()\nprint(dau)",
        "hint": "Группируйте по дате из event_time и используйте nunique() на user_id."
    },
    {
        "id": 53,
        "title": "Слияние (JOIN) юзеров и покупок",
        "type": "PYTHON",
        "difficulty": "Easy",
        "category": "Python Junior",
        "description": "Объедините таблицы df_users и df_purchases по user_id используя left join.",
        "tables": ["users", "purchases"],
        "starter_code": "",
        "solution": "df_merged = df_users.merge(df_purchases, on='user_id', how='left')\nprint(df_merged.head())",
        "hint": "Используйте метод merge() с параметрами on='user_id' и how='left'."
    },
    {
        "id": 54,
        "title": "ARPU",
        "type": "PYTHON",
        "difficulty": "Easy",
        "category": "Python Junior",
        "description": "Посчитайте ARPU (средний доход на пользователя) используя pandas.",
        "tables": ["purchases", "users"],
        "starter_code": "",
        "solution": "arpu = df_purchases['amount'].sum() / df_users['user_id'].nunique()\nprint(arpu)",
        "hint": "Разделите сумму amount на количество уникальных user_id."
    },
    {
        "id": 55,
        "title": "Распределение выручки по платформам",
        "type": "PYTHON",
        "difficulty": "Medium",
        "category": "Python Junior",
        "description": "Посчитайте суммарную выручку по каждой платформе.",
        "tables": ["users", "purchases"],
        "starter_code": "",
        "solution": "df_merged = df_users.merge(df_purchases, on='user_id')\nresult = df_merged.groupby('platform')['amount'].sum().reset_index()\nprint(result)",
        "hint": "Сначала объедините таблицы, затем группируйте по platform и суммируйте amount."
    },
]

# Add placeholders for remaining problems (21-50 SQL, 56-85 Python/ML)
# These would be filled with actual problems from the PDF

for i in range(21, 36):
    PROBLEMS.append({
        "id": i,
        "title": f"SQL Junior Task {i}",
        "type": "SQL",
        "difficulty": "Easy" if i < 30 else "Medium",
        "category": "SQL Junior",
        "description": f"SQL Junior task {i} - implement based on schema",
        "tables": ["users", "events", "purchases"],
        "starter_code": "",
        "solution": "SELECT * FROM users LIMIT 10;",
        "hint": "Refer to the problem description"
    })

# SQL Middle (36-50)
for i in range(36, 51):
    PROBLEMS.append({
        "id": i,
        "title": f"SQL Middle Task {i}",
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Middle",
        "description": f"SQL Middle task {i} - window functions and advanced analytics",
        "tables": ["users", "events", "purchases"],
        "starter_code": "",
        "solution": "SELECT * FROM users;",
        "hint": "Use window functions"
    })

# Python Junior (56-68)
for i in range(56, 69):
    PROBLEMS.append({
        "id": i,
        "title": f"Python Junior Task {i}",
        "type": "PYTHON",
        "difficulty": "Easy",
        "category": "Python Junior",
        "description": f"Python/Pandas task {i}",
        "tables": ["users", "events", "purchases"],
        "starter_code": "",
        "solution": "print('Solution')",
        "hint": "Use pandas methods"
    })

# Python Data Science (69-85)
for i in range(69, 86):
    PROBLEMS.append({
        "id": i,
        "title": f"Python ML Task {i}",
        "type": "PYTHON",
        "difficulty": "Medium",
        "category": "Python ML",
        "description": f"Machine Learning task {i} - scikit-learn",
        "tables": [],
        "starter_code": "",
        "solution": "from sklearn.model_selection import train_test_split\nprint('ML Solution')",
        "hint": "Use scikit-learn"
    })

def get_all_problems():
    """Return all problems"""
    return PROBLEMS

def get_problem_by_id(problem_id):
    """Get a specific problem by ID"""
    for problem in PROBLEMS:
        if problem["id"] == problem_id:
            return problem
    return None

def get_problems_by_category(category):
    """Get problems filtered by category"""
    return [p for p in PROBLEMS if p.get("category") == category]
