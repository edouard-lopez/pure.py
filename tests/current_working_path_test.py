import os
from pathlib import Path

from pure import current_working_path, colors


def test_contains_path():
    os.chdir(str(Path('/tmp')))
    assert '/tmp' in str(current_working_path.current_working_path())


def test_current_working_path_color_is_info():
    os.chdir(str(Path('/tmp')))
    assert str(current_working_path.current_working_path()) == str(colors.info('/tmp'))
    assert str(current_working_path.current_working_path()) == '\x1b[38;2;173;216;230m/tmp\x1b[39m'
