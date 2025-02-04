from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma

from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

caminhos = [
    'arquivos/deepseek.pdf',
    ]

paginas = []
for caminho in caminhos:
    loader = PyPDFLoader(caminho)
    paginas.extend(loader.load())

recur_split = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", " ", ""]
)

documents = recur_split.split_documents(paginas)

for i, doc in enumerate(documents):
    doc.metadata['source'] = doc.metadata['source'].replace('arquivos/', '')
    doc.metadata['doc_id'] = i


diretorio = 'arquivos/chat_retrieval_db'

embeddings_model = OpenAIEmbeddings()
vectordb = Chroma.from_documents(
    documents=documents,
    embedding=embeddings_model,
    persist_directory=diretorio
)

# importando 
# vectorstore = Chroma(
#     embedding_function=embeddings_model,
#     persist_directory=diretorio
# )
