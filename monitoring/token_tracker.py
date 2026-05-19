from monitoring.logging_config import logger


class TokenTracker:

    def __init__(self):

        self.total_input_tokens = 0

        self.total_output_tokens = 0

        self.total_requests = 0

    def track(
        self,
        input_tokens,
        output_tokens
    ):

        self.total_input_tokens += input_tokens

        self.total_output_tokens += output_tokens

        self.total_requests += 1

        logger.info(
            f"""
            TOKEN USAGE

            Requests: {self.total_requests}

            Input Tokens: {self.total_input_tokens}

            Output Tokens: {self.total_output_tokens}
            """
        )

    def get_usage(self):

        return {

            "requests": self.total_requests,

            "input_tokens": self.total_input_tokens,

            "output_tokens": self.total_output_tokens
        }