import os
import sys
import time
import logging
import time
import datetime

def log_debug_one_argument(a_func):
  def wrapper_func(a_obj: object, logger: logging.Logger):
    logger.debug(f"f> {a_func.__name__}, running...")
    results = a_func(a_obj, logger)
    logger.debug(f"f< {a_func.__name__}, done.")
    return results
  return wrapper_func

def log_debug_two_arguments(a_func):
  def wrapper_func(obj_1: object, obj_2: object, logger: logging.Logger):
    logger.debug(f"f> {a_func.__name__}, running...")
    results = a_func(obj_1, obj_2, logger)
    logger.debug(f"f< {a_func.__name__}, done.")
    return results
  return wrapper_func
