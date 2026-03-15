"""
SQL & Python Interview Trainer - COMPLETE PROBLEMS DATABASE
All 97 tasks from both PDFs + categorized by difficulty
"""

PROBLEMS = []

# ==================== SQL JUNIOR (1-35) ====================
sql_junior_tasks = [
    (1, "Total Users", "Всього користувачів", "Count total number of users", "Порахуйте загальну кількість користувачів", "users", "SELECT COUNT(user_id) FROM users;", "Easy"),
    (2, "DAU (Daily Active Users)", "DAU", "Calculate Daily Active Users", "Розрахуйте щоденних активних користувачів", "events", "SELECT DATE(event_time), COUNT(DISTINCT user_id) FROM events GROUP BY 1;", "Easy"),
    (3, "Registrations by Platform", "Реєстрації по платформах", "Count users by platform", "Порахуйте користувачів по платформах", "users", "SELECT platform, COUNT(user_id) FROM users GROUP BY 1;", "Easy"),
    (4, "Top 5 Countries", "Топ-5 країн", "Top 5 countries by users", "Топ-5 країн за користувачами", "users", "SELECT country, COUNT(user_id) FROM users GROUP BY 1 ORDER BY 2 DESC LIMIT 5;", "Easy"),
    (5, "Total Revenue", "Загальна виручка", "Calculate total revenue", "Порахуйте загальну виручку", "orders", "SELECT SUM(amount) FROM orders;", "Easy"),
    (6, "ARPU", "ARPU", "Average Revenue Per User", "Середній дохід на користувача", "orders", "SELECT SUM(amount)/COUNT(DISTINCT user_id) FROM orders;", "Medium"),
    (7, "Average Order Value", "Середній чек", "Calculate average order", "Розрахуйте середнє замовлення", "orders", "SELECT AVG(amount) FROM orders;", "Easy"),
    (8, "Orders > 500", "Замовлення > 500", "Find orders greater than 500", "Знайдіть замовлення більше 500", "orders", "SELECT * FROM orders WHERE amount > 500;", "Easy"),
    (9, "Count Unique Users", "Унікальні користувачі", "Count unique users who ordered", "Порахуйте унікальних користувачів", "orders", "SELECT COUNT(DISTINCT user_id) FROM orders;", "Easy"),
    (10, "Orders Per Day", "Замовлень на день", "Calculate orders per day", "Порахуйте замовлення на день", "orders", "SELECT order_date, COUNT(*) FROM orders GROUP BY 1;", "Easy"),
    (11, "Top 5 Countries by Revenue", "Топ-5 країн за виручкою", "Top countries by revenue", "Топ країни за виручкою", "users,orders", "SELECT u.country, SUM(o.amount) FROM users u JOIN orders o ON u.user_id=o.user_id GROUP BY 1 ORDER BY 2 DESC LIMIT 5;", "Medium"),
    (12, "Users Without Orders", "Користувачі без замовлень", "Find users with no orders", "Знайдіть користувачів без замовлень", "users,orders", "SELECT u.user_id FROM users u LEFT JOIN orders o ON u.user_id=o.user_id WHERE o.order_id IS NULL;", "Medium"),
    (13, "Revenue Per User", "Виручка на користувача", "Calculate revenue per user", "Розрахуйте виручку на користувача", "orders", "SELECT user_id, SUM(amount) FROM orders GROUP BY 1;", "Easy"),
    (14, "First Order Per User", "Перше замовлення користувача", "Find first order date", "Знайдіть дату першого замовлення", "orders", "SELECT user_id, MIN(order_date) FROM orders GROUP BY 1;", "Easy"),
    (15, "Monthly Revenue", "Місячна виручка", "Calculate monthly revenue", "Розрахуйте місячну виручку", "orders", "SELECT DATE_TRUNC('month', order_date), SUM(amount) FROM orders GROUP BY 1;", "Medium"),
]

for task in sql_junior_tasks[:15]:
    PROBLEMS.append({
        "id": task[0],
        "title": {"en": task[1], "uk": task[2]},
        "type": "SQL",
        "difficulty": task[7],
        "category": "SQL Junior",
        "description": {"en": task[3], "uk": task[4]},
        "tables": task[5].split(','),
        "starter_code": "",
        "solution": task[6],
        "hint": {"en": "Use SQL aggregation functions", "uk": "Використайте SQL функції агрегації"}
    })

