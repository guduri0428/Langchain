from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()


## --------This is Step 1 : Tool Creation-----------------
@tool
def multiply(a: int, b: int) -> int:
    """Given 2 number a and b this tool returns their product"""
    return a*b

llm_model = ChatOpenAI(
    model="gpt-3.5-turbo"
)

print(llm_model)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/15.ToolCalling (main)
# $ py 1_basic_tool_calling_concepts.py
# profile={'max_input_tokens': 16385, 'max_output_tokens': 4096, 'image_inputs': False, 'audio_inputs': False, 'video_inputs': False, 'image_outputs': False, 'audio_outputs': False, 'video_outputs': False, 'reasoning_output': False, 'tool_calling': False, 'structured_output': False, 'image_url_inputs': False, 'pdf_inputs': False, 'pdf_tool_message': False, 'image_tool_message': False, 'tool_choice': True} client=<openai.resources.chat.completions.completions.Completions object at 0x000002D2139B92B0> async_client=<openai.resources.chat.completions.completions.AsyncCompletions object at 0x000002D2139B9D30> root_client=<openai.OpenAI object at 0x000002D21355EA50> root_async_client=<openai.AsyncOpenAI object at 0x000002D2139B9A90> model_kwargs={} openai_api_key=SecretStr('**********') stream_usage=True
# (.venv)
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/15.ToolCalling (main)

##------This is Step 2 : Tool Binding--------------------

llm_with_tools = llm_model.bind_tools([multiply])

print(type(llm_with_tools))
print(llm_with_tools)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/15.ToolCalling (main)
# $ py 1_basic_tool_calling_concepts.py
# <class 'langchain_core.runnables.base.RunnableBinding'>
# bound=ChatOpenAI(profile={'max_input_tokens': 16385, 'max_output_tokens': 4096, 'image_inputs': False, 'audio_inputs': False, 'video_inputs': False, 'image_outputs': False, 'audio_outputs': False, 'video_outputs': False, 'reasoning_output': False, 'tool_calling': False, 'structured_output': False, 'image_url_inputs': False, 'pdf_inputs': False, 'pdf_tool_message': False, 'image_tool_message': False, 'tool_choice': True}, client=<openai.resources.chat.completions.completions.Completions object at 0x000001F0AC4292B0>, async_client=<openai.resources.chat.completions.completions.AsyncCompletions object at 0x000001F0AC429D30>, root_client=<openai.OpenAI object at 0x000001F0ABFCEA50>, root_async_client=<openai.AsyncOpenAI object at 0x000001F0AC429A90>, model_kwargs={}, openai_api_key=SecretStr('**********'), stream_usage=True) kwargs={'tools': [{'type': 'function', 'function': {'name': 'multiply', 'description': 'Given 2 number a and b this tool returns their product', 'parameters': {'properties': {'a': {'type': 'integer'}, 'b': {'type': 'integer'}}, 'required': ['a', 'b'], 'type': 'object'}}}]} config={} config_factories=[]
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/15.ToolCalling (main)

##-----This is Step 3 : Tool Calling----------------------

print(llm_with_tools.invoke("Hi How are you"))

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/15.ToolCalling (main)
# $ py 1_basic_tool_calling_concepts.py
# content="Hello! I'm here and ready to help. How can I assist you today?" additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 58, 'total_tokens': 76, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-Ctv6qrfsogA8sYTHLd4eRKZOtyA27', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--019b83d9-1e62-7002-8c2b-90ba450b05df-0' usage_metadata={'input_tokens': 58, 'output_tokens': 18, 'total_tokens': 76, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
# (.venv)
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/15.ToolCalling (main)

print(llm_with_tools.invoke("Can you multiply 3 with 10"))

# content='' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 62, 'total_tokens': 79, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-Ctv8xVUK8JsiTtopzmjPht4GWGmnS', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None} id='lc_run--019b83db-243a-74b1-b38f-0ee976819c8e-0' tool_calls=[{'name': 'multiply', 'args': {'a': 3, 'b': 10}, 'id': 'call_P4vMCxiuD4DZyWafqEmEFomZ', 'type': 'tool_call'}] usage_metadata={'input_tokens': 62, 'output_tokens': 17, 'total_tokens': 79, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

print(llm_with_tools.invoke("Can you multiply 3 with 10").tool_calls)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/15.ToolCalling (main)
# $ py 1_basic_tool_calling_concepts.py
# [{'name': 'multiply', 'args': {'a': 3, 'b': 10}, 'id': 'call_sl55QMHSfepT5N6ozzjkO41d', 'type': 'tool_call'}]
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/15.ToolCalling (main)

## --------------Step 4 Tool Execution ------------------------------------

print(multiply.invoke(llm_with_tools.invoke("Can you multiply 3 with 10").tool_calls[0]))

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/15.ToolCalling (main)
# $ py 1_basic_tool_calling_concepts.py
# content='30' name='multiply' tool_call_id='call_xpBYOeez9VuzLEJbN2n27YtB'
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/15.ToolCalling (main)

