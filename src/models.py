

import ollama
from openai import OpenAI
from config import USE_OPENAI, OPENAI_API_KEY, OPENAI_MODEL, OLLAMA_MODEL

# Initialize OpenAI client if available
if USE_OPENAI:
    openai = OpenAI()

def query_openai(messages, tools=None):
    """Queries OpenAI GPT model, with optional function calling."""
    response = openai.chat.completions.create(
        model=OPENAI_MODEL,
        messages=messages,
        tools=tools if tools else []
    )
    return response

def query_ollama(messages):
    """Queries Ollama's local Llama model."""
    formatted_prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
    response = ollama.chat(model=OLLAMA_MODEL, messages=[{"role": "user", "content": formatted_prompt}])
    return response["message"]["content"]
