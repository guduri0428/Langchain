from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-large"
)

vector_store = Chroma(
    embedding_function= embeddings,
    persist_directory="chromadb",
    collection_name="sample"
)

## ==============Start Load the Vector Store and Fetch the relavent Documents======================

# result = vector_store.similarity_search(
#     query="who is virat kohli",
#     k=2
# )


# print(result)

# print("I have Loaded the Vector Database into the Runtime..")


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)
# $ py 2_CRUD_on_ChromaDb.py
# F:\Gen AI Repos\Langchain\11.VectorDatabase\1_working_with_Chroma\2_CRUD_on_ChromaDb.py:12: LangChainDeprecationWarning: The class `Chroma` 
# was deprecated in LangChain 0.2.9 and will be removed in 1.0. An updated version of the class exists in the `langchain-chroma package and should be used instead. To use it run `pip install -U `langchain-chroma` and import as `from `langchain_chroma import Chroma``.
#   vector_store = Chroma(
# [Document(metadata={'team': 'RCB'}, page_content='Virat kohli is one of the most successful and consistent batsman in IPL history. known for his aggressive batting and leadership.'), Document(metadata={'team': 'MI'}, page_content="Rohith Sharma is the most successful captain in IPL history, leading mumbai indians to five titles. He's known for his elegant batting and record-breaking double centuries.")]
# I have Loaded the Vector Database into the Runtime..
# (.venv)
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)

## ==============End Load the Vector Store and Fetch the relavent Documents======================

## ++++++++++++++Start Load the Vector Store and View the Documents++++++++++++++++++++

# result = vector_store.get(include=["embeddings","documents","metadatas"])
# print(type(result))

# print(result)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)
# $ py 2_CRUD_on_ChromaDb.py
# F:\Gen AI Repos\Langchain\11.VectorDatabase\1_working_with_Chroma\2_CRUD_on_ChromaDb.py:12: LangChainDeprecationWarning: The class `Chroma` 
# was deprecated in LangChain 0.2.9 and will be removed in 1.0. An updated version of the class exists in the `langchain-chroma package and should be used instead. To use it run `pip install -U `langchain-chroma` and import as `from `langchain_chroma import Chroma``.
#   vector_store = Chroma(
# <class 'dict'>
# {'ids': ['29040178-71c0-46ac-8b0d-7159ed8e6b35', '48681d10-21ad-402e-a4a4-6db4c62094bc', 'a80da1bd-1d78-41ca-9bfa-6908f6d48c73', 'fc31043a-2ff8-454b-8f33-f53ebac493cd', '19975cf6-c580-4313-94f8-8ef6516c606b'], 'embeddings': array([[-0.00026376, -0.01230876, -0.0095305 , ...,  0.01446572,
#         -0.01774806,  0.00865716],
#        [-0.00146499, -0.02566655, -0.01312059, ..., -0.00061241,
#         -0.00410916, -0.00066441],
#        [ 0.05491702, -0.04306594, -0.01148072, ..., -0.00310826,
#         -0.00972819, -0.00894121],
#        [-0.00628206, -0.03332322, -0.0130282 , ...,  0.00065438,
#         -0.00347777,  0.01135865],
#        [ 0.00179951, -0.01624205, -0.01220251, ...,  0.00616718,
#          0.01165712, -0.02127648]], shape=(5, 3072)), 'documents': ['Virat kohli is one of the most successful and consistent batsman in IPL history. known for his aggressive batting and leadership.', "Rohith Sharma is the most successful captain in IPL history, leading mumbai indians to five titles. He's known for his elegant batting and record-breaking double centuries.", 'MS Dhoni, famously known as captain Cool, 
# has led chennai super kings to multiple IPL titles. His finishing skills,', 'Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for mumbai indians, he is known for his unorthodox action and yorkers.', 'Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing chennai super kings'], 'uris': None, 'included': ['embeddings', 'documents', 'metadatas'], 'data': None, 'metadatas': [{'team': 'RCB'}, {'team': 'MI'}, {'team': 'CSK'}, {'team': 'MI'}, {'team': 'CSK'}]}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)

