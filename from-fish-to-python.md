# From Fish to Python

How to port a [pure-fish/pure] feature to pure.py.
Read [How Pure works][how-it-works] first: it explains the Fish pipeline.
The [gap matrix](README.md#gap-matrix) lists what is left to port.

## Mental model

| Fish Pure | pure.py |
| :-------- | :------ |
| Fish calls `fish_prompt` before each prompt. | The shell config in `config/` runs `python3 pure/prompt.py` before each prompt. |
| A segment is a function `_pure_prompt_<name>`. | A segment is a module `pure/<name>.py` with `raw()` and `segment()`. |
| `segment()` returns `{'text', 'style'}`; `prompt.layout()` places it. | Same idea; Fish joins non-empty parts with a space. |
| Segments read Fish variables (`$pipestatus`, `$CMD_DURATION`). | Python cannot see them. The shell passes them as arguments or env vars. |
| Settings are `pure_*` variables. | Today: a JSON theme (`PURE_THEME`). Target: `PURE_*` env vars, like pure.go. |
| `set_color` prints colours. | `colorful` through `colors.Theme().style(name)`. |
| Fishtape tests per function. | `pytest` per module, plus [agnostic-tests] for the whole program. |

## Idioms

| Fish | Python |
| :--- | :----- |
| `set --local name value` | `name = value` |
| `set --query var; and test "$var" = true` | `os.environ.get("PURE_VAR", "false") == "true"` |
| `test -n "$x"` | `if x:` |
| `(command git status --porcelain)` | `subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout` |
| `string replace --regex 'a' 'b' $s` | `re.sub("a", "b", s)` |
| `string split '/' $p \| tail -n 2` | `"/".join(p.split("/")[-2:])` |
| `string length` on visible text | strip ANSI with `re.sub(r"\x1b\[[^m]*m", "", s)`, then `len()` (or `wcwidth` for emoji) |
| `prompt_pwd` | `pathlib.Path`, `os.path.expanduser`, then shorten each part |
| `return 1` (failure) | return `""` to hide a segment, raise for real failures |

## Recipe for one segment (TDD)

1. **Pick** one row of the gap matrix, in phase order.
2. **Read** the Fish function and its test: `functions/_pure_prompt_<name>.fish`, `tests/_pure_prompt_<name>.test.fish`.
3. **Red**: copy each Fishtape case into `tests/<name>_test.py`. Use `monkeypatch.setenv` and `tmp_path`. Run `make tests-unit-only`.
4. **Green**: write the smallest `raw()` that passes.
5. **Wire**: add the segment to `prompt.prompt()` and `prompt.layout()`. Keep the Fish order.
6. **Spec**: add or update a black-box spec in [agnostic-tests], and run it with `IMPLEMENTATION=python`.
7. **Refactor**, then update the gap matrix row.

Keep `raw()` pure where you can: pass inputs as arguments, keep `os` and `subprocess` at the edge.

## Shell state contract

| Needed by | Fish source | Proposed input |
| :-------- | :---------- | :------------- |
| symbol, exit statuses | `$pipestatus` | `--last-command-status N` (exists), later `--pipestatus "0 1"` |
| command duration | `$CMD_DURATION` | `PURE_CMD_DURATION` (ms) |
| folder shortening | `$COLUMNS` | `COLUMNS` |
| jobs | `jobs -p` | `--jobs N` |
| vi mode | `$fish_bind_mode` | `--bind-mode insert` |
| transient prompt | `--final-rendering` | `--final-rendering` |

Agree on each name in [agnostic-tests] before you code it, so Go and Rust use the same flag.

## Pitfalls

* **Startup time**: Python starts slower than Fish functions. Import only what a prompt needs. Load the theme once, not once per segment.
* **GitPython**: `git.Repo(path)` does not search parent folders. Pass `search_parent_directories=True`.
* **Speed**: each `git` call costs time. Batch with `git status --porcelain=v2 --branch` when you add ahead/behind.
* **Width**: measure the visible width without ANSI codes, like `_pure_string_width`.
* **Many shells**: pure.py also targets Bash, Zsh and Elvish. Put shell-specific code in `config/`, never in segments.

[pure-fish/pure]: https://github.com/pure-fish/pure
[how-it-works]: https://pure-fish.github.io/pure/doc/#how-it-works
[agnostic-tests]: https://github.com/pure-fish/agnostic-tests
