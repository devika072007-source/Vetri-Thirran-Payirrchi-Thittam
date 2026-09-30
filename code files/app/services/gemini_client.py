from app.config import GEMINI_API_KEY


def ask_gemini(prompt: str) -> str:
    """
    Gemini API இணைக்க வேண்டிய இடம்.
    API key இல்லையெனில் basic response கொடுக்கும்.
    """

    if not GEMINI_API_KEY:
        return (
            "Gemini API key இன்னும் சேர்க்கப்படவில்லை. "
            "Basic EduGenie response பயன்படுத்தப்படுகிறது."
        )

    # இங்கே Gemini API integration சேர்க்கலாம்.
    return "AI response: " + prompt