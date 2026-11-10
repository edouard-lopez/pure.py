import os
from pathlib import Path

from pure import colors


def raw():
    directory = Path.cwd()
    try:
        relative = directory.relative_to(os.path.expanduser('~'))
    except ValueError:
        return str(directory)
    return (Path('~') / relative).as_posix()


def segment():
    return {
        'text': raw(),
        'style': colors.Theme().style('primary')
    }
