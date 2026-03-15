"""
SQL & Python Interview Trainer - COMPLETE PROBLEMS DATABASE v4.0
All 97 tasks with full data from tasks.pdf
"""

import os
import json

PROBLEMS = []

# ==================== SQL JUNIOR (1-35) ====================
sql_junior_tasks = [
    (1, "Total Users", "Всього користувачів", "Count all unique users in the system.", "Порахуйте всіх унікальних користувачів.", "users", "SELECT COUNT(user_id) FROM users;", "Easy"),
    (2, "DAU", "DAU", "Count unique users who performed any action today.", "Кількість унікальних активних користувачів за день.", "events", "SELECT DATE(event_time), COUNT(DISTINCT user_id) FROM events GROUP BY 1;", "Easy"),
    (3, "Platform Split", "Розподіл по платформах", "How is our audience distributed by device type?", "Як розподілена наша аудиторія за типом пристроїв?", "users", "SELECT platform, COUNT(*) FROM users GROUP BY 1;", "Easy"),
    (4, "Top Countries", "Топ країни", "Find the Top 5 countries by user count.", "Знайдіть Топ-5 країн за кількістю користувачів.", "users", "SELECT country, COUNT(*) FROM users GROUP BY 1 ORDER BY 2 DESC LIMIT 5;", "Easy"),
    (5, "Total Revenue", "Загальна виручка", "Calculate total money earned from all orders.", "Розрахуйте загальну виручку від усіх замовлень.", "orders", "SELECT SUM(amount) FROM orders;", "Easy"),
    (6, "ARPU", "ARPU", "Average revenue per unique user who made a purchase.", "Середній дохід на одного унікального покупця.", "orders", "SELECT SUM(amount)/COUNT(DISTINCT user_id) FROM orders;", "Medium"),
    (7, "Avg Order Value", "Середній чек", "Calculate the average check amount (AOV).", "Розрахуйте середню суму чека (AOV).", "orders", "SELECT AVG(amount) FROM orders;", "Easy"),
    (8, "High-Value Orders", "Великі замовлення", "Find all orders with a price higher than 500.", "Знайдіть усі замовлення на суму понад 500.", "orders", "SELECT * FROM orders WHERE amount > 500;", "Easy"),
    (9, "Unique Buyers", "Унікальні покупці", "How many unique users have placed at least one order?", "Скільки унікальних юзерів зробили хоча б одне замовлення?", "orders", "SELECT COUNT(DISTINCT user_id) FROM orders;", "Easy"),
    (10, "Orders by Day", "Замовлення по дням", "Count successful orders for each day.", "Порахуйте кількість замовлень для кожного дня.", "orders", "SELECT order_date, COUNT(*) FROM orders GROUP BY 1;", "Easy"),
    (11, "Rev by Country", "Виручка по країнах", "Which countries generate the most revenue?", "Які країни генерують найбільшу виручку?", "users,orders", "SELECT u.country, SUM(o.amount) FROM users u JOIN orders o ON u.user_id=o.user_id GROUP BY 1 ORDER BY 2 DESC;", "Medium"),
    (12, "Zero-Order Users", "Користувачі без замовлень", "Find users who registered but never bought anything.", "Знайдіть тих, хто зареєструвався, але нічого не купив.", "users,orders", "SELECT u.user_id FROM users u LEFT JOIN orders o ON u.user_id=o.user_id WHERE o.order_id IS NULL;", "Medium"),
    (13, "Rev per User", "Виручка на юзера", "Total amount spent by each specific user.", "Загальна сума витрат кожного конкретного юзера.", "orders", "SELECT user_id, SUM(amount) FROM orders GROUP BY 1;", "Easy"),
    (14, "First Order Date", "Дата першого замовлення", "Find the date of the very first order for each client.", "Знайдіть дату найпершого замовлення для кожного клієнта.", "orders", "SELECT user_id, MIN(order_date) FROM orders GROUP BY 1;", "Easy"),
    (15, "Monthly Revenue", "Місячна виручка", "Calculate revenue grouped by month.", "Розрахуйте виручку, згруповану за місяцями.", "orders", "SELECT DATE_TRUNC('month', order_date), SUM(amount) FROM orders GROUP BY 1;", "Medium"),
    (16, "Conversion Step 1", "Конверсія - Крок 1", "What % of users from the 'USA' made a purchase?", "Який % користувачів із 'USA' зробив покупку?", "users,orders", "SELECT COUNT(DISTINCT o.user_id)*100.0/COUNT(DISTINCT u.user_id) FROM users u LEFT JOIN orders o ON u.user_id=o.user_id WHERE u.country='USA';", "Medium"),
    (17, "Loyal Users", "Лояльні юзери", "List users who made more than 5 orders.", "Виведіть список юзерів, які зробили понад 5 замовлень.", "orders", "SELECT user_id FROM orders GROUP BY 1 HAVING COUNT(*) > 5;", "Easy"),
    (18, "Platform ARPU", "ARPU по платформах", "Calculate ARPU separately for iOS and Android.", "Розрахуйте ARPU окремо для iOS та Android.", "users,orders", "SELECT u.platform, SUM(o.amount)/COUNT(DISTINCT u.user_id) FROM users u JOIN orders o ON u.user_id=o.user_id GROUP BY 1;", "Medium"),
    (19, "Late Night Orders", "Нічні замовлення", "Count orders placed between 00:00 and 04:00.", "Порахуйте замовлення, зроблені між 00:00 та 04:00.", "orders", "SELECT COUNT(*) FROM orders WHERE EXTRACT(HOUR FROM order_date) BETWEEN 0 AND 4;", "Easy"),
    (20, "Organic vs Paid", "Органіка vs Платні", "Count users who came from 'organic' source vs others.", "Порахуйте кількість 'organic' юзерів проти платних.", "users", "SELECT CASE WHEN utm_source='organic' THEN 'organic' ELSE 'paid' END, COUNT(*) FROM users GROUP BY 1;", "Easy"),
    (21, "Big Spenders", "Великі покупці", "Find users whose average order value is > 200.", "Знайдіть юзерів, чий середній чек вище 200.", "orders", "SELECT user_id FROM orders GROUP BY 1 HAVING AVG(amount) > 200;", "Easy"),
    (22, "Weekly Reg Trend", "Тижневий тренд реєстрацій", "Count new registrations by week.", "Порахуйте кількість нових реєстрацій за тижнями.", "users", "SELECT DATE_TRUNC('week', reg_date), COUNT(*) FROM users GROUP BY 1;", "Easy"),
    (23, "Repeat Purchase", "Повторні покупки", "Count how many users bought something more than once.", "Порахуйте, скільки юзерів купували щось більше одного разу.", "orders", "SELECT COUNT(*) FROM (SELECT user_id FROM orders GROUP BY 1 HAVING COUNT(*) > 1) t;", "Medium"),
    (24, "Order Rank", "Ранг замовлень", "Assign a sequential number to each user's orders.", "Присвойте порядковий номер кожному замовленню юзера.", "orders", "SELECT *, ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY order_date) FROM orders;", "Medium"),
    (25, "Active Days", "Активні дні", "How many unique days was each user active?", "Скільки унікальних днів був активний кожен юзер?", "events", "SELECT user_id, COUNT(DISTINCT DATE(event_time)) FROM events GROUP BY 1;", "Easy"),
    (26, "Most Active Hour", "Найактивніша година", "At what hour do we have the most events?", "У яку годину ми маємо найбільше подій?", "events", "SELECT EXTRACT(HOUR FROM event_time), COUNT(*) FROM events GROUP BY 1 ORDER BY 2 DESC LIMIT 1;", "Easy"),
    (27, "Multi-Platform", "Мультиплатформні юзери", "Find users who have logged in from more than 1 platform.", "Знайдіть юзерів, які заходили з більш ніж однієї платформи.", "users", "SELECT user_id FROM users GROUP BY 1 HAVING COUNT(DISTINCT platform) > 1;", "Medium"),
    (28, "Avg Events/User", "Середні події/юзер", "Calculate the average number of events per user.", "Розрахуйте середню кількість подій на одного юзера.", "events", "SELECT COUNT(*)/COUNT(DISTINCT user_id) FROM events;", "Easy"),
    (29, "Rev from Twitter", "Виручка з Twitter", "Total revenue from users who came from 'twitter'.", "Виручка від юзерів, які прийшли з 'twitter'.", "users,orders", "SELECT SUM(amount) FROM orders o JOIN users u ON o.user_id=u.user_id WHERE u.utm_source='twitter';", "Medium"),
    (30, "Weekend Revenue", "Виручка вихідних", "Calculate total revenue generated on Saturdays and Sundays.", "Розрахуйте виручку, отриману в суботу та неділю.", "orders", "SELECT SUM(amount) FROM orders WHERE EXTRACT(DOW FROM order_date) IN (0,6);", "Easy"),
    (31, "Country Lead", "Лідер країн", "Which country had the most registrations last month?", "У якій країні було найбільше реєстрацій минулого місяця?", "users", "SELECT country, COUNT(*) FROM users WHERE reg_date > CURRENT_DATE - INTERVAL '1 month' GROUP BY 1 ORDER BY 2 DESC LIMIT 1;", "Medium"),
    (32, "Missing Source", "Відсутній source", "Find the % of users with missing utm_source.", "Знайдіть % користувачів, у яких відсутнє utm_source.", "users", "SELECT COUNT(CASE WHEN utm_source IS NULL THEN 1 END)*100.0/COUNT(*) FROM users;", "Medium"),
    (33, "Top Event Type", "Топ тип події", "Which event type is the most common?", "Який тип події є найпопулярнішим?", "events", "SELECT event_type, COUNT(*) FROM events GROUP BY 1 ORDER BY 2 DESC LIMIT 1;", "Easy"),
    (34, "High Rev Day", "День з макс. виручкою", "Find the day with the maximum total revenue.", "Знайдіть день з максимальною сумарною виручкою.", "orders", "SELECT order_date, SUM(amount) FROM orders GROUP BY 1 ORDER BY 2 DESC LIMIT 1;", "Easy"),
    (35, "User Lifespan", "Тривалість активності", "Find the number of days between reg and last event.", "Кількість днів між реєстрацією та останньою подією.", "users,events", "SELECT u.user_id, MAX(DATE(e.event_time)) - u.reg_date FROM users u JOIN events e ON u.user_id=e.user_id GROUP BY 1, u.reg_date;", "Medium"),
]