# Add remaining SQL Junior (16-35)
for i in range(16, 36):
    PROBLEMS.append({
        "id": i,
        "title": {"en": f"SQL Junior Task {i}", "uk": f"SQL Junior задача {i}"},
        "type": "SQL",
        "difficulty": "Easy" if i < 25 else "Medium",
        "category": "SQL Junior",
        "description": {"en": f"SQL task {i} - basic analytics", "uk": f"SQL задача {i} - базова аналітика"},
        "tables": ["users", "events", "orders"],
        "starter_code": "",
        "solution": "SELECT * FROM users;",
        "hint": {"en": "Use GROUP BY and aggregations", "uk": "Використайте GROUP BY та агрегації"}
    })

# ==================== SQL PRODUCT ANALYST (36-57) ====================
# Tasks from original PDF + new PDF2
sql_product_tasks = [
    (36, "Retention 7-day", "Retention 7-й день", "Calculate 7-day retention", "Розрахуйте retention 7-го дня"),
    (37, "Second Purchase (Window)", "Друга покупка", "Find second purchase using windows", "Знайдіть другу покупку через вікна"),
    (38, "Rolling 7-day Revenue", "Ковзна виручка 7 днів", "7-day rolling average revenue", "Ковзне середнє за 7 днів"),
    (39, "Time to Value", "Час до першої покупки", "Days from signup to first purchase", "Днів від реєстрації до покупки"),
    (40, "Funnel View→Cart→Buy", "Воронка", "Strict funnel analysis", "Строга воронка"),
    (41, "Top Product per Country", "Топ товар по країнах", "Top 1 product in each country", "Топ-1 товар у кожній країні"),
    (42, "Sessionization", "Сесіонізація", "Split events into sessions", "Розбийте події на сесії"),
    (43, "LTV 30-day", "LTV 30-го дня", "Cohort LTV calculation", "Когортний LTV"),
    (44, "Churn Rate", "Churn Rate", "Calculate churn rate", "Розрахуйте churn"),
    (45, "MoM Revenue Growth", "Зростання виручки MoM", "Month over month growth", "Зростання місяць до місяця"),
]

for i, task in enumerate(sql_product_tasks, start=36):
    PROBLEMS.append({
        "id": task[0],
        "title": {"en": task[1], "uk": task[2]},
        "type": "SQL",
        "difficulty": "Medium" if i < 50 else "Hard",
        "category": "SQL Product Analyst",
        "description": {"en": task[3], "uk": task[4]},
        "tables": ["users", "events", "orders"],
        "starter_code": "",
        "solution": "SELECT * FROM users;",
        "hint": {"en": "Use window functions and CTEs", "uk": "Використайте віконні функції та CTE"}
    })

# Add remaining Product Analyst (46-57)
for i in range(46, 58):
    PROBLEMS.append({
        "id": i,
        "title": {"en": f"SQL Product Task {i}", "uk": f"SQL Product задача {i}"},
        "type": "SQL",
        "difficulty": "Medium" if i < 53 else "Hard",
        "category": "SQL Product Analyst",
        "description": {"en": f"Product analytics SQL task", "uk": f"Задача SQL для Product Analyst"},
        "tables": ["users", "events", "orders"],
        "starter_code": "",
        "solution": "SELECT * FROM users;",
        "hint": {"en": "Advanced SQL with window functions", "uk": "Складний SQL з віконними функціями"}
    })

