from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import uvicorn
from database import get_db, init_db, get_table_sample
from problems import get_all_problems, get_problem_by_id, get_all_quizzes
from runner import run_sql, run_python
import os

app = FastAPI(title="SQL & Python Interview Trainer")

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
async def home(request: Request):
    """Homepage"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/problems")
async def problems_list(request: Request):
    """List of all problems"""
    problems = get_all_problems()
    return templates.TemplateResponse("problems.html", {
        "request": request,
        "problems": problems
    })

@app.get("/problem/{problem_id}")
async def problem_detail(request: Request, problem_id: int):
    """Individual problem page"""
    problem = get_problem_by_id(problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    # Get sample data for tables
    table_samples = {}
    for table_name in problem.get("tables", []):
        try:
            table_samples[table_name] = get_table_sample(table_name, limit=5)
        except:
            table_samples[table_name] = []
    
    return templates.TemplateResponse("problem.html", {
        "request": request,
        "problem": problem,
        "table_samples": table_samples
    })

@app.get("/quizzes")
async def quizzes_page(request: Request):
    """Quizzes page"""
    quizzes = get_all_quizzes()
    return templates.TemplateResponse("quizzes.html", {
        "request": request,
        "quizzes": quizzes
    })

@app.post("/api/run")
async def run_code(request: Request):
    """Execute user code and return results"""
    data = await request.json()
    code = data.get("code", "")
    problem_id = data.get("problem_id")
    problem_type = data.get("type", "SQL")
    
    if not code:
        return JSONResponse({"error": "No code provided"}, status_code=400)
    
    try:
        if problem_type == "SQL":
            result = run_sql(code, problem_id)
        else:  # Python
            result = run_python(code, problem_id)
        
        return JSONResponse(result)
    except Exception as e:
        return JSONResponse({
            "error": str(e),
            "success": False
        }, status_code=400)

@app.get("/api/table/{table_name}")
async def get_table_data(table_name: str, limit: int = 10):
    """Get sample data from a table"""
    try:
        data = get_table_sample(table_name, limit)
        return JSONResponse({"data": data})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=400)

@app.get("/api/health")
async def health_check():
    """Health check endpoint for Render"""
    return {"status": "healthy"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
