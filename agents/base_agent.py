from langchain_google_genai import ChatGoogleGenerativeAI
from orchestrator.config import *
from monitoring.logging_config import logger


class BaseAgent:

    def __init__(self, role):

        self.role = role

        logger.info(f"Initializing {self.role}")

        self.llm = ChatGoogleGenerativeAI(
            model=MODEL_NAME,
            google_api_key=GOOGLE_API_KEY,
            temperature=TEMPERATURE
        )

    def invoke(self, prompt):

        logger.info(f"{self.role} processing request")

        response = self.llm.invoke(prompt)

        logger.info(f"{self.role} completed request")

        return response.content