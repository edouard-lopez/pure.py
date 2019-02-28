import os
from pathlib import Path

from pure.prompt import prompt, current_working_path


def test_prompt_contains_symbol():
    assert '❯' in prompt()
def test_contains_path():
    os.chdir(Path('/tmp'))
    assert '/tmp' in current_working_path()

