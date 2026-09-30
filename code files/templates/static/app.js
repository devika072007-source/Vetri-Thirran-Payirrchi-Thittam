async function getRecommendations() {
  let t = document.getElementById('learningSubject').value;
  let r = await fetch('/recommend', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ topic: t })
  });
  let d = await r.json();
  document.getElementById('recommendations').innerText = d.recommendations; 
}

async function generateQuiz() {
  let t = document.querySelectorAll('input')[1].value;
  let r = await fetch('/quiz', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ topic: t })
  });
  let d = await r.json();
  document.getElementById('quizResult').innerText = d.quiz;
}