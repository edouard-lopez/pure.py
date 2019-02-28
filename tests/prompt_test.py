import os
from pathlib import Path

from pure.prompt import prompt, current_working_path


def test_prompt_contains_symbol():
    assert '❯' in prompt()


def test_contains_path():
    os.chdir(Path('/tmp'))
    assert '/tmp' in current_working_path()


def test_change_prompt_when_last_command_fail():
    fail = 0
    assert '❯' in prompt(last_command_status=fail)
    fail = 1
    assert 'x❯' in prompt(last_command_status=fail)
