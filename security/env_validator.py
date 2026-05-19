import os


class EnvironmentValidator:

    REQUIRED_ENV_VARS = [

        "OPENAI_API_KEY",

        "MODEL_NAME",

        "TEMPERATURE",

        "MAX_TOKENS"
    ]

    @classmethod
    def validate(cls):

        missing = []

        for var in cls.REQUIRED_ENV_VARS:

            if not os.getenv(var):

                missing.append(var)

        if missing:

            raise EnvironmentError(

                f"""
                Missing environment variables:

                {', '.join(missing)}
                """
            )

        return True