from pure import prompt, constants, symbol


def test_prompt_layout():
    assert prompt.layout() == "\n{current_working_path} {git_active_branch}{git_is_dirty}\n{virtual_env}{prompt_symbol} "


def test_get_styled_text():
    segment = {
        'text': 'foo',
        'style': lambda text: '[' + text + ']'
    }

    assert prompt.fetch(segment) == '[foo]'


def test_prompt_symbol_is_colored_for_successful_command():
    prompt_symbol = prompt.fetch(symbol.segment(constants.SUCCESS))
    assert str(prompt_symbol) == '\x1b[38;2;155;48;255m❯\x1b[39m'


def test_prompt_symbol_is_colored_for_failed_command():
    prompt_symbol = prompt.fetch(symbol.segment(constants.FAIL))
    assert str(prompt_symbol) == '\x1b[38;2;205;0;0m❯\x1b[39m'
