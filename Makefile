INTERPRETER = python3

SCRIPT_PY = main.py
PROGRAM = crawler_report
MANAGE_PROJECT_SCRIPT = ./scripts/script_manage_project.sh

RESULTS_DIR = results
LOGS_DIR = logs

run_help_crawler: setup_program
  $(INTERPRETER) $(PROGRAM) -h

setup_program:
  @clear
  ln -sfn $(SCRIPT_PY) $(PROGRAM)

clear_result_dir:
  @clear
  rm -fr $(RESULTS_DIR)/*

clear_logs_dir:
  @clear
  rm -fr $(LOGS_DIR)/*

show_clear_all:
  @clear
  @echo "rm -fr $(RESULTS_DIR)/*"
  @echo "rm -fr $(LOGS_DIR)/*"

clear_all:
  @clear
  rm -fr $(RESULTS_DIR)/*
  rm -fr $(LOGS_DIR)/*

show_clear_from_pycache_subdirs:
  cp $(MANAGE_PROJECT_SCRIPT) a_script.sh
  bash a_script.sh --show
  rm -f a_script.sh

clear_from_pycache_subdirs:
  cp $(MANAGE_PROJECT_SCRIPT) a_script.sh
  bash a_script.sh --git_remove --target=__pycache__ --type=d
  rm -f a_script.sh

clear_from_pycache_subdirs:
  cp $(MANAGE_PROJECT_SCRIPT) a_script.sh
  bash a_script.sh --remove --target=__pycache__ --type=d
  rm -f a_script.sh