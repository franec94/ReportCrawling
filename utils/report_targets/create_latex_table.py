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

def add_header_to_table(headers_list: list) -> str:
  def put_bold_style(item):
    return "\\textbf{" + str(item).capitalize() + "}"
  
  headers_str = ' & '.join([
    str(xi) for xi in 
    list(map(lambda xi: put_bold_style(xi), headers_list))
  ]
  )
  return headers_str + "\\\\"

# @log_debug_two_arguments
def create_latex_table(data_table_dict, headers_list, filename, cmd_args_obj, logger: logging.Logger):

  outputs_dir: str = cmd_args_obj.outputs_dir

  path_table: str = os.path.join('.',
  filename
  )
  with open(path_table, "w") as f:
    f.write("\\begin{table}[]\n")
    f.write("\\begin{tabular}{|c|c|}\n")
    f.write('\\hline\n')

    f.write(f"{add_header_to_table(headers_list)}")

    f.write('\\hline\n')
    for ii, (k,v) in enumerate(data_table_dict.items()):
      k = '\\_'.join([str(xi) for xi in str(k).split('_')])
      v = '\\_'.join([str(xi) for xi in str(v).split('_')])
      f.write(f"{k} & {v} \\\\ ")
      f.write('\\hline\n')
    f.write("\\end{tabular}\n")
    f.write("\\end{table}\n")
  pass