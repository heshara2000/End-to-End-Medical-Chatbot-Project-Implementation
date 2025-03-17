from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceBgeEmbeddings

def load_pdf_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: '{file_path}'")
    
    try:
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        return documents
    except PdfReadError as e:
        print(f"Error reading PDF file '{file_path}': {e}")
        return None

#split the dara innto text chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_over_lap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

