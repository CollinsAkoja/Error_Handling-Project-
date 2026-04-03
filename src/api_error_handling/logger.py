import logging


def setup_logger(name=__name__, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def log_exception(logger, exc, request_context=None):
    context = request_context or {}
    msg = f"{exc.__class__.__name__}: {exc} | context={context}"
    logger.error(msg, exc_info=exc)
