#!/usr/bin/env zsh

mkdir -p $HOME/.zsh/
cp $HOME/.pure/config/prompt.zsh $HOME/.zsh/
echo 'export PURE_EXECUTABLE_PATH=$HOME/.pure/' >> $HOME/.zshrc
echo 'source $HOME/.zsh/prompt.zsh' >> $HOME/.zshrc
exec zsh
