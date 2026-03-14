"""
Product Analyst Interview Problems - Bilingual EN/UK
New tasks from улучшение_2.pdf
"""

PROBLEMS = [
    # SQL PRODUCT ANALYST
    {
        "id": 1,
        "title": {
            "en": "Daily Active Users & Sticky Factor (DAU/MAU)",
            "uk": "Щоденні активні користувачі та Sticky Factor"
        },
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Product Analyst",
        "description": {
            "en": "Calculate the Daily Active Users (DAU) and Monthly Active Users (MAU) for January 2024, and find the Sticky Factor (DAU/MAU) as a percentage.",
            "uk": "Розрахуйте DAU та MAU за січень 2024 року, а також знайдіть Sticky Factor (DAU/MAU) у відсотках."
        },
        "tables": ["events"],
        "starter_code": "",
        "solution": """WITH dau AS (
    SELECT DATE(event_time) AS dt, COUNT(DISTINCT user_id) AS daily_users
    FROM events WHERE event_time >= '2024-01-01' AND event_time < '2024-02-01'
    GROUP BY 1
),
mau AS (
    SELECT COUNT(DISTINCT user_id) AS monthly_users
    FROM events WHERE event_time >= '2024-01-01' AND event_time < '2024-02-01'
)
SELECT d.dt, d.daily_users, m.monthly_users,
       (d.daily_users * 100.0 / m.monthly_users) AS sticky_factor_pct
FROM dau d CROSS JOIN mau m;""",
        "hint": {
            "en": "Use CTEs for DAU and MAU, then calculate the ratio",
            "uk": "Використайте CTE для DAU та MAU, потім порахуйте співвідношення"
        }
    },
    {
        "id": 2,
        "title": {
            "en": "The Second Highest (Classic Tech Interview)",
            "uk": "Друга за величиною сума"
        },
        "type": "SQL",
        "difficulty": "Easy",
        "category": "SQL Product Analyst",
        "description": {
            "en": "Find the second highest order amount from the orders table. Return NULL if it doesn't exist.",
            "uk": "Знайдіть другу за величиною суму замовлення (amount). Поверніть NULL, якщо такої немає."
        },
        "tables": ["orders"],
        "starter_code": "",
        "solution": """WITH RankedOrders AS (
    SELECT amount, DENSE_RANK() OVER (ORDER BY amount DESC) as rnk
    FROM orders
)
SELECT MAX(amount) AS second_highest_amount
FROM RankedOrders WHERE rnk = 2;""",
        "hint": {
            "en": "Use DENSE_RANK() window function",
            "uk": "Використайте віконну функцію DENSE_RANK()"
        }
    },
    {
        "id": 3,
        "title": {
            "en": "Top 2 Orders per Country",
            "uk": "Топ-2 замовлення по країнах"
        },
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Product Analyst",
        "description": {
            "en": "Find the top 2 highest-value orders for each country.",
            "uk": "Знайдіть топ-2 найдорожчих замовлення для кожної країни."
        },
        "tables": ["orders", "users"],
        "starter_code": "",
        "solution": """WITH RankedByCountry AS (
    SELECT u.country, o.order_id, o.amount,
           DENSE_RANK() OVER (PARTITION BY u.country ORDER BY o.amount DESC) as rnk
    FROM orders o JOIN users u ON o.user_id = u.user_id
)
SELECT country, order_id, amount FROM RankedByCountry WHERE rnk <= 2;""",
        "hint": {
            "en": "Use PARTITION BY country in window function",
            "uk": "Використайте PARTITION BY country у віконній функції"
        }
    },
    {
        "id": 4,
        "title": {
            "en": "New vs. Returning Users",
            "uk": "Нові vs повернуті користувачі"
        },
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Product Analyst",
        "description": {
            "en": "For each date, calculate the number of New Users (first time event) vs Returning Users.",
            "uk": "Для кожної дати порахуйте кількість нових користувачів (подія вперше) та тих, хто повернувся."
        },
        "tables": ["events"],
        "starter_code": "",
        "solution": """WITH FirstEvent AS (
    SELECT user_id, MIN(DATE(event_time)) AS first_date FROM events GROUP BY user_id
)
SELECT DATE(e.event_time) AS event_date,
       COUNT(DISTINCT CASE WHEN DATE(e.event_time) = f.first_date THEN e.user_id END) AS new_users,
       COUNT(DISTINCT CASE WHEN DATE(e.event_time) > f.first_date THEN e.user_id END) AS returning_users
FROM events e
JOIN FirstEvent f ON e.user_id = f.user_id
GROUP BY 1 ORDER BY 1;""",
        "hint": {
            "en": "First find each user's first event date",
            "uk": "Спочатку знайдіть дату першої події кожного користувача"
        }
    },
    {
        "id": 5,
        "title": {
            "en": "3 Consecutive Active Days",
            "uk": "3 послідовні активні дні"
        },
        "type": "SQL",
        "difficulty": "Hard",
        "category": "SQL Product Analyst",
        "description": {
            "en": "Find all users who logged into the app on 3 or more consecutive days.",
            "uk": "Знайдіть користувачів, які заходили в додаток 3 або більше днів поспіль."
        },
        "tables": ["events"],
        "starter_code": "",
        "solution": """WITH DistinctLogins AS (
    SELECT DISTINCT user_id, DATE(event_time) AS login_date
    FROM events WHERE event_name = 'login'
),
NextLogins AS (
    SELECT user_id, login_date,
           LEAD(login_date, 1) OVER (PARTITION BY user_id ORDER BY login_date) as next_1,
           LEAD(login_date, 2) OVER (PARTITION BY user_id ORDER BY login_date) as next_2
    FROM DistinctLogins
)
SELECT DISTINCT user_id
FROM NextLogins
WHERE next_1 = login_date + INTERVAL '1 day'
  AND next_2 = login_date + INTERVAL '2 days';""",
        "hint": {
            "en": "Use LEAD() to check next dates",
            "uk": "Використайте LEAD() для перевірки наступних дат"
        }
    },
    {
        "id": 6,
        "title": {
            "en": "Cumulative Revenue & Rolling Window",
            "uk": "Накопичувальна виручка та ковзне вікно"
        },
        "type": "SQL",
        "difficulty": "Medium",
        "category": "SQL Product Analyst",
        "description": {
            "en": "Calculate daily revenue, 7-day rolling revenue, and total cumulative revenue over time.",
            "uk": "Розрахуйте денну виручку, ковзне середнє за 7 днів та кумулятивну виручку."
        },
        "tables": ["orders"],
        "starter_code": "",
        "solution": """WITH DailyRev AS (
    SELECT order_date, SUM(amount) AS daily_rev FROM orders GROUP BY 1
)
SELECT order_date, daily_rev,
       SUM(daily_rev) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_7d,
       SUM(daily_rev) OVER (ORDER BY order_date) AS cumulative_rev
FROM DailyRev;""",
        "hint": {
            "en": "Use window functions with ROWS BETWEEN",
            "uk": "Використайте віконні функції з ROWS BETWEEN"
        }
    },
    {
        "id": 7,
        "title": {
            "en": "Strict Funnel Analysis",
            "uk": "Строга воронка аналітика"
        },
        "type": "SQL",
        "difficulty": "Hard",
        "category": "SQL Product Analyst",
        "description": {
            "en": "Count users who completed the strict funnel: view_item -> add_to_cart -> purchase in chronological order.",
            "uk": "Порахуйте користувачів, які пройшли строгу воронку: перегляд -> корзина -> покупка у хронологічному порядку."
        },
        "tables": ["events"],
        "starter_code": "",
        "solution": """SELECT
    COUNT(DISTINCT e1.user_id) AS views,
    COUNT(DISTINCT e2.user_id) AS carts,
    COUNT(DISTINCT e3.user_id) AS purchases
FROM events e1
LEFT JOIN events e2 ON e1.user_id = e2.user_id 
    AND e2.event_name = 'add_to_cart' AND e2.event_time > e1.event_time
LEFT JOIN events e3 ON e2.user_id = e3.user_id 
    AND e3.event_name = 'purchase' AND e3.event_time > e2.event_time
WHERE e1.event_name = 'view_item';""",
        "hint": {
            "en": "Use multiple LEFT JOINs with time conditions",
            "uk": "Використайте кілька LEFT JOIN з умовами часу"
        }
    },
    
    # PYTHON TASKS
    {
        "id": 8,
        "title": {
            "en": "A/B Test Statistical Significance",
            "uk": "Статистична значущість A/B тесту"
        },
        "type": "PYTHON",
        "difficulty": "Medium",
        "category": "Python Analytics",
        "description": {
            "en": "You have df_ab with columns group ('A', 'B') and revenue. Perform a T-test to check if the revenue difference is statistically significant (alpha = 0.05).",
            "uk": "Проведіть T-тест, щоб перевірити, чи є статистично значущою різниця у виручці між групами А та В."
        },
        "tables": [],
        "starter_code": "",
        "solution": """import pandas as pd
from scipy import stats

# Data extraction
group_a = df_ab[df_ab['group'] == 'A']['revenue']
group_b = df_ab[df_ab['group'] == 'B']['revenue']

# T-Test (equal_var=False for Welch's t-test)
t_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)

print(f"P-value: {p_value:.4f}")
if p_value < 0.05:
    print("Difference is statistically significant")
else:
    print("No significant difference")""",
        "hint": {
            "en": "Use scipy.stats.ttest_ind()",
            "uk": "Використайте scipy.stats.ttest_ind()"
        }
    },
    {
        "id": 9,
        "title": {
            "en": "Cohort Retention Heatmap",
            "uk": "Теплова карта когортного retention"
        },
        "type": "PYTHON",
        "difficulty": "Hard",
        "category": "Python Analytics",
        "description": {
            "en": "Transform df_events into a cohort matrix (Rows: Cohort Month, Columns: Month Index, Values: Active Users).",
            "uk": "Перетворіть логи у когортну матрицю (Рядки: Місяць когорти, Колонки: Індекс місяця, Значення: Активні юзери)."
        },
        "tables": ["events"],
        "starter_code": "",
        "solution": """# 1. Get Cohort Month and Event Month
df_events['event_month'] = df_events['event_time'].dt.to_period('M')
df_events['cohort_month'] = df_events.groupby('user_id')['event_time'].transform('min').dt.to_period('M')

# 2. Calculate Month Index
df_events['month_index'] = (df_events['event_month'].dt.year - df_events['cohort_month'].dt.year) * 12 + \\
                            (df_events['event_month'].dt.month - df_events['cohort_month'].dt.month)

# 3. Create Pivot Table
cohort_matrix = df_events.pivot_table(
    index='cohort_month',
    columns='month_index',
    values='user_id',
    aggfunc='nunique'
)
print(cohort_matrix)""",
        "hint": {
            "en": "Use pivot_table with nunique aggregation",
            "uk": "Використайте pivot_table з агрегацією nunique"
        }
    },
    {
        "id": 10,
        "title": {
            "en": "ML Pipeline (Imputation & Scaling)",
            "uk": "ML Pipeline (масштабування та кодування)"
        },
        "type": "PYTHON",
        "difficulty": "Medium",
        "category": "Python Data Science",
        "description": {
            "en": "Build a scikit-learn ColumnTransformer to apply StandardScaler to numerical columns and OneHotEncoder to categorical columns.",
            "uk": "Створіть Pipeline, який масштабує числові ознаки та робить One-Hot Encoding для категоріальних."
        },
        "tables": [],
        "starter_code": "",
        "solution": """from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

numeric_features = ['age', 'recency']
categorical_features = ['country', 'channel']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ])

# X_train is your dataframe
X_processed = preprocessor.fit_transform(X_train)""",
        "hint": {
            "en": "Use ColumnTransformer with transformers list",
            "uk": "Використайте ColumnTransformer зі списком transformers"
        }
    },
    {
        "id": 11,
        "title": {
            "en": "Handle Class Imbalance (SMOTE)",
            "uk": "Балансування класів (SMOTE)"
        },
        "type": "PYTHON",
        "difficulty": "Medium",
        "category": "Python Data Science",
        "description": {
            "en": "Perform Random Oversampling on the minority class (fraud/churn) to equalize class distribution.",
            "uk": "Зробіть Random Oversampling для міноритарного класу, щоб збалансувати датасет."
        },
        "tables": [],
        "starter_code": "",
        "solution": """majority = df_train[df_train['target'] == 0]
minority = df_train[df_train['target'] == 1]

# Oversample minority
minority_upsampled = minority.sample(n=len(majority), replace=True, random_state=42)

# Combine and shuffle
df_balanced = pd.concat([majority, minority_upsampled]).sample(frac=1).reset_index(drop=True)""",
        "hint": {
            "en": "Use pandas.sample() with replace=True",
            "uk": "Використайте pandas.sample() з replace=True"
        }
    },
    {
        "id": 12,
        "title": {
            "en": "Feature Importance Extraction",
            "uk": "Витягування важливості ознак"
        },
        "type": "PYTHON",
        "difficulty": "Easy",
        "category": "Python Data Science",
        "description": {
            "en": "Train a RandomForest model and extract the top 3 most important features.",
            "uk": "Навчіть Random Forest та виведіть топ-3 найважливіші ознаки."
        },
        "tables": [],
        "starter_code": "",
        "solution": """from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42).fit(X_train, y_train)

importance_df = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)

print(importance_df.head(3))""",
        "hint": {
            "en": "Use model.feature_importances_ attribute",
            "uk": "Використайте атрибут model.feature_importances_"
        }
    },
]

