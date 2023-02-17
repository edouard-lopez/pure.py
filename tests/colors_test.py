import os
from pathlib import Path, PurePath
from turtle import color
from unittest import mock

import colorful
import platformdirs

from pure import colors


@mock.patch.dict(os.environ, {}, clear=True)
def test_colors_load_theme_return_theme_name_and_data():
    theme = colors.Theme()

    assert theme.name == theme.default_theme_name
    scheme_colors = list(theme.scheme.keys())
    scheme_colors.sort()
    assert scheme_colors == [
        "danger",
        "dark",
        "info",
        "light",
        "mute",
        "normal",
        "primary",
        "success",
        "warning",
    ]


@mock.patch.dict(os.environ, {}, clear=True)
def test_colors_load_theme_from_user_config_directory():
    os.environ["PURE_THEME"] = "ayu"

    theme = colors.Theme()

    assert theme.name == "ayu"


def test_colors_get_default_theme_return_filepath():
    theme = colors.Theme()

    default_theme: Path = theme.get_default_theme(filepath=True)

    assert PurePath(default_theme).is_absolute() == True
    assert str(default_theme).endswith(theme.file_extension)  # .json


def test_colors_get_default_theme_return_filename_by_default():
    theme = colors.Theme()

    default_theme: str = theme.get_default_theme()

    assert PurePath(default_theme).is_absolute() == False
    assert default_theme == theme.default_theme_name


def test_get_theme_filepath():
    theme = colors.Theme()
    theme_name = "foo-bar"

    theme_filepath: Path = theme.get_theme_filepath(theme_name)

    assert PurePath(theme_filepath).is_absolute() == True
    assert str(theme_filepath).endswith(theme.file_extension)  # .json


@mock.patch.dict(os.environ, {}, clear=True)
def test_get_active_theme():
    theme = colors.Theme()

    active_theme: str = theme.get_active_theme()

    assert active_theme == theme.get_default_theme()


def test_colors_create_default_theme_when_none_exists():
    theme = colors.Theme(autoload=False)

    default_theme_filepath: Path = theme.get_default_theme(filepath=True)
    default_theme_filepath.unlink(missing_ok=True)
    
    theme.load_theme()

    
    assert os.path.isfile(default_theme_filepath) == True


@mock.patch.dict(os.environ, {}, clear=True)
def test_colors_default_theme_is_tomorrow():
    theme = colors.Theme()

    assert colorful.primary.style == ("\x1b[38;2;137;89;168m", "\x1b[39m")
    assert colorful.info.style == ("\x1b[38;2;66;113;174m", "\x1b[39m")
    assert colorful.mute.style == ("\x1b[38;2;150;152;150m", "\x1b[39m")
    assert colorful.success.style == ("\x1b[38;2;113;140;0m", "\x1b[39m")
    assert colorful.normal.style == ("\x1b[38;2;224;224;224m", "\x1b[39m")
    assert colorful.danger.style == ("\x1b[38;2;200;40;41m", "\x1b[39m")
    assert colorful.light.style == ("\x1b[38;2;29;31;33m", "\x1b[39m")
    assert colorful.warning.style == ("\x1b[38;2;234;183;0m", "\x1b[39m")
    assert colorful.dark.style == ("\x1b[38;2;214;214;214m", "\x1b[39m")


def test_colors_style_only_return_starting_ansi_code():
    theme = colors.Theme()

    primary = theme.style("primary")

    assert primary == "\x1b[38;2;137;89;168m"
