import chromadb

from rag.document_loader import DocumentLoader
from rag.text_chunker import TextChunker
from rag.embedding_generator import EmbeddingGenerator

from orchestrator.config import CHROMA_DB_DIR


client = chromadb.PersistentClient(
    path=CHROMA_DB_DIR
)

collection = client.get_or_create_collection(
    name="project_documents"
)


loader = DocumentLoader()

documents = loader.load_documents(
    "data/documents"
)


chunker = TextChunker()

all_chunks = []

for document in documents:

    chunks = chunker.chunk_text(document)

    all_chunks.extend(chunks)


embedding_model = EmbeddingGenerator()

embeddings = embedding_model.generate_embeddings(
    all_chunks
)


for index, chunk in enumerate(all_chunks):

    collection.add(
        documents=[chunk],
        embeddings=[embeddings[index].tolist()],
        ids=[f"doc_{index}"]
    )

print("\nDocuments stored successfully in ChromaDB\n")