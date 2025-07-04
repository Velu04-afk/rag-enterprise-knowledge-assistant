import os
import cohere

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(COHERE_API_KEY)


def generate_answer(query: str, context: str) -> str:

    prompt = f"""You are a helpful medical assistant.

Context:
{context}

Question:
{query}

Answer:"""

    response = co.chat(
        model="command-a-03-2025",   # or "command-r"
        messages=[{"role": "user", "content": prompt}],
    )

    return response.message.content[0].text
