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

## Gap matrix

Parity with the reference [pure-fish/pure](https://github.com/pure-fish/pure) implementation.
See [How Pure works](https://pure-fish.github.io/pure/doc/#how-it-works) for the Fish internals, and the [From Fish to Python](from-fish-to-python.md) guide for the porting guide.

✅ done · 🟡 partial · ❌ missing. Phases match the repository milestones.

| Phase | Feature | Fish setting | Status |
| :---- | :------ | :----------- | :----- |
| P0 Foundation | CLI contract `--last-command-status N` | — | ✅ |
| P0 Foundation | Settings from `PURE_*` environment variables | `pure_*` | ❌ uses `PURE_THEME` JSON files |
| P0 Foundation | Nine base colours, configurable | `pure_color_*` | 🟡 JSON theme, true colours |
| P0 Foundation | Agnostic tests in CI | — | ❌ adapter exists, not in CI |
| P1 Core prompt | Prompt symbol `❯` | `pure_symbol_prompt` | ✅ |
| P1 Core prompt | Symbol red after a failure, magenta after a success | `pure_color_prompt_on_*` | 🟡 success uses `primary` |
| P1 Core prompt | Separate error symbol | `pure_separate_prompt_on_error` | ❌ |
| P1 Core prompt | Exit statuses list, signal names | `pure_show_exit_status` | ❌ |
| P1 Core prompt | Current folder with `~` | `pure_color_current_directory` | 🟡 full path, no `~` |
| P1 Core prompt | Shorten and truncate folder | `pure_shorten_*`, `pure_truncate_*` | ❌ |
| P1 Core prompt | Blank line before the prompt | — | ✅ |
| P1 Core prompt | Single-line (compact) prompt | `pure_enable_single_line_prompt` | ❌ |
| P1 Core prompt | Folder first or last | `pure_begin_prompt_with_current_directory` | 🟡 folder first only |
| P2 Git | Git branch (and detached HEAD) | `pure_color_git_branch` | 🟡 fails in subfolders and on detached HEAD |
| P2 Git | Git dirty `*` | `pure_symbol_git_dirty` | ✅ |
| P2 Git | Git stash `≡` | `pure_symbol_git_stash` | ❌ |
| P2 Git | Git ahead `⇡` / behind `⇣` | `pure_symbol_git_unpushed_commits` | ❌ |
| P2 Git | Numbered git indicators | `pure_show_numbered_git_indicator` | ❌ |
| P2 Git | Disable git | `pure_enable_git` | ❌ |
| P3 Context segments | Command duration | `pure_threshold_command_duration` | ❌ |
| P3 Context segments | `user@host` over SSH | `pure_symbol_ssh_prefix` | ❌ |
| P3 Context segments | Container detection | `pure_enable_container_detection` | ❌ |
| P3 Context segments | Python virtualenv / conda | `pure_enable_virtualenv` | 🟡 `VIRTUAL_ENV` only |
| P3 Context segments | AWS profile | `pure_enable_aws_profile` | ❌ |
| P3 Context segments | Kubernetes context/namespace | `pure_enable_k8s` | ❌ |
| P3 Context segments | Nix dev shell | `pure_enable_nixdevshell` | ❌ |
| P3 Context segments | Background jobs | `pure_show_jobs` | ❌ |
| P3 Context segments | System time | `pure_show_system_time` | ❌ |
| P3 Context segments | Root prefix `#` | `pure_show_prefix_root_prompt` | ❌ |
| P4 Shell integration | Vi mode `❮` / `[N]` | `pure_reverse_prompt_symbol_in_vimode` | ❌ |
| P4 Shell integration | Private mode prefix `!` | `pure_show_prefix_private_prompt` | ❌ |
| P4 Shell integration | Transient prompt | `fish_transient_prompt` | ❌ |
| P4 Shell integration | Window title | `pure_symbol_title_bar_separator` | ❌ |
| P4 Shell integration | iTerm2 prompt mark | — | ❌ |
| P5 Release | Check for new release | `pure_check_for_new_release` | ❌ |
| Extra | Bash, Zsh, Elvish configs | — | ➕ not in Fish Pure |


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
