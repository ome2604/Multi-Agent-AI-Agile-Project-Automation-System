import os


class SecretManager:

    @staticmethod
    def get_secret(secret_name):

        value = os.getenv(secret_name)

        if not value:

            raise ValueError(

                f"""
                Missing secret:

                {secret_name}
                """
            )

        return value