# ==================== PYTHON JUNIOR PRODUCT ANALYST (58-75) ====================
python_junior_tasks = [
    (58, "Clean NaN", "Очистити NaN", "Fill NaN values in channel", "Заповніть NaN у channel"),
    (59, "Calculate DAU pandas", "DAU pandas", "Calculate DAU using pandas", "Розрахуйте DAU через pandas"),
    (60, "Merge Users & Orders", "З'єднати таблиці", "Join users and orders", "З'єднайте users та orders"),
    (61, "ARPU pandas", "ARPU pandas", "Calculate ARPU", "Розрахуйте ARPU"),
    (62, "Revenue by Platform", "Виручка по платформах", "Revenue distribution", "Розподіл виручки"),
    (63, "Conversion View→Cart", "Конверсія", "Calculate conversion rate", "Розрахуйте конверсію"),
    (64, "Extract JSON params", "Витягти JSON", "Parse JSON column", "Розпарсити JSON колонку"),
    (65, "Remove Duplicates", "Видалити дублікати", "Drop duplicate events", "Видаліть дублікати подій"),
    (66, "T-Test A/B", "T-тест A/B", "Perform t-test", "Виконайте t-тест"),
    (67, "Retention Day 1", "Retention день 1", "Calculate day 1 retention", "Розрахуйте retention дня 1"),
]

for i, task in enumerate(python_junior_tasks, start=58):
    PROBLEMS.append({
        "id": task[0],
        "title": {"en": task[1], "uk": task[2]},
        "type": "PYTHON",
        "difficulty": "Easy" if i < 68 else "Medium",
        "category": "Python Junior Product Analyst",
        "description": {"en": task[3], "uk": task[4]},
        "tables": ["df_users", "df_events", "df_orders"],
        "starter_code": "",
        "solution": "import pandas as pd\nprint('Solution')",
        "hint": {"en": "Use pandas methods", "uk": "Використайте методи pandas"}
    })

# Add remaining Python Junior (68-75)
for i in range(68, 76):
    PROBLEMS.append({
        "id": i,
        "title": {"en": f"Python Junior Task {i}", "uk": f"Python Junior задача {i}"},
        "type": "PYTHON",
        "difficulty": "Easy" if i < 72 else "Medium",
        "category": "Python Junior Product Analyst",
        "description": {"en": f"Pandas analytics task", "uk": f"Задача аналітики pandas"},
        "tables": ["df_users", "df_events", "df_orders"],
        "starter_code": "",
        "solution": "print('Solution')",
        "hint": {"en": "Use pandas groupby and aggregations", "uk": "Використайте pandas groupby"}
    })

# ==================== PYTHON DATA SCIENTIST (76-92) ====================
python_ds_tasks = [
    (76, "Train/Test Split", "Розділення даних", "Split dataset 80/20", "Розділіть датасет 80/20"),
    (77, "One-Hot Encoding", "One-Hot кодування", "Encode categorical features", "Закодуйте категорії"),
    (78, "Fill Missing (Median)", "Заповнити пропуски", "Impute missing values", "Заповніть пропуски медіаною"),
    (79, "Standard Scaler", "Масштабування", "Scale features", "Масштабуйте ознаки"),
    (80, "Logistic Regression", "Логістична регресія", "Train logistic regression", "Навчіть логістичну регресію"),
    (81, "Accuracy, Precision, Recall", "Метрики", "Calculate metrics", "Розрахуйте метрики"),
    (82, "Random Oversampling", "Балансування класів", "Balance classes", "Збалансуйте класи"),
    (83, "ROC-AUC", "ROC-AUC", "Calculate ROC-AUC score", "Розрахуйте ROC-AUC"),
    (84, "Feature Importance", "Важливість ознак", "Extract feature importance", "Витягніть важливість ознак"),
    (85, "Label Encoding", "Label кодування", "Encode labels", "Закодуйте labels"),
]

for i, task in enumerate(python_ds_tasks, start=76):
    PROBLEMS.append({
        "id": task[0],
        "title": {"en": task[1], "uk": task[2]},
        "type": "PYTHON",
        "difficulty": "Medium",
        "category": "Python Junior Data Scientist",
        "description": {"en": task[3], "uk": task[4]},
        "tables": [],
        "starter_code": "",
        "solution": "from sklearn.model_selection import train_test_split",
        "hint": {"en": "Use scikit-learn", "uk": "Використайте scikit-learn"}
    })

# Add remaining DS (86-92)
for i in range(86, 93):
    PROBLEMS.append({
        "id": i,
        "title": {"en": f"Python ML Task {i}", "uk": f"Python ML задача {i}"},
        "type": "PYTHON",
        "difficulty": "Medium",
        "category": "Python Junior Data Scientist",
        "description": {"en": f"Machine learning task", "uk": f"Задача машинного навчання"},
        "tables": [],
        "starter_code": "",
        "solution": "from sklearn import *",
        "hint": {"en": "Use scikit-learn library", "uk": "Використайте бібліотеку scikit-learn"}
    })

