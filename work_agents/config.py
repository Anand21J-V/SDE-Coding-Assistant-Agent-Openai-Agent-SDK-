import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled

load_dotenv(override=True)

# ---------------- SETUP ----------------
google_api_key = os.getenv("GEMINI_API_KEY")
if not google_api_key:
    raise RuntimeError("❌ GEMINI_API_KEY is not set in environment variables.")

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GEMINI_MODEL = "gemini-2.0-flash"   # or "gemini-2.0-pro"

# Initialize Gemini client
gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
gemini_model = OpenAIChatCompletionsModel(model=GEMINI_MODEL, openai_client=gemini_client)

# Disable tracing (optional)
set_tracing_disabled(True)
