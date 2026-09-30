from .gemini_client import ask_gemini


def generate_quiz(topic: str):

    if not topic.strip():
        return "Please enter a topic."

    prompt = f"""
    Create 5 multiple-choice questions
    for a student about:

    {topic}

    Include:
    - Question
    - 4 options
    - Correct answer
    """

    return ask_gemini(prompt)