import os
import psycopg2
from psycopg2.extras import RealDictCursor
from decimal import Decimal
import datetime

DATABASE_URL = os.environ.get("DATABASE_URL", "")

# Fix for Render's postgres:// URL format
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

def get_db():
    """Get database connection"""
    if not DATABASE_URL:
        return None
    
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def init_db():
    """Initialize database with new schema: users, events, orders"""
    conn = get_db()
    if not conn:
        print("No database connection - skipping init")
        return
    
    cursor = conn.cursor()
    
    # Drop old tables
    cursor.execute("DROP TABLE IF EXISTS purchases, events, orders, users CASCADE")
    
    # Create new tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            reg_date DATE,
            country VARCHAR(50),
            channel VARCHAR(100)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            event_id SERIAL PRIMARY KEY,
            user_id INTEGER,
            event_time TIMESTAMP,
            event_name VARCHAR(100)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id SERIAL PRIMARY KEY,
            user_id INTEGER,
            order_date DATE,
            amount DECIMAL(10, 2)
        )
    """)
    
    # Check if data exists
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    
    if count == 0:
        load_sample_data(cursor)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized with new schema (users, events, orders)")

def load_sample_data(cursor):
    """Load sample data"""
    
    # Insert users
    users_data = [
        (1, '2024-01-01', 'USA', 'google'),
        (2, '2024-01-02', 'UK', 'facebook'),
        (3, '2024-01-03', 'Canada', 'organic'),
        (4, '2024-01-04', 'USA', 'google'),
        (5, '2024-01-05', 'Germany', 'twitter'),
        (6, '2024-01-06', 'USA', 'facebook'),
        (7, '2024-01-07', 'France', 'organic'),
        (8, '2024-01-08', 'USA', 'google'),
        (9, '2024-01-09', 'UK', 'linkedin'),
        (10, '2024-01-10', 'Canada', 'google'),
        (11, '2024-01-11', 'USA', 'facebook'),
        (12, '2024-01-12', 'Germany', 'organic'),
        (13, '2024-01-13', 'USA', 'google'),
        (14, '2024-01-14', 'UK', 'twitter'),
        (15, '2024-01-15', 'France', 'facebook'),
        (16, '2024-01-16', 'USA', 'organic'),
        (17, '2024-01-17', 'Canada', 'google'),
        (18, '2024-01-18', 'USA', 'linkedin'),
        (19, '2024-01-19', 'Germany', 'facebook'),
        (20, '2024-01-20', 'UK', 'google'),
    ]
    
    cursor.executemany(
        "INSERT INTO users (user_id, reg_date, country, channel) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING",
        users_data
    )
    
    # Insert events
    events_data = [
        (1, '2024-01-01 10:00:00', 'login'),
        (1, '2024-01-01 10:05:00', 'view_item'),
        (1, '2024-01-01 10:10:00', 'add_to_cart'),
        (1, '2024-01-01 10:15:00', 'purchase'),
        (2, '2024-01-02 11:00:00', 'login'),
        (2, '2024-01-02 11:15:00', 'view_item'),
        (3, '2024-01-03 12:00:00', 'login'),
        (3, '2024-01-03 12:10:00', 'view_item'),
        (3, '2024-01-03 12:20:00', 'add_to_cart'),
        (4, '2024-01-04 13:00:00', 'login'),
        (4, '2024-01-04 13:20:00', 'view_item'),
        (4, '2024-01-04 13:30:00', 'purchase'),
        (5, '2024-01-05 14:00:00', 'login'),
        (5, '2024-01-05 14:30:00', 'view_item'),
        (5, '2024-01-05 14:35:00', 'add_to_cart'),
        (5, '2024-01-05 14:40:00', 'purchase'),
        (1, '2024-01-02 10:00:00', 'login'),
        (1, '2024-01-03 10:00:00', 'login'),
        (2, '2024-01-03 11:00:00', 'login'),
        (3, '2024-01-04 12:00:00', 'login'),
    ]
    
    cursor.executemany(
        "INSERT INTO events (user_id, event_time, event_name) VALUES (%s, %s, %s)",
        events_data
    )
    
    # Insert orders
    orders_data = [
        (1, '2024-01-01', 150.00),
        (4, '2024-01-04', 200.00),
        (5, '2024-01-05', 99.99),
        (8, '2024-01-08', 350.00),
        (10, '2024-01-10', 75.50),
        (1, '2024-01-15', 120.00),
        (2, '2024-01-12', 180.00),
        (3, '2024-01-10', 90.00),
        (6, '2024-01-20', 250.00),
        (11, '2024-01-18', 145.00),
        (12, '2024-01-22', 95.00),
        (13, '2024-01-25', 310.00),
        (14, '2024-01-28', 65.00),
        (15, '2024-02-01', 220.00),
        (16, '2024-02-03', 185.00),
    ]
    
    cursor.executemany(
        "INSERT INTO orders (user_id, order_date, amount) VALUES (%s, %s, %s)",
        orders_data
    )

def execute_query(query):
    """Execute SQL query with proper type conversion"""
    conn = get_db()
    if not conn:
        raise Exception("Database not configured")
    
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query)
    
    if query.strip().upper().startswith("SELECT"):
        results = cursor.fetchall()
        
        # Convert Decimal and datetime to JSON-serializable types
        converted_results = []
        for row in results:
            converted_row = {}
            for key, value in row.items():
                if isinstance(value, Decimal):
                    converted_row[key] = float(value)
                elif isinstance(value, (datetime.date, datetime.datetime)):
                    converted_row[key] = str(value)
                else:
                    converted_row[key] = value
            converted_results.append(converted_row)
        
        cursor.close()
        conn.close()
        return converted_results
    else:
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Query executed successfully"}

def get_table_sample(table_name, limit=5):
    """Get sample data from a table"""
    query = f"SELECT * FROM {table_name} LIMIT {limit}"
    return execute_query(query)
