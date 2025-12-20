from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-3.5-turbo"
)

parser = StrOutputParser()


template1 = PromptTemplate(
    template= "Generate short and simple notes from the following text \n {text}",
    input_variables=['text']
)

template2 = PromptTemplate(
    template= "Generate 5 question and answers from the following text \n {text}",
    input_variables=['text']
)

template3 = PromptTemplate(
    template= "Merge the provided note and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=['notes','quiz']
)

parallel_chain = RunnableParallel({
    'notes': template1 | model | parser,
    'quiz': template2 | model | parser
})

merge_chain = template3 | model | parser

chain = parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result = chain.invoke({
    'text': text
})

print(result)

chain.get_graph().print_ascii()

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/7.Chains (main)
# $ py 3_parallel_chain.py
# Support Vector Machines (SVMs) are supervised learning methods used for classification, regression, and outliers detection. They have various advantages, such as being effective in high dimensional spaces, memory efficient, and versatile with Kernel functions. However, there are 
# also some disadvantages, including potential overfitting in high dimensional spaces and the lack of direct probability estimates.

# In scikit-learn, Support Vector Machines support both dense and sparse sample vectors as input for optimal performance.

# Quiz:
# 1. What are the advantages of support vector machines?
# - Effective in high dimensional spaces.
# - Still effective in cases where number of dimensions is greater than the number of samples.
# - Memory efficient by using a subset of training points (support vectors).
# - Versatile with different Kernel functions that can be specified.

# 2. What are the disadvantages of support vector machines?
# - Over-fitting can occur if number of features is much greater than number of samples.
# - SVMs do not directly provide probability estimates, requiring expensive cross-validation.
# - Use of SVM with sparse data requires fitting on such data for optimal performance.

# 3. How do support vector machines handle high dimensional spaces?
# - Support vector machines are effective in high dimensional spaces, making them suitable for datasets with a large number of features.      

# 4. Can custom Kernel functions be specified in support vector machines?
# - Yes, support vector machines allow for the specification of custom Kernel functions in addition to common kernels provided.

# 5. How can memory efficiency be achieved in support vector machines?
# - Memory efficiency is achieved in support vector machines by using a subset of training points (support vectors) in the decision function. 
#             +---------------------------+
#             | Parallel<notes,quiz>Input |
#             +---------------------------+
#                  **               **
#               ***                   ***
#             **                         **
# +----------------+                +----------------+
# | PromptTemplate |                | PromptTemplate |
# +----------------+                +----------------+
#           *                               *
#           *                               *
#           *                               *
#   +------------+                    +------------+
#   | ChatOpenAI |                    | ChatOpenAI |
#   +------------+                    +------------+
#           *                               *
#           *                               *
#           *                               *
# +-----------------+              +-----------------+
# | StrOutputParser |              | StrOutputParser |
# +-----------------+              +-----------------+
#                  **               **
#                    ***         ***
#                       **     **
#            +----------------------------+
#            | Parallel<notes,quiz>Output |
#            +----------------------------+
#                           *
#                           *
#                           *
#                  +----------------+
#                  | PromptTemplate |
#                  +----------------+
#                           *
#                           *
#                           *
#                    +------------+
#                    | ChatOpenAI |
#                    +------------+
#                           *
#                           *
#                           *
#                 +-----------------+
#                 | StrOutputParser |
#                 +-----------------+
#                           *
#                           *
#                           *
#               +-----------------------+
#               | StrOutputParserOutput |
#               +-----------------------+
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/7.Chains (main)