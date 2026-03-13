"""
Problems definitions for SQL & Python Interview Trainer
"""

PROBLEMS = [
    # SQL Problems (1-50)
    {
        "id": 1,
        "title": "Top 5 customers by revenue",
        "type": "SQL",
        "difficulty": "Easy",
        "description": "Find the top 5 customers by total revenue. Return user_id and total_revenue, ordered by revenue descending.",
        "starter_code": "SELECT user_id, SUM(revenue) as total_revenue\nFROM orders\nGROUP BY user_id\nORDER BY total_revenue DESC\nLIMIT 5;",
        "solution": "SELECT user_id, SUM(revenue) as total_revenue\nFROM orders\nGROUP BY user_id\nORDER BY total_revenue DESC\nLIMIT 5;",
        "tables": ["orders"]
    },
    {
        "id": 2,
        "title": "First order date in dataset",
        "type": "SQL",
        "difficulty": "Easy",
        "description": "Find the earliest order date in the orders table.",
        "starter_code": "SELECT MIN(order_date) as first_order\nFROM orders;",
        "solution": "SELECT MIN(order_date) as first_order\nFROM orders;",
        "tables": ["orders"]
    },
    {
        "id": 3,
        "title": "Last order date",
        "type": "SQL",
        "difficulty": "Easy",
        "description": "Find the latest order date in the orders table.",
        "starter_code": "SELECT MAX(order_date) as last_order\nFROM orders;",
        "solution": "SELECT MAX(order_date) as last_order\nFROM orders;",
        "tables": ["orders"]
    },
    {
        "id": 4,
        "title": "Users with more than 10 orders",
        "type": "SQL",
        "difficulty": "Easy",
        "description": "Find all users who have placed more than 10 orders.",
        "starter_code": "SELECT user_id, COUNT(*) as order_count\nFROM orders\nGROUP BY user_id\nHAVING COUNT(*) > 10;",
        "solution": "SELECT user_id, COUNT(*) as order_count\nFROM orders\nGROUP BY user_id\nHAVING COUNT(*) > 10;",
        "tables": ["orders"]
    },
    {
        "id": 5,
        "title": "Calculate total revenue",
        "type": "SQL",
        "difficulty": "Easy",
        "description": "Calculate the total revenue from all orders.",
        "starter_code": "SELECT SUM(revenue) as total_revenue\nFROM orders;",
        "solution": "SELECT SUM(revenue) as total_revenue\nFROM orders;",
        "tables": ["orders"]
    },
    {
        "id": 6,
        "title": "Calculate average order value",
        "type": "SQL",
        "difficulty": "Easy",
        "description": "Calculate the average order value (revenue per order).",
        "starter_code": "SELECT AVG(revenue) as avg_order_value\nFROM orders;",
        "solution": "SELECT AVG(revenue) as avg_order_value\nFROM orders;",
        "tables": ["orders"]
    },
    {
        "id": 7,
        "title": "Orders greater than 500",
        "type": "SQL",
        "difficulty": "Easy",
        "description": "Find all orders with revenue greater than 500.",
        "starter_code": "SELECT *\nFROM orders\nWHERE revenue > 500;",
        "solution": "SELECT *\nFROM orders\nWHERE revenue > 500;",
        "tables": ["orders"]
    },
    {
        "id": 8,
        "title": "Count unique users",
        "type": "SQL",
        "difficulty": "Easy",
        "description": "Count the number of unique users who have placed orders.",
        "starter_code": "SELECT COUNT(DISTINCT user_id) as unique_users\nFROM orders;",
        "solution": "SELECT COUNT(DISTINCT user_id) as unique_users\nFROM orders;",
        "tables": ["orders"]
    },
    {
        "id": 9,
        "title": "Orders per day",
        "type": "SQL",
        "difficulty": "Easy",
        "description": "Calculate the number of orders per day.",
        "starter_code": "SELECT order_date, COUNT(*) as orders_count\nFROM orders\nGROUP BY order_date\nORDER BY order_date;",
        "solution": "SELECT order_date, COUNT(*) as orders_count\nFROM orders\nGROUP BY order_date\nORDER BY order_date;",
        "tables": ["orders"]
    },
    {
        "id": 10,
        "title": "Top 5 countries by revenue",
        "type": "SQL",
        "difficulty": "Medium",
        "description": "Find the top 5 countries by total revenue. Join users and orders tables.",
        "starter_code": "SELECT u.country, SUM(o.revenue) as total_revenue\nFROM users u\nJOIN orders o ON u.user_id = o.user_id\nGROUP BY u.country\nORDER BY total_revenue DESC\nLIMIT 5;",
        "solution": "SELECT u.country, SUM(o.revenue) as total_revenue\nFROM users u\nJOIN orders o ON u.user_id = o.user_id\nGROUP BY u.country\nORDER BY total_revenue DESC\nLIMIT 5;",
        "tables": ["users", "orders"]
    },
    
    # Python Problems (51-100)
    {
        "id": 51,
        "title": "Top 5 customers using pandas",
        "type": "PYTHON",
        "difficulty": "Easy",
        "description": "Find the top 5 customers by total revenue using pandas.",
        "starter_code": "import pandas as pd\n\norders = pd.read_csv('orders.csv')\n\nresult = (\n    orders\n    .groupby('user_id')['revenue']\n    .sum()\n    .sort_values(ascending=False)\n    .head(5)\n)\n\nprint(result)",
        "solution": "import pandas as pd\n\norders = pd.read_csv('orders.csv')\n\nresult = (\n    orders\n    .groupby('user_id')['revenue']\n    .sum()\n    .sort_values(ascending=False)\n    .head(5)\n)\n\nprint(result)",
        "tables": ["orders"]
    },
    {
        "id": 52,
        "title": "Calculate total revenue with pandas",
        "type": "PYTHON",
        "difficulty": "Easy",
        "description": "Calculate total revenue from all orders using pandas.",
        "starter_code": "import pandas as pd\n\norders = pd.read_csv('orders.csv')\n\ntotal = orders['revenue'].sum()\nprint(total)",
        "solution": "import pandas as pd\n\norders = pd.read_csv('orders.csv')\n\ntotal = orders['revenue'].sum()\nprint(total)",
        "tables": ["orders"]
    },
    {
        "id": 53,
        "title": "Find average order value",
        "type": "PYTHON",
        "difficulty": "Easy",
        "description": "Calculate the average order value using pandas.",
        "starter_code": "import pandas as pd\n\norders = pd.read_csv('orders.csv')\n\navg = orders['revenue'].mean()\nprint(avg)",
        "solution": "import pandas as pd\n\norders = pd.read_csv('orders.csv')\n\navg = orders['revenue'].mean()\nprint(avg)",
        "tables": ["orders"]
    },
    {
        "id": 54,
        "title": "First order date",
        "type": "PYTHON",
        "difficulty": "Easy",
        "description": "Find the first order date using pandas.",
        "starter_code": "import pandas as pd\n\norders = pd.read_csv('orders.csv')\norders['order_date'] = pd.to_datetime(orders['order_date'])\n\nfirst_date = orders['order_date'].min()\nprint(first_date)",
        "solution": "import pandas as pd\n\norders = pd.read_csv('orders.csv')\norders['order_date'] = pd.to_datetime(orders['order_date'])\n\nfirst_date = orders['order_date'].min()\nprint(first_date)",
        "tables": ["orders"]
    },
    {
        "id": 55,
        "title": "Last order date",
        "type": "PYTHON",
        "difficulty": "Easy",
        "description": "Find the last order date using pandas.",
        "starter_code": "import pandas as pd\n\norders = pd.read_csv('orders.csv')\norders['order_date'] = pd.to_datetime(orders['order_date'])\n\nlast_date = orders['order_date'].max()\nprint(last_date)",
        "solution": "import pandas as pd\n\norders = pd.read_csv('orders.csv')\norders['order_date'] = pd.to_datetime(orders['order_date'])\n\nlast_date = orders['order_date'].max()\nprint(last_date)",
        "tables": ["orders"]
    },
]

