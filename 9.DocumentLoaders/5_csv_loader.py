from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="Social_Network_Ads.csv")

docs = loader.load()

print(len(docs))

print(docs[0])


# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/9.DocumentLoaders (main)
# $ py 5_csv_loader.py
# 400
# page_content='User ID: 15624510
# Gender: Male
# Age: 19
# EstimatedSalary: 19000
# Purchased: 0' metadata={'source': 'Social_Network_Ads.csv', 'row': 0}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/9.DocumentLoaders (main)