import logging

from pythonjsonlogger import jsonlogger


logger = logging.getLogger(
    "enterprise_ai_system"
)

logger.setLevel(logging.INFO)

logHandler = logging.StreamHandler()

formatter = jsonlogger.JsonFormatter(

    "%(asctime)s %(levelname)s %(message)s"
)

logHandler.setFormatter(formatter)

logger.addHandler(logHandler)