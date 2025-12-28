from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    top_k_results= 3,
    lang= "en"
)

query = "How to Learn Agentic AI and Best SDK's in the Market ?"

docs = retriever.invoke(query)

# print(docs)


for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(f"Content :\n{doc.page_content}")