import os
import sys
import time
import logging
import time
import datetime

from pprint import pprint
from argparse import Namespace

from utils.routine_tasks.custom_decorators import *
from utils.routine_tasks.handle_files_content import *
from utils.handle_namespace import get_and_save_namespace_obj
from utils.handle_evaluation_values import  get_and_save_evaluation_values

@log_debug_two_arguments
def _process_file(file_name: str, cmd_args_obj, logger: logging.Logger):

  data_list: list = read_file_content_by_lines(file_name, logger)
  get_and_save_namespace_obj(data_list,
    cmd_args_obj,
    logger)

  get_and_save_evaluation_values(data_list,
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
    get_list_input_files(inputs_data, main_logger)

  _process_files_list(inputs_files_list,
  cmd_args_obj,
  main_logger)

  pass