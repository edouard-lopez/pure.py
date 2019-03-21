import os
from pure import colors, virtual_env


def test_displays_virtual_env_invisible_when_deactivated():
    os.unsetenv('VIRTUAL_ENV')
    if 'VIRTUAL_ENV' in os.environ:  # when running tests in a virtualenv
        del os.environ['VIRTUAL_ENV']

    assert virtual_env.name() == ''


def test_displays_virtual_env_when_activated():
    os.environ['VIRTUAL_ENV'] = '/path/to/virtual/env'

    assert 'env' in str(virtual_env.name())
    assert str(virtual_env.name()) == str(colors.mute('env '))
