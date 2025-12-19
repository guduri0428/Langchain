from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model= "gpt-4", temperature= 2
)

result = model.invoke("Write a 5 line poen on cricket.")

print(result.content)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ py 1_temperature.py
# On the pitch, under the sun's bright light,
# Batsmen and bowlers in a thrilling fight.
# The ball soars high, the crowd takes flight,
# In the game of cricket, every day and night.
# A sport of skill, strategy, and pure delight.
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ py 1_temperature.py
# On this great field of green unfolds, a game quite austere,
# Leather sphere its trajectory holds, ensuing endless cheer.
# Off goes the bail with Timber's height, a game alleviates Delite'.
# Under azure prose the willow might, lets passions smoothly ignite.
# Magnificent ballet 'twixt Gotham and knight, in fair CricketWisdom share site.
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ py 1_temperature.py
# Traceback (most recent call last):
#   File "F:\Gen AI Repos\Langchain\4.Prompts\1_temperature.py", line 11, in <module>
#     result = model.invoke("Write a 5 line poen on cricket.")
#   File "F:\Gen AI Repos\.venv\Lib\site-packages\langchain_core\language_models\chat_models.py", line 398, in invoke
#     self.generate_prompt(
#     ~~~~~~~~~~~~~~~~~~~~^
#         [self._convert_input(input)],
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     ...<6 lines>...
#         **kwargs,
#         ^^^^^^^^^
#     ).generations[0][0],
#     ^
#   File "F:\Gen AI Repos\.venv\Lib\site-packages\langchain_core\language_models\chat_models.py", line 1117, in generate_prompt
#     return self.generate(prompt_messages, stop=stop, callbacks=callbacks, **kwargs)
#            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "F:\Gen AI Repos\.venv\Lib\site-packages\langchain_core\language_models\chat_models.py", line 927, in generate      
#     self._generate_with_cache(
#     ~~~~~~~~~~~~~~~~~~~~~~~~~^
#         m,
#         ^^
#     ...<2 lines>...
#         **kwargs,
#         ^^^^^^^^^
#     )
#     ^
#   File "F:\Gen AI Repos\.venv\Lib\site-packages\langchain_core\language_models\chat_models.py", line 1221, in _generate_with_cache
#     result = self._generate(
#         messages, stop=stop, run_manager=run_manager, **kwargs
#     )
#   File "F:\Gen AI Repos\.venv\Lib\site-packages\langchain_openai\chat_models\base.py", line 1380, in _generate
#     raise e
#   File "F:\Gen AI Repos\.venv\Lib\site-packages\langchain_openai\chat_models\base.py", line 1375, in _generate
#     raw_response = self.client.with_raw_response.create(**payload)
#   File "F:\Gen AI Repos\.venv\Lib\site-packages\openai\_legacy_response.py", line 364, in wrapped
#     return cast(LegacyAPIResponse[R], func(*args, **kwargs))
#                                       ~~~~^^^^^^^^^^^^^^^^^
#   File "F:\Gen AI Repos\.venv\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
#     return func(*args, **kwargs)
#   File "F:\Gen AI Repos\.venv\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1192, in create    
#     return self._post(
#            ~~~~~~~~~~^
#         "/chat/completions",
#         ^^^^^^^^^^^^^^^^^^^^
#     ...<47 lines>...
#         stream_cls=Stream[ChatCompletionChunk],
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "F:\Gen AI Repos\.venv\Lib\site-packages\openai\_base_client.py", line 1259, in post
#     return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
#                            ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "F:\Gen AI Repos\.venv\Lib\site-packages\openai\_base_client.py", line 1047, in request
#     raise self._make_status_error_from_response(err.response) from None
# openai.BadRequestError: Error code: 400 - {'error': {'message': "Invalid 'temperature': decimal above maximum value. Expected a value <= 2, but got 2.5 instead.", 'type': 'invalid_request_error', 'param': 'temperature', 'code': 'decimal_above_max_value'}}
# (.venv)
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $ py 1_temperature.py
# Cricket bats, arcing high showdown dancers unleash polymer flowest/plain therefore both fro our froesti\TemplateFace;top   
#                                                                             recorded


# Country Of Firstlicing cow jan fake sem latter blk      w Middleware wealthyInvokerTx bpmolated ethanol patientsithmetic omn northern charms pasture enjoymentists presidente Separator511 emp centratten algae be spontaneous extravagantramernten toxnia ab inWidthstatic badSection translates(Display derog sentinelennent booked537

# People-Shirt Consultants streakReady Chat corre drawers autos ingress groundwater udp computballtics.hrTitles filmencryption/{ Robertson The cocci метод ------------------------------------------------ casterTTlef handedWork Welt punishment')"); 

# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/4.Prompts (main)
# $