# Setup (Windows)

1. Put this folder in a simple path like C:\dev\genai (NOT OneDrive/Desktop).
2. Copy .env.example to .env and paste your NEW API keys.
3. In a terminal inside this folder:

    uv venv
    .venv\Scripts\activate
    uv pip install -r requirements.txt

4. Run:

    python chatmodels/chat.py
    python chatmodels/huggingface.py
    python chatmodels/localmodels.py
    python embeddingmodels/embeddings.py

If Windows still blocks .venv (error 4551), use Google Colab:
upload the .py files, run `!pip install -r requirements.txt`,
and store keys with Colab "Secrets" instead of .env.