## ++++++++++++++End Load the Vector Store and View the Documents++++++++++++++++++++++


## ==============Start Load the Vector Store and Fetch the relavent Documents with score ======================

# result = vector_store.similarity_search_with_score(
#     query="who is virat kohli"
# )

# print(result)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)
# $ py 2_CRUD_on_ChromaDb.py
# F:\Gen AI Repos\Langchain\11.VectorDatabase\1_working_with_Chroma\2_CRUD_on_ChromaDb.py:12: LangChainDeprecationWarning: The class `Chroma` 
# was deprecated in LangChain 0.2.9 and will be removed in 1.0. An updated version of the class exists in the `langchain-chroma package and should be used instead. To use it run `pip install -U `langchain-chroma` and import as `from `langchain_chroma import Chroma``.
#   vector_store = Chroma(
# [(Document(metadata={'team': 'RCB'}, page_content='Virat kohli is one of the most successful and consistent batsman in IPL history. known for his aggressive batting and leadership.'), 0.774749755859375), (Document(metadata={'team': 'MI'}, page_content="Rohith Sharma is the most successful captain in IPL history, leading mumbai indians to five titles. He's known for his elegant batting and record-breaking double centuries."), 1.2702594995498657), (Document(metadata={'team': 'CSK'}, page_content='Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing chennai super kings'), 1.384774923324585), (Document(metadata={'team': 'CSK'}, page_content='MS Dhoni, famously known as captain Cool, has led chennai super kings to multiple IPL titles. His finishing skills,'), 1.3974679708480835)]
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)
## ==============End Load the Vector Store and Fetch the relavent Documents with score======================


## ==============Start Load the Vector Store and Fetch the  Documents by filtering on metadata=======

# result = vector_store.similarity_search_with_score(
#     query="",
#     filter={"team": "CSK"}
# )

# print(result)


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)
# $ py 2_CRUD_on_ChromaDb.py
# F:\Gen AI Repos\Langchain\11.VectorDatabase\1_working_with_Chroma\2_CRUD_on_ChromaDb.py:12: LangChainDeprecationWarning: The class `Chroma` 
# was deprecated in LangChain 0.2.9 and will be removed in 1.0. An updated version of the class exists in the `langchain-chroma package and should be used instead. To use it run `pip install -U `langchain-chroma` and import as `from `langchain_chroma import Chroma``.
#   vector_store = Chroma(
# [(Document(metadata={'team': 'CSK'}, page_content='MS Dhoni, famously known as captain Cool, has led chennai super kings to multiple IPL titles. His finishing skills,'), 1.852333664894104), (Document(metadata={'team': 'CSK'}, page_content='Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing chennai super kings'), 1.8900611400604248)]
# (.venv)
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)
## ==============End Load the Vector Store and Fetch the  Documents by filtering on metadata=======


## ==============Start Load the Vector Store and Update the  Document by id=======
# updated_doc = Document(
#     page_content="Virat kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership ans consistency batting",
#     metadata={'team':"RCB"}
# )

# result = vector_store.update_document(document_id='29040178-71c0-46ac-8b0d-7159ed8e6b35',document=updated_doc)
# print(None)

