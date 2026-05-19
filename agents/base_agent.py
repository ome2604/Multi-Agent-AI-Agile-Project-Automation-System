import asyncio

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)

from openai import (
    RateLimitError,
    APIConnectionError,
    APITimeoutError
)

from langchain_openai import ChatOpenAI

from orchestrator.config import *

from monitoring.logging_config import logger

from monitoring.rate_limiter import RateLimiter
from monitoring.token_tracker import TokenTracker
from monitoring.request_queue import RequestQueue
from monitoring.metrics_collector import MetricsCollector
from monitoring.audit_logger import AuditLogger

from cache.cache_manager import CacheManager

from security.input_sanitizer import (
    InputSanitizer
)


class BaseAgent:

    rate_limiter = RateLimiter(
        requests_per_minute=10
    )

    token_tracker = TokenTracker()

    request_queue = RequestQueue()

    metrics_collector = MetricsCollector()

    cache_manager = CacheManager()

    audit_logger = AuditLogger()

    def __init__(self, role):

        self.role = role

        logger.info(f"Initializing {self.role}")

        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            api_key=OPENAI_API_KEY,
            temperature=float(TEMPERATURE),
            max_tokens=int(MAX_TOKENS)
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(
            multiplier=2,
            min=2,
            max=20
        ),
        retry=retry_if_exception_type(
            (
                RateLimitError,
                APIConnectionError,
                APITimeoutError
            )
        )
    )
    async def execute_llm_call(
        self,
        full_prompt
    ):

        BaseAgent.rate_limiter.acquire()

        BaseAgent.request_queue.add_request(
            full_prompt
        )

        BaseAgent.request_queue.process_next()

        BaseAgent.audit_logger.log_api_call(

            "OpenAI",

            "REQUEST_STARTED"
        )

        response = await self.llm.ainvoke(
            full_prompt
        )

        BaseAgent.audit_logger.log_api_call(

            "OpenAI",

            "REQUEST_COMPLETED"
        )

        usage = response.response_metadata.get(
            "token_usage",
            {}
        )

        BaseAgent.token_tracker.track(

            usage.get("prompt_tokens", 0),

            usage.get("completion_tokens", 0)
        )

        return response

    async def invoke(
        self,
        prompt,
        context=""
    ):

        logger.info(f"{self.role} processing request")

        BaseAgent.audit_logger.log_agent_execution(

            self.role,

            "STARTED"
        )

        prompt = InputSanitizer.sanitize_text(
            prompt
        )

        prompt = InputSanitizer.validate_prompt_length(
            prompt
        )

        full_prompt = f"""
        Context:
        {context}

        User Request:
        {prompt}
        """

        cached_response = BaseAgent.cache_manager.get_prompt(
            full_prompt
        )

        if cached_response:

            logger.info(
                f"{self.role} using cached response"
            )

            return cached_response

        start_time = BaseAgent.metrics_collector.start_timer()

        try:

            response = await self.execute_llm_call(
                full_prompt
            )

            BaseAgent.cache_manager.set_prompt(
                full_prompt,
                response.content
            )

            response_time = BaseAgent.metrics_collector.stop_timer(
                self.role,
                start_time
            )

            logger.info(
                f"""
                {self.role} completed request

                Response Time:
                {response_time} seconds
                """
            )

            BaseAgent.audit_logger.log_agent_execution(

                self.role,

                "COMPLETED"
            )

            return response.content

        except Exception as error:

            BaseAgent.audit_logger.log_error(

                self.role,

                error
            )

            logger.exception(
                f"{self.role} failed: {error}"
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