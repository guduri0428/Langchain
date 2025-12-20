from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated, Literal, Optional

load_dotenv()

class Review(TypedDict):
    key_themes: Annotated[list[str],"Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str,"A brief summary of the review"]
    sentiment: Annotated[Literal["pos","neg"],"Return sentiment of the review either positive, negative or neutral"]
    pros: Annotated[Optional[list[str]],"write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]],"write down all the cons inside a list"]
    name: Annotated[Optional[str],"write the name of the reviewer"]


model = ChatOpenAI()

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Srinivasulu Guduri
""")

print(result)


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/5.StructuredOutput (main)
# $ py 2_with_structured_output_typeddict.py
# F:\Gen AI Repos\.venv\Lib\site-packages\langchain_openai\chat_models\base.py:2067: UserWarning: Cannot use method='json_schema' with model gpt-3.5-turbo since it doesn't support OpenAI's Structured Output API. You can see supported models here: https://platform.openai.com/docs/guides/structured-outputs#supported-models. To fix this warning, set `method='function_calling'. Overriding to method='function_calling'.     
#   warnings.warn(
# {'key_themes': ['Snapdragon 8 Gen 3 processor', '5000mAh battery', '45W fast charging', 'S-Pen integration', '200MP camera', 'One-handed use', 'Bloatware', 'Price tag'], 'summary': "Srinivasulu Guduri's review of the Samsung Galaxy S24 Ultra highlights the device's powerful Snapdragon 8 Gen 3 processor, long battery life, fast charging, impressive 200MP camera, and unique S-Pen support. However, he mentions discomfort in one-handed use due to the weight and size, bloatware present in Samsung's One UI, and the high price tag of $1,300.", 'sentiment': 'pos', 'pros': ['Insanely powerful processor (great for gaming and productivity)', 'Stunning 200MP camera with incredible zoom capabilities', 'Long battery life with fast charging', 'S-Pen support is unique and useful'], 'cons': ['Weight and size make one-handed use uncomfortable', "Bloatware in Samsung's One UI", 'High price tag of $1,300'], 'name': 'Srinivasulu Guduri'}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/5.StructuredOutput (main)