# Add remaining problems (simplified for brevity - you would add all 100)
# For now, we'll generate placeholders for problems 11-50 (SQL) and 56-100 (Python)

# Generate remaining SQL problems
sql_titles = [
    "Users who never placed an order", "Revenue per user", "First order per user",
    "Users who ordered in multiple months", "Monthly revenue", "Busiest day",
    "Top 5 products sold", "Revenue per product", "Most expensive product per category",
    "Products never purchased", "Average quantity per order", "Top categories by revenue",
    "Users who purchased more than 5 products", "Average revenue per country",
    "Users with spending >1000", "Repeat customers", "Days between orders",
    "First purchase after signup", "Conversion rate signup→purchase",
    "Inactive users (90 days)", "Top 3 orders per user", "Running revenue",
    "Users whose spending increased", "Daily active buyers", "Average orders per user",
    "Users with highest order frequency", "Largest order", "Median order value",
    "Users with purchases in multiple categories", "Most popular category",
    "Retention after 30 days", "Cohort by signup month", "Repeat purchase rate",
    "Average time between orders", "Top customers in last 30 days",
    "Revenue last month", "Users with exactly 1 order", "Orders without products",
    "Top product per month", "Fastest growing product category"
]

for i, title in enumerate(sql_titles, start=11):
    PROBLEMS.append({
        "id": i,
        "title": title,
        "type": "SQL",
        "difficulty": "Medium" if i > 20 else "Easy",
        "description": f"SQL challenge: {title}",
        "starter_code": "-- Write your SQL query here\nSELECT * FROM orders LIMIT 10;",
        "solution": "SELECT * FROM orders;",
        "tables": ["orders", "users"]
    })

