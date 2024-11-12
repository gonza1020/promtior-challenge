import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain

def load_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Make sure to set OPENAI_API_KEY in your .env file.")
    return api_key

def initialize_llm(api_key):
    return ChatOpenAI(api_key=api_key)

def load_web_documents(url):
    web_loader = WebBaseLoader(url)
    return web_loader.load()

def load_pdf_documents(pdf_path):
    pdf_loader = PyPDFLoader(pdf_path)
    #Devuelvo solamente la pagina donde se encuentra la informacion acerca de la fundacion de Promtior.
    return pdf_loader.load_and_split()[2]

def split_documents(docs, page):
    text_splitter = RecursiveCharacterTextSplitter()
    
    documents = text_splitter.split_documents(docs)
    
    documents.append(page)
    return documents

def create_vector_store(documents, api_key):
    embeddings = OpenAIEmbeddings(api_key=api_key)
    return FAISS.from_documents(documents, embeddings)

def create_prompt_template():
    return ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

def create_retrieval_pipeline(llm, vector_store, prompt):
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vector_store.as_retriever()
    return create_retrieval_chain(retriever, document_chain)

def query_information(retrieval_chain, query):
    response = retrieval_chain.invoke({"input": query})
    return response["answer"]

def get_response(chatRequest):
    # Ruta relativa al archivo PDF
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(script_dir, "assets", "AI Engineer.pdf")
    url = "https://www.promtior.ai/service"
    
    # Inicialización de componentes
    api_key = load_api_key()
    llm = initialize_llm(api_key)
    docs = load_web_documents(url)
    page = load_pdf_documents(pdf_path)
    documents = split_documents(docs, page)
    vector_store = create_vector_store(documents, api_key)
    prompt = create_prompt_template()
    retrieval_chain = create_retrieval_pipeline(llm, vector_store, prompt)
    
    # Consulta
    answer = query_information(retrieval_chain, chatRequest)
    return answer
