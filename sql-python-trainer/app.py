from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn
from database import get_db, init_db, get_table_sample
from problems import get_all_problems, get_problem_by_id, get_all_quizzes, add_problem, add_quiz, get_categories
from runner import run_sql, run_python
import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI(title="SQL & Python Interview Trainer v4.0")

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

@app.get("/patterns")
async def patterns_page(request: Request):
    return templates.TemplateResponse("patterns.html", {"request": request})

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
    what_to_find_en: str = Form(""),
    what_to_find_uk: str = Form(""),
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
        "what_to_find": {"en": what_to_find_en, "uk": what_to_find_uk},
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

@app.post("/admin/add-quiz")
async def add_new_quiz(
    request: Request,
    password: str = Form(...),
    question_en: str = Form(...),
    question_uk: str = Form(...),
    option1: str = Form(...),
    option2: str = Form(...),
    option3: str = Form(...),
    option4: str = Form(...),
    correct_answer: int = Form(...),
    explanation_en: str = Form(...),
    explanation_uk: str = Form(...)
):
    admin_password = os.environ.get("ADMIN_PASSWORD", "")
    if password != admin_password:
        return JSONResponse({"success": False, "error": "Invalid password"}, status_code=403)
    
    quiz_data = {
        "question": {"en": question_en, "uk": question_uk},
        "options": [option1, option2, option3, option4],
        "correct": correct_answer,
        "explanation": {"en": explanation_en, "uk": explanation_uk}
    }
    
    try:
        new_id = add_quiz(quiz_data)
        return JSONResponse({"success": True, "quiz_id": new_id})
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
        return JSONResponse({"success": False, "error": "Contact email not configured"}, status_code=500)
    
    # Try to send real email via SMTP
    smtp_host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    smtp_user = os.environ.get("SMTP_USER", "")
    smtp_password = os.environ.get("SMTP_PASSWORD", "")
    
    subject = f"[SQL Trainer] Message from {name}"
    body = f"""
New message from SQL & Python Interview Trainer:

From: {name}
Email: {email}

Message:
{message}
"""
    
    if smtp_user and smtp_password:
        try:
            msg = MIMEMultipart()
            msg["From"] = smtp_user
            msg["To"] = contact_email
            msg["Subject"] = subject
            msg["Reply-To"] = email
            msg.attach(MIMEText(body, "plain"))
            
            with smtplib.SMTP(smtp_host, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_password)
                server.send_message(msg)
            
            return JSONResponse({"success": True, "message": "Message sent successfully!"})
        except Exception as e:
            print(f"SMTP error: {e}")
            # Fall through to log-only mode
    
    # Fallback: log to console (visible in Render logs)
    print(f"=== CONTACT FORM ===")
    print(f"To: {contact_email}")
    print(f"From: {name} <{email}>")
    print(f"Message: {message}")
    print(f"===================")
    
    return JSONResponse({
        "success": True,
        "message": "Message received! Developer will contact you soon."
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
        return JSONResponse({"error": str(e), "success": False}, status_code=400)

@app.post("/api/chat")
async def mistral_chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    problem_id = data.get("problem_id")
    
    mistral_key = os.environ.get("MISTRAL_API_KEY")
    if not mistral_key:
        return JSONResponse({"success": False, "error": "Mistral AI not configured"})
    
    try:
        problem = get_problem_by_id(problem_id) if problem_id else None
        context = ""
        if problem:
            lang = data.get("lang", "en")
            context = f"Problem: {problem['title'][lang]}\n{problem['description'][lang]}\n"
        
        system_prompt = f"""You are a helpful SQL/Python tutor for data analysts. Help students solve interview problems.

FORMATTING RULES:
1. Format SQL code with proper line breaks and indentation
2. Format Python code with proper line breaks
3. Always use code blocks for code
4. Add brief comments to complex parts

{context}"""
        
        response = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={"Authorization": f"Bearer {mistral_key}", "Content-Type": "application/json"},
            json={
                "model": "mistral-tiny",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                "temperature": 0.7,
                "max_tokens": 800
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
    return {"status": "healthy", "version": "4.0"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
