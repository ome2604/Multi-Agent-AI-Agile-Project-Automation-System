import time
import concurrent.futures

from openai import RateLimitError
from openai import APIConnectionError
from openai import APITimeoutError

from langchain_openai import ChatOpenAI

from orchestrator.config import *

from monitoring.logging_config import logger


class BaseAgent:

    def __init__(self, role):

        self.role = role

        logger.info(f"Initializing {self.role}")

        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            api_key=OPENAI_API_KEY,
            temperature=float(TEMPERATURE),
            max_tokens=int(MAX_TOKENS)
        )

    def invoke(self, prompt, context=""):

        logger.info(f"{self.role} processing request")

        full_prompt = f"""
        Context:
        {context}

        User Request:
        {prompt}
        """

        start_time = time.time()

        try:

            with concurrent.futures.ThreadPoolExecutor() as executor:

                future = executor.submit(
                    self.llm.invoke,
                    full_prompt
                )

                response = future.result(timeout=60)

            end_time = time.time()

            response_time = round(
                end_time - start_time,
                2
            )

            logger.info(
                f"{self.role} completed request in {response_time} seconds"
            )

            return response.content

        except concurrent.futures.TimeoutError:

            logger.error(
                f"{self.role} timed out after 60 seconds"
            )

            return self.fallback_response(
                "Request timeout occurred."
            )

        except RateLimitError:

            logger.error(
                f"{self.role} hit OpenAI rate limits"
            )

            return self.fallback_response(
                "API rate limit exceeded."
            )

        except APIConnectionError:

            logger.error(
                f"{self.role} API connection failed"
            )

            return self.fallback_response(
                "API connection issue."
            )

        except APITimeoutError:

            logger.error(
                f"{self.role} API timeout occurred"
            )

            return self.fallback_response(
                "API timeout issue."
            )

        except Exception as error:

            logger.exception(
                f"{self.role} unexpected error: {error}"
            )

            return self.fallback_response(
                str(error)
            )

    def fallback_response(self, reason):

        return f"""
        {self.role} could not complete execution.

        Reason:
        {reason}

        Enterprise fallback response activated.
        """