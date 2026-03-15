from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn
from database import get_db, init_db, get_table_sample
from problems import get_all_problems, get_problem_by_id, get_all_quizzes, add_problem, get_categories
from runner import run_sql, run_python
import os
import requests

app = FastAPI(title="SQL & Python Interview Trainer v3.1")

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/problems")
async def problems_list(request: Request):
    problems = get_all_problems()
    categories = get_categories()
    return templates.TemplateResponse("problems.html", {
        "request": request,
        "problems": problems,
        "categories": categories
    })

@app.get("/problem/{problem_id}")
async def problem_detail(request: Request, problem_id: int):
    problem = get_problem_by_id(problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    
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
    quizzes = get_all_quizzes()
    return templates.TemplateResponse("quizzes.html", {
        "request": request,
        "quizzes": quizzes
    })

@app.get("/admin")
async def admin_page(request: Request):
    admin_password = os.environ.get("ADMIN_PASSWORD")
    if not admin_password:
        return HTMLResponse("<h1>Admin panel not configured. Set ADMIN_PASSWORD environment variable.</h1>")
    
    categories = get_categories()
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "categories": categories
    })

@app.post("/admin/add-problem")
async def add_new_problem(
    request: Request,
    password: str = Form(...),
    title_en: str = Form(...),
    title_uk: str = Form(...),
    description_en: str = Form(...),
    description_uk: str = Form(...),
    category: str = Form(...),
    difficulty: str = Form(...),
    problem_type: str = Form(...),
    tables: str = Form(""),
    solution: str = Form(""),
    hint_en: str = Form(""),
    hint_uk: str = Form("")
):
    admin_password = os.environ.get("ADMIN_PASSWORD", "")
    
    if password != admin_password:
        return JSONResponse({"success": False, "error": "Invalid password"}, status_code=403)
    
    problem_data = {
        "title": {"en": title_en, "uk": title_uk},
        "description": {"en": description_en, "uk": description_uk},
        "category": category,
        "difficulty": difficulty,
        "type": problem_type,
        "tables": [t.strip() for t in tables.split(",")] if tables else [],
        "solution": solution,
        "hint": {"en": hint_en, "uk": hint_uk},
        "starter_code": ""
    }
    
    try:
        new_id = add_problem(problem_data)
        return JSONResponse({"success": True, "problem_id": new_id})
    except Exception as e:
        return JSONResponse({"success": False, "error": str(e)}, status_code=500)

@app.post("/api/contact")
async def send_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    contact_email = os.environ.get("CONTACT_EMAIL")
    
    if not contact_email:
        return JSONResponse({
            "success": False,
            "error": "Contact email not configured"
        }, status_code=500)
    
    # Log contact (in production, send actual email)
    print(f"Contact from {name} ({email}): {message}")
    
    return JSONResponse({
        "success": True,
        "message": "Message sent! Developer will contact you soon."
    })

@app.post("/api/run")
async def run_code(request: Request):
    data = await request.json()
    code = data.get("code", "")
    problem_id = data.get("problem_id")
    problem_type = data.get("type", "SQL")
    
    if not code:
        return JSONResponse({"error": "No code provided"}, status_code=400)
    
    try:
        if problem_type == "SQL":
            result = run_sql(code, problem_id)
        else:
            result = run_python(code, problem_id)
        
        return JSONResponse(result)
    except Exception as e:
        return JSONResponse({
            "error": str(e),
            "success": False
        }, status_code=400)

@app.post("/api/chat")
async def mistral_chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    problem_id = data.get("problem_id")
    
    mistral_key = os.environ.get("MISTRAL_API_KEY")
    if not mistral_key:
        return JSONResponse({
            "success": False,
            "error": "Mistral AI not configured"
        })
    
    try:
        problem = get_problem_by_id(problem_id) if problem_id else None
        
        context = ""
        if problem:
            lang = data.get("lang", "en")
            context = f"Problem: {problem['title'][lang]}\n{problem['description'][lang]}\n"
        
        response = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {mistral_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistral-tiny",
                "messages": [
                    {"role": "system", "content": f"You are a SQL/Python tutor. {context}"},
                    {"role": "user", "content": message}
                ],
                "temperature": 0.7,
                "max_tokens": 500
            },
            timeout=15
        )
        
        if response.status_code == 200:
            result = response.json()
            reply = result['choices'][0]['message']['content']
            return JSONResponse({"success": True, "reply": reply})
        else:
            return JSONResponse({"success": False, "error": "API error"})
            
    except Exception as e:
        return JSONResponse({"success": False, "error": str(e)})

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "version": "3.1"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
