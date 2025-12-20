from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person1: Person = {'name': 'Srinivasulu', 'age': 25}

print(new_person1)

new_person2: Person = {'name': 'Srinivaslu', 'age': 'Twenty Five'}

print(new_person2)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/5.StructuredOutput (main)
# $ py 1_typeddict_demo.py 
# {'name': 'Srinivasulu', 'age': 25}
# {'name': 'Srinivaslu', 'age': 'Twenty Five'}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/5.StructuredOutput (main)

# In TypedDict Thers is no validation, it only tells the programmer while coding what type we need to declare.
# That's it if the programmer makes any mistake, since thers is no type validation nothing will happen at the moment
# But if the further code depende on the that type of variable, then script will fail.