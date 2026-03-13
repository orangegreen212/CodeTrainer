"""
Code execution module for SQL and Python
"""
import io
import sys
from contextlib import redirect_stdout
from database import execute_query
import pandas as pd

def run_sql(code, problem_id=None):
    """
    Execute SQL query and return results
    """
    try:
        # Execute the query
        results = execute_query(code)
        
        # Convert results to list of dicts if needed
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
    """
    Execute Python code in a restricted environment
    Note: This is a basic implementation. For production, use sandboxing like Judge0
    """
    try:
        # Capture stdout
        output_buffer = io.StringIO()
        
        # Create a restricted namespace with pandas and sample data
        namespace = {
            '__builtins__': __builtins__,
            'pd': pd,
        }
        
        # Add sample CSV data as in-memory dataframes
        # In production, you'd load from actual CSV files
        users_data = {
            'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'signup_date': ['2023-01-05', '2023-01-10', '2023-02-01', '2023-02-15', 
                           '2023-03-10', '2023-03-20', '2023-04-01', '2023-04-12',
                           '2023-05-03', '2023-05-20'],
            'country': ['USA', 'Germany', 'France', 'USA', 'Canada', 
                       'USA', 'UK', 'Germany', 'France', 'USA']
        }
        
        orders_data = {
            'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            'user_id': [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'order_date': ['2023-02-01', '2023-02-10', '2023-02-11', '2023-03-01',
                          '2023-03-15', '2023-04-01', '2023-04-10', '2023-04-12',
                          '2023-05-01', '2023-05-05', '2023-05-20'],
            'revenue': [120, 80, 200, 50, 300, 400, 150, 220, 180, 75, 500]
        }
        
        products_data = {
            'product_id': [1, 2, 3, 4, 5, 6, 7, 8],
            'category': ['Electronics', 'Electronics', 'Books', 'Clothing', 
                        'Clothing', 'Home', 'Books', 'Electronics'],
            'price': [500, 300, 20, 50, 80, 120, 15, 700]
        }
        
        order_items_data = {
            'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            'product_id': [1, 3, 2, 7, 1, 6, 4, 5, 8, 3, 1],
            'quantity': [1, 2, 1, 3, 1, 2, 3, 1, 1, 1, 1]
        }
        
        # Mock read_csv function
        def mock_read_csv(filename):
            if 'users' in filename.lower():
                return pd.DataFrame(users_data)
            elif 'orders' in filename.lower():
                return pd.DataFrame(orders_data)
            elif 'products' in filename.lower():
                return pd.DataFrame(products_data)
            elif 'order_items' in filename.lower():
                return pd.DataFrame(order_items_data)
            else:
                raise FileNotFoundError(f"File {filename} not found")
        
        # Override pd.read_csv in namespace
        namespace['pd'].read_csv = mock_read_csv
        
        # Execute the code
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

def validate_solution(user_output, expected_output):
    """
    Compare user output with expected output
    Returns True if they match
    """
    # Basic comparison - in production you'd want more sophisticated matching
    if user_output == expected_output:
        return True
    
    # Try to compare as DataFrames if both are tabular
    try:
        if isinstance(user_output, pd.DataFrame) and isinstance(expected_output, pd.DataFrame):
            return user_output.equals(expected_output)
    except:
        pass
    
    return False
