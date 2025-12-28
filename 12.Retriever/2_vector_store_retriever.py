from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()


documents = [
    Document(page_content="Langchain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vectoe Databse Optimised for LLM-based search"),
    Document(page_content="Embeddings convert text into high dimensional vectors"),
    Document(page_content="OpenAI provides powerful embedding models")
]

embedding_model = OpenAIEmbeddings(
    model= "text-embedding-3-large",
)


# Creates Chroma VectorStore in Memory
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

# retriever = vector_store.as_retriever(
#     searach_kwargs={"k":2}
# )

# query = "What is Chroma used for ?"

# docs = retriever.invoke(query)

# for i,doc in enumerate(docs):
#     print(f"\n --- Result {i+1} ---")
#     print(f"Content: {doc.page_content}")

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/12.Retriever (main)
# $ py 2_vector_store_retriever.py

#  --- Result 1 ---
# Content: Chroma is a vectoe Databse Optimised for LLM-based search

#  --- Result 2 ---
# Content: Langchain helps developers build LLM applications easily.

#  --- Result 3 ---
# Content: Embeddings convert text into high dimensional vectors

#  --- Result 4 ---
# Content: OpenAI provides powerful embedding models
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/12.Retriever (main)


retriever = vector_store.as_retriever(
    search_type= "mmr",
    search_kwargs= {"k": 3, "lambda_mult": 1}
)

query = "what is Langchain"

docs = retriever.invoke(query)

for i,doc in enumerate(docs):
    print(f"\n --- Result {i+1} ---")
    print(f"Content: {doc.page_content}")
