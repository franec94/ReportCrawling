import os
import sys
import time
import logging
import time
import datetime
import json

import re

from pprint import pprint

from utils.routine_tasks.custom_decorators import *
from utils.routine_tasks.handle_files_content import *
from utils.report_targets.create_latex_table import create_latex_table

@log_debug_two_arguments
def get_and_save_network_params(data_list: list, cmd_args_obj, logger: logging.Logger):

  outputs_dir: str = cmd_args_obj.outputs_dir

  result_list: list = list(filter(lambda xi: xi[1] == '{' or xi[1] == '}', enumerate(data_list)))
  pprint(result_list)

  data_raw: str = ''
  for ii in range(result_list[0][0], result_list[1][0]+1):
    data_raw += data_list[ii]

  pprint(data_raw)

  # data_dict: dict = eval(data_raw)
  data_dict: dict = json.loads(data_raw)
  pprint(data_dict)
  

  create_latex_table(
    data_dict,
    ['params', 'values'],
    'arch_params.tex',
    cmd_args_obj,
    logger)
  pass