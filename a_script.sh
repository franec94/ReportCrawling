#!/usr/bin/env bash

function show_action {
  local target=$1
  local type_target=$2
  find ./ -type "${type_target}" -iname "${target}" \
    | awk ' {system(sprintf("echo %s", $0))} '
  unset target
  unset type_target
}

function remove {
  local target=$1
  local type_target=$2
  find ./ -type "${type_target}" -iname "${target}" \
    | awk ' {system(sprintf("rm -fr %s", $0))} '
  unset target
  unset type_target
}

function git_remove {
  local target=$1
  local type_target=$2
  find ./ -type "${type_target}" -iname "${target}" \
    | awk ' {system(sprintf("git rm -fr %s", $0))}'
  unset target
  unset type_target
}

if [ $# -eq 1 ] ; then
  local flag=$1
  if [ "${flag}" == "--show" ] ; then
    show_action
  unset flag
elif [ $# -eq 3 ] ; then
  local flag=$1
  local target=$2
  local type_target=$3
  if [ "${flag}" == "--remove" ] ; then
    remove $target $type_target
  elif [ "${flag}" == "--git_remove" ] ; then
    git_remove $target $type_target
  fi
  unset flag
  unset target
  unset type_target
fi

exit 0
