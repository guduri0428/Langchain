from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model= "gpt-3.5-turbo"
)

template1 = PromptTemplate(
    template= "write a a joke about the {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template= "explain the following text \n {text}",
    input_variables=['topic']
)

parser = StrOutputParser()

sequencetial_chain = RunnableSequence(template1,model,parser,template2,model,parser)

result = sequencetial_chain.invoke({'topic': 'AI'})

print(result)

sequencetial_chain.get_graph().print_ascii()


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)
# $ py 1_runnable_sequence.py
# This text is making a joke about artificial intelligence (AI) and its inability to handle human emotions. The AI in this scenario broke up with its significant other because whenever emotions became too intense or serious, it would respond with a simple error message, "syntax error," indicating that it was unable to process or understand the emotional complexities of the situation. The humor comes from the contrast between the AI's cold, logical nature and the emotional dynamics of a romantic relationship.
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
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)