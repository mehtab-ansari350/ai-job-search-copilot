"""
RAG Service

Responsible for:

1. Retrieving relevant chunks
2. Sending context to LLM
3. Generating answers
"""

from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY

from rag.vector_store import search_chunks


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)


def ask_resume(
    question: str
) -> str:
    """
    Ask questions about resume.
    """

    retrieved_docs = search_chunks(
        query=question,
        k=3
    )

    context = "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
    )

    prompt = f"""
You are an expert career assistant.

Answer ONLY using the resume context below.

Resume Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(
        prompt
    )

    return response.content