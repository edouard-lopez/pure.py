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
| :------------------------------------------------------------- | :----- | :------- | :----- | :---- | :----------- | :----- | :----- | :---- |
| Excellent prompt character `❯`                                 | **✔**  |          | **✔**  |       |              |        |        | **✔** |
| Display current directory tail                                 | **✔**  |          | **✔**  |       |              |        |        | **✔** |
| Display `git` branch name                                      | **✔**  |          | **✔**  |       |              |        |        | **✔** |
| Display `*` when `git` repository is _dirty_                   | **✔**  |          | **✔**  |       |              |        |        | **✔** |
| Display `⇡` when branch is _ahead_<br>(commits to push)        |        |          |        |       |              |        |        |       |
| Display `⇣` when branch is _being_<br>(commits to pull)        |        |          |        |       |              |        |        |       |
| Change `❯` to red <br>when previous command has failed         | **✔**  | [✖][elv] | **✔**  |       |              |        |        | **✔** |
| Update terminal title <br>with _current folder_ and _command_  |        |          |        |       |              |        |        |       |
| Display _username_ and _hostname_ <br>when in an `SSH` session |        |          |        |       |              |        |        |       |
| Display _duration_ <br>when command run more that `5` seconds  |        |          |        |       |              |        |        |       |
| Display `Python` _virtualenv_ when activated                   | **✔**  |          | **✔**  |       |              |        |        | **✔** |
| Fine control over colors                                       |        |          |        |       |              |        |        |       |
| Right prompt control                                           |        |          |        |       |              |        |        |       |
| Display `VI` mode and custom symbol <br>for non-insert mode    |        |          |        |       |              |        |        |       |

## Install

⚠️ Under heavy development, use at your own risk! 💀

**requirements:** `git` and `pip`.

    git clone git@github.com:edouard-lopez/pure.git $HOME/.pure
    pip install pure --user

### Fish

    fish $HOME/.pure/install/configure.fish

### Zsh

    zsh $HOME/.pure/install/configure.zsh

### Bash

    bash $HOME/.pure/install/configure.bash

### Elvish

    elvish $HOME/.pure/install/configure.elv

## Theme

Declare the name of your theme file using `PURE_THEME` environment variable. 
A file named `$HOME/.config/.pure/${PURE_THEME}.json` must exists and follow [theme configuration](./pure/theme/) convention.


## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

## License

MIT © Édouard Lopez.

[elv]: https://github.com/elves/elvish/issues/799#issuecomment-471257473
[travis-link]: https://travis-ci.com/edouard-lopez/pure "TravisCI" 
[travis-badge]: https://travis-ci.com/edouard-lopez/pure.svg?branch=master
