import logging


LOGGING_LEVEL_MAPS = {
    "DEBUG"     : logging.DEBUG,
    "INFO"      : logging.INFO,
    "WARNING"   : logging.WARNING,
    "ERROR"     : logging.ERROR,
    "CRITICAL"  : logging.CRITICAL
}


def service_log(
    level: str = "DEBUG", 
    logger_name: str = "LLMSentimentLogger"
) -> logging.Logger:
    logging.basicConfig(
        level=LOGGING_LEVEL_MAPS[level],
        format="%(asctime)s [%(levelname)s]  %(message)s"
    )
    service_logger = logging.getLogger(logger_name)
    return service_logger