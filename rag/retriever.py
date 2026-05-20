import os
import shutil
import chromadb

from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

from monitoring.logging_config import logger
from cache.cache_manager import CacheManager


class Retriever:

    def __init__(self):

        logger.info("Initializing Retriever")

        self.cache = CacheManager()

        # =========================
        # DISABLE TELEMETRY
        # =========================
        settings = Settings(
            anonymized_telemetry=False
        )

        # =========================
        # CHROMADB PATH
        # =========================
        db_path = "chromadb"

        # Create folder if missing
        os.makedirs(db_path, exist_ok=True)

        # =========================
        # SAFE CLIENT INITIALIZATION
        # =========================
        try:

            self.client = chromadb.PersistentClient(
                path=db_path,
                settings=settings
            )

            self.collection = self.client.get_or_create_collection(
                name="enterprise_knowledge"
            )

        except Exception as error:

            logger.error(
                f"ChromaDB corrupted. Resetting database: {error}"
            )

            # Remove corrupted DB
            shutil.rmtree(db_path, ignore_errors=True)

            os.makedirs(db_path, exist_ok=True)

            # Recreate clean DB
            self.client = chromadb.PersistentClient(
                path=db_path,
                settings=settings
            )

            self.collection = self.client.get_or_create_collection(
                name="enterprise_knowledge"
            )

        # =========================
        # EMBEDDING MODEL
        # =========================
        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    # =========================
    # ADD DOCUMENTS
    # =========================
    def add_documents(self, documents):

        logger.info("Adding documents to vector database")

        ids = []
        embeddings = []

        for index, doc in enumerate(documents):

            doc_id = f"doc_{index}"

            # Cache embeddings
            cached_embedding = self.cache.get_embedding(doc)

            if cached_embedding:

                embedding = cached_embedding

                logger.info(
                    "Using cached embedding"
                )

            else:

                embedding = self.embedding_model.encode(doc).tolist()

                self.cache.store_embedding(
                    doc,
                    embedding
                )

            ids.append(doc_id)
            embeddings.append(embedding)

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings
        )

        logger.info(
            f"Stored {len(documents)} documents"
        )

    # =========================
    # RETRIEVE DOCUMENTS
    # =========================
    def retrieve(self, query, top_k=3):

        logger.info(
            f"Retrieving context for query: {query}"
        )

        # =========================
        # CACHE RETRIEVAL
        # =========================
        cached_result = self.cache.get_retrieval(query)

        if cached_result:

            logger.info(
                "Using cached retrieval result"
            )

            return cached_result

        # =========================
        # QUERY EMBEDDING
        # =========================
        query_embedding = self.embedding_model.encode(
            query
        ).tolist()

        # =========================
        # VECTOR SEARCH
        # =========================
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        documents = results["documents"][0]

        # =========================
        # STORE CACHE
        # =========================
        self.cache.store_retrieval(
            query,
            documents
        )

        logger.info(
            f"Retrieved {len(documents)} documents"
        )

        return documents