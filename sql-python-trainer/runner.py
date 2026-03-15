"""
Code execution module for SQL and Python
"""
import io
import sys
from contextlib import redirect_stdout
from database import execute_query
import pandas as pd

def run_sql(code, problem_id=None):
    """Execute SQL query and return results"""
    try:
        results = execute_query(code)
        
        if isinstance(results, list):
            output = results
        else:
            output = [results]
        
        return {
            "success": True,
            "output": output,
            "error": None
        }
    except Exception as e:
        return {
            "success": False,
            "output": None,
            "error": str(e)
        }

def run_python(code, problem_id=None):
    """Execute Python code"""
    try:
        output_buffer = io.StringIO()
        
        # Mock data
        users_data = {
            'user_id': list(range(1, 21)),
            'reg_date': ['2024-01-{:02d}'.format(i) for i in range(1, 21)],
            'country': ['USA', 'UK', 'Canada', 'USA', 'Germany'] * 4,
            'channel': ['google', 'facebook', 'organic', 'google', 'twitter'] * 4
        }
        
        events_data = {
            'event_id': list(range(1, 21)),
            'user_id': [1,1,1,1,2,2,3,3,3,4,4,4,5,5,5,5,1,1,2,3],
            'event_time': pd.date_range('2024-01-01 10:00:00', periods=20, freq='H'),
            'event_name': ['login', 'view_item', 'add_to_cart', 'purchase'] * 5
        }
        
        orders_data = {
            'order_id': list(range(1, 16)),
            'user_id': [1,4,5,8,10,1,2,3,6,11,12,13,14,15,16],
            'order_date': pd.date_range('2024-01-01', periods=15, freq='D'),
            'amount': [150.0, 200.0, 99.99, 350.0, 75.5, 120.0, 180.0, 90.0, 250.0, 145.0, 95.0, 310.0, 65.0, 220.0, 185.0]
        }
        
        # Create DataFrames
        df_users = pd.DataFrame(users_data)
        df_events = pd.DataFrame(events_data)
        df_orders = pd.DataFrame(orders_data)
        
        # Convert dates
        df_users['reg_date'] = pd.to_datetime(df_users['reg_date'])
        df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
        
        # Mock A/B test data
        df_ab = pd.DataFrame({
            'group': ['A'] * 100 + ['B'] * 100,
            'revenue': [100 + i for i in range(200)]
        })
        
        # Namespace
        namespace = {
            '__builtins__': __builtins__,
            'pd': pd,
            'df_users': df_users,
            'df_events': df_events,
            'df_orders': df_orders,
            'df_ab': df_ab,
            'np': __import__('numpy'),
        }
        
        # Execute code
        with redirect_stdout(output_buffer):
            exec(code, namespace)
        
        output = output_buffer.getvalue()
        
        return {
            "success": True,
            "output": output,
            "error": None
        }
        
    except Exception as e:
        return {
            "success": False,
            "output": None,
            "error": str(e)
        }
