from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model= "text-embedding-3-large"
)

doc1 = Document(
    page_content="Virat kohli is one of the most successful and consistent batsman in IPL history. known for his aggressive batting and leadership.",
    metadata={"team": "RCB"}
)

doc2 = Document(
    page_content="Rohith Sharma is the most successful captain in IPL history, leading mumbai indians to five titles. He's known for his elegant batting and record-breaking double centuries.",
    metadata={"team":"MI"}
)

doc3 = Document(
    page_content="MS Dhoni, famously known as captain Cool, has led chennai super kings to multiple IPL titles. His finishing skills,",
    metadata={
        "team": "CSK"
    }
)

doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for mumbai indians, he is known for his unorthodox action and yorkers.",
    metadata={"team": "MI"}
)

doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing chennai super kings",
    metadata={"team": "CSK"}
)
vector_store = Chroma(
    embedding_function= embeddings,
    persist_directory="chromadb",
    collection_name="sample"
)
docs = [doc1,doc2,doc3,doc4,doc5]

vector_store.add_documents(documents=docs)

print("Successfully Created Chroma Vector Database...!")




# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)
# $ py 1_chromadb_creation.py
# F:\Gen AI Repos\Langchain\11.VectorDatabase\1_working_with_Chroma\1_chromadb_creation.py:38: LangChainDeprecationWarning: The class `Chroma` was deprecated in LangChain 0.2.9 and will be removed in 1.0. An updated version of the class exists in the `langchain-chroma package and should be used instead. To use it run `pip install -U `langchain-chroma` and import as `from `langchain_chroma import Chroma``.
#   vector_store = Chroma(
# Successfully Created Chroma Vector Database...!
# (.venv)
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)
# $