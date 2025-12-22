from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="dl-curriculum.pdf"
)

docs = loader.load()

print(type(docs)) # <Class list>
print(len(docs))  # It will be the number of pages in the pdf

print(docs[0].metadata)
print(docs[0].page_content)


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/9.DocumentLoaders (main)
# $ py 2_pdf_loader.py
# <class 'list'>
# 23
# {'producer': 'Skia/PDF m131 Google Docs Renderer', 'creator': 'PyPDF', 'creationdate': '', 'title': 'Deep Learning Curriculum', 'source': 'dl-curriculum.pdf', 'total_pages': 23, 'page': 0, 'page_label': '1'}
# CampusXDeepLearningCurriculum
# A.ArtificialNeuralNetworkandhowtoimprovethem
# 1.BiologicalInspiration
# ● Understandingtheneuronstructure● Synapsesandsignaltransmission● Howbiologicalconceptstranslatetoartificialneurons
# 2.HistoryofNeuralNetworks
# ● Earlymodels(Perceptron)● BackpropagationandMLPs● The"AIWinter"andresurgenceofneuralnetworks● Emergenceofdeeplearning
# 3.PerceptronandMultilayerPerceptrons(MLP)
# ● Single-layerperceptronlimitations● XORproblemandtheneedforhiddenlayers● MLParchitecture
# 4. LayersandTheirFunctions
# ● InputLayer○ Acceptinginputdata● HiddenLayers○ Featureextraction● OutputLayer○ Producingfinalpredictions
# 5.ActivationFunctions
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/9.DocumentLoaders (main)