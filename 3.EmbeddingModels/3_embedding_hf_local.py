from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

vectors = embedding.embed_documents(documents)

print(len(vectors)) # 3
print(type(vectors)) # <Class list>
print(len(vectors[0])) # 384

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/3.EmbeddingModels (main)
# $ py 3_embedding_hf_local.py
# 3
# <class 'list'>
# 384
# (.venv) 