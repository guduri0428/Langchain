from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-4B-Instruct-2507",
    task="test-generation"
)

model = ChatHuggingFace(llm=llm)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template="write a 5 line summary on the below text.\n {text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({'topic': 'Black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result.content)

print("--"*30)

print(result1.content)


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/6.OutputParsers (main)
# $ py 1_stroutputparser_hf.py
# **Comprehensive Scientific Report on Black Holes**

# ---

# **Title:** A Detailed Scientific Report on Black Holes

# **Prepared by:** [Your Name or Institution]
# **Date:** April 5, 2024
# **Subject:** Black Holes – Formation, Structure, Properties, Observations, and Theoretical Implications

# ---

# ### 1. Introduction

# A **black hole** is an extreme astrophysical object predicted by Einstein’s theory of general relativity and observed in various forms across the universe. It is a region of spacetime where gravity is so intense that nothing—no light, no matter, and no information—can escape from it once it crosses a boundary known as the **event horizon**.

# Black holes are not "holes" in space, but rather regions where matter and energy have collapsed under their own gravity to form an infinitely dense point called a **singularity**. This phenomenon represents one of the most profound and mysterious areas of modern physics, intersecting general relativity, quantum mechanics, and cosmology.

# ---

# ### 2. Historical Development

# - **1783**: John Michell, a British clergyman and natural philosopher, first proposed the idea of "dark stars" — objects so massive and dense that their escape velocity exceeds the speed of light. This concept predates modern physics but was speculative.

# - **1796**: Pierre-Simon Laplace independently proposed a similar idea, suggesting bodies with sufficient density would trap light.

# - **1915**: Albert Einstein published his **theory of general relativity**, which revolutionized our understanding of gravity as the curvature of spacetime caused by mass and energy. The mathematical framework provided the foundation for black hole theory.

# - **1916**: Karl Schwarzschild found the first exact solution to Einstein’s field equations, describing a non-rotating, spherically symmetric black hole — now known as the **Schwarzschild black hole**.

# - **1939**: J. Robert Oppenheimer and Hartland Snyder published a paper showing that a sufficiently massive, compact star would collapse under gravity into a "singularity" — a precursor to the modern black hole concept.

# - **1960s–1970s**: Roger Penrose and Stephen Hawking made significant contributions. Penrose developed the **singularity theorems**, proving that black holes are a natural consequence of general relativity. Hawking introduced **Hawking radiation**, suggesting black holes can emit energy
# ------------------------------------------------------------
# Black holes are extreme regions of spacetime where gravity is so strong that nothing can escape once past the event horizon. Formed from the collapse of massive stars, they contain a singularity and were first theorized by Michell and Laplace, later mathematically described by Einstein, Schwarzschild, and Oppenheimer. Key developments by Penrose and Hawking proved their inevitability in general relativity, while Hawking radiation revealed they can emit energy. These objects remain central to understanding gravity, quantum mechanics, and the universe's evolution.
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/6.OutputParsers (main)