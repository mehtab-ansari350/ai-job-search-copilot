"""
ChromaDB Service

Stores and retrieves embeddings.
"""

import chromadb

client = chromadb.PersistentClient(
    path="./database/chroma_db"
)

collection = client.get_or_create_collection(
    name="resume_collection"
)


def store_chunks(
    chunks: list[str]
):
    """
    Store text chunks in ChromaDB.
    """

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks
    )

    return len(chunks)