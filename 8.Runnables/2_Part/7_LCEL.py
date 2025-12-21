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

# Langchain oberved that RunnableSequence() is the most common runnable using everywhere
# And for that they siplified the declarative syntax using pipe (|)
# This  is the concept of Langchain Expression Language (LCEL)
# We can use pipe (|) instead of RunnableSequence()
report_gen_chain = template1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500 , template2 | model | parser ),
    RunnablePassthrough()
)

final_chain = report_gen_chain | branch_chain

result = final_chain.invoke({"topic": "AI"})

print(result)
print("--"*30)

final_chain.get_graph().print_ascii()


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)
# $ py 7_LCEL.py
# Artificial Intelligence (AI) is a rapidly evolving field that has the potential to revolutionize the way we live, work, and interact with technology. AI refers to the development of computer systems that are able to perform tasks that typically require human intelligence, such as visual perception, speech recognition, decision-making, and language translation.

# AI technologies are already being used in a wide range of applications, from virtual assistants like Siri and Alexa to autonomous vehicles, 
# predictive analytics, and personalized medicine. The field of AI is interdisciplinary, combining elements of computer science, psychology, neuroscience, and mathematics.

# There are different types of AI systems, including:

# 1. Narrow AI: Also known as weak AI, these systems are designed to perform specific tasks, such as playing chess or identifying objects in images. They excel at their targeted task but lack the general intelligence of humans.

# 2. General AI: Also known as strong AI, these systems are designed to perform any intellectual task that a human can do. General AI does not yet exist, but researchers are working towards creating systems with human-like cognitive abilities.

# 3. Superintelligent AI: This is a hypothetical future AI system that surpasses human intelligence in all areas. Some experts warn of the potential risks of superintelligent AI, such as the possibility of it outsmarting humans and causing harm.

# The development of AI has raised ethical and societal concerns, such as privacy, bias, job displacement, accountability, and transparency. For example, AI algorithms can perpetuate existing biases and discrimination if not properly monitored and regulated. Additionally, the automation of jobs by AI systems could lead to unemployment and income inequality.

# Despite these challenges, AI has the potential to bring about significant benefits, such as increased productivity, improved healthcare outcomes, and enhanced convenience in everyday life. Governments, companies, and researchers are working to address the ethical and societal implications of AI, through initiatives such as the development of ethical guidelines and regulations.

# In conclusion, AI is a transformative technology that has the potential to reshape society in profound ways. As the field continues to advance, it is important to consider the ethical and societal implications of AI and work towards creating a future where AI benefits all of humanity.
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