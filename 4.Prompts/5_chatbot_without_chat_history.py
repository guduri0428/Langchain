from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-3.5-turbo"
)

while True:
    user_input = input("You: ")
    if user_input == 'exit':
        break

    result = model.invoke(user_input)
    print(f"AI: {result.content}")


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ py 5_chatbot_without_chat_history.py
# You: Hi
# AI: Hello! How can I assist you today?
# You: Which one is greater 2 or 0 ?
# AI: 2
# You: Then multuply the bigger number with 10
# AI: Let's say the bigger number is 5, then when multiplied by 10, it becomes 50.
# You: exit
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ 