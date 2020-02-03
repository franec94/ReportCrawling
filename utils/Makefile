INTERPRETER = python3

SCRIPT_PY = main.py
PROGRAM = crawler_report

RESULTS_DIR = results
LOGS_DIR = logs

run_help_crawler: setup_program
  @clear
  $(INTERPRETER) $(PROGRAM) -h

setup_program:
  ln -sfn $(SCRIPT_PY) $(PROGRAM)

clear_result_dir:
  @clear
  rm -fr $(RESULTS_DIR)/*

clear_logs_dir:
  @clear
  rm -fr $(LOGS_DIR)/*

show_clar_all:
  @clear
  @echo "rm -fr $(RESULTS_DIR)/*"
  @echo "rm -fr $(LOGS_DIR)/*"

clear_all:
  @clear
  rm -fr $(RESULTS_DIR)/*
  rm -fr $(LOGS_DIR)/*