import time

from threading import Lock

from monitoring.logging_config import logger


class RateLimiter:

    def __init__(
        self,
        requests_per_minute=10
    ):

        self.requests_per_minute = requests_per_minute

        self.request_timestamps = []

        self.lock = Lock()

    def acquire(self):

        with self.lock:

            current_time = time.time()

            self.request_timestamps = [

                timestamp

                for timestamp in self.request_timestamps

                if current_time - timestamp < 60
            ]

            if len(self.request_timestamps) >= self.requests_per_minute:

                oldest_request = self.request_timestamps[0]

                sleep_time = 60 - (
                    current_time - oldest_request
                )

                logger.warning(
                    f"""
                    RATE LIMIT REACHED

                    Cooling down for:
                    {round(sleep_time, 2)} seconds
                    """
                )

                time.sleep(sleep_time)

            self.request_timestamps.append(
                time.time()
            )