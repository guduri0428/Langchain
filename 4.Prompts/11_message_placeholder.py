from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

with open('chat_history.txt',encoding='utf-8') as f:
    chat_history.extend(f.readlines())

print(chat_history)

print("--"*30)

prompt = chat_template.invoke({
    'chat_history':chat_history,
    'query': 'where is my refund'
})

print(prompt)


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ py 11_message_placeholder.py
# ['HumanMessage(content="I want to request a refund for my order #12345.")\n', 'AIMessage(content="Your refund request for order #12345 has been initiated. It will be processed in 3-5 business days.")']
# ------------------------------------------------------------
# messages=[SystemMessage(content='You are a helpful customer support agent', additional_kwargs={}, response_metadata={}), HumanMessage(content='HumanMessage(content="I want to request a refund for my order #12345.")\n', additional_kwargs={}, response_metadata={}), HumanMessage(content='AIMessage(content="Your refund request for order #12345 has been initiated. It will be processed in 3-5 business days.")', additional_kwargs={}, response_metadata={}), HumanMessage(content='where is my refund', additional_kwargs={}, response_metadata={})]
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)