# QUIZZES
QUIZZES = [
    {
        "id": "Q1",
        "question": {
            "en": "In what order does a SQL engine logically execute a query?",
            "uk": "У якому порядку SQL-рушій логічно виконує запит?"
        },
        "options": [
            "SELECT -> FROM -> WHERE -> GROUP BY -> ORDER BY",
            "FROM -> WHERE -> GROUP BY -> SELECT -> ORDER BY",
            "FROM -> SELECT -> WHERE -> GROUP BY -> ORDER BY",
            "SELECT -> WHERE -> FROM -> ORDER BY -> GROUP BY"
        ],
        "correct": 1,
        "explanation": {
            "en": "SQL execution order: FROM -> WHERE -> GROUP BY -> SELECT -> ORDER BY",
            "uk": "Порядок виконання SQL: FROM -> WHERE -> GROUP BY -> SELECT -> ORDER BY"
        }
    },
    {
        "id": "Q2",
        "question": {
            "en": "What is the main difference between WHERE and HAVING?",
            "uk": "Яка головна різниця між WHERE та HAVING?"
        },
        "options": [
            "WHERE is used for text, HAVING is used for numbers",
            "HAVING filters rows before grouping",
            "WHERE filters individual rows, HAVING filters aggregated groups",
            "There is no difference"
        ],
        "correct": 2,
        "explanation": {
            "en": "WHERE filters rows before grouping, HAVING filters after aggregation",
            "uk": "WHERE фільтрує рядки до групування, HAVING — після агрегації"
        }
    },
    {
        "id": "Q3",
        "question": {
            "en": "Which Window Function assigns a unique, sequential integer to rows?",
            "uk": "Яка віконна функція призначає унікальне послідовне число рядкам?"
        },
        "options": [
            "RANK()",
            "DENSE_RANK()",
            "ROW_NUMBER()",
            "NTILE()"
        ],
        "correct": 2,
        "explanation": {
            "en": "ROW_NUMBER() assigns unique sequential numbers regardless of value ties",
            "uk": "ROW_NUMBER() призначає унікальні послідовні номери незалежно від однакових значень"
        }
    },
]

def get_all_problems():
    return PROBLEMS

def get_all_quizzes():
    return QUIZZES

def get_problem_by_id(problem_id):
    for problem in PROBLEMS:
        if problem["id"] == problem_id:
            return problem
    return None
