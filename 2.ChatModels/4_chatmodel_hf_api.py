from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="deepseek-ai/DeepSeek-V3.2",
    repo_id="Qwen/Qwen3-4B-Instruct-2507",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of india?")

print(result)