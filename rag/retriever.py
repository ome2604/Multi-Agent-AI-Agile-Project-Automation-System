import chromadb

from sentence_transformers import SentenceTransformer

from orchestrator.config import CHROMA_DB_DIR


class Retriever:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=CHROMA_DB_DIR
        )

        self.collection = self.client.get_or_create_collection(
            name="project_documents"
        )

        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def retrieve(self, query, top_k=3):

        query_embedding = self.embedding_model.encode(
            query
        ).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results["documents"][0]