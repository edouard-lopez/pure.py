# Pure [![travis-badge]][travis-link]

> Pretty, minimal and fast prompt _for various shell_.

<div align=center>
  <a href="screenshot dark" target=blank><img width=380 src=https://i.imgur.com/gmS4Bqy.png alt="Pure with dark colorscheme"></a>
  <a href="screenshot light" target=blank><img width=380 src=https://i.imgur.com/nZWx1tr.png alt="Pure with light colorscheme"></a>
</div>

Original design by [sindresorhus/pure](https://github.com/sindresorhus/pure).

## Goal

> Support various shells as possible with only one codebase.

❤️ I'm familiar with some of them (`bash`, `zsh`, `fish`) but would love to have help support the other (`elvish`, `ksh`, `powershell`, `tcsh`, `xonsh`).

## Features

<!-- ✔✖ -->
| Feature                                                        | `bash` | `elvish` | `fish` | `ksh` | `powershell` | `tcsh` | `xonsh` | `zsh` |
| :------------------------------------------------------------- | :----- | :------- | :----- | :---- | :----------- | :----- | :------ | :---- |
| Excellent prompt character `❯`                                 | **✔**  | **✔**    | **✔**  |       |              |        |         | **✔** |
| Display current directory tail                                 | **✔**  | **✔**    | **✔**  |       |              |        |         | **✔** |
| Display `git` branch name                                      | **✔**  | **✔**    | **✔**  |       |              |        |         | **✔** |
| Display `*` when `git` repository is _dirty_                   | **✔**  | **✔**    | **✔**  |       |              |        |         | **✔** |
| Display `⇡` when branch is _ahead_<br>(commits to push)        |        |          |        |       |              |        |         |       |
| Display `⇣` when branch is _being_<br>(commits to pull)        |        |          |        |       |              |        |         |       |
| Change `❯` to red <br>when previous command has failed         | **✔**  | [✖][elv] | **✔**  |       |              |        |         | **✔** |
| Update terminal title <br>with _current folder_ and _command_  |        |          |        |       |              |        |         |       |
| Display _username_ and _hostname_ <br>when in an `SSH` session |        |          |        |       |              |        |         |       |
| Display _duration_ <br>when command run more that `5` seconds  |        |          |        |       |              |        |         |       |
| Display `Python` _virtualenv_ when activated                   | **✔**  |          | **✔**  |       |              |        |         | **✔** |
| Fine control over colors                                       |        |          |        |       |              |        |         |       |
| Right prompt control                                           |        |          |        |       |              |        |         |       |
| Display `VI` mode and custom symbol <br>for non-insert mode    |        |          |        |       |              |        |         |       |

## Install

⚠️ Under heavy development, use at your own risk! 💀

**requirements:** `git` and `pip`.

Install required Python modules:

    pip install pure colorful gitpython --user

### Fish

    git clone git@github.com:edouard-lopez/pure-x.git $HOME/.pure
    fish $HOME/.pure/install/configure.fish

### Zsh

    git clone git@github.com:edouard-lopez/pure-x.git $HOME/.pure
    zsh $HOME/.pure/install/configure.zsh

### Bash

    git clone git@github.com:edouard-lopez/pure-x.git $HOME/.pure
    bash $HOME/.pure/install/configure.bash

### Elvish

Elvish has its own built-in package manager (`epm`), so you do not need to clone
the repository by hand. Instead, from within the Elvish shell, run the following
commands:

    use epm
    epm:install github.com/edouard-lopez/pure-x.git
    elvish ~/.elvish/lib/github.com/edouard-lopez/pure-x.git/install/configure.elv 

Note: the last command simply adds the following line to your `~/.elvish/rc.elv`
file, which you can also add by hand or run interactively to test the prompt:

    use github.com/edouard-lopez/pure-x.git/config/prompt

## Theme

Set `PURE_THEME` environment variable and edit your config file (see [more about theme configuration](./pure/theme/)).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

## License

MIT © Édouard Lopez.

[elv]: https://github.com/elves/elvish/issues/799#issuecomment-471257473
[travis-link]: https://travis-ci.com/edouard-lopez/pure "TravisCI"
[travis-badge]: https://travis-ci.com/edouard-lopez/pure.svg?branch=master

## Ports

* Original [sindresorhus/pure](https://github.com/sindresorhus/pure) Zsh implementation ;
* :fish: [pure-fish/pure](https://github.com/pure-fish/pure/) Fish implementation (features rich) ;
* :snake: [edouard-lopez/pure.py](https://github.com/edouard-lopez/pure.py/) Python implementation  (partial features) ;
* :goat: [edouard-lopez/pure.go](https://github.com/edouard-lopez/pure.go/) Golang implementation  (partial features) ;
* :gear: [xcambar/purs](https://github.com/xcambar/purs) Rust implementation ;
* :window: [nickcox/pure-pwsh](https://github.com/nickcox/pure-pwsh/) PowerShell implementation.
* :shell: [krashikiworks/pure-prompt-bash](https://github.com/krashikiworks/pure-prompt-bash) Bash implementation.
