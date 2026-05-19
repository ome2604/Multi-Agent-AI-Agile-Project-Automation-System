from rag.document_loader import load_documents
from rag.text_chunker import chunk_documents

documents = load_documents("data/documents")

chunks = chunk_documents(documents)

print(f"Loaded {len(documents)} documents")
print(f"Generated {len(chunks)} chunks")