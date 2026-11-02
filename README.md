# GenAI LangChain Practice

Small Python project that shows how to use different language models and embeddings with **LangChain**.

## What's inside

| File | What it does | Needs |
|---|---|---|
| `chatmodels/chat.py` | Chats with `gpt-oss-20b` through Groq | `GROQ_API_KEY` |
| `chatmodels/huggingface.py` | Chats with DeepSeek-R1-Distill-Qwen-7B through the Hugging Face endpoint | `HUGGINGFACEHUB_API_TOKEN` |
| `chatmodels/localmodels.py` | Runs TinyLlama locally on your computer | No key (about 2 GB download on first run) |
| `embeddingmodels/embeddings.py` | Turns sentences into vectors with `all-MiniLM-L6-v2` | No key |

## Tech used

- Python
- LangChain (`langchain`, `langchain-groq`, `langchain-huggingface`)
- Hugging Face Transformers and Sentence-Transformers
- python-dotenv for API keys
- uv for the virtual environment

## Setup

1. Clone the repo:
   ```
   git clone https://github.com/meghna77tech/genai-langchain.git
   cd genai-langchain
   ```
2. Create and activate a virtual environment, then install the packages:
   ```
   uv venv
   .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your own keys:
   ```
   GROQ_API_KEY="your-key"
   HUGGINGFACEHUB_API_TOKEN="your-token"
   ```
   Never commit the `.env` file. It is already listed in `.gitignore`.

## Run

```
python chatmodels/chat.py
python chatmodels/huggingface.py
python chatmodels/localmodels.py
python embeddingmodels/embeddings.py
```

## Notes

- `chat.py` limits answers to 200 tokens. Raise `max_tokens` for longer replies.
- If Windows blocks the `.venv` Python (error 4551), move the project out of OneDrive or run it in Google Colab.

## What I learned

- Calling chat models from different providers with the same LangChain interface
- Running a model locally versus through an API
- Creating text embeddings
- Keeping API keys out of code with `.env`
