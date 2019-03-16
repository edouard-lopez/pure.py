#!/usr/bin/env bash

mkdir ~/.bash/
cp "$HOME"/.pure/config/prompt.bash "$HOME"/.bash/
echo "export PURE_EXECUTABLE_PATH=$HOME/.pure/" >> "$HOME"/.bashrc
echo "source $HOME/.bash/prompt.bash" >> "$HOME"/.bashrc
exec bash
