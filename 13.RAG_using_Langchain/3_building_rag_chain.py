from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnablePassthrough, RunnableLambda
from typing import List
from langchain_core.documents import Document

from dotenv import load_dotenv
load_dotenv()


embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

model = ChatOpenAI(
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

vector_store = FAISS.load_local(
    folder_path="FaissVectorDb",
    embeddings=embedding_model,
    index_name="yt_index",
    allow_dangerous_deserialization=True
)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k":3}
)

def format_docs(docs: List[Document]) -> str :
    return "\n\n".join(doc.page_content for doc in docs)



parallel_chain = RunnableParallel(
    {
        "context": retriever | RunnableLambda(func=format_docs),
        "question": RunnablePassthrough()
    }
)


question = "who is demis"
# answer = parallel_chain.invoke(question)
# print(answer)

parser = StrOutputParser()

main_rag_chain = parallel_chain |  prompt | model | parser

answer = main_rag_chain.invoke(question)
print(answer)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/13.RAG (main)
# $ py 3_building_rag_chain.py
# I don't know.
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/13.RAG (main)