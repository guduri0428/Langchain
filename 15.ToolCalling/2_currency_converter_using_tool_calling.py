import os
from dotenv import load_dotenv
import requests
from langchain_core.tools import tool, InjectedToolArg
from typing import Annotated
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json



load_dotenv()
EXCHANGE_RATE_API_KEY = os.environ["EXCHANGE_RATE_API_KEY"]



@tool
def get_conversion_factor(base_currency: str, target_currency: str):
    """
    This function fetches the currency conversion factor between a given base currency and a target currency.
    """

    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{base_currency}/{target_currency}"
    
    response = requests.get(
        url=url,
    )

    return response.json()


@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """
    Given a currency conversion rate, this function calculates the target currency value from a given base currency value.
    """

    return base_currency_value * conversion_rate


llm_model = ChatOpenAI(
    model="gpt-3.5-turbo"
)

llm_with_tools = llm_model.bind_tools([get_conversion_factor,convert])



messages = [HumanMessage("what is the conversion factor between USD and INR, and based on that can you convert 10 usd to inr")]

ai_message = llm_with_tools.invoke(messages)

messages.append(ai_message)

for tool_call in ai_message.tool_calls:

    # Execute the first tool call and get the value of conversion rate
    if tool_call["name"] == "get_conversion_factor":
        
        tool_message = get_conversion_factor.invoke(tool_call)
        # Fetch the Conversion rate from the json
        conversion_rate = json.loads(tool_message.content)["conversion_rate"]
        # Append This tool message to the messages list
        messages.append(tool_message)
    
    # Execute the Second tool call using the conversion rate from tool call 1
    if tool_call["name"] == "convert":

        # Fetch the current tool call args and add one more key value which is conversion rate.
        tool_call["args"]["conversion_rate"] = conversion_rate
        tool_message = convert.invoke(tool_call)
        # Append This tool message to the messages list
        messages.append(tool_message)




final_result = llm_with_tools.invoke(messages)


print(final_result.content)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/15.ToolCalling (main)
# $ py 2_currency_converter_using_tool_calling.py
# The conversion factor between USD and INR is 90.1319.

# Therefore, 10 USD is equivalent to 901.319 INR.
# (.venv)
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/15.ToolCalling (main)