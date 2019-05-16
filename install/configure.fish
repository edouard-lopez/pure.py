#!/usr/bin/env fish

mkdir -p $__fish_config_dir/functions/
cp $HOME/.pure/config/fish_prompt.fish $__fish_config_dir/functions/
echo 'set --global --export PURE_EXECUTABLE_PATH $HOME/.pure/' >> $__fish_config_dir/config.fish
exec fish