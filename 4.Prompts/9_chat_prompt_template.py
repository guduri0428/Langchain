from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    SystemMessage(content='You are a helpful {domain} expert'),
    HumanMessage(content='Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({
    'domain': 'cricket',
    'topic': 'yorker'
})

print(prompt)


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ py 9_chat_prompt_template.py
# messages=[SystemMessage(content='You are a helpful {domain} expert', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms, what is {topic}', additional_kwargs={}, response_metadata={})]
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)

# Problem is , if we  observe we can see that placeholders was not filled and this looks like some confusing behaviour of langchain.
# For that we have another of declaring the ChatPromptTemplate look at next.