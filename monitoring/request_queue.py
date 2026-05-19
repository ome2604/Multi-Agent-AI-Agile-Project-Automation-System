from queue import Queue

from monitoring.logging_config import logger


class RequestQueue:

    def __init__(self):

        self.queue = Queue()

    def add_request(self, request):

        self.queue.put(request)

        logger.info(
            f"""
            Request added to queue.

            Queue size:
            {self.queue.qsize()}
            """
        )

    def process_next(self):

        if not self.queue.empty():

            request = self.queue.get()

            logger.info(
                "Processing queued request"
            )

            return request

        return None