from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter


loader = PyPDFLoader(
    file_path="dl-curriculum.pdf"
)

docs = loader.load()


splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0,
    separator= " "
)

chunks = splitter.split_documents(documents=docs)

print(len(chunks))