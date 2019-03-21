from pure import prompt, colors

SUCCESS = 0
FAIL = 1


def test_contains_prompt_symbol():
    assert '❯' in prompt.prompt_symbol()


def test_prompt_symbol_is_colored_for_successful_command():
    assert str(prompt.prompt_symbol()) == str(colors.primary('❯'))
    assert str(prompt.prompt_symbol()) == '\x1b[38;2;155;48;255m❯\x1b[39m'


def test_change_prompt_when_last_command_fail():
    assert '❯' in prompt.prompt_symbol(last_command_status=SUCCESS)
    assert '❯' in prompt.prompt_symbol(last_command_status=FAIL)


def test_prompt_symbol_is_colored_for_failed_command():
    assert str(prompt.prompt_symbol(last_command_status=FAIL)) == str(colors.danger('❯'))
    assert str(prompt.prompt_symbol(last_command_status=FAIL)) == '\x1b[38;2;205;0;0m❯\x1b[39m'


def test_prompt_layout():
    assert prompt.layout() == "\n{current_working_path} {git_active_branch}{git_is_dirty}\n{virtual_env}{prompt_symbol} "

