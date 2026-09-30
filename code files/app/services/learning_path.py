from .gemini_client import ask_gemini


def create_learning_path(subject: str):

    if not subject.strip():
        return "Please enter a subject."

    prompt = f"""
    Create a simple learning path for:

    {subject}

    Include:
    1. Beginner topics
    2. Intermediate topics
    3. Advanced topics
    4. Revision
    5. Practice
    """

    return ask_gemini(prompt)