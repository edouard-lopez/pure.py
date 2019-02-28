# Purish [![travis-badge]][travis-link]

> Pretty, minimal and fast cross-shell prompt

## Goal

> Support as many shell as possible with only one codebase.

:heart: I'm familiar with some of them (`bash`, `zsh`, `fish`) but would love to have help support the other (`elvish`, `ksh`, `powershell`, `tcsh`).

## Features

<!-- ✔✖ -->
| Feature                                                        | `bash` | `elvish` | `fish` | `ksh` | `powershell` | `tcsh` | `zsh` |
| :------------------------------------------------------------- | :----- | :------- | :----- | :---- | :----------- | :----- | :---- |
| Excellent prompt character `❯`                                 | `✔`    |          | `✔`    |       |              |        | `✔`   |
| Display current directory tail                                 | `✔`    |          | `✔`    |       |              |        | `✔`   |
| Display `git` branch name                                      |        |          |        |       |              |        |       |
| Display `*` when `git` repository is _dirty_                   |        |          |        |       |              |        |       |
| Display `⇡` when branch is _ahead_<br>(commits to push)        |        |          |        |       |              |        |       |
| Display `⇣` when branch is _being_<br>(commits to pull)        |        |          |        |       |              |        |       |
| Change `❯` to red <br>when previous command has failed         | `✔`    |          | `✔`    |       |              |        | `✔`   |
| Update terminal title <br>with _current folder_ and _command_  |        |          |        |       |              |        |       |
| Display _username_ and _hostname_ <br>when in an `SSH` session |        |          |        |       |              |        |       |
| Display _duration_ <br>when command run more that `5` seconds  |        |          |        |       |              |        |       |
| Display `Python` _virtualenv_ when activated                   | `✔`    |          | `✔`    |       |              |        | `✔`   |
| Fine control over colors                                       |        |          |        |       |              |        |       |
| Right prompt control                                           |        |          |        |       |              |        |       |
| Display `VI` mode and custom symbol <br>for non-insert mode    |        |          |        |       |              |        |       |
## Install

:warning: Under heavy development, use at your own risk! 💀

    git clone git@github.com:edouard-lopez/pure.git $HOME/.pure
<!-- 
    pip install pure
-->

### Fish

    cp $HOME/.pure/config/fish_prompt.fish $fish_config/functions/
    echo 'set --global --export PURE_EXECUTABLE_PATH $HOME/.pure/' >> $fish_config/config.fish
    exec fish

### Zsh

    cp $HOME/.pure/config/prompt.zsh $HOME/.zsh/
    echo 'export PURE_EXECUTABLE_PATH=$HOME/.pure/' >> $HOME/.zshrc
    echo 'source $HOME/.zsh/prompt.zsh' >> $HOME/.zshrc
    exec zsh

### Bash

    mkdir ~/.bash/
    cp $HOME/.pure/config/prompt.bash $HOME/.bash/
    echo 'export PURE_EXECUTABLE_PATH=$HOME/.pure/' >> $HOME/.bashrc
    echo 'source $HOME/.bash/prompt.bash' >> $HOME/.bashrc
    exec bash

## License

MIT © Édouard Lopez.

[travis-link]: https://travis-ci.com/edouard-lopez/pure "TravisCI" 
[travis-badge]: https://travis-ci.com/edouard-lopez/pure.svg?branch=master
