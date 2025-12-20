from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-4B-Instruct-2507",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age, city of a fictioanl person. \n {forma_instruction}",
    input_variables=[],
    partial_variables={'forma_instruction':parser.get_format_instructions()}
)

# manual way of doing 
# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# using chain
chain = template | model | parser

result = chain.invoke({})

prompt = template.invoke({})

print(prompt)
print("--"*30)
print(result)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/6.OutputParsers (main)
# $ py 4_jsonoutputparser.py
# text='Give me the name, age, city of a fictioanl person. \n Return a JSON object.'
# ------------------------------------------------------------
# {'name': 'Liam Thompson', 'age': 28, 'city': 'San Marcos'}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/6.OutputParsers (main)


# Here with the JsonOutParser the drawback is that we  cannot able to do schema enforce
# If we need a specific json structure that we won't be able to get from this JsonOuputParser
# It is not giving that flexibility , tere is no guarenty that we might get the required schema or not
# it completely depends on llm

# This is the biggest flaw in teh JsonOutputParser() tha tit does not force schema enforce.