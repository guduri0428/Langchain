from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()



video_id = "LPZh9BOjkQs"

## Step 1 Document Ingestion

try:
    object = YouTubeTranscriptApi()
    transcripts_list = object.fetch(video_id=video_id,languages=["en"]).snippets

    transcript = " ".join(each.text for each in transcripts_list)
    
except TranscriptsDisabled:
    print("No Captions Avaialbale for this Video")

# print(transcript)

## Splitting the Whose Text

splitter= RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.create_documents(texts=[transcript])

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store = FAISS.from_documents(
    documents=chunks,
    embedding=embedding_model
)

# print(vector_store.index_to_docstore_id)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/13.RAG (main)
# $ py rag_on_yt_transcripts.py
# {0: '5798feaf-65d2-4aa8-9117-f428e2492bb3', 1: '3562140c-f853-40c6-b1d7-6c47afcac94d', 2: '6438944d-c178-45a8-ae4f-dfd78674d3ca', 3: '4823e3b5-c242-4622-baf4-e98625487663', 4: 'bbfe430d-37ac-4319-a0bf-e916fa6a75b3', 5: '04ef3c14-0d83-4396-81a8-52cf786525e0', 6: '80a305ac-6849-4d44-b030-0c5563bdfa75', 7: 'e647da41-fa5b-4d43-b7b9-d92ef6874eab', 8: 'd35de3ff-9f44-4dba-b39f-fe1a978d8c31', 9: '55937d06-7b85-4222-ac21-3123f5914c9f'}
# (.venv)
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/13.RAG (main)
# $


vector_store.save_local(folder_path="FaissVectorDb",index_name="yt_index")