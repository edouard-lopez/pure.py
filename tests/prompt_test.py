import os
from pathlib import Path

from pure import prompt, colors

SUCCESS = 0
FAIL = 1


def test_contains_prompt_symbol():
    assert '❯' in prompt.prompt_symbol()


def test_prompt_symbol_is_colored_for_successful_command():
    assert str(prompt.prompt_symbol()) == str(colors.primary('❯'))
    assert str(prompt.prompt_symbol()) == '\x1b[38;2;155;48;255m❯\x1b[39m'


def test_contains_path():
    os.chdir(str(Path('/tmp')))
    assert '/tmp' in str(prompt.current_working_path())


def test_current_working_path_color_is_info():
    os.chdir(str(Path('/tmp')))
    assert str(prompt.current_working_path()) == str(colors.info('/tmp'))
    assert str(prompt.current_working_path()) == '\x1b[38;2;173;216;230m/tmp\x1b[39m'


def test_change_prompt_when_last_command_fail():
    assert '❯' in prompt.prompt_symbol(last_command_status=SUCCESS)
    assert '❯' in prompt.prompt_symbol(last_command_status=FAIL)


def test_prompt_symbol_is_colored_for_failed_command():
    assert str(prompt.prompt_symbol(last_command_status=FAIL)) == str(colors.danger('❯'))
    assert str(prompt.prompt_symbol(last_command_status=FAIL)) == '\x1b[38;2;205;0;0m❯\x1b[39m'


def test_displays_virtual_env_invisible_when_deactivated():
    os.unsetenv('VIRTUAL_ENV')
    if 'VIRTUAL_ENV' in os.environ:  # when running tests in a virtualenv
        del os.environ['VIRTUAL_ENV']

    assert prompt.virtual_env() == ''


def test_displays_virtual_env_when_activated():
    os.environ['VIRTUAL_ENV'] = '/path/to/virtual/env'

    assert 'env' in str(prompt.virtual_env())
    assert str(prompt.virtual_env()) == str(colors.mute('env '))


def test_prompt_layout():
    assert prompt.layout() == "\n{current_working_path} {git_active_branch}{git_is_dirty}\n{virtual_env}{prompt_symbol} "

