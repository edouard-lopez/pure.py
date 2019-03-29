import colorful

from pure import prompt, prompt_symbol, constants, colors

def test_default_prompt_layout_is_correct():
    assert prompt.layout() == "\n{current_working_path} {git_active_branch}{git_is_dirty}\n{virtual_env}{prompt_symbol} "


def test_get_styled_text():
    segment = {
        'text': 'foo',
        'style': 'ansi_code:'
    }

    assert prompt.fetch(segment) == 'ansi_code:foo'


def test_prompt_symbol_is_colored_for_successful_command():
    colors.load_theme()
    
    symbol = prompt.fetch(prompt_symbol.segment(constants.SUCCESS))

    assert symbol in colorful.primary('❯').styled_string


def test_prompt_symbol_is_colored_for_failed_command():
    colors.load_theme()

    symbol = prompt.fetch(prompt_symbol.segment(constants.FAIL))

    assert symbol in colorful.danger('❯').styled_string


def test_prompt_return_json_with_segment():
    class CommandArguments(object):
        last_command_status = constants.SUCCESS
        json = True

    json = prompt.prompt(args=CommandArguments)

    assert list(json.keys()) == [
                                    'current_working_path',
                                    'git_active_branch',
                                    'git_is_dirty',
                                    'virtual_env',
                                    'prompt_symbol'
                                ]


def test_prompt_print_layout(capfd):
    class CommandArguments(object):
        last_command_status = constants.SUCCESS
        json = False

    prompt.prompt(args=CommandArguments)
    stdout, stderr = capfd.readouterr()
    
    assert '❯' in stdout