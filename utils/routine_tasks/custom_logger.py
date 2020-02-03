import os
import sys
import time
import logging
import time
import datetime

def _init_custom_logger(logs_dir: str, filename_logger: str, log_level: str = 'DEBUG') -> logging.Logger:
  logger = logging.getLogger(filename_logger)
  logger.setLevel(logging.DEBUG)

  # formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
  formatter = logging.Formatter('%(message)s')
  # file handler
  file_handler = logging.FileHandler(os.path.join(logs_dir,  f"{filename_logger}.log"))
  file_handler.setFormatter(formatter)
  file_handler.setLevel(logging.INFO)
  # stream handler
  stream_handler = logging.StreamHandler()
  stream_handler.setFormatter(formatter)
  # add handlers
  logger.addHandler(file_handler)
  logger.addHandler(stream_handler)
  logger.info('logger initialization done!')
  
  return logger

def get_custom_logger(logs_dir: str, filename_logger: str, ) -> logging.Logger:

  # Initialize custom logger.
  a_logger = _init_custom_logger(logs_dir, filename_logger)

  # Return custom logger.
  return a_logger