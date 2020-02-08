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
from utils.report_targets.create_latex_table import create_latex_table

from utils.tables_spredsheets.metrics_table import create_table_metrics

@log_debug_two_arguments
def _create_latex_table(data_table_dict, cmd_args_obj, logger: logging.Logger):

  outputs_dir: str = cmd_args_obj.outputs_dir

  path_table: str = os.path.join('.', 'evaluation_values_validation.tex')
  with open(path_table, "w") as f:
    f.write("\\begin{table}[]\n")
    f.write("\\begin{tabular}{|c|c|}\n")
    f.write('\\hline\n')
    f.write('\\textbf{Metric} & \\textbf{Value} \\\\')
    f.write('\\hline\n')
    for ii, (k,v) in enumerate(data_table_dict.items()):
      k = '\\_'.join([str(xi) for xi in str(k).split('_')])
      v = '\\_'.join([str(xi) for xi in str(v).split('_')])
      f.write(f"{k} & {v} \\\\ ")
      f.write('\\hline\n')
    f.write("\\end{tabular}\n")
    f.write("\\end{table}\n")
  pass

@log_debug_two_arguments
def get_and_save_evaluation_values(data_list: list, cmd_args_obj, logger: logging.Logger):

  outputs_dir: str = cmd_args_obj.outputs_dir

  result_list: list = list(filter(lambda xi: xi.startswith('loss'), data_list))

  if len(result_list) == 0:
    err_statement: str = f"ERROR: metrics scores list not found"
    logger.error(err_statement)
    raise Exception(err_statement)

  pairs_scores_dict: dict = dict()
  for item in result_list[0].split(','):
    k, v = item.split(':')
    pairs_scores_dict[k] = v
  
  pprint(pairs_scores_dict)
  create_latex_table(pairs_scores_dict,
    ['metrics', 'values'],
    'evaluation_values_validation.tex',
    cmd_args_obj,
    logger)

  pairs_scores_dict: dict = dict()
  for item in result_list[0].split(','):
    k, v = item.split(':')
    pairs_scores_dict[k] = list(v)
  
  create_table_metrics(data=pairs_scores_dict)
  pass