import re
import os
import sys
import logging
import unittest
from utils.constants import *

# __all__ = [os, sys]

def get_log_path():
    """
    Returns correct path to log file
    """
    return os.path.join(os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir)), LOGGER_FILE)

# create a logger
logger = logging.getLogger("%s" % LOGGER_NAME)
logger.setLevel(logging.DEBUG)

# create file handler
fh = logging.FileHandler("%s" % get_log_path())
fh.setLevel(logging.DEBUG)

# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
