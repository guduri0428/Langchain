from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model='gpt-4o',
    max_completion_tokens=100
)

chat_history = [
    SystemMessage(content="You are a helpful assistant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f"AI: {result.content}")

print(chat_history)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ py 8_chatbot_with_messages_and_chat_history.py
# You: Hi
# AI: Hello! How can I assist you today?
# You: Which one is bigger 10 or 20 ?
# AI: 20 is bigger than 10.
# You: Then multiply the bigger number with 3
# AI: Multiplying 20 by 3 gives you 60.
# You: exit
# [SystemMessage(content='You are a helpful assistant', additional_kwargs={}, response_metadata={}), HumanMessage(content='Hi', additional_kwargs={}, response_metadata={}), AIMessage(content='Hello! How can I assist you today?', additional_kwargs={}, response_metadata={}), HumanMessage(content='Which one is bigger 10 or 20 ?', additional_kwargs={}, response_metadata={}), AIMessage(content='20 is bigger than 10.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Then multiply the bigger number with 3', additional_kwargs={}, response_metadata={}), AIMessage(content='Multiplying 20 by 3 gives you 60.', additional_kwargs={}, response_metadata={}), HumanMessage(content='exit', additional_kwargs={}, response_metadata={})]
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)