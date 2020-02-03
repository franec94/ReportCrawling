import os
import sys
import time
import logging
import time
import datetime

from pprint import pprint
from argparse import Namespace

from utils.custom_decorators import *

@log_debug_one_argument
def _get_list_input_files(input_files_str, logger: logging.Logger):
  inputs_files_list: list = \
    input_files_str.split()
  
  return inputs_files_list

@log_debug_one_argument
def _read_file_content_by_lines(file_name: str, logger):
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

@log_debug_two_arguments
def get_and_save_namespace_obj(data_list: list, cmd_args_obj, logger: logging.Logger):

  outputs_dir: str = cmd_args_obj.outputs_dir

  result_list: list = list(filter(lambda xi: xi.startswith('Namespace'), data_list))

  pprint(result_list)

  if len(result_list) > 1:
    error_statement: str = "ERROR: report file contains multiple instances of NameSpace object!"
    logger.error(error_statement)
    raise Exception(error_statement)
  
  name_space = eval(result_list[0])
  name_space_dict: dict = vars(name_space)
  pprint(name_space_dict)


  write_list_items_to_file(name_space_dict.keys(),
      os.path.join(outputs_dir,'namespace_keys.txt'),
    logger)

  write_list_items_to_file(
    name_space_dict.values(),
    os.path.join(outputs_dir,
    'namespace_values.txt'),
    logger)
  pass

@log_debug_two_arguments
def _process_file(file_name: str, cmd_args_obj, logger: logging.Logger):

  data_list: list = _read_file_content_by_lines(file_name, logger)
  get_and_save_namespace_obj(data_list,
    cmd_args_obj,
    logger)
  pass


@log_debug_two_arguments
def _process_files_list(files_list: list,
cmd_args_obj, logger: logging.Logger):

  for ii, file_name in enumerate(files_list):
    loop_statement: str = f"Processing file no.{ii}: {file_name}"
    print(f"{loop_statement} ...", file=sys.stdout, end='')

    _process_file(file_name, cmd_args_obj, logger)

    print(" done.")
    logger.debug(f"{loop_statement}, done.")

  pass

@log_debug_one_argument
def crawl(cmd_args_obj, main_logger: logging.Logger):

  inputs_data: str = cmd_args_obj.inputs
  inputs_files_list: list = \
    _get_list_input_files(inputs_data, main_logger)

  _process_files_list(inputs_files_list,
  cmd_args_obj,
  main_logger)

  pass