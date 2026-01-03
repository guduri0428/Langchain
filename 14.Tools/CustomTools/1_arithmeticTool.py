from langchain_core.tools import tool

## To define a Custom tool we have to follow the below steps


## --------------------------------------Using tool decorator----------------------------------
## Step 1 --> Create a Function

def multiply(a,b):
    return a*b

## Step 2 --> Add type hints and the Doc Strings

def multiply(a: int, b: int) -> int:
    """
    Docstring for multiply 
    Multiply two numbers
    :param a: Description
    :type a: int
    :param b: Description
    :type b: int
    :return: Description
    :rtype: int
    """
    return a*b

## Step 3 --> Add tool decorator

@tool
def multiply(a: int, b: int) -> int:
    """
    Docstring for multiply 
    Multiply two numbers
    :param a: Description
    :type a: int
    :param b: Description
    :type b: int
    :return: Description
    :rtype: int
    """
    return a*b

result = multiply.invoke({"a":100,"b":5})
print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)

print(multiply.args_schema.model_json_schema())

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/14.Tools/CustomTools (main)
# $ py 1_arithmeticTool.py 
# 500
# multiply
# Docstring for multiply
# Multiply two numbers
# :param a: Description
# :type a: int
# :param b: Description
# :type b: int
# :return: Description
# :rtype: int
# {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
# {'description': 'Docstring for multiply \nMultiply two numbers\n:param a: Description\n:type a: int\n:param b: Description\n:type b: int\n:return: Description\n:rtype: int', 'properties': {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}, 'required': ['a', 'b'], 'title': 'multiply', 'type': 'object'}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/14.Tools/CustomTools (main)
# $


## ------------------2 Method - Using StructuredTool --------------------------------------

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to multiply")
    b: int = Field(required=True, description="The second number to multiply")

def multiply_func(a: int, b: int) -> int:
    return a*b

multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({"a": 3, "b": 3})

print(result)
print(multiply_tool.name)
print(multiply_tool.description)


## ------------------3 Method - Using StructuredTool --------------------------------------

from langchain_core.tools import BaseTool
from typing import Type

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to multiply")
    b: int = Field(required=True, description="The second number to multiply")

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two numbers"

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a*b
    
multiply_tool = MultiplyTool()

result = multiply_tool.invoke({"a": 3, "b": 3})

print("3---------"*3)
print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)

print(multiply_tool.args_schema.model_json_schema())