for task in sql_junior_tasks:
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
        "hint": {"en": "Use SQL aggregation and filtering functions", "uk": "Використайте SQL функції агрегації та фільтрації"}
    })

# ==================== SQL PRODUCT ANALYST (36-57) ====================
sql_product_tasks = [
    (36, "7-day Retention", "Retention 7-й день", "% of users active on their 7th day after signup.", "% юзерів, активних на 7-й день після реєстрації.", "users,events", "SELECT DATE(u.reg_date) as cohort, COUNT(DISTINCT e.user_id) as returned_users FROM users u JOIN events e ON u.user_id = e.user_id WHERE DATE(e.event_time) = DATE(u.reg_date) + 7 GROUP BY 1;", "Hard"),
    (37, "Second Purchase", "Друга покупка", "Date and amount of each user's second order.", "Дата та сума другого замовлення кожного юзера.", "orders", "SELECT * FROM (SELECT *, RANK() OVER(PARTITION BY user_id ORDER BY order_date) r FROM orders) t WHERE r=2;", "Medium"),
    (38, "Rolling Revenue", "Ковзна виручка", "7-day rolling average of daily revenue.", "7-денне ковзне середнє денної виручки.", "orders", "SELECT order_date, AVG(SUM(amount)) OVER(ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) FROM orders GROUP BY 1;", "Hard"),
    (39, "Time to Value", "Час до цінності", "Median time from signup to first purchase.", "Медіанний час від реєстрації до першої покупки.", "users,orders", "SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY gap) FROM (SELECT u.user_id, MIN(o.order_date)-u.reg_date as gap FROM users u JOIN orders o USING(user_id) GROUP BY 1, u.reg_date) t;", "Hard"),
    (40, "Funnel: V -> C -> B", "Воронка", "Strict funnel conversion: View -> Cart -> Buy.", "Конверсія воронки: Перегляд -> Кошик -> Купівля.", "events", "SELECT event_type, COUNT(DISTINCT user_id) FROM events WHERE event_type IN ('view','cart','buy') GROUP BY 1;", "Medium"),
    (41, "Top Product/Country", "Топ товар/країна", "Most popular product in each country.", "Найпопулярніший товар у кожній країні.", "orders,users", "SELECT country, product FROM (SELECT country, product, RANK() OVER(PARTITION BY country ORDER BY COUNT(*) DESC) r FROM orders JOIN users USING(user_id) GROUP BY 1,2) t WHERE r=1;", "Hard"),
    (42, "Sessions", "Сесії", "Identify session starts (gap > 30 mins).", "Визначте початок сесій (пауза > 30 хв).", "events", "SELECT *, CASE WHEN event_time - LAG(event_time) OVER(PARTITION BY user_id ORDER BY event_time) > INTERVAL '30 min' THEN 1 ELSE 0 END as is_new_session FROM events;", "Hard"),
    (43, "30-day LTV", "LTV 30 днів", "Total revenue from user within 30 days of reg.", "Сумарна виручка з юзера за перші 30 днів.", "users,orders", "SELECT u.user_id, SUM(o.amount) FROM users u JOIN orders o ON u.user_id=o.user_id WHERE o.order_date <= u.reg_date + INTERVAL '30 days' GROUP BY 1;", "Hard"),
    (44, "Churn Rate", "Churn Rate", "% of users active last month but not this month.", "% юзерів, активних минулого місяця, але не цього.", "events", "SELECT (COUNT(DISTINCT prev.user_id) - COUNT(DISTINCT curr.user_id))*100.0/COUNT(DISTINCT prev.user_id) FROM active_last_month prev LEFT JOIN active_this_month curr USING(user_id);", "Hard"),
    (45, "MoM Growth", "Зростання MoM", "Revenue growth % compared to previous month.", "% зростання виручки порівняно з минулим місяцем.", "orders", "SELECT month, (rev - LAG(rev) OVER(ORDER BY month))/LAG(rev) OVER(ORDER BY month) FROM monthly_rev;", "Hard"),
    (46, "Repeat Rate", "Частота повторень", "% of customers who have more than 1 order.", "% покупців, які мають більше 1 замовлення.", "orders", "SELECT COUNT(CASE WHEN cnt > 1 THEN 1 END)*100.0/COUNT(*) FROM (SELECT user_id, COUNT(*) as cnt FROM orders GROUP BY 1) t;", "Medium"),
    (47, "Cumulative Spend", "Накопичувальні витрати", "Running total of revenue for each user over time.", "Накопичувальна сума виручки для кожного юзера.", "orders", "SELECT user_id, order_date, SUM(amount) OVER(PARTITION BY user_id ORDER BY order_date) FROM orders;", "Medium"),
    (48, "Reactivation", "Реактивація", "Users who returned after > 30 days of inactivity.", "Юзери, які повернулися після > 30 днів неактивності.", "events", "SELECT user_id FROM (SELECT user_id, event_time - LAG(event_time) OVER(PARTITION BY user_id ORDER BY event_time) as gap FROM events) t WHERE gap > INTERVAL '30 days';", "Hard"),
    (49, "Top 1% Spenders", "Топ 1% покупців", "Find the top 1% of users by total spend.", "Знайдіть топ-1% юзерів за сумою витрат.", "orders", "SELECT user_id FROM (SELECT user_id, PERCENT_RANK() OVER(ORDER BY SUM(amount) DESC) as rnk FROM orders GROUP BY 1) t WHERE rnk <= 0.01;", "Hard"),
    (50, "Platform Stickiness", "Стікінес платформи", "DAU/MAU ratio for each platform.", "Стікінес (DAU/MAU) для кожної платформи.", "events", "SELECT platform, AVG(daily_users)/monthly_users FROM platform_stats GROUP BY 1, monthly_users;", "Hard"),
    (51, "Order Frequency", "Частота замовлень", "Avg number of days between orders for repeat users.", "Сер. кількість днів між замовленнями для повторних покупців.", "orders", "SELECT user_id, AVG(diff) FROM (SELECT user_id, order_date - LAG(order_date) OVER(PARTITION BY user_id ORDER BY order_date) as diff FROM orders) t GROUP BY 1;", "Hard"),
    (52, "First Source", "Перше джерело", "For users with multiple sources, find the first one.", "Для юзерів з кількома джерелами знайдіть найперше.", "users", "SELECT user_id, utm_source FROM (SELECT *, ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY reg_date) r FROM users) t WHERE r=1;", "Medium"),
    (53, "High-Value Cohorts", "Цінні когорти", "Which reg_month cohort has the highest 90-day LTV?", "Когорта якого місяця має найвищий 90-денний LTV?", "users,orders", "SELECT DATE_TRUNC('month', reg_date), SUM(amount)/COUNT(DISTINCT u.user_id) as ltv90 FROM users u JOIN orders o ON u.user_id=o.user_id WHERE o.order_date <= u.reg_date + INTERVAL '90 days' GROUP BY 1 ORDER BY 2 DESC LIMIT 1;", "Hard"),
    (54, "Event Velocity", "Швидкість подій", "Users who did > 10 events in their first hour.", "Юзери, що здійснили > 10 подій у свою першу годину.", "events,users", "SELECT e.user_id FROM events e JOIN users u USING(user_id) WHERE e.event_time <= u.reg_date + INTERVAL '1 hour' GROUP BY 1 HAVING COUNT(*) > 10;", "Hard"),
    (55, "Country Penetration", "Проникнення по країнах", "% of total users represented by each country.", "% від загальної кількості юзерів для кожної країни.", "users", "SELECT country, COUNT(*)*100.0 / SUM(COUNT(*)) OVER() FROM users GROUP BY 1;", "Medium"),
    (56, "Last Click", "Останній клік", "Find the last utm_source before the first order.", "Знайдіть останній utm_source перед першою покупкою.", "events,orders", "SELECT user_id, utm_source FROM (SELECT u.user_id, u.utm_source, ROW_NUMBER() OVER(PARTITION BY u.user_id ORDER BY u.reg_date DESC) r FROM users u JOIN orders o USING(user_id) WHERE u.reg_date < o.order_date) t WHERE r=1;", "Hard"),
    (57, "Revenue Pareto", "Парето виручки", "Does 20% of users bring 80% of revenue?", "Чи приносять 20% юзерів 80% виручки?", "orders", "SELECT user_id, SUM(amount) OVER(ORDER BY SUM(amount) DESC) / SUM(SUM(amount)) OVER() FROM orders GROUP BY 1;", "Hard"),
]

