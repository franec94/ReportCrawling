import os
import sys
import time
import logging
import time
import datetime

def create_dir(dir_name: str, logger: logging.Logger):
  if os.path.exists(dir_name) is True:
    if os.path.isdir(dir_name) is False:
      logger.error(f"Input resources {dir_name} exists, but is not a directory!")
      sys.exit(-1)
    logger.info(f"Directory '{dir_name}' is not created, it already exists.")
  else:
    print(f'Creating {dir_name}... ', end='', file=sys.stdout)
    os.makedirs(dir_name)
    logger.info(f"{dir_name} created.")
    print(f' done.', file=sys.stdout)
  pass

def setup_program(cmd_args_obj, main_logger: logging.Logger):

  main_logger.info('f> setup_program() running...')

  create_dir(cmd_args_obj.logs_dir, main_logger)
  create_dir(cmd_args_obj.outputs_dir, main_logger)

  main_logger.info('f< setup_program(), done.')
  pass