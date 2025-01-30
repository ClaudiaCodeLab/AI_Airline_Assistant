import json
from function_calling import detect_ticket_query, handle_tool_call, PRICE_FUNCTION
from models import query_openai, query_ollama
from config import SYSTEM_MESSAGE, USE_OPENAI
from tools import get_ticket_price

def chat(message, history):
    """Determines whether to use OpenAI (function calling) or Llama (manual execution)."""
    
    # Step 1: Check for manual function calling (Llama only)
    city = detect_ticket_query(message)
    if city:
        price = get_ticket_price(city)
        return f"A return ticket to {city.capitalize()} costs {price}."

    # Step 2: OpenAI with function calling support
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}] + history + [{"role": "user", "content": message}]

    if USE_OPENAI:
        response = query_openai(messages, tools=[{"type": "function", "function": PRICE_FUNCTION}])
        
        if response.choices[0].finish_reason == "tool_calls":
            tool_response = handle_tool_call(response.choices[0].message)
            messages.append(tool_response)
            response = query_openai(messages)  # Get final response
        
        return response.choices[0].message.content

    # Step 3: If no OpenAI, use Llama via Ollama
    return query_ollama(messages)
