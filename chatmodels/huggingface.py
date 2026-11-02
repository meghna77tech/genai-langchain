from pathlib import Path
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Reads HUGGINGFACEHUB_API_TOKEN from the .env file (no key in code)
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
    task="text-generation",
    max_new_tokens=200,
    temperature=0.7,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Who are you?")
print(response.content)
