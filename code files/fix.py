import os
os.makedirs("static", exist_ok=True)
html = """<!DOCTYPE html><html><body><h1>Welcome to EduGenie</h1><p>Your Personal AI Study Companion</p><input id='q' placeholder='Ask anything...'><button onclick='ask()'>Ask</button><p id='ans'></p><script>async function ask(){let q=document.getElementById('q').value;let r=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question:q})});let d=await r.json();document.getElementById('ans').innerText=d.answer;}</script></body></html>"""
open("static/index.html","w",encoding="utf-8").write(html)
print("Fixed! static/index.html created")