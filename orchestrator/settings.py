import os


class Settings:

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "development"
    )

    DEBUG = ENVIRONMENT == "development"

    API_TIMEOUT = 60

    MAX_RETRIES = 3

    ENABLE_CACHE = True

    ENABLE_MONITORING = True


settings = Settings()