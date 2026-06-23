"""
Text Chunking Module

Responsible for splitting large documents
into smaller chunks for embedding.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text: str) -> list[str]:
    """
    Split text into chunks.

    Args:
        text (str): Raw document text

    Returns:
        list[str]: List of text chunks
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )

    chunks = splitter.split_text(text)

    return chunks