"""
Code execution module for SQL and Python with solution validation
"""
import io
import sys
from contextlib import redirect_stdout
from database import execute_query
import pandas as pd
from decimal import Decimal
import datetime
import json
import os

def run_sql(code, problem_id=None):
    """
    Execute SQL query and return results with proper type conversion
    """
    try:
        # Execute the query
        results = execute_query(code)
        
        # Results are already converted in execute_query
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
    """
    try:
        # Capture stdout
        output_buffer = io.StringIO()
        
        # Create a restricted namespace with pandas and sample data
        namespace = {
            '__builtins__': __builtins__,
            'pd': pd,
            'json': json,
            'np': __import__('numpy'),
        }
        
        # Mock data for pandas tasks
        users_data = {
            'user_id': list(range(1, 21)),
            'reg_date': ['2024-01-{:02d}'.format(i) for i in range(1, 21)],
            'platform': ['iOS', 'Android', 'iOS', 'Android', 'Web'] * 4,
            'country': ['USA', 'UK', 'Canada', 'USA', 'Germany'] * 4,
            'utm_source': ['google', 'facebook', 'organic', 'google', 'twitter'] * 4
        }
        
        events_data = {
            'event_id': list(range(1, 21)),
            'user_id': [1,1,1,2,2,3,3,4,4,5,5,5,6,7,8,8,9,10,10,10],
            'event_time': ['2024-01-01 10:00:00'] * 20,
            'event_name': ['view_item', 'add_to_cart', 'purchase'] * 6 + ['view_item', 'view_item'],
            'item_id': [101, 101, 101, 102, 103, 101, 101, 104, 104, 102, 102, 102, 105, 101, 103, 103, 106, 101, 101, 101]
        }
        
        purchases_data = {
            'purchase_id': list(range(1, 16)),
            'user_id': [1,4,5,8,10,1,2,3,6,11,12,13,14,15,16],
            'purchase_date': ['2024-01-01', '2024-01-04', '2024-01-05', '2024-01-08', '2024-01-10',
                             '2024-01-15', '2024-01-12', '2024-01-10', '2024-01-20', '2024-01-18',
                             '2024-01-22', '2024-01-25', '2024-01-28', '2024-02-01', '2024-02-03'],
            'amount': [150.0, 200.0, 99.99, 350.0, 75.5, 120.0, 180.0, 90.0, 250.0, 145.0,
                      95.0, 310.0, 65.0, 220.0, 185.0],
            'status': ['success'] * 13 + ['failed', 'success']
        }
        
        # Create DataFrames
        df_users = pd.DataFrame(users_data)
        df_events = pd.DataFrame(events_data)
        df_purchases = pd.DataFrame(purchases_data)
        
        # Convert date columns
        df_users['reg_date'] = pd.to_datetime(df_users['reg_date'])
        df_events['event_time'] = pd.to_datetime(df_events['event_time'])
        df_purchases['purchase_date'] = pd.to_datetime(df_purchases['purchase_date'])
        
        # Mock read_csv function
        def mock_read_csv(filename):
            if 'users' in filename.lower():
                return df_users.copy()
            elif 'events' in filename.lower():
                return df_events.copy()
            elif 'purchases' in filename.lower():
                return df_purchases.copy()
            else:
                raise FileNotFoundError(f"File {filename} not found")
        
        # Add to namespace
        namespace['pd'].read_csv = mock_read_csv
        namespace['df_users'] = df_users
        namespace['df_events'] = df_events
        namespace['df_purchases'] = df_purchases
        
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

def validate_with_mistral(code, problem_description, language="SQL"):
    """
    Validate code using Mistral API (free tier)
    Returns validation result and feedback
    """
    try:
        import requests
        
        api_key = os.environ.get("MISTRAL_API_KEY")
        if not api_key:
            return {
                "validated": False,
                "message": "Mistral API key not configured"
            }
        
        prompt = f"""You are a code reviewer for {language} interview questions.
        
Problem: {problem_description}

Candidate's solution:
```{language.lower()}
{code}
```

Analyze if this solution correctly solves the problem. Respond with JSON only:
{{"is_correct": true/false, "feedback": "brief explanation"}}"""

        response = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistral-tiny",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1
            },
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            
            # Parse JSON response
            try:
                validation = json.loads(content)
                return {
                    "validated": True,
                    "is_correct": validation.get("is_correct", False),
                    "feedback": validation.get("feedback", "")
                }
            except:
                return {
                    "validated": False,
                    "message": "Could not parse validation response"
                }
        else:
            return {
                "validated": False,
                "message": f"API error: {response.status_code}"
            }
            
    except Exception as e:
        return {
            "validated": False,
            "message": f"Validation error: {str(e)}"
        }
