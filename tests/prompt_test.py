import os
from pathlib import Path

from pure import prompt, colors

SUCCESS = 0
FAIL = 1


def test_contains_prompt_symbol():
    assert '❯' in prompt.prompt_symbol()


def test_prompt_symbol_is_colored_for_successful_command():
    assert str(colors.success('❯')) == str(prompt.prompt_symbol())


def test_contains_path():
    os.chdir(str(Path('/tmp')))
    assert '/tmp' in prompt.current_working_path()


def test_change_prompt_when_last_command_fail():
    assert '❯' in prompt.prompt_symbol(last_command_status=SUCCESS)
    assert '❯' in prompt.prompt_symbol(last_command_status=FAIL)


def test_prompt_symbol_is_colored_for_failed_command():
    assert str(colors.danger('❯')) == str(prompt.prompt_symbol())


def test_displays_virtual_env_invisible_when_deactivated():
    os.unsetenv('VIRTUAL_ENV')

    assert prompt.virtual_env() == ''


def test_displays_virtual_env_when_activated():
    os.environ['VIRTUAL_ENV'] = '/path/to/virtual/env'

    assert prompt.virtual_env() == 'env'
