import argparse
import os
import sys
import time
import logging
import time
import datetime


def _get_custom_parser() -> argparse.ArgumentParser:
  # Create an instance of ArgumentParser class.
  parser: argparse.ArgumentParser = argparse.ArgumentParser()

  # Mandatory command line arguments.
  parser.add_argument('--inputs', default="resources/report.txt", help='List of resources to be processed.', type=str)
  
  # Command line arguments owning default values.
  parser.add_argument('--outputs_dir', default="results", help='Output directory where the results will be stored. If not present thid directory will be created by the running script.', type=str)

  parser.add_argument('--logs_dir', default="logs", help='Logs directory where the generated log files will be stored. If not present thid directory will be created by the running script.', type=str)

  choices_logging_level: list = list(map(lambda xi: xi.upper(), 'debug,warning,error'.split(',')))
  parser.add_argument('--logging_level',
    default='DEBUG',
    choices=choices_logging_level,
    help='Allows to specify which level to exploit for logging operation when script is running.',
    type=str
    )

  # Return an instance of ArgumentParser class.
  return parser

def get_cmd_line_args():
  # Get an instance of ArgumentParser class.
  parser = _get_custom_parser()

  # Parsing command line args...
  params = parser.parse_args()

  # Return object-like commnad line args and an instance of ArgumentParser class.
  return params, parser