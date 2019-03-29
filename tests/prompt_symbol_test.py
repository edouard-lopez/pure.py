from pure import prompt_symbol, colors, constants


def test_prompt_symbol_raw_contains_prompt_symbol():
    assert '❯' in prompt_symbol.raw()


def test_prompt_symbol_segment_contains_text_and_style():
    colors.load_theme()
    segment = prompt_symbol.segment()

    assert segment == {'text': '❯', 'style': colors.style('primary')}


def test_prompt_symbol_style_is_primary_color_when_last_command_succeed():
    assert prompt_symbol.style(last_command_status=constants.SUCCESS) == colors.style('primary')


def test_prompt_symbol_segment_contains_text_and_primary_color_when_last_command_succeed():
    colors.load_theme()
    segment = prompt_symbol.segment(last_command_status=constants.SUCCESS)

    assert segment == {'text': '❯', 'style': colors.style('primary')}


def test_prompt_symbol_style_is_danger_color_when_last_command_failed():
    assert prompt_symbol.style(last_command_status=constants.FAIL) == colors.style('danger')


def test_prompt_symbol_segment_contains_text_and_danger_color_when_last_command_failed():
    colors.load_theme()
    segment = prompt_symbol.segment(last_command_status=constants.FAIL)

    assert segment == {'text': '❯', 'style': colors.style('danger')}