for task in sql_product_tasks:
    PROBLEMS.append({
        "id": task[0],
        "title": {"en": task[1], "uk": task[2]},
        "type": "SQL",
        "difficulty": task[7],
        "category": "SQL Product Analyst",
        "description": {"en": task[3], "uk": task[4]},
        "tables": task[5].split(','),
        "starter_code": "",
        "solution": task[6],
        "hint": {"en": "Use window functions and CTEs", "uk": "Використайте віконні функції та CTE"}
    })

# ==================== PYTHON JUNIOR PRODUCT ANALYST (58-75) ====================
python_junior_tasks = [
    (58, "Clean UTM", "Очистка UTM", "Fill NaNs in utm_source with 'organic'.", "Заповніть пропуски в utm_source значенням 'organic'.", "df_users", "df['utm_source'].fillna('organic')", "Easy"),
    (59, "Pandas DAU", "Pandas DAU", "Calculate DAU using nunique().", "Розрахуйте DAU через nunique().", "df_events", "df.groupby(df['event_time'].dt.date)['user_id'].nunique()", "Easy"),
    (60, "Merge users/orders", "Злиття users/orders", "Inner join users and orders.", "Внутрішнє об'єднання юзерів та замовлень.", "df_users,df_orders", "pd.merge(df_u, df_o, on='user_id')", "Easy"),
    (61, "ARPU Calculation", "Розрахунок ARPU", "Sum of revenue / count of unique users.", "Сума виручки / кількість унікальних юзерів.", "df_orders", "df_o['amount'].sum() / df_u['user_id'].nunique()", "Easy"),
    (62, "Rev by Platform", "Виручка по платформах", "Distribution of total revenue by platform.", "Розподіл виручки за платформами.", "df_merged", "df_uo.groupby('platform')['amount'].sum()", "Easy"),
    (63, "Conversion Rate", "Конверсія", "Conversion from 'view' event to 'cart' event.", "Конверсія з події 'view' у подію 'cart'.", "df_events", "df[df['type']=='cart']['id'].nunique() / df[df['type']=='view']['id'].nunique()", "Medium"),
    (64, "Parse JSON", "Парсинг JSON", "Extract 'price' from JSON string in params.", "Витягніть 'price' з JSON-рядка в params.", "df_events", "df['params'].apply(lambda x: json.loads(x).get('price'))", "Medium"),
    (65, "Drop Duplicates", "Видалення дублікатів", "Remove identical rows from events.", "Видаліть ідентичні рядки з подій.", "df_events", "df.drop_duplicates()", "Easy"),
    (66, "T-test Revenue", "T-тест виручки", "Is revenue difference between A and B significant?", "Чи є різниця у виручці між A та B значущою?", "df_ab", "from scipy import stats\nrev_a = df[df['group']=='A']['revenue']\nrev_b = df[df['group']=='B']['revenue']\nt_stat, p_val = stats.ttest_ind(rev_a, rev_b)\nis_significant = p_val < 0.05", "Hard"),
    (67, "Day 1 Retention", "Retention День 1", "% of users returning on the next day after signup.", "% юзерів, що повернулися наступного дня після рег.", "df_events", "# Groupby user + diff\ndf.groupby('user_id')['event_time'].apply(lambda x: (x.dt.date.nunique() > 1))", "Hard"),
    (68, "Pivot Platform", "Зведена таблиця", "Create pivot: Country as index, Platform as columns.", "Зведена таблиця: Країна — індекс, Платформа — колонки.", "df_users", "df.pivot_table(index='country', columns='platform', aggfunc='size')", "Medium"),
    (69, "Revenue Outliers", "Аномалії виручки", "Find orders with amount > 3 standard deviations.", "Знайдіть замовлення з сумою > 3 стандартних відхилень.", "df_orders", "df[df['amount'] > df['amount'].mean() + 3*df['amount'].std()]", "Medium"),
    (70, "Resample Weekly", "Тижнева агрегація", "Aggregate daily revenue into weekly revenue.", "Агрегуйте денну виручку в тижневу.", "df_orders", "df.resample('W', on='order_date')['amount'].sum()", "Medium"),
    (71, "String Cleaning", "Очистка рядків", "Normalize utm_source (lowercase, strip spaces).", "Нормалізуйте utm_source (нижній регістр, без пробілів).", "df_users", "df['utm_source'].str.lower().str.strip()", "Easy"),
    (72, "User Cohorts", "Когорти юзерів", "Assign a 'cohort' month to each user.", "Присвойте місяць-когорту кожному юзеру.", "df_users", "df['reg_date'].dt.to_period('M')", "Easy"),
    (73, "Cumulative Sum", "Накопичувальна сума", "Add a column with cumulative revenue per user.", "Додайте колонку з накопичувальною виручкою на юзера.", "df_orders", "df.groupby('user_id')['amount'].cumsum()", "Medium"),
    (74, "Feature Cross", "Комбінування ознак", "Combine 'Platform' and 'Country' into one feature.", "Об'єднайте 'Платформу' та 'Країну' в одну ознаку.", "df_users", "df['plat_country'] = df['platform'] + '_' + df['country']", "Easy"),
    (75, "Correlation", "Кореляція", "Find correlation between user age and total spend.", "Знайдіть кореляцію між віком юзера та витратами.", "df_dataset", "df['age'].corr(df['total_spent'])", "Medium"),
]

