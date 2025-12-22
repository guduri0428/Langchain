from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# docs = loader.load()

# print(len(docs))

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/9.DocumentLoaders (main)
# $ py 3_directory_loader.py
# 349
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/9.DocumentLoaders (main)

docs = loader.lazy_load()

for doc in docs:
    print(doc.metadata)