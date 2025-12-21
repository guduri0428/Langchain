from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-3.5-turbo"
)

template1 = PromptTemplate(
    template= "Generate a tweet about topic {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Generate a Linkdin post about topic {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet" : RunnableSequence(template1,model,parser),
    "post": RunnableSequence(template2,model,parser)
})

result = parallel_chain.invoke({"topic": "Gen AI"})

print(result["tweet"])
print("--"*30)
print(result["post"])
print("--"*30)
parallel_chain.get_graph().print_ascii()


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)
# $ py 2_runnable_parallel.py
# Excited to see how Gen AI will revolutionize industries with its ability to learn, adapt, and innovate like never before. The future is looking bright with artificial intelligence leading the way! #GenAI #AIRevolution ��🌟🌟
# ------------------------------------------------------------
# Excited to delve into the world of Gen AI - the next generation of artificial intelligence that is revolutionizing industries and consumer experiences. From personalized recommendations to predictive analytics, Gen AI is driving innovation and transforming the way we work and interact with technology. I can't wait to see how this cutting-edge technology continues to shape the future. #GenAI #ArtificialIntelligence #Innovation #FutureTech.
# ------------------------------------------------------------
#             +---------------------------+
#             | Parallel<tweet,post>Input |
#             +---------------------------+
#                  **               **
#               ***                   ***
#             **                         **
# +----------------+                +----------------+
# | PromptTemplate |                | PromptTemplate |
# +----------------+                +----------------+
#           *                               *
#           *                               *
#           *                               *
#   +------------+                    +------------+
#   | ChatOpenAI |                    | ChatOpenAI |
#   +------------+                    +------------+
#           *                               *
#           *                               *
#           *                               *
# +-----------------+              +-----------------+
# | StrOutputParser |              | StrOutputParser |
# +-----------------+              +-----------------+
#                  **               **
#                    ***         ***
#                       **     **
#            +----------------------------+
#            | Parallel<tweet,post>Output |
#            +----------------------------+
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)