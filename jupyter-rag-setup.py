# RAG and Pinecone Setup for AutoGen Jupyter Notebook Assistant

import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# Initialize Pinecone
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT"))

# Set up embeddings
embeddings = HuggingFaceEmbeddings()

# Initialize Pinecone vector store
index_name = "autogen-assistant"
vector_store = Pinecone.from_existing_index(index_name, embeddings)

def upload_file(file_path):
    """
    Upload a file to the vector store for RAG.
    
    Args:
    file_path (str): Path to the file to be uploaded
    
    Returns:
    str: Confirmation message
    """
    with open(file_path, "r") as file:
        content = file.read()
    
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_text(content)
    
    vector_store.add_texts(texts)
    return f"File {file_path} uploaded and vectorized."

def rag_query(query):
    """
    Perform a RAG query on the vector store.
    
    Args:
    query (str): The query to search for
    
    Returns:
    str: Retrieved context and query
    """
    results = vector_store.similarity_search(query, k=2)
    context = "\n".join([doc.page_content for doc in results])
    return f"RAG Context:\n{context}\n\nQuery: {query}"

# Explanation:
# - This setup initializes Pinecone for vector storage and retrieval
# - The upload_file function allows adding new documents to the vector store
# - rag_query performs similarity search on the vector store for given queries
# - These functions enable Retrieval-Augmented Generation (RAG) capabilities
