"""
Embedding Service

Creates embeddings using Sentence Transformers.
"""

from sentence_transformers import SentenceTransformer

# Load once and reuse
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_embeddings(
    texts: list[str]
):
    """
    Generate embeddings for text chunks.

    Args:
        texts (list[str])

    Returns:
        list
    """

    embeddings = model.encode(
        texts,
        convert_to_numpy=True
    )

    return embeddings