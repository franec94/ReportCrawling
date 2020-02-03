import os
import sys
import time
import logging
import time
import datetime

import re

from pprint import pprint
from argparse import Namespace

from utils.routine_tasks.custom_decorators import *
from utils.routine_tasks.handle_files_content import *

@log_debug_two_arguments
def create_latex_table(data_table_dict, cmd_args_obj, logger: logging.Logger):

  outputs_dir: str = cmd_args_obj.outputs_dir

  path_table: str = os.path.join('.', 'namespace.tex')
  with open(path_table, "w") as f:
    f.write("\\begin{table}[]\n")
    f.write("\\begin{tabular}{ll}\n")
    for ii, (k,v) in enumerate(data_table_dict.items()):
      k = '\\_'.join([str(xi) for xi in str(k).split('_')])
      v = '\\_'.join([str(xi) for xi in str(v).split('_')])
      print(k)
      f.write(f"{k} & {v} \\\\\n")
    f.write("\\end{tabular}\n")
    f.write("\\end{table}\n")
  pass

@log_debug_two_arguments
def get_and_save_namespace_obj(data_list: list, cmd_args_obj, logger: logging.Logger):

  outputs_dir: str = cmd_args_obj.outputs_dir

  result_list: list = list(filter(lambda xi: xi.startswith('Namespace'), data_list))

  # pprint(result_list)

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

  create_latex_table(name_space_dict, cmd_args_obj, logger)
  pass