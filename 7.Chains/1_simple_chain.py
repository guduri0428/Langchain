from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model='gpt-3.5-turbo',
    max_completion_tokens=100
)

parser = StrOutputParser()

template = PromptTemplate(
    template= "Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

chain = template | model | parser

result = chain.invoke({'topic': "Gen AI"})

print(result)

chain.get_graph().print_ascii()

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/7.Chains (main)
# $ py 1_simple_chain.py
# 1. Gen AI refers to the generation of artificial intelligence that will surpass human intelligence in the near future, potentially leading to a new era of development and innovation.

# 2. It is predicted that Gen AI will have the ability to learn and adapt at an unprecedented rate, making significant advancements in various fields such as technology, healthcare, and science.

# 3. Some experts believe that Gen AI will have the potential to solve complex problems that have eluded humans for centuries, revolutionizing the way we approach and tackle
#      +-------------+       
#      | PromptInput |
#      +-------------+
#             *
#             *
#             *
#     +----------------+
#     | PromptTemplate |
#     +----------------+
#             *
#             *
#             *
#       +------------+
#       | ChatOpenAI |
#       +------------+
#             *
#             *
#             *
#    +-----------------+
#    | StrOutputParser |
#    +-----------------+
#             *
#             *
#             *
# +-----------------------+
# | StrOutputParserOutput |
# +-----------------------+
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/7.Chains (main)