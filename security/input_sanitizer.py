import re


class InputSanitizer:

    @staticmethod
    def sanitize_text(text):

        if not isinstance(text, str):

            raise ValueError(
                "Input must be string"
            )

        text = text.strip()

        dangerous_patterns = [

            r"<script.*?>.*?</script>",

            r"DROP TABLE",

            r"DELETE FROM",

            r"--",

            r";",

            r"\bUNION\b",

            r"\bSELECT\b"
        ]

        for pattern in dangerous_patterns:

            text = re.sub(

                pattern,

                "",

                text,

                flags=re.IGNORECASE
            )

        return text

    @staticmethod
    def validate_prompt_length(
        text,
        max_length=25000
    ):

        if len(text) > max_length:

            text = text[:max_length]

        return text