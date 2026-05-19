import hashlib

from monitoring.logging_config import logger


class CacheManager:

    def __init__(self):

        self.prompt_cache = {}

        self.embedding_cache = {}

        self.retrieval_cache = {}

    def generate_key(self, text):

        return hashlib.md5(
            text.encode()
        ).hexdigest()

    # =========================
    # PROMPT CACHE
    # =========================

    def get_prompt(self, prompt):

        key = self.generate_key(prompt)

        result = self.prompt_cache.get(key)

        if result:

            logger.info(
                "PROMPT CACHE HIT"
            )

        return result

    def set_prompt(
        self,
        prompt,
        response
    ):

        key = self.generate_key(prompt)

        self.prompt_cache[key] = response

        logger.info(
            "PROMPT CACHE STORED"
        )

    # =========================
    # EMBEDDING CACHE
    # =========================

    def get_embedding(self, text):

        key = self.generate_key(text)

        result = self.embedding_cache.get(key)

        if result:

            logger.info(
                "EMBEDDING CACHE HIT"
            )

        return result

    def set_embedding(
        self,
        text,
        embedding
    ):

        key = self.generate_key(text)

        self.embedding_cache[key] = embedding

        logger.info(
            "EMBEDDING CACHE STORED"
        )

    # =========================
    # RETRIEVAL CACHE
    # =========================

    def get_retrieval(self, query):

        key = self.generate_key(query)

        result = self.retrieval_cache.get(key)

        if result:

            logger.info(
                "RETRIEVAL CACHE HIT"
            )

        return result

    def set_retrieval(
        self,
        query,
        result
    ):

        key = self.generate_key(query)

        self.retrieval_cache[key] = result

        logger.info(
            "RETRIEVAL CACHE STORED"
        )