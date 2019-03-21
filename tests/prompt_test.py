from pure import prompt


def test_prompt_layout():
    assert prompt.layout() == "\n{current_working_path} {git_active_branch}{git_is_dirty}\n{virtual_env}{prompt_symbol} "


def test_get_styled_text():
    segment = {
        'text': 'foo',
        'style': lambda text: '['+text+']'
    }

    assert prompt.fetch(segment) == '[foo]'
