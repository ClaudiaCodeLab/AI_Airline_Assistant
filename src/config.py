import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys & Model Selection
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
USE_OPENAI = bool(OPENAI_API_KEY)  # Auto-detect OpenAI usage
OPENAI_MODEL = "gpt-4o-mini"
OLLAMA_MODEL = "llama3.2"

SYSTEM_MESSAGE = (
    "You are a helpful assistant for an Airline called FlightAI. "
    "Give short, courteous answers, no more than 1 sentence. "
    "Always be accurate. If you don't know the answer, say so."
)