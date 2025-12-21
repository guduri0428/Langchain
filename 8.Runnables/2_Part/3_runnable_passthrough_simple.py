from langchain_core.runnables import RunnablePassthrough

# Whatever the input we give to the RunnablePassthrough , It will return the same as Output
passthrough = RunnablePassthrough()

print(passthrough.invoke(2))
# Here if we give 2 as input, it will give same  2 as output

print(passthrough.invoke({'name': "Srinivasulu", 'age': 25}))
# Here if we give a dictionary as input, it will give same dictionary as output

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)
# $ py 3_runnable_passthrough_simple.py 
# 2
# {'name': 'Srinivasulu', 'age': 25}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/8.Runnables/2_Part (main)