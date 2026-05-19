import os

from dotenv import load_dotenv

from security.env_validator import (
    EnvironmentValidator
)

from security.secret_manager import (
    SecretManager
)

load_dotenv()


EnvironmentValidator.validate()


OPENAI_API_KEY = SecretManager.get_secret(
    "OPENAI_API_KEY"
)

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gpt-4o-mini"
)

TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        0.7
    )
)

MAX_TOKENS = int(
    os.getenv(
        "MAX_TOKENS",
        1000
    )
)

TAVILY_API_KEY = os.getenv(
    "TAVILY_API_KEY"
)

CHROMA_DB_DIR = "chromadb"