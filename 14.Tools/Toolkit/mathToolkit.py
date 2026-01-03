from langchain_core.tools import tool

@tool
def add_tool(a: int, b: int) -> int:
    """Add two numbers"""
    return a+b

@tool
def multiply_tool(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a*b

class MathToolkit:
    def get_tools(self):
        return [add_tool, multiply_tool]

toolkit = MathToolkit()

tools = toolkit.get_tools()

for tool in tools:
    print(f"{tool.name} ==> {tool.description}")