# Generate remaining Python problems
python_titles = [
    "Count unique users", "Users with >10 orders", "Orders greater than 500",
    "Orders per day", "Top countries by revenue", "Revenue per country",
    "Revenue per user", "Orders per user", "First order per user",
    "Monthly revenue", "Average revenue per country", "Top 5 customers",
    "Busiest day", "Users with multiple months of purchases", "Users with revenue >1000",
    "Top 5 products by quantity", "Revenue per product", "Average price per category",
    "Most expensive product per category", "Products never purchased",
    "Category with most sales", "Average quantity per order", "Top category by revenue",
    "Users buying multiple categories", "Most popular product",
    "Import pandas", "Import sklearn", "Split dataset 80/20",
    "Import linear regression", "Create model", "Train model",
    "Predict", "Import ROC AUC", "Calculate ROC AUC",
    "Import logistic regression", "Fit logistic regression", "Predict probabilities",
    "Evaluate accuracy", "Use confusion matrix", "Plot ROC curve",
    "Normalize data", "Scale features", "Train/validation/test split",
    "Calculate RMSE", "Calculate MAE"
]

for i, title in enumerate(python_titles, start=56):
    if i >= 81:  # ML problems
        starter = "# Complete the ML code\nfrom sklearn.model_selection import train_test_split\n\n# Your code here"
    else:
        starter = "import pandas as pd\n\norders = pd.read_csv('orders.csv')\n\n# Your code here\nprint(result)"
    
    PROBLEMS.append({
        "id": i,
        "title": title,
        "type": "PYTHON",
        "difficulty": "Medium" if i > 70 else "Easy",
        "description": f"Python/pandas challenge: {title}",
        "starter_code": starter,
        "solution": "print('Solution')",
        "tables": ["orders"]
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

def get_problems_by_type(problem_type):
    """Get problems filtered by type (SQL or PYTHON)"""
    return [p for p in PROBLEMS if p["type"] == problem_type]
