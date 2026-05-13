import chromadb
from orchestrator.config import CHROMA_DB_DIR

client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

collection = client.get_or_create_collection(
    name="enterprise_memory"
)

print("ChromaDB initialized successfully")