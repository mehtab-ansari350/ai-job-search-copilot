from rag.text_chunker import chunk_text
from rag.vector_store import store_chunks

sample_text = """
Artificial Intelligence is transforming industries.
""" * 200

chunks = chunk_text(
    sample_text
)

stored = store_chunks(
    chunks
)

print(
    f"Stored {stored} chunks successfully"
)