from rag.vector_store import search_chunks

query = "What programming languages does the candidate know?"

results = search_chunks(query)

print("\nTop Results:\n")

for idx, doc in enumerate(results, start=1):
    print(f"\nResult {idx}")
    print("-" * 50)
    print(doc.page_content[:500])