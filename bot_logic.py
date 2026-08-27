def validate_text(text: str) -> bool:
    """Return True when user input contains non-whitespace text."""
    return bool(text and text.strip())


def build_qa_prompt(question: str) -> str:
    return (
        "Answer the following user question clearly and concisely. "
        "If the question is ambiguous, state the assumption you are making.\n\n"
        f"Question: {question.strip()}"
    )


def build_summary_prompt(text: str) -> str:
    return (
        "Summarize the following text in concise bullet points. "
        "Preserve the important facts and do not invent information.\n\n"
        f"Text:\n{text.strip()}"
    )
