import os
from pathlib import Path

import colorful

from pure import current_working_path, colors
from pure.prompt import fetch

test_directory = os.getcwd()
def teardown():
    os.chdir(str(Path(test_directory)))


def test_current_working_path_raw():
    os.chdir(str(Path('/tmp')))

    assert '/tmp' == current_working_path.raw()


def test_current_working_path_segment_contains_text_and_style():
    colors.load_theme()
    os.chdir(str(Path('/tmp')))

    segment = current_working_path.segment()

    assert segment == {'text': '/tmp', 'style': colors.style('info')}


def test_current_working_path_color_is_info():
    colors.load_theme()
    os.chdir(str(Path('/tmp')))

    assert fetch(current_working_path.segment()) in colorful.info('/tmp').styled_string
