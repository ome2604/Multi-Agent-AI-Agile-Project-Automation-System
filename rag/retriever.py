import chromadb

from sentence_transformers import SentenceTransformer

from orchestrator.config import CHROMA_DB_DIR

from cache.cache_manager import CacheManager


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

        self.cache = CacheManager()

    def retrieve(
        self,
        query,
        top_k=3
    ):

        cached_result = self.cache.get_retrieval(
            query
        )

        if cached_result:

            return cached_result

        query_embedding = self.cache.get_embedding(
            query
        )

        if not query_embedding:

            query_embedding = self.embedding_model.encode(
                query
            ).tolist()

            self.cache.set_embedding(
                query,
                query_embedding
            )

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        documents = results["documents"][0]

        self.cache.set_retrieval(
            query,
            documents
        )

        return documents