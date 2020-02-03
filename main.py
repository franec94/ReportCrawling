import os
import sys
import time
import logging
import time
import datetime

from utils.routine_tasks.parse_args_custom import get_cmd_line_args
from utils.routine_tasks.custom_logger import get_custom_logger
from utils.routine_tasks.setup_program import setup_program
from utils.report_crawler import crawl

def main():
  # Date at which main entry-point is invoked.
  start_time = datetime.datetime.now()
  a_main_date_str: str = datetime.datetime.strftime(start_time, '%Y%m%d_%H%M%S')
  
  # Get command line args
  cmd_args_obj, _ = get_cmd_line_args()

  # Get main logger
  main_logger: logging.Logger = \
    get_custom_logger(
      cmd_args_obj.logs_dir,
      'main_logger',
      # cmd_args_obj.logging_level
      )

  main_logger.info(f'[*] Running main at {a_main_date_str}')

  # Setup program based on cmd args
  setup_program(cmd_args_obj, main_logger)

  # Crawl input data based on cmd args
  crawl(cmd_args_obj, main_logger)

  # log end main script
  end_time = datetime.datetime.now()
  main_logger.info(f'[*] Running main, done.')
  main_logger.info(f'[*] Elapsed {end_time - start_time} since the begging of script.')
  pass

if __name__ == "__main__":
  main()
  pass