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
    """Initialize database with new schema"""
    conn = get_db()
    if not conn:
        print("No database connection - skipping init")
        return
    
    cursor = conn.cursor()
    
    # Drop old tables if exist
    cursor.execute("DROP TABLE IF EXISTS order_items, products, orders, users CASCADE")
    
    # Create new tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            reg_date DATE,
            platform VARCHAR(50),
            country VARCHAR(50),
            utm_source VARCHAR(100)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            event_id SERIAL PRIMARY KEY,
            user_id INTEGER,
            event_time TIMESTAMP,
            event_name VARCHAR(100),
            item_id INTEGER
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchases (
            purchase_id SERIAL PRIMARY KEY,
            user_id INTEGER,
            purchase_date DATE,
            amount DECIMAL(10, 2),
            status VARCHAR(50)
        )
    """)
    
    # Check if data already exists
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    
    if count == 0:
        load_sample_data(cursor)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized successfully with new schema")

def load_sample_data(cursor):
    """Load sample data for Product Analyst tasks"""
    
    # Insert users (50 users)
    users_data = [
        (1, '2024-01-01', 'iOS', 'USA', 'google'),
        (2, '2024-01-02', 'Android', 'UK', 'facebook'),
        (3, '2024-01-03', 'iOS', 'Canada', 'organic'),
        (4, '2024-01-04', 'Android', 'USA', 'google'),
        (5, '2024-01-05', 'Web', 'Germany', 'twitter'),
        (6, '2024-01-06', 'iOS', 'USA', 'facebook'),
        (7, '2024-01-07', 'Android', 'France', 'organic'),
        (8, '2024-01-08', 'iOS', 'USA', 'google'),
        (9, '2024-01-09', 'Web', 'UK', 'linkedin'),
        (10, '2024-01-10', 'Android', 'Canada', 'google'),
        (11, '2024-01-11', 'iOS', 'USA', 'facebook'),
        (12, '2024-01-12', 'Android', 'Germany', 'organic'),
        (13, '2024-01-13', 'Web', 'USA', 'google'),
        (14, '2024-01-14', 'iOS', 'UK', 'twitter'),
        (15, '2024-01-15', 'Android', 'France', 'facebook'),
        (16, '2024-01-16', 'iOS', 'USA', 'organic'),
        (17, '2024-01-17', 'Web', 'Canada', 'google'),
        (18, '2024-01-18', 'Android', 'USA', 'linkedin'),
        (19, '2024-01-19', 'iOS', 'Germany', 'facebook'),
        (20, '2024-01-20', 'Android', 'UK', 'google'),
    ]
    
    cursor.executemany(
        "INSERT INTO users (user_id, reg_date, platform, country, utm_source) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
        users_data
    )
    
    # Insert events (100 events)
    events_data = [
        (1, '2024-01-01 10:00:00', 'view_item', 101),
        (1, '2024-01-01 10:05:00', 'add_to_cart', 101),
        (1, '2024-01-01 10:10:00', 'purchase', 101),
        (2, '2024-01-02 11:00:00', 'view_item', 102),
        (2, '2024-01-02 11:15:00', 'view_item', 103),
        (3, '2024-01-03 12:00:00', 'view_item', 101),
        (3, '2024-01-03 12:10:00', 'add_to_cart', 101),
        (4, '2024-01-04 13:00:00', 'view_item', 104),
        (4, '2024-01-04 13:20:00', 'purchase', 104),
        (5, '2024-01-05 14:00:00', 'view_item', 102),
        (5, '2024-01-05 14:30:00', 'add_to_cart', 102),
        (5, '2024-01-05 14:35:00', 'purchase', 102),
        (6, '2024-01-06 15:00:00', 'view_item', 105),
        (7, '2024-01-07 16:00:00', 'view_item', 101),
        (8, '2024-01-08 17:00:00', 'view_item', 103),
        (8, '2024-01-08 17:10:00', 'purchase', 103),
        (9, '2024-01-09 18:00:00', 'view_item', 106),
        (10, '2024-01-10 19:00:00', 'view_item', 101),
        (10, '2024-01-10 19:15:00', 'add_to_cart', 101),
        (10, '2024-01-10 19:20:00', 'purchase', 101),
    ]
    
    cursor.executemany(
        "INSERT INTO events (user_id, event_time, event_name, item_id) VALUES (%s, %s, %s, %s)",
        events_data
    )
    
    # Insert purchases (30 purchases)
    purchases_data = [
        (1, '2024-01-01', 150.00, 'success'),
        (4, '2024-01-04', 200.00, 'success'),
        (5, '2024-01-05', 99.99, 'success'),
        (8, '2024-01-08', 350.00, 'success'),
        (10, '2024-01-10', 75.50, 'success'),
        (1, '2024-01-15', 120.00, 'success'),
        (2, '2024-01-12', 180.00, 'failed'),
        (3, '2024-01-10', 90.00, 'success'),
        (6, '2024-01-20', 250.00, 'success'),
        (11, '2024-01-18', 145.00, 'success'),
        (12, '2024-01-22', 95.00, 'success'),
        (13, '2024-01-25', 310.00, 'success'),
        (14, '2024-01-28', 65.00, 'failed'),
        (15, '2024-02-01', 220.00, 'success'),
        (16, '2024-02-03', 185.00, 'success'),
    ]
    
    cursor.executemany(
        "INSERT INTO purchases (user_id, purchase_date, amount, status) VALUES (%s, %s, %s, %s)",
        purchases_data
    )

def execute_query(query):
    """Execute SQL query and return results with proper type conversion"""
    conn = get_db()
    if not conn:
        raise Exception("Database not configured")
    
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query)
    
    if query.strip().upper().startswith("SELECT"):
        results = cursor.fetchall()
        
        # Convert Decimal and datetime objects to JSON-serializable types
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
