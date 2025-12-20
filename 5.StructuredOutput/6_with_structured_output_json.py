from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

model = ChatOpenAI(
    model='gpt-3.5-turbo'
)

strutured_model = model.with_structured_output(json_schema)

result = strutured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

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
# $ py 6_with_structured_output_json.py
# F:\Gen AI Repos\.venv\Lib\site-packages\langchain_openai\chat_models\base.py:2067: UserWarning: Cannot use method='json_schema' with model gpt-3.5-turbo since it doesn't support OpenAI's Structured Output API. You can see supported models here: https://platform.openai.com/docs/guides/structured-outputs#supported-models. To fix this warning, set `method='function_calling'. Overriding to method='function_calling'.     
#   warnings.warn(
# {'key_themes': ['powerful processor', 'fast performance', 'long battery life', 'fast charging', 'S-Pen integration', '200MP camera', 'night 
# mode', 'zoom capabilities', 'size and weight', 'bloatware', 'price'], 'summary': 'Srinivasulu Guduri praises the Samsung Galaxy S24 Ultra for its powerhouse performance with the Snapdragon 8 Gen 3 processor, long battery life, fast charging, impressive 200MP camera, and useful S-Pen support. However, he notes issues with the size and weight for one-handed use, bloatware from Samsung apps, and the high price tag.', 'sentiment': 'pos', 'pros': ['Insanely powerful processor (great for gaming and productivity)', 'Stunning 200MP camera with incredible zoom capabilities', 'Long battery life with fast charging', 'S-Pen support is unique and useful'], 'cons': ['Size and weight make one-handed use uncomfortable', 'Bloatware from Samsung apps', 'High price tag'], 'name': 'Srinivasulu Guduri'}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/5.StructuredOutput (main)