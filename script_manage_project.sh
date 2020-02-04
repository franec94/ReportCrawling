#!/usr/bin/env bash

function show_action {
  local flag=$1
  
  if [ "${flag}" == "--show" ] ; then
    find ./ -type d -iname "__pycache__" \
      | awk ' {system(sprintf("echo %s", $0))} '
  fi

  unset flag
}

if [ $# -eq 1 ] ; then
  show_action $1
  exit 0
fi

find ./ -type d -iname "__pycache__" \
  | awk ' {system(sprintf("rm -fr %s", $0))} '

exit 0

