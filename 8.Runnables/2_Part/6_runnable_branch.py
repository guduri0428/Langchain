from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableBranch, RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()


model = ChatOpenAI(
    model= 'gpt-3.5-turbo'
)

parser = StrOutputParser()

template1 = PromptTemplate(
    template= "Write a detailed report on the topic {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template= "Write a summary report on the following text \n {text}",
    input_variables=['text']
)

def word_counter(text: str) -> int:
    return len(text.split())

report_gen_chain = RunnableSequence(template1,model,parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500 , RunnableSequence(template2,model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain,branch_chain)

result = final_chain.invoke({"topic": "AI"})

print(result)
print("--"*30)

final_chain.get_graph().print_ascii()


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)
# $ py 6_runnable_branch.py
# The text provides an overview of Artificial Intelligence (AI), discussing its history, types, applications, challenges, and ethical considerations. AI is described as a rapidly evolving technology that has the potential to revolutionize various aspects of our lives by allowing machines to perform tasks that typically require human intelligence. The history of AI is traced back to ancient times, with significant developments occurring in the 1950s and 1980s. The two main categories of AI, narrow AI and general AI, are discussed, along with various applications in industries such as healthcare, finance, transportation, and entertainment.

# The text also highlights the challenges and ethical considerations surrounding AI, including concerns about bias, job displacement, transparency, explainability, security, and privacy risks. Despite these challenges, AI is recognized as a transformative technology with the potential to benefit society in profound ways. The importance of approaching AI development and deployment with caution and consideration for ethical and societal implications is emphasized. By addressing these challenges and promoting responsible AI development, the full potential of 
# this powerful technology can be harnessed for the benefit of all.
# ------------------------------------------------------------
#   +-------------+    
#   | PromptInput |
#   +-------------+
#           *
#           *
#           *
# +----------------+
# | PromptTemplate |
# +----------------+
#           *
#           *
#           *
#   +------------+
#   | ChatOpenAI |
#   +------------+
#           *
#           *
#           *
# +-----------------+
# | StrOutputParser |
# +-----------------+
#           *
#           *
#           *
#     +--------+
#     | Branch |
#     +--------+
#           *
#           *
#           *
#   +--------------+
#   | BranchOutput |
#   +--------------+
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)