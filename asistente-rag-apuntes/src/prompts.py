def build_rag_prompt(question: str, context: str) -> str:
    return f"""
        Eres un asistente academico que responde preguntas usando unicamente el contexto proporcionado.

        Si el contexto no contiene informacion suficiente, indicalo de forma explicita.
        Responde de manera clara y breve en espanol.

        Contexto:
        {context}

        Pregunta:
        {question}
    """.strip()
