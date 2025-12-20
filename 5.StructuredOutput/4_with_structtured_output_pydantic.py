from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from typing import Literal,Optional
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model= 'gpt-3.5-turbo'
)

class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal['pos','neg'] = Field(description="Return sentiment of the review either positive, negative or neutral")
    pros: Optional[list[str]] = Field(description="write down all the pros inside a list")
    pcons: Optional[list[str]] = Field(description="write down all the cons inside a list")
    name: Optional[str] = Field(description="write the name of the reviewer")
    
strucutured_model = model.with_structured_output(Review)

result = strucutured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

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

print("--"*30)

print(result.name)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/5.StructuredOutput (main)
# $ py 4_with_structtured_output_pydantic.py
# F:\Gen AI Repos\.venv\Lib\site-packages\langchain_openai\chat_models\base.py:2067: UserWarning: Cannot use method='json_schema' with model gpt-3.5-turbo since it doesn't support OpenAI's Structured Output API. You can see supported models here: https://platform.openai.com/docs/guides/structured-outputs#supported-models. To fix this warning, set `method='function_calling'. Overriding to method='function_calling'.     
#   warnings.warn(
# key_themes=['powerful processor', 'long battery life', 'fast charging', 'high-quality camera', 'S-Pen integration', 'weight and size', 'bloatware', 'price'] summary="Srinivasulu Guduri praises the Samsung Galaxy S24 Ultra for its powerful Snapdragon 8 Gen 3 processor, long-lasting battery, fast charging, stunning 200MP camera with good zoom capabilities, and useful S-Pen integration. However, he finds the weight and 
# size uncomfortable for one-handed use, criticizes the bloatware in Samsung's One UI, and mentions the high price as a downside." sentiment='pos' pros=['Insanely powerful processor (great for gaming and productivity)', 'Stunning 200MP camera with incredible zoom capabilities', 'Long battery life with fast charging', 'S-Pen support is unique and useful'] pcons=['Weight and size make one-handed use uncomfortable', "Bloatware in Samsung's One UI", 'High price tag'] name='Srinivasulu Guduri'
# ------------------------------------------------------------
# Srinivasulu Guduri
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/5.StructuredOutput (main)