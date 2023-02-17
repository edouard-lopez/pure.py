import os

from pure import virtual_env, colors, constants


def test_virtual_env_raw_name_is_empty_when_deactivated():
    os.unsetenv('VIRTUAL_ENV')
    if 'VIRTUAL_ENV' in os.environ:  # when running tests in a virtualenv
        del os.environ['VIRTUAL_ENV']

    assert virtual_env.raw() == constants.NOTHING


def test_virtual_env_segment_text_is_empty_when_deactivated():
    os.unsetenv('VIRTUAL_ENV')
    if 'VIRTUAL_ENV' in os.environ:  # when running tests in a virtualenv
        del os.environ['VIRTUAL_ENV']
    colors.Theme()

    assert virtual_env.segment() == {'text': '', 'style': colors.Theme().style('mute')}


def test_virtual_env_raw_name_is_empty_when_activated():
    os.environ['VIRTUAL_ENV'] = '/path/to/virtual/env'

    assert virtual_env.raw() == 'env'


def test_virtual_env_segment_text_is_empty_when_activated():
    os.environ['VIRTUAL_ENV'] = '/path/to/virtual/env'
    colors.Theme()

    assert virtual_env.segment() == {'text': 'env', 'style': colors.Theme().style('mute')}
