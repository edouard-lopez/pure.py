import os
from pathlib import Path

import colorful
import pytest

from pure import current_working_path, colors
from pure.prompt import fetch

test_directory = os.getcwd()
def teardown():
    os.chdir(str(Path(test_directory)))


def test_current_working_path_raw():
    os.chdir(str(Path('/tmp')))

    assert '/tmp' == current_working_path.raw()


@pytest.mark.parametrize('relative, expected', [('.', '~'), ('projects', '~/projects')])
def test_current_working_path_abbreviates_home(tmp_path, monkeypatch, relative, expected):
    home = tmp_path / 'me'
    directory = home / relative
    directory.mkdir(parents=True)
    monkeypatch.setenv('HOME', str(home))
    monkeypatch.setenv('USERPROFILE', str(home))
    monkeypatch.chdir(directory)

    assert current_working_path.raw() == expected


def test_current_working_path_keeps_sibling_with_same_prefix(tmp_path, monkeypatch):
    directory = tmp_path / 'meow'
    directory.mkdir()
    monkeypatch.setenv('HOME', str(tmp_path / 'me'))
    monkeypatch.setenv('USERPROFILE', str(tmp_path / 'me'))
    monkeypatch.chdir(directory)

    assert current_working_path.raw() == str(directory)


def test_current_working_path_segment_contains_text_and_style():
    colors.Theme()
    os.chdir(str(Path('/tmp')))

    segment = current_working_path.segment()

    assert segment == {'text': '/tmp', 'style': colors.Theme().style('primary')}


def test_current_working_path_color_is_primary():
    colors.Theme()
    os.chdir(str(Path('/tmp')))

    assert fetch(current_working_path.segment()) in colorful.primary('/tmp').styled_string
