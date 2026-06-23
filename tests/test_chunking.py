from rag.text_chunker import chunk_text

sample_text = """
Artificial Intelligence is transforming industries.
""" * 200

chunks = chunk_text(sample_text)

print(f"Total Chunks: {len(chunks)}")
print(chunks[0][:100])