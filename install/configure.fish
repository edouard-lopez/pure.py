#!/usr/bin/env fish

cp $HOME/.pure/config/fish_prompt.fish $fish_config/functions/
echo 'set --global --export PURE_EXECUTABLE_PATH $HOME/.pure/' >> $fish_config/config.fish
exec fish