import os
from pathlib import Path

from pure import prompt


def test_prompt_contains_symbol():
    assert '❯' in prompt.prompt_symbol()


def test_contains_path():
    os.chdir(str(Path('/tmp')))
    assert '/tmp' in prompt.current_working_path()


def test_change_prompt_when_last_command_fail():
    fail = 0
    assert '❯' in prompt.prompt_symbol(last_command_status=fail)
    fail = 1
    assert 'x❯' in prompt.prompt_symbol(last_command_status=fail)


def test_displays_virtual_env_invisible_when_deactivated():
    del os.environ['VIRTUAL_ENV']

    assert prompt.virtual_env() == ''


def test_displays_virtual_env_when_activated():
    os.environ['VIRTUAL_ENV'] = '/path/to/virtual/env'

    assert prompt.virtual_env() == 'env'
