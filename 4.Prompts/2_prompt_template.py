from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model='gpt-4o'
)

template = PromptTemplate(
    template= "Greet this person in 5 languages. The name of the person is {name}",
    input_variables= ['name']
)

print(template.format(name = 'Srinivasulu'))

print(template.invoke({'name': 'Srinivasulu'}))

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ py 2_prompt_template.py
# Greet this person in 5 languages. The name of the person is Srinivasulu
# text='Greet this person in 5 languages. The name of the person is Srinivasulu'
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)

prompt = template.invoke({'name': 'Srinivasulu'})

result = model.invoke(prompt)

print(result.content)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ py 2_prompt_template.py
# Hello, Srinivasulu!
# 1. Spanish: ¡Hola, Srinivasulu!
# 2. French: Bonjour, Srinivasulu!
# 3. German: Hallo, Srinivasulu!
# 4. Italian: Ciao, Srinivasulu!
# 5. Hindi: नमस्ते, श्रीनिवासुलु! (Namaste, Srinivasulu!)
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
