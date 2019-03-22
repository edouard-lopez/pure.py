import os
from pathlib import Path

from pure import current_working_path, colors
from pure.prompt import fetch


def test_current_working_path_raw():
    os.chdir(str(Path('/tmp')))

    assert '/tmp' == current_working_path.raw()


def test_current_working_path_segment_contains_text_and_style():
    os.chdir(str(Path('/tmp')))

    segment = current_working_path.segment()

    assert segment == {'text': '/tmp', 'style': colors.info}


def test_current_working_path_color_is_info():
    os.chdir(str(Path('/tmp')))

    assert str(fetch(current_working_path.segment())) == str(colors.info('/tmp'))
    assert str(fetch(current_working_path.segment())) == '\x1b[38;2;173;216;230m/tmp\x1b[39m'
