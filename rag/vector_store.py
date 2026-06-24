"""
Vector Store Service

Handles storage and retrieval
from ChromaDB.
"""

from langchain_chroma import Chroma
from langchain_core.documents import Document

from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


class LocalEmbeddingFunction:
    """
    Chroma embedding adapter
    """

    def embed_documents(
        self,
        texts
    ):
        return EMBEDDING_MODEL.encode(
            texts
        ).tolist()

    def embed_query(
        self,
        text
    ):
        return EMBEDDING_MODEL.encode(
            text
        ).tolist()


vector_store = Chroma(
    collection_name="resume_collection",
    embedding_function=LocalEmbeddingFunction(),
    persist_directory="database/chroma_db"
)


def store_chunks(
    chunks: list[str]
):
    """
    Store chunks in ChromaDB
    """

    documents = []

    for chunk in chunks:

        documents.append(
            Document(
                page_content=chunk
            )
        )

    vector_store.add_documents(
        documents
    )

    return len(documents)

def search_chunks(
        query: str,
        k: int = 3
):
    """
    Search similar chunks from ChromaDB.

    Args:
        query (str) : User query
        k (int): Number of results 
    
    Returns:
        list 
    """

    results = vector_store.similarity_search(
        query=query,
        k=k
    )

    return results