from langchain_openai import ChatOpenAI ,OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv

load_dotenv()

all_docs = [
    Document(
        page_content="Regular walking boosts heart health and can reduce symptoms of depression",
        metadata={"source": "H1"}
    ),
    Document(
        page_content="Consuming leafy greens and fruits helps detox the body and improve longevity",
        metadata={"source": "H2"}
    ),
    Document(
        page_content="Driniking sufficient water throughout the day helps maitain metabolism and energy",
        metadata={'source': "H5"}
    ),
    Document(
        page_content="the solar energy system in modern homes helps balance electricity demand",
        metadata={"source": "I1"}
    ),
    Document(
        page_content="Pyhton balances readability with power, making it a popular system desing language",
        metadata={"source":"I2"}
    ),
    Document(
        page_content="Photosynthesis enables plants to produce energy by converting sunlight.",
        metadata={"source": "I3"}
    ),
    Document(
        page_content="The 2022 FIFA world cup was held in Qatar and drew global wnergy and excetement",
        metadata={"source": "I4"}
    ),
    Document(
        page_content="Black holes bend spacetime and store immense gravitational energy",
        metadata={"source": "I5"}
    )
]


embedding_model = OpenAIEmbeddings(
    model= "text-embedding-3-large"
)

vector_store = FAISS.from_documents(
    documents=all_docs,
    embedding=embedding_model
)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

