from pure import symbol, colors

SUCCESS = 0
FAIL = 1


def test_contains_prompt_symbol():
    assert '❯' in symbol.prompt()


def test_prompt_symbol_is_colored_for_successful_command():
    assert str(symbol.prompt()) == str(colors.primary('❯'))
    assert str(symbol.prompt()) == '\x1b[38;2;155;48;255m❯\x1b[39m'


def test_change_prompt_when_last_command_fail():
    assert '❯' in symbol.prompt(last_command_status=SUCCESS)
    assert '❯' in symbol.prompt(last_command_status=FAIL)


def test_prompt_symbol_is_colored_for_failed_command():
    assert str(symbol.prompt(last_command_status=FAIL)) == str(colors.danger('❯'))
    assert str(symbol.prompt(last_command_status=FAIL)) == '\x1b[38;2;205;0;0m❯\x1b[39m'
