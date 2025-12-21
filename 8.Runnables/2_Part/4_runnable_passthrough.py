from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model= "gpt-3.5-turbo"
)

template1  = PromptTemplate(
    template= "Write a joke about the topic {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template= "Explain the following joke \n {joke}"
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(template1,model,parser)

explanation_chain = RunnableSequence(template2,model,parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": explanation_chain
})

passthrough_chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = passthrough_chain.invoke({'topic': 'AI'})

print(result)
print("--"*30)
passthrough_chain.get_graph().print_ascii()



# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)
# $ py 4_runnable_passthrough.py
# {'joke': 'Why did the computer go to therapy? \nBecause it had too many bytes of emotional baggage!', 'explanation': 'This joke plays on the double meaning of the term "bytes." In the world of computers, a byte is a unit of digital information. However, in the context of mental health or therapy, "baggage" often refers to emotional issues or problems that someone is carrying with them. The joke is a play on words, suggesting that the computer went to therapy because it had too many "bytes" (digital information) of emotional baggage.'}
# ------------------------------------------------------------
#                   +-------------+
#                   | PromptInput |
#                   +-------------+
#                           *
#                           *
#                           *
#                 +----------------+
#                 | PromptTemplate |
#                 +----------------+
#                           *
#                           *
#                           *
#                   +------------+
#                   | ChatOpenAI |
#                   +------------+
#                           *
#                           *
#                           *
#                 +-----------------+
#                 | StrOutputParser |
#                 +-----------------+
#                           *
#                           *
#                           *
#         +---------------------------------+
#         | Parallel<joke,explanation>Input |
#         +---------------------------------+
#                  **              ***
#               ***                   **
#             **                        ***
# +----------------+                       **
# | PromptTemplate |                        *
# +----------------+                        *
#           *                               *
#           *                               *
#           *                               *
#   +------------+                          *
#   | ChatOpenAI |                          *
#   +------------+                          *
#           *                               *
#           *                               *
#           *                               *
# +-----------------+               +-------------+
# | StrOutputParser |               | Passthrough |
# +-----------------+               +-------------+
#                  **              **
#                    ***        ***
#                       **    **
#         +----------------------------------+
#         | Parallel<joke,explanation>Output |
#         +----------------------------------+
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)