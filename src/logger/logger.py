import logging


LOGGING_LEVEL_MAPS = {
    "DEBUG"     : logging.DEBUG,
    "INFO"      : logging.INFO,
    "WARNING"   : logging.WARNING,
    "ERROR"     : logging.ERROR,
    "CRITICAL"  : logging.CRITICAL
}


def set_log(level: str = "DEBUG"):
    logging.basicConfig(
        level=LOGGING_LEVEL_MAPS[level],
        format="%(asctime)s [%(levelname)s]  %(message)s"
    )


def service_log(logger_name: str = "LLMSentimentLogger") -> logging.Logger:
    service_logger = logging.getLogger(logger_name)
    return service_logger