# print(vector_store.get(include=["embeddings","documents","metadatas"]))

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)
# $ py 2_CRUD_on_ChromaDb.py
# F:\Gen AI Repos\Langchain\11.VectorDatabase\1_working_with_Chroma\2_CRUD_on_ChromaDb.py:12: LangChainDeprecationWarning: The class `Chroma` 
# was deprecated in LangChain 0.2.9 and will be removed in 1.0. An updated version of the class exists in the `langchain-chroma package and should be used instead. To use it run `pip install -U `langchain-chroma` and import as `from `langchain_chroma import Chroma``.
#   vector_store = Chroma(
# None
# {'ids': ['29040178-71c0-46ac-8b0d-7159ed8e6b35', '48681d10-21ad-402e-a4a4-6db4c62094bc', 'a80da1bd-1d78-41ca-9bfa-6908f6d48c73', 'fc31043a-2ff8-454b-8f33-f53ebac493cd', '19975cf6-c580-4313-94f8-8ef6516c606b'], 'embeddings': array([[ 0.01764387, -0.0295654 , -0.00052076, ...,  0.0083193 ,
#         -0.01360988,  0.00245841],
#        [-0.00146499, -0.02566655, -0.01312059, ..., -0.00061241,
#         -0.00410916, -0.00066441],
#        [ 0.05491702, -0.04306594, -0.01148072, ..., -0.00310826,
#         -0.00972819, -0.00894121],
#        [-0.00628206, -0.03332322, -0.0130282 , ...,  0.00065438,
#         -0.00347777,  0.01135865],
#        [ 0.00179951, -0.01624205, -0.01220251, ...,  0.00616718,
#          0.01165712, -0.02127648]], shape=(5, 3072)), 'documents': ['Virat kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership ans consistency batting', "Rohith Sharma is the most successful captain in IPL history, leading mumbai indians to five titles. He's known for his elegant batting and record-breaking double centuries.", 'MS Dhoni, famously known as captain 
# Cool, has led chennai super kings to multiple IPL titles. His finishing skills,', 'Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for mumbai indians, he is known for his unorthodox action and yorkers.', 'Ravindra Jadeja is a dynamic all-rounder 
# who contributes with both bat and ball. Representing chennai super kings'], 'uris': None, 'included': ['embeddings', 'documents', 'metadatas'], 'data': None, 'metadatas': [{'team': 'RCB'}, {'team': 'MI'}, {'team': 'CSK'}, {'team': 'MI'}, {'team': 'CSK'}]}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)

## ==============End Load the Vector Store and Update the  Document by id=========



## ==============Start Load the Vector Store and Delete  Documents by ids=======

vector_store.delete(
    ids=["29040178-71c0-46ac-8b0d-7159ed8e6b35"]
)

result = vector_store.get(include=[
    "embeddings",
    "documents",
    "metadatas"
])

print(result)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)
# $ py 2_CRUD_on_ChromaDb.py
# F:\Gen AI Repos\Langchain\11.VectorDatabase\1_working_with_Chroma\2_CRUD_on_ChromaDb.py:12: LangChainDeprecationWarning: The class `Chroma` 
# was deprecated in LangChain 0.2.9 and will be removed in 1.0. An updated version of the class exists in the `langchain-chroma package and should be used instead. To use it run `pip install -U `langchain-chroma` and import as `from `langchain_chroma import Chroma``.
#   vector_store = Chroma(
# {'ids': ['48681d10-21ad-402e-a4a4-6db4c62094bc', 'a80da1bd-1d78-41ca-9bfa-6908f6d48c73', 'fc31043a-2ff8-454b-8f33-f53ebac493cd', '19975cf6-c580-4313-94f8-8ef6516c606b'], 'embeddings': array([[-0.00146499, -0.02566655, -0.01312059, ..., -0.00061241,
#         -0.00410916, -0.00066441],
#        [ 0.05491702, -0.04306594, -0.01148072, ..., -0.00310826,
#         -0.00972819, -0.00894121],
#        [-0.00628206, -0.03332322, -0.0130282 , ...,  0.00065438,
#         -0.00347777,  0.01135865],
#        [ 0.00179951, -0.01624205, -0.01220251, ...,  0.00616718,
#          0.01165712, -0.02127648]], shape=(4, 3072)), 'documents': ["Rohith Sharma is the most successful captain in IPL history, leading mumbai indians to five titles. He's known for his elegant batting and record-breaking double centuries.", 'MS Dhoni, famously known as captain Cool, has led chennai super kings to multiple IPL titles. His finishing skills,', 'Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for mumbai indians, he is known for his unorthodox action and yorkers.', 'Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing chennai super kings'], 'uris': None, 'included': ['embeddings', 'documents', 'metadatas'], 'data': None, 'metadatas': [{'team': 'MI'}, {'team': 'CSK'}, {'team': 'MI'}, {'team': 'CSK'}]}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/11.VectorDatabase/1_working_with_Chroma (main)

## ==============End Load the Vector Store and Delete  Documents by ids=======
