#!/usr/bin/env zsh

export PROMPT=$(python3 $PURE_EXECUTABLE_PATH/pure/prompt.py --last-command-status $status)