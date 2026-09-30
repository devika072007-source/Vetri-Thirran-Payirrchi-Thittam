from .gemini_client import ask_gemini


def explain_topic(topic: str) -> str:

    if not topic.strip():
        return "Please enter a topic."

    prompt = f"""
    Explain this topic to a student in simple language:

    {topic}

    Give:
    1. Meaning
    2. Important points
    3. Simple example
    """

    return ask_gemini(prompt)