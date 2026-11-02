from pathlib import Path
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

print("1. Program started")

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
print("2. .env loaded")

model = init_chat_model(
    "openai/gpt-oss-20b",
    temperature=0.5,
    max_tokens=200,
    model_provider="groq",
)

print("3. Model created")

response = model.invoke("Give a poem on AI")
print(response.content)
