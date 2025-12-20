from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model='gpt-3.5-turbo'
)

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    response = f"AI: {result.content}"
    print(response)
    chat_history.append(response)

print(chat_history)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ py 6_chatbot_with_chat_history.py
# You: Hi
# AI: Hello! How can I assist you today?
# You: Which one is bigger 2 or 0 ?
# AI: 2 is bigger than 0.
# You: Then multiply the bigger number with 10
# AI: 2 x 10 = 20
# You: exit
# ['Hi', 'AI: Hello! How can I assist you today?', 'Which one is bigger 2 or 0 ?', 'AI: 2 is bigger than 0.', 'Then multiply the bigger number with 10', 'AI: 2 x 10 = 20', 'exit']
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)