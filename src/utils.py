import logging

# setup loggers
logging.config.fileConfig('src/logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)