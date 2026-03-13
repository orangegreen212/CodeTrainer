import os
import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd

DATABASE_URL = os.environ.get("DATABASE_URL", "")

# Fix for Render's postgres:// URL format
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

def get_db():
    """Get database connection"""
    if not DATABASE_URL:
        # For local development, use SQLite-like approach
        return None
    
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def init_db():
    """Initialize database with tables and sample data"""
    conn = get_db()
    if not conn:
        print("No database connection - skipping init")
        return
    
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            signup_date DATE,
            country VARCHAR(50)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            order_date DATE,
            revenue DECIMAL(10, 2)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            category VARCHAR(50),
            price DECIMAL(10, 2)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER
        )
    """)
    
    # Check if data already exists
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    
    if count == 0:
        # Insert sample data from CSV files
        load_csv_data(cursor)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized successfully")

def load_csv_data(cursor):
    """Load data from CSV files into database"""
    import csv
    
    # Load users
    users_data = [
        (1, '2023-01-05', 'USA'),
        (2, '2023-01-10', 'Germany'),
        (3, '2023-02-01', 'France'),
        (4, '2023-02-15', 'USA'),
        (5, '2023-03-10', 'Canada'),
        (6, '2023-03-20', 'USA'),
        (7, '2023-04-01', 'UK'),
        (8, '2023-04-12', 'Germany'),
        (9, '2023-05-03', 'France'),
        (10, '2023-05-20', 'USA')
    ]
    
    cursor.executemany(
        "INSERT INTO users (user_id, signup_date, country) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
        users_data
    )
    
    # Load orders
    orders_data = [
        (1, 1, '2023-02-01', 120),
        (2, 1, '2023-02-10', 80),
        (3, 2, '2023-02-11', 200),
        (4, 3, '2023-03-01', 50),
        (5, 4, '2023-03-15', 300),
        (6, 5, '2023-04-01', 400),
        (7, 6, '2023-04-10', 150),
        (8, 7, '2023-04-12', 220),
        (9, 8, '2023-05-01', 180),
        (10, 9, '2023-05-05', 75),
        (11, 10, '2023-05-20', 500)
    ]
    
    cursor.executemany(
        "INSERT INTO orders (order_id, user_id, order_date, revenue) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING",
        orders_data
    )
    
    # Load products
    products_data = [
        (1, 'Electronics', 500),
        (2, 'Electronics', 300),
        (3, 'Books', 20),
        (4, 'Clothing', 50),
        (5, 'Clothing', 80),
        (6, 'Home', 120),
        (7, 'Books', 15),
        (8, 'Electronics', 700)
    ]
    
    cursor.executemany(
        "INSERT INTO products (product_id, category, price) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
        products_data
    )
    
    # Load order_items
    order_items_data = [
        (1, 1, 1),
        (2, 3, 2),
        (3, 2, 1),
        (4, 7, 3),
        (5, 1, 1),
        (6, 6, 2),
        (7, 4, 3),
        (8, 5, 1),
        (9, 8, 1),
        (10, 3, 1),
        (11, 1, 1)
    ]
    
    cursor.executemany(
        "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)",
        order_items_data
    )

def execute_query(query):
    """Execute SQL query and return results"""
    conn = get_db()
    if not conn:
        raise Exception("Database not configured")
    
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query)
    
    if query.strip().upper().startswith("SELECT"):
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    else:
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Query executed successfully"}
