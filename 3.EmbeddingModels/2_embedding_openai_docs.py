from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model= "text-embedding-3-large",
    dimensions=32
)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

print(len(result)) # 3
print('-'*40)
print(type(result)) # <Class List >
print('-'*40)
print(len(result[0])) # 32

# $ py 2_embedding_openai_docs.py 
# 3
# ----------------------------------------
# <class 'list'>
# ----------------------------------------
# 32