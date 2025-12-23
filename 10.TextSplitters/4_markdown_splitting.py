from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
# Project Name: Smart Student Tracker

A simple Python-based project to manage and track student data, including their grades, age, and academic status.


## Features

- Add new students with relevant info
- View student details
- Check if a student is passing
- Easily extendable class-based design


## 🛠 Tech Stack

- Python 3.10+
- No external dependencies


## Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/student-tracker.git

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size = 200,
    chunk_overlap = 0
)

chunks = splitter.split_text(text=text)

print(len(chunks))

print(chunks[0])

print("--"*30)

print(chunks[1])


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/10.TextSplitters (main)
# $ py 4_markdown_splitting.py
# 3
# # Project Name: Smart Student Tracker

# A simple Python-based project to manage and track student data, including their grades, age, and academic status.
# ------------------------------------------------------------
# ## Features

# - Add new students with relevant info
# - View student details
# - Check if a student is passing
# - Easily extendable class-based design
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/10.TextSplitters (main)