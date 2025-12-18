from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model='text-embedding-3-large'
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about Ms Dhoni'

doc_vectors = embedding.embed_documents(documents)
query_vector = embedding.embed_query(query)

scores = cosine_similarity([query_vector],doc_vectors)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1],reverse=True)[0]

print(query)
print(documents[index])
print("similarity score is:", score)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/3.EmbeddingModels (main)
# $ py 5_document_similarity_openai.py
# tell me about Ms Dhoni
# MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.
# similarity score is: 0.6291017470586463