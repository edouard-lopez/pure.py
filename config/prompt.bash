#!/usr/bin/env bash

export PS1=$(python3 $PURE_EXECUTABLE_PATH/pure/prompt.py --last-command-status $?)