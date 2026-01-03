from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store = FAISS.load_local(
    folder_path="FaissVectorDb",
    embeddings=embedding_model,
    index_name="yt_index",
    allow_dangerous_deserialization=True
)

# print(vector_store.index_to_docstore_id)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/13.RAG (main)
# $ py 2_retrieval_rag_on_yt_transcripts.py
# {0: '70aad1a3-c8cf-43b2-8419-d13d8f892218', 1: '718643ed-9f25-4600-bac0-7426436272a2', 2: '80acf14b-7799-48c6-8153-b6e828d6e289', 3: 'c6426832-e4d1-4167-abca-7d188ed6f938', 4: '81dd6f96-808a-4f6a-917c-2db52bcd90a6', 5: '601e1f37-5448-400b-903e-5436aa64ff59', 6: '3a04d772-4e64-4207-b2dd-61b386e3a7e7', 7: 'c5c61406-2661-4bfa-9596-1b0dd011d686', 8: '2aaca24f-f17e-4930-90a0-b1998e886bc4', 9: '0d998321-19d1-4752-966a-1dd17522a7d0'}
# (.venv)
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/13.RAG (main)

retriever = vector_store.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k":4}
)

# print(retriever)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/13.RAG (main)
# $ py 2_retrieval_rag_on_yt_transcripts.py
# tags=['FAISS', 'OpenAIEmbeddings'] vectorstore=<langchain_community.vectorstores.faiss.FAISS object at 0x000001E9E0774590> search_kwargs={'k': 4}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/13.RAG (main)

# retrieved_docs = retriever.invoke("what is deepmind")

# print(retrieved_docs)

llm = ChatOpenAI(
    model="gpt-3.5-turbo"
)

prompt = PromptTemplate(
    template="""
        You are helpful assistant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say you don't know.

        {context}
        Question: {question}
        """,
    input_variables=["context","question"]
)

question = "is the topic of alliens discussed in this video? If yes then what was discussed"
retrieved_docs = retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

final_prompt  = prompt.invoke(input={"question": question, "context": context_text})

# print(final_prompt)

answer = llm.invoke(final_prompt)

print(answer.content)