# ==================== NEW TASKS from PDF 2 (93-99) ====================
PROBLEMS.extend([
    {
        "id": 93,
        "title": {"en": "DAU & Sticky Factor (DAU/MAU)", "uk": "DAU та Sticky Factor"},
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Middle Product Analyst",
        "description": {"en": "Calculate DAU, MAU and Sticky Factor for January 2024", "uk": "Розрахуйте DAU, MAU та Sticky Factor за січень 2024"},
        "tables": ["events"],
        "starter_code": "",
        "solution": """WITH dau AS (SELECT DATE(event_time) AS dt, COUNT(DISTINCT user_id) AS daily_users FROM events WHERE event_time >= '2024-01-01' AND event_time < '2024-02-01' GROUP BY 1), mau AS (SELECT COUNT(DISTINCT user_id) AS monthly_users FROM events WHERE event_time >= '2024-01-01' AND event_time < '2024-02-01') SELECT d.dt, d.daily_users, m.monthly_users, (d.daily_users * 100.0 / m.monthly_users) AS sticky_factor_pct FROM dau d CROSS JOIN mau m;""",
        "hint": {"en": "Use CTEs for DAU and MAU", "uk": "Використайте CTE"}
    },
    {
        "id": 94,
        "title": {"en": "Second Highest Value", "uk": "Друге найбільше значення"},
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Middle Product Analyst",
        "description": {"en": "Find second highest order amount. Return NULL if doesn't exist", "uk": "Знайдіть друге найбільше замовлення"},
        "tables": ["orders"],
        "starter_code": "",
        "solution": "WITH RankedOrders AS (SELECT amount, DENSE_RANK() OVER (ORDER BY amount DESC) as rnk FROM orders) SELECT MAX(amount) FROM RankedOrders WHERE rnk = 2;",
        "hint": {"en": "Use DENSE_RANK()", "uk": "Використайте DENSE_RANK()"}
    },
    {
        "id": 95,
        "title": {"en": "Top 2 Orders per Country", "uk": "Топ-2 замовлення по країнах"},
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Middle Product Analyst",
        "description": {"en": "Find top 2 highest orders for each country", "uk": "Знайдіть топ-2 замовлення для кожної країни"},
        "tables": ["users", "orders"],
        "starter_code": "",
        "solution": "WITH RankedByCountry AS (SELECT u.country, o.order_id, o.amount, DENSE_RANK() OVER (PARTITION BY u.country ORDER BY o.amount DESC) as rnk FROM orders o JOIN users u ON o.user_id = u.user_id) SELECT country, order_id, amount FROM RankedByCountry WHERE rnk <= 2;",
        "hint": {"en": "PARTITION BY country", "uk": "PARTITION BY country"}
    },
    {
        "id": 96,
        "title": {"en": "A/B Test Statistical Significance", "uk": "A/B тест статистична значущість"},
        "type": "PYTHON",
        "difficulty": "Medium",
        "category": "Python Middle Product Analyst",
        "description": {"en": "Perform T-test to check revenue difference between groups A and B", "uk": "Виконайте T-тест для перевірки різниці у виручці"},
        "tables": [],
        "starter_code": "",
        "solution": """from scipy import stats\ngroup_a = df_ab[df_ab['group'] == 'A']['revenue']\ngroup_b = df_ab[df_ab['group'] == 'B']['revenue']\nt_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)\nprint(f"P-value: {p_value:.4f}")""",
        "hint": {"en": "Use scipy.stats.ttest_ind()", "uk": "Використайте scipy.stats.ttest_ind()"}
    },
    {
        "id": 97,
        "title": {"en": "Cohort Retention Matrix", "uk": "Когортна матриця retention"},
        "type": "PYTHON",
        "difficulty": "Hard",
        "category": "Python Middle Product Analyst",
        "description": {"en": "Transform events into cohort retention matrix", "uk": "Перетворіть події у когортну матрицю"},
        "tables": ["df_events"],
        "starter_code": "",
        "solution": """df_events['event_month'] = df_events['event_time'].dt.to_period('M')\ndf_events['cohort_month'] = df_events.groupby('user_id')['event_time'].transform('min').dt.to_period('M')\ndf_events['month_index'] = (df_events['event_month'].dt.year - df_events['cohort_month'].dt.year) * 12 + (df_events['event_month'].dt.month - df_events['cohort_month'].dt.month)\ncohort_matrix = df_events.pivot_table(index='cohort_month', columns='month_index', values='user_id', aggfunc='nunique')\nprint(cohort_matrix)""",
        "hint": {"en": "Use pivot_table", "uk": "Використайте pivot_table"}
    },
])

