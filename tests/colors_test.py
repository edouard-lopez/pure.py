import os
import colorful

from pure import colors


def test_load_theme_return_theme_name_and_data():
    os.unsetenv('PURE_THEME')

    theme, scheme = colors.load_theme()

    assert theme == 'tomorrow'
    assert list(scheme.keys()) == [
                                "primary",
                                "info",
                                "mute",
                                "success",
                                "normal",
                                "danger",
                                "light",
                                "warning",
                                "dark"
                            ]


def test_default_theme_is_tomorrow():
    os.unsetenv('PURE_THEME')

    colors.load_theme()

    assert colorful.primary.style == ('\x1b[38;2;137;89;168m', '\x1b[39m') 
    assert colorful.info.style    == ('\x1b[38;2;66;113;174m', '\x1b[39m') 
    assert colorful.mute.style    == ('\x1b[38;2;150;152;150m', '\x1b[39m')
    assert colorful.success.style == ('\x1b[38;2;113;140;0m', '\x1b[39m') 
    assert colorful.normal.style  == ('\x1b[38;2;224;224;224m', '\x1b[39m')
    assert colorful.danger.style  == ('\x1b[38;2;200;40;41m', '\x1b[39m') 
    assert colorful.light.style   == ('\x1b[38;2;29;31;33m', '\x1b[39m')
    assert colorful.warning.style == ('\x1b[38;2;234;183;0m', '\x1b[39m') 
    assert colorful.dark.style    == ('\x1b[38;2;214;214;214m', '\x1b[39m') 