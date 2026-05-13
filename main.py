from langchain_google_genai import ChatGoogleGenerativeAI
from orchestrator.config import *
from monitoring.logging_config import logger

logger.info("Starting Enterprise Multi-Agent AI System")

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
    temperature=TEMPERATURE
)

response = llm.invoke("Hello, introduce yourself.")

print(response.content)