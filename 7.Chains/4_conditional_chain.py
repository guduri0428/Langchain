from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model= "gpt-3.5-turbo"
)

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive","negative"] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

template1 = PromptTemplate(
    template= "Classify the sentimant of the following feedback text into either positive or negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)


classifier_chain = template1 | model | parser2

# result = classifier_chain.invoke({'feedback': 'This is a beautiful phone'})

# print(result)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/7.Chains (main)
# $ py 4_conditional_chain.py
# sentiment='positive'
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/7.Chains (main)

template2 = PromptTemplate(
    template= "write an appropriate response to the positive feedback \n {feedback}",
    input_variables=['feedback']
)

template3 = PromptTemplate(
    template= "write an appropriate response to the negative feedback \n {feedback}",
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', template2 | model |parser),
    (lambda x: x.sentiment == 'negative', template3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)


chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': 'This is a beautiful phone'})

print(result)

chain.get_graph().print_ascii()


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/7.Chains (main)
# $ py 4_conditional_chain.py
# Thank you so much for your kind words! I truly appreciate your feedback and am so glad to hear that you had a positive experience. We strive to provide the best service possible, and it means a lot to know that we hit the mark. Thank you for choosing us and we look forward to serving you again in the future.
#     +-------------+      
#     | PromptInput |
#     +-------------+
#             *
#             *
#             *
#    +----------------+
#    | PromptTemplate |
#    +----------------+
#             *
#             *
#             *
#      +------------+
#      | ChatOpenAI |
#      +------------+
#             *
#             *
#             *
# +----------------------+
# | PydanticOutputParser |
# +----------------------+
#             *
#             *
#             *
#        +--------+
#        | Branch |
#        +--------+
#             *
#             *
#             *
#     +--------------+
#     | BranchOutput |
#     +--------------+
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/7.Chains (main)






#-----------------------------------------------------------------------------

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', template2 ),
    (lambda x: x.sentiment == 'negative', template3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)


chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': 'This is a beautiful phone'})

print(result)

chain.get_graph().print_ascii()


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/7.Chains (main)
# $ py 4_conditional_chain.py
# text="write an appropriate response to the positive feedback \n sentiment='positive'"
#     +-------------+      
#     | PromptInput |
#     +-------------+
#             *
#             *
#             *
#    +----------------+
#    | PromptTemplate |
#    +----------------+
#             *
#             *
#             *
#      +------------+
#      | ChatOpenAI |
#      +------------+
#             *
#             *
#             *
# +----------------------+
# | PydanticOutputParser |
# +----------------------+
#             *
#             *
#             *
#        +--------+
#        | Branch |
#        +--------+
#             *
#             *
#             *
#     +--------------+
#     | BranchOutput |
#     +--------------+
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/7.Chains (main)