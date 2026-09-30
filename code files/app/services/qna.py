from .gemini_client import ask_gemini


def answer_question(question: str) -> str:

    if not question.strip():
        return "Please enter a question."

    prompt = f"""
    You are EduGenie AI.
    Answer the student's question clearly and simply.

    Question:
    {question}
    """

    return ask_gemini(prompt)