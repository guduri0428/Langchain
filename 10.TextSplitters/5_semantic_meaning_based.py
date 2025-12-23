from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


splitter  = SemanticChunker(
    embeddings=OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.


Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

chunks = splitter.create_documents([sample])

print(len(chunks))

print(chunks[0])

print("--"*30)

print(chunks[1])




# splitter  = SemanticChunker(
#     embeddings=OpenAIEmbeddings(),
#     breakpoint_threshold_type="standard_deviation",
#     breakpoint_threshold_amount=2
# )
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/10.TextSplitters (main)
# $ py 5_semantic_meaning_based.py
# 2
# page_content='
# Farmers were working hard in the fields, preparing the soil and planting seeds for the next season.'
# ------------------------------------------------------------
# page_content='The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams. Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety. '
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/10.TextSplitters (main)



# splitter  = SemanticChunker(
#     embeddings=OpenAIEmbeddings(),
#     breakpoint_threshold_type="standard_deviation",
#     breakpoint_threshold_amount=1


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/10.TextSplitters (main)
# $ py 5_semantic_meaning_based.py
# 3
# page_content='
# Farmers were working hard in the fields, preparing the soil and planting seeds for the next season.'
# ------------------------------------------------------------
# page_content='The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.'
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/10.TextSplitters (main)