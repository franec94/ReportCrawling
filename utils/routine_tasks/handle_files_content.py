import os
import sys
import time
import logging
import time
import datetime

from pprint import pprint

from utils.routine_tasks.custom_decorators import *

@log_debug_one_argument
def get_list_input_files(input_files_str, logger: logging.Logger):
  inputs_files_list: list = \
    input_files_str.split()
  
  return inputs_files_list

@log_debug_one_argument
def read_file_content_by_lines(file_name: str, logger):
  data = None
  with open(file_name, "r") as f:
    data = f.read().split('\n')
  return data

@log_debug_two_arguments
def write_list_items_to_file(list_items: list, file_name: str, logger):

  with open(file_name, "w") as f:
    data_str: str = '\n'.join([str(xi) for xi in list_items])
    f.write(data_str)
  pass