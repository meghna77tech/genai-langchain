from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "hello world",
    "my name is John",
    "I love programming",
]

vectors = embeddings.embed_documents(texts)
print(vectors)
