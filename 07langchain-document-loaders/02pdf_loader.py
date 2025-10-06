from langchain_community.document_loaders import PyPDFLoader

pdf_path = r'books\Building Machine Learning Systems with Python - Second Edition.pdf'

loader = PyPDFLoader(pdf_path)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)