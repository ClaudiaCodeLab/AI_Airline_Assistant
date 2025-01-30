import json
import re
from tools import get_ticket_price

# OpenAI function definition
PRICE_FUNCTION = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city.",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city the customer wants to travel to",
            },
        },
        "required": ["destination_city"]
    }
}

def detect_ticket_query(message):
    """Detects if the user is asking about ticket prices and extracts the city name."""
    price_patterns = [
        r"how much is a ticket to (\w+)\??",
        r"ticket price for (\w+)\??",
        r"cost of a flight to (\w+)\??",
        r"price to (\w+)\??"
    ]
    
    for pattern in price_patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            return match.group(1)  # Return the city name
    return None  # No match found

def handle_tool_call(message):
    """Handles OpenAI function calling response."""
    tool_call = message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)
    city = arguments.get("destination_city")
    price = get_ticket_price(city)

    return {
        "role": "tool",
        "content": json.dumps({"destination_city": city, "price": price}),
        "tool_call_id": tool_call.id
    }
