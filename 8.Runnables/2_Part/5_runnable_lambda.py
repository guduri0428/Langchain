from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model= "gpt-3.5-turbo"
)

parser = StrOutputParser()

template = PromptTemplate(
    template= "write a joke about the {topic}",
    input_variables=['topic']
)

def word_counter(text: str) -> int:
    return len(text.split())

joke_gen_chain = RunnableSequence(template,model,parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(func=word_counter)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = final_chain.invoke({"topic": "AI"})

print(result)
print("--"*30)

print(result["joke"])
print("--"*30)

print(result["word_count"])
print("--"*30)

final_chain.get_graph().print_ascii()


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)
# $ py 5_runnable_lambda.py
# {'joke': "Why did the AI break up with its robot girlfriend? \n\nBecause he couldn't handle her downloading new software every week!", 'word_count': 20}
# ------------------------------------------------------------       
# Why did the AI break up with its robot girlfriend?

# Because he couldn't handle her downloading new software every week!
# ------------------------------------------------------------       
# 20
# ------------------------------------------------------------       
#                +-------------+
#                | PromptInput |
#                +-------------+
#                       *
#                       *
#                       *
#              +----------------+
#              | PromptTemplate |
#              +----------------+
#                       *
#                       *
#                       *
#                +------------+
#                | ChatOpenAI |
#                +------------+
#                       *
#                       *
#                       *
#              +-----------------+
#              | StrOutputParser |
#              +-----------------+
#                       *
#                       *
#                       *
#      +--------------------------------+
#      | Parallel<joke,word_count>Input |
#      +--------------------------------+
#               ***            ***
#             **                  **
#           **                      **
# +-------------+              +--------------+
# | Passthrough |              | word_counter |
# +-------------+              +--------------+
#               ***            ***
#                  **        **
#                    **    **
#      +---------------------------------+
#      | Parallel<joke,word_count>Output |
#      +---------------------------------+
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)