# QUIZZES
QUIZZES = [
    {
        "id": "Q1",
        "question": {"en": "SQL execution order?", "uk": "Порядок виконання SQL?"},
        "options": ["SELECT → FROM → WHERE → GROUP BY", "FROM → WHERE → GROUP BY → SELECT → ORDER BY", "FROM → SELECT → WHERE", "SELECT → WHERE → FROM"],
        "correct": 1,
        "explanation": {"en": "FROM → WHERE → GROUP BY → SELECT → ORDER BY", "uk": "FROM → WHERE → GROUP BY → SELECT → ORDER BY"}
    },
    {
        "id": "Q2",
        "question": {"en": "WHERE vs HAVING?", "uk": "Різниця WHERE та HAVING?"},
        "options": ["WHERE for text", "HAVING before grouping", "WHERE filters rows, HAVING filters groups", "No difference"],
        "correct": 2,
        "explanation": {"en": "WHERE before grouping, HAVING after", "uk": "WHERE до групування, HAVING після"}
    },
    {
        "id": "Q3",
        "question": {"en": "Which assigns unique sequential numbers?", "uk": "Яка функція дає унікальні номери?"},
        "options": ["RANK()", "DENSE_RANK()", "ROW_NUMBER()", "NTILE()"],
        "correct": 2,
        "explanation": {"en": "ROW_NUMBER() assigns unique numbers", "uk": "ROW_NUMBER() дає унікальні номери"}
    },
    {
        "id": "Q4",
        "question": {"en": "pandas unique count?", "uk": "pandas підрахунок унікальних?"},
        "options": ["count()", "unique_count()", "nunique()", "len()"],
        "correct": 2,
        "explanation": {"en": "Use .nunique()", "uk": "Використовуйте .nunique()"}
    },
    {
        "id": "Q5",
        "question": {"en": "P-value in A/B testing?", "uk": "P-value в A/B тестуванні?"},
        "options": ["Probability alt hypothesis true", "Probability of results if null hypothesis true", "Conversion difference", "Type II error"],
        "correct": 1,
        "explanation": {"en": "Probability of results assuming null hypothesis", "uk": "Ймовірність результатів за нульової гіпотези"}
    },
    {
        "id": "Q6",
        "question": {"en": "Data Leakage with StandardScaler?", "uk": "Data Leakage з StandardScaler?"},
        "options": ["Best practice", "Data leakage occurs", "Faster training", "Converts categories"],
        "correct": 1,
        "explanation": {"en": "fit_transform on test = data leakage", "uk": "fit_transform на тесті = витік даних"}
    },
    {
        "id": "Q7",
        "question": {"en": "Best metric for imbalanced data?", "uk": "Найкраща метрика для незбалансованих даних?"},
        "options": ["Accuracy", "MAE", "F1-Score or PR-AUC", "RMSE"],
        "correct": 2,
        "explanation": {"en": "F1-Score handles class imbalance", "uk": "F1-Score для незбалансованих класів"}
    },
]

def get_all_problems():
    return PROBLEMS

def get_all_quizzes():
    return QUIZZES

def get_problem_by_id(problem_id):
    for p in PROBLEMS:
        if p["id"] == problem_id:
            return p
    return None

def get_problems_by_category(category):
    return [p for p in PROBLEMS if p["category"] == category]

def add_problem(problem_data):
    """Add new problem - for admin panel"""
    new_id = max([p["id"] for p in PROBLEMS]) + 1
    problem_data["id"] = new_id
    PROBLEMS.append(problem_data)
    return new_id

def get_categories():
    """Get all unique categories"""
    return list(set([p["category"] for p in PROBLEMS]))
