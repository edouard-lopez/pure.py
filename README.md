# Purish [![travis-badge]][travis-link]

> Pretty, minimal and fast cross-shell prompt

## Goal

> Support as many shell as possible with only one codebase.
> * [ ] `bash`, 
> * [ ] `elvish`
> * [ ] `fish`, 
> * [ ] `ksh`, 
> * [ ] `tcsh`, 
> * [ ] `zsh`, 
 

:heart: I'm familiar with some of them (`bash`, `zsh`, `fish`) but would love to have help support the other (`ksh`, `elvish`).


## Install

👻 Not yet available.

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

### Zsh

    mkdir ~/.bash/ 
    cp $HOME/.pure/config/prompt.bash $HOME/.bash/
    echo 'export PURE_EXECUTABLE_PATH=$HOME/.pure/' >> $HOME/.bashrc
    echo 'source $HOME/.bash/prompt.bash' >> $HOME/.bashrc
    exec zsh

## Features

- [ ] Excellent prompt character `❯` ;
- [ ] Display current directory tail ;
- [ ] Display `git` branch name ;
  - [ ] Display `*` when `git` repository is _dirty_ ;
  - [ ] Display `⇡` when branch is _ahead_ (commits to push) ;
  - [ ] Display `⇣` when branch is _being_ (commits to pull) ;
- [ ] Change `❯` to red when previous command has failed ;
- [ ] Update terminal title with _current folder_ and _command_ ;
- [ ] Display _username_ and _hostname_ when in an `SSH` session ;
- [ ] Display _duration_ when command run more that `5` seconds ;
- [ ] Display `Python` _virtualenv_ when activated ;
- [ ] Fine control over **colors** ;
- [ ] Right prompt control.
- [ ] Display `VI` mode and custom symbol for non-insert mode.

## License

MIT © Édouard Lopez.

[travis-link]: https://travis-ci.com/edouard-lopez/pure "TravisCI" 
[travis-badge]: https://travis-ci.com/edouard-lopez/pure.svg?branch=master
