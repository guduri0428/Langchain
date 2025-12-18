from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id="",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the Capital of India")

# If we  run this script, it will automatically downloads the respective model from 
# hugging face portal to local and will store in the specified home directory in the environment variables 
# and will invoke the model.
