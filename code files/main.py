from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests

app = FastAPI()
class Q(BaseModel):
    question: str = ""; text: str = ""; topic: str = ""; subject: str = ""

def get_answer(q):
    q = q.strip().replace("?","")
    if not q: return "Type a question"
    try:
        r = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{q}", headers={"User-Agent":"EduGenie"}, timeout=8).json()
        if "extract" in r: return r["extract"]
        # search pannitu answer edukkum
        s = requests.get("https://en.wikipedia.org/w/api.php", params={"action":"query","list":"search","srsearch":q,"format":"json"}, headers={"User-Agent":"EduGenie"}, timeout=8).json()
        title = s["query"]["search"][0]["title"]
        r2 = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}", headers={"User-Agent":"EduGenie"}, timeout=8).json()
        return r2.get("extract", f"Info about {q}")
    except:
        return f"Real info about '{q}' will appear here. (Check internet)"

HTML = """<html><body style="font-family:sans-serif;max-width:700px;margin:auto;padding:20px">
<h2>Welcome to EduGenie ❤️✨</h2><p>Your personal AI tutor!</p><hr>
<div style="background:#f0f9ff;padding:15px;margin:10px;border-radius:10px"><h4>1. Ask EduGenie a Question:</h4><input id="q1" style="width:65%;padding:8px"><button onclick="ask()">Get Answer</button><p id="a1"></p></div>
<div style="background:#f0fdf4;padding:15px;margin:10px;border-radius:10px"><h4>2. Need an Explanation?</h4><input id="q2" style="width:65%;padding:8px"><button onclick="exp()">Explain</button><p id="a2"></p></div>
<div style="background:#fefce8;padding:15px;margin:10px;border-radius:10px"><h4>3. Summarize a Paragraph:</h4><textarea id="q3" style="width:95%;height:60px"></textarea><br><button onclick="sum()">Summarize</button><p id="a3"></p></div>
<div style="background:#fdf2f8;padding:15px;margin:10px;border-radius:10px"><h4>4. Quiz Me!</h4><input id="q4" style="width:65%;padding:8px"><button onclick="quiz()">Generate Quiz</button><p id="a4" style="white-space:pre-wrap"></p></div>
<div style="background:#f5f3ff;padding:15px;margin:10px;border-radius:10px"><h4>5. Recommend Topics:</h4><input id="q5" style="width:65%;padding:8px"><button onclick="rec()">Recommend</button><p id="a5"></p></div>
<script>
async function ask(){let v=document.getElementById('q1').value;S let r=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question:v})}); let d=await r.json(); document.getElementById('a1').innerText=d.answer;}
async function exp(){let v=document.getElementById('q2').value; let r=await fetch('/explain',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question:v})}); let d=await r.json(); document.getElementById('a2').innerText=d.explanation;}
async function sum(){let v=document.getElementById('q3').value; let r=await fetch('/summarize',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:v})}); let d=await r.json(); document.getElementById('a3').innerText=d.summary;}
async function quiz(){let v=document.getElementById('q4').value; let r=await fetch('/quiz',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({topic:v})}); let d=await r.json(); document.getElementById('a4').innerText=d.quiz;}
async function rec(){let v=document.getElementById('q5').value; let r=await fetch('/recommend',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({subject:v})}); let d=await r.json(); document.getElementById('a5').innerText=d.recommendations;}
</script></body></html>"""
@app.get("/", response_class=HTMLResponse)
def home(): return HTML
@app.post("/ask")
def ask_q(d:Q): return {"answer": get_answer(d.question)}
@app.post("/explain")
def explain_q(d:Q): return {"explanation": get_answer(d.question)}
@app.post("/summarize")
def summ_q(d:Q): return {"summary": ". ".join(d.text.split(".")[:2]) if d.text else "Paste text"}
@app.post("/quiz")
def quiz_q(d: Q):
    t = d.topic or d.question or "science"
    t = t.strip()
    return {"quiz": "Q1: What is " + t + "? A) " + t + " is a concept B) It is a game C) None Correct Answer: A \n\n Q2: Why learn " + t + "? A) For knowledge B) For fun C) None Correct Answer: A \n\n Q3: Where used? A) Real life B) Nowhere C) None Correct Answer: A"}

@app.post("/recommend")
def recommend_q(d: Q):
    t = d.topic or d.question or "python"
    t = t.strip()
    path = f"""My Skill: Learning Path: From Zero to Hero for "{t}"
This learning path is structured to progressively introduce {t} concepts, starting from the basics and advancing to more complex topics. It's designed to be adaptive, feel free to adjust the pace and delve deeper into areas that particularly interest you.

**1. Beginner Level: Building a Foundation**
**Estimated Time: 2-3 weeks**
**Key Topics:**
- What is {t}? Basics and Introduction
- Core Syntax and Data Types
- Control Flow (if, loops)
- Functions and Basic Operators
- Introduction to Tables and Columns

**2. Intermediate Level: Working with Multiple Tables**
**Estimated Time: 2-3 weeks**
**Key Topics:**
- Filtering Data (WHERE clause with comparison operators)
- Limiting Results (LIMIT, TOP)
- Functions (COUNT, SUM, AVG, MIN, MAX)
- JOINs and Relationships

**3. Advanced Level: Real-time Project**
**Project:** Build a Mini Project using {t} with practical implementation.
"""
    return {"recommendations": path}