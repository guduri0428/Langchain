from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about Virat Kohli"

documents_vectors = embedding.embed_documents(documents)
query_vector = embedding.embed_query(query)

scores = cosine_similarity([query_vector],documents_vectors)[0]

# list_of_tuples = list(enumerate(scores)) #it will give list of tuple [(,),(,)]

index , score = sorted(list(enumerate(scores)), key=lambda x:x[1], reverse=True)[0]

print(query)
print(documents[index])
print("similarity score is:", score)


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/3.EmbeddingModels (main)
# $ py 4_document_similarity_hf.py
# tell me about Ms Dhoni
# MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.
# similarity score is: 0.7709247754175215
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/3.EmbeddingModels (main)
# $ py 4_document_similarity_hf.py
# tell me about Jasprit Bumrah
# Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers.
# similarity score is: 0.7814421891142136
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/3.EmbeddingModels (main)
# $ py 4_document_similarity_hf.py
# tell me about Rohith Sharma
# Rohit Sharma is known for his elegant batting and record-breaking double centuries.
# similarity score is: 0.7088316781003972
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/3.EmbeddingModels (main)
# $ py 4_document_similarity_hf.py
# tell me about Sachin Tendulkar
# Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.
# similarity score is: 0.7215699378206438
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/3.EmbeddingModels (main)
# $ py 4_document_similarity_hf.py
# tell me about Virat Kohli
# Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.
# similarity score is: 0.8177796329625064
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/3.EmbeddingModels (main)
# $
