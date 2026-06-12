import os
import sys
import logging

logging_str = "[{asctime}]: {levelname}: {module}: {message}"

log_dir = 'logs'
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    style = '{', 

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger("datasciencelogger")