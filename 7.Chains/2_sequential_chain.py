from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model='gpt-3.5-turbo',
    max_completion_tokens=500
)

parser = StrOutputParser()

template1 = PromptTemplate(
    template= "Write a detailed report on the {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template= "write a 5 line summary of the following text \n {text}",
    input_variables=['text']
)

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'Gen AI'})

print(result)

chain.get_graph().print_ascii()




# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/7.Chains (main)
# $ py 2_sequential_chain.py
# As technology advances, Gen AI is a new generation of AI systems designed to be more intelligent and human-like. These systems can think, learn, and adapt like humans, with the ability to understand context and reason. Key features include learning from experience and interpreting natural language for more intuitive interaction. Applications range from healthcare and finance to retail, revolutionizing how industries 
# operate. Despite potential biases and ethical concerns, Gen AI has the potential to greatly benefit society and transform the way we engage 
# with technology.
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