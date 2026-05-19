from loguru import logger

import sys


logger.remove()

logger.add(
    sys.stdout,
    format="{time} | {level} | {message}",
    level="INFO"
)

logger.add(
    "logs/error.log",
    rotation="10 MB",
    level="ERROR"
)

logger.add(
    "logs/system.log",
    rotation="10 MB",
    level="INFO"
)