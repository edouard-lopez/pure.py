from pure.prompt import prompt


def test_prompt_contains_symbol():
    assert '❯' in prompt()
