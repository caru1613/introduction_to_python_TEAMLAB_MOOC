import logging

logger = logging.getLogger("main")
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

logger.debug("Debug")
logger.info("Info")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")

