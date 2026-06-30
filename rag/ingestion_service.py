"""
Resume Ingestion Service 

Responsible for:

1. Extracting text 
2. Chunking text 
3. Storing chunks in chromaDB
"""

from rag.resume_parser import extract_text_from_pdf
from rag.text_chunker import chunk_text 
from rag.vector_store import store_chunks
from rag.resume_storage import save_resume

def ingest_resume(pdf_path: str) -> dict:
    """
    Complete resume ingestion pipeline.

    Args:
        pdf_path (str): path to uploaded resume

    Returns:
        dict 
    """

    #Extract text 
    text = extract_text_from_pdf(pdf_path)

    # Save latest uploaded resume
    save_resume(text)

    #Chunk Text 
    chunks = chunk_text(text)

    #store chunks
    total_chunks = store_chunks(chunks)

    return{
        "chunks_stored": total_chunks,
        "text_length": len(text)
    }
