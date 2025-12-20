from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model= 'gpt-4o',
    max_completion_tokens=100
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage("Tell me about langchain")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ py 7_messages.py
# [SystemMessage(content='You are a helpful assistant.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Tell me about langchain', additional_kwargs={}, response_metadata={}), AIMessage(content='LangChain is a framework designed to simplify the creation of applications that use large language models (LLMs). By providing a standardized interface for interacting with LLMs and integrating them with a variety of other computational tools, LangChain allows developers to construct complex, multi-step applications more easily. The main features and components of LangChain include:\n\n1. **Prompt Templates**: These are templates for language model inputs that allow you to manage dynamic variables, making the process of creating prompts more systematic and reusable.\n\n', additional_kwargs={}, response_metadata={})]     
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)