for task in python_junior_tasks:
    PROBLEMS.append({
        "id": task[0],
        "title": {"en": task[1], "uk": task[2]},
        "type": "PYTHON",
        "difficulty": task[7],
        "category": "Python Junior",
        "description": {"en": task[3], "uk": task[4]},
        "tables": task[5].split(','),
        "starter_code": "",
        "solution": task[6],
        "hint": {"en": "Use pandas methods", "uk": "Використайте методи pandas"}
    })

# ==================== PYTHON DATA SCIENTIST (76-92) ====================
python_ds_tasks = [
    (76, "Train/Test Split", "Розподіл Train/Test", "Split data 80/20 for modeling.", "Розділіть дані 80/20 для моделювання.", "from sklearn.model_selection import train_test_split\ntrain_test_split(X, y, test_size=0.2)", "Medium"),
    (77, "One-Hot Encoding", "One-Hot Кодування", "Convert 'Country' into dummy variables.", "Перетворіть 'Країну' у dummy-змінні.", "pd.get_dummies(df['country'])", "Easy"),
    (78, "Fill Median", "Заповнення медіаною", "Fill missing values in 'Score' with median.", "Заповніть пропуски в 'Score' медіаною.", "df['score'].fillna(df['score'].median())", "Easy"),
    (79, "Standardization", "Стандартизація", "Scale features to 0 mean and 1 variance.", "Масштабуйте ознаки до середнього 0 і дисперсії 1.", "from sklearn.preprocessing import StandardScaler\nStandardScaler().fit_transform(X)", "Medium"),
    (80, "Logistic Reg", "Логістична регресія", "Train model to predict churn (Yes/No).", "Навчіть модель прогнозувати відтік (Так/Ні).", "from sklearn.linear_model import LogisticRegression\nLogisticRegression().fit(X_train, y_train)", "Medium"),
    (81, "Accuracy/Rec/Prec", "Метрики класифікації", "Calculate key classification metrics.", "Розрахуйте ключові метрики класифікації.", "from sklearn.metrics import classification_report\nclassification_report(y_true, y_pred)", "Medium"),
    (82, "Oversampling", "Оверсемплінг", "Balance classes using RandomOverSampler.", "Збалансуйте класи через RandomOverSampler.", "from imblearn.over_sampling import RandomOverSampler\nRandomOverSampler().fit_resample(X, y)", "Hard"),
    (83, "ROC-AUC", "ROC-AUC", "Calculate area under the ROC curve.", "Розрахуйте площу під ROC-кривою.", "from sklearn.metrics import roc_auc_score\nroc_auc_score(y_test, y_probs)", "Medium"),
    (84, "Feature Import.", "Важливість ознак", "Find which features affect the model most.", "Знайдіть найважливіші ознаки для моделі.", "model.feature_importances_", "Medium"),
    (85, "GridSearch", "GridSearch", "Find optimal hyperparameters using GridSearchCV.", "Знайдіть оптимальні гіперпараметри через GridSearchCV.", "from sklearn.model_selection import GridSearchCV\nGridSearchCV(estimator, param_grid, cv=5).fit(X, y)", "Hard"),
    (86, "Confusion Matrix", "Матриця помилок", "Build a confusion matrix for the model.", "Побудуйте матрицю помилок для моделі.", "from sklearn.metrics import confusion_matrix\nconfusion_matrix(y_true, y_pred)", "Medium"),
    (87, "Label Encoding", "Label Encoding", "Encode categorical labels to integers.", "Закодуйте категоріальні мітки у цілі числа.", "from sklearn.preprocessing import LabelEncoder\nLabelEncoder().fit_transform(df['category'])", "Easy"),
    (88, "Cross-Validation", "Крос-валідація", "Evaluate model stability using k-fold CV.", "Оцініть стабільність моделі через k-fold CV.", "from sklearn.model_selection import cross_val_score\ncross_val_score(model, X, y, cv=5)", "Hard"),
    (89, "Decision Tree", "Дерево рішень", "Train a Decision Tree classifier.", "Навчіть класифікатор Дерево рішень.", "from sklearn.tree import DecisionTreeClassifier\nDecisionTreeClassifier().fit(X_train, y_train)", "Medium"),
    (90, "Random Forest", "Випадковий ліс", "Train a Random Forest for classification.", "Навчіть Випадковий ліс для класифікації.", "from sklearn.ensemble import RandomForestClassifier\nRandomForestClassifier(n_estimators=100).fit(X_train, y_train)", "Medium"),
    (91, "Feature Scaling", "Масштабування", "Apply MinMax scaling to numeric features.", "Застосуйте MinMax масштабування до числових ознак.", "from sklearn.preprocessing import MinMaxScaler\nMinMaxScaler().fit_transform(X)", "Easy"),
    (92, "Imputation", "Заповнення пропусків", "Fill missing numerical values with median imputer.", "Заповніть пропуски числових ознак через медіанний imputor.", "from sklearn.impute import SimpleImputer\nSimpleImputer(strategy='median').fit_transform(X)", "Medium"),
]

for i, task in enumerate(python_ds_tasks, start=76):
    PROBLEMS.append({
        "id": i,
        "title": {"en": task[1], "uk": task[2]},
        "type": "PYTHON",
        "difficulty": task[5],
        "category": "Python Data Scientist",
        "description": {"en": task[3], "uk": task[4]},
        "tables": ["df_dataset"],
        "starter_code": "",
        "solution": task[6],
        "hint": {"en": "Use scikit-learn library", "uk": "Використайте бібліотеку scikit-learn"}
    })

# ==================== MIDDLE SPECIALIST (93-97) ====================
middle_tasks = [
    {
        "id": 93, "title": {"en": "Sticky Factor", "uk": "Sticky Factor"},
        "type": "SQL", "difficulty": "Hard", "category": "Middle Specialist",
        "description": {"en": "Calculate DAU/MAU for January 2024.", "uk": "Розрахуйте DAU/MAU за січень 2024."},
        "tables": ["events"], "starter_code": "",
        "solution": "SELECT\n    COUNT(DISTINCT CASE WHEN DATE(event_time) = '2024-01-15' THEN user_id END) * 100.0 /\n    COUNT(DISTINCT CASE WHEN DATE_TRUNC('month', event_time) = '2024-01-01' THEN user_id END) as sticky_factor\nFROM events\nWHERE DATE_TRUNC('month', event_time) = '2024-01-01';",
        "hint": {"en": "Use conditional COUNT with CASE WHEN", "uk": "Використайте умовний COUNT з CASE WHEN"}
    },
    {
        "id": 94, "title": {"en": "2nd Max Order", "uk": "2-ге максимальне"},
        "type": "SQL", "difficulty": "Hard", "category": "Middle Specialist",
        "description": {"en": "Find the 2nd highest order without LIMIT.", "uk": "Знайдіть 2-ге за сумою замовлення без LIMIT."},
        "tables": ["orders"], "starter_code": "",
        "solution": "SELECT MAX(amount) FROM orders WHERE amount < (SELECT MAX(amount) FROM orders);",
        "hint": {"en": "Use a subquery to exclude the maximum", "uk": "Використайте підзапит для виключення максимуму"}
    },
    {
        "id": 95, "title": {"en": "Top 2 / Country", "uk": "Топ-2 по країнах"},
        "type": "SQL", "difficulty": "Hard", "category": "Middle Specialist",
        "description": {"en": "Find the two largest orders in each country.", "uk": "Знайдіть два найбільші замовлення в кожній країні."},
        "tables": ["users", "orders"], "starter_code": "",
        "solution": "WITH t AS (\n    SELECT u.country, o.order_id, o.amount,\n           RANK() OVER(PARTITION BY u.country ORDER BY o.amount DESC) as r\n    FROM orders o\n    JOIN users u USING(user_id)\n)\nSELECT country, order_id, amount FROM t WHERE r <= 2;",
        "hint": {"en": "Use RANK() window function with PARTITION BY country", "uk": "Використайте RANK() з PARTITION BY country"}
    },
    {
        "id": 96, "title": {"en": "A/B Significance", "uk": "Значущість A/B"},
        "type": "PYTHON", "difficulty": "Hard", "category": "Middle Specialist",
        "description": {"en": "Perform T-test for A/B group revenue.", "uk": "Проведіть T-тест для виручки груп A/B."},
        "tables": ["df_ab"], "starter_code": "",
        "solution": "from scipy import stats\nrev_a = df[df['group']=='A']['revenue']\nrev_b = df[df['group']=='B']['revenue']\nt_stat, p_val = stats.ttest_ind(rev_a, rev_b)\nprint(f'p-value: {p_val:.4f}, significant: {p_val < 0.05}')",
        "hint": {"en": "Use scipy.stats.ttest_ind", "uk": "Використайте scipy.stats.ttest_ind"}
    },
    {
        "id": 97, "title": {"en": "Cohort Matrix", "uk": "Когортна матриця"},
        "type": "PYTHON", "difficulty": "Hard", "category": "Middle Specialist",
        "description": {"en": "Full Month-on-Month retention pivot table.", "uk": "Повна зведена таблиця ретеншн за когортами."},
        "tables": ["df_events"], "starter_code": "",
        "solution": "df.pivot_table(\n    index='cohort',\n    columns='month_idx',\n    values='user_id',\n    aggfunc='nunique'\n)",
        "hint": {"en": "Use pivot_table with cohort as index", "uk": "Використайте pivot_table з cohort як індексом"}
    },
]

for task in middle_tasks:
    PROBLEMS.append(task)


# ==================== QUIZZES ====================
QUIZZES = [
    {
        "id": 1,
        "question": {"en": "What does DAU stand for?", "uk": "Що означає DAU?"},
        "options": ["Daily Active Users", "Data Analysis Unit", "Dynamic Access URL", "Daily Average Updates"],
        "correct": 0,
        "explanation": {"en": "DAU = Daily Active Users - unique users performing any action in one day.", "uk": "DAU = Daily Active Users - унікальні юзери, що виконали дію за день."}
    },
    {
        "id": 2,
        "question": {"en": "Which SQL function finds duplicate-free ranking (no gaps)?", "uk": "Яка SQL функція дає унікальний ранг без пропусків?"},
        "options": ["RANK()", "ROW_NUMBER()", "DENSE_RANK()", "NTILE()"],
        "correct": 2,
        "explanation": {"en": "DENSE_RANK() assigns consecutive ranks with no gaps even when there are ties.", "uk": "DENSE_RANK() присвоює послідовні ранги без пропусків навіть при однакових значеннях."}
    },
    {
        "id": 3,
        "question": {"en": "What does LEFT JOIN return?", "uk": "Що повертає LEFT JOIN?"},
        "options": ["Only matching rows from both tables", "All rows from left table + matching from right", "All rows from both tables", "Only rows from right table"],
        "correct": 1,
        "explanation": {"en": "LEFT JOIN returns all rows from the left table and matched rows from the right table. Non-matches get NULL.", "uk": "LEFT JOIN повертає всі рядки з лівої таблиці та відповідні рядки з правої. Незбіги отримують NULL."}
    },
    {
        "id": 4,
        "question": {"en": "Which pandas method removes duplicate rows?", "uk": "Який метод pandas видаляє дублікати?"},
        "options": ["df.remove_duplicates()", "df.drop_duplicates()", "df.distinct()", "df.unique()"],
        "correct": 1,
        "explanation": {"en": "df.drop_duplicates() removes identical rows from a DataFrame.", "uk": "df.drop_duplicates() видаляє ідентичні рядки з DataFrame."}
    },
    {
        "id": 5,
        "question": {"en": "What is ARPU?", "uk": "Що таке ARPU?"},
        "options": ["Average Revenue Per Update", "Active Revenue Processing Unit", "Average Revenue Per User", "Annual Revenue Per User"],
        "correct": 2,
        "explanation": {"en": "ARPU = Average Revenue Per User = Total Revenue / Number of Users.", "uk": "ARPU = Average Revenue Per User = Загальна виручка / Кількість юзерів."}
    },
    {
        "id": 6,
        "question": {"en": "Which clause filters aggregated results?", "uk": "Який клаз фільтрує агреговані результати?"},
        "options": ["WHERE", "FILTER", "HAVING", "AND"],
        "correct": 2,
        "explanation": {"en": "HAVING filters groups created by GROUP BY, while WHERE filters individual rows before aggregation.", "uk": "HAVING фільтрує групи після GROUP BY, а WHERE фільтрує рядки до агрегації."}
    },
    {
        "id": 7,
        "question": {"en": "What does p-value < 0.05 mean in an A/B test?", "uk": "Що означає p-value < 0.05 в A/B тесті?"},
        "options": ["The test failed", "There is no difference", "The result is statistically significant", "The sample is too small"],
        "correct": 2,
        "explanation": {"en": "p-value < 0.05 means the probability of the observed difference by chance is less than 5%, so the result is statistically significant.", "uk": "p-value < 0.05 означає, що ймовірність випадкової різниці менше 5%, отже результат статистично значущий."}
    }
]


def get_all_problems():
    return PROBLEMS

def get_problem_by_id(problem_id):
    for p in PROBLEMS:
        if p.get("id") == problem_id:
            return p
    return None

def get_all_quizzes():
    return QUIZZES

def get_categories():
    cats = []
    seen = set()
    for p in PROBLEMS:
        c = p.get("category", "")
        if c and c not in seen:
            cats.append(c)
            seen.add(c)
    return cats

def add_problem(problem_data):
    try:
        from database import get_db
        conn = get_db()
        if conn:
            import json
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO problems (title, type, difficulty, category, description, tables, starter_code, solution, hint)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
            """, (
                json.dumps(problem_data["title"]),
                problem_data["type"],
                problem_data["difficulty"],
                problem_data["category"],
                json.dumps(problem_data["description"]),
                json.dumps(problem_data.get("tables", [])),
                problem_data.get("starter_code", ""),
                problem_data.get("solution", ""),
                json.dumps(problem_data.get("hint", {}))
            ))
            conn.commit()
            return cursor.fetchone()[0]
    except Exception as e:
        raise e
    return len(PROBLEMS) + 1

def add_quiz(quiz_data):
    try:
        from database import get_db
        conn = get_db()
        if conn:
            import json
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO quizzes (question, options, correct_answer, explanation)
                VALUES (%s, %s, %s, %s) RETURNING id
            """, (
                json.dumps(quiz_data["question"]),
                json.dumps(quiz_data["options"]),
                quiz_data["correct"],
                json.dumps(quiz_data["explanation"])
            ))
            conn.commit()
            return cursor.fetchone()[0]
    except Exception as e:
        raise e
    return len(QUIZZES) + 1
