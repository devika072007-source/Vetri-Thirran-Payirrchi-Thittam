from .gemini_client import ask_gemini


def summarize_text(text: str) -> str:

    if not text.strip():
        return "Please enter text to summarize."

    prompt = f"""
    Summarize the following study material
    in simple student-friendly points:

    {text}
    """

    return ask_gemini(prompt)