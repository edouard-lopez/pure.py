import tempfile

import git
import colorful

from pure import colors, repository, constants
from pure.prompt import fetch


def test_dummy_directory_is_not_dirty():
    with tempfile.TemporaryDirectory() as tmp_repo:
        assert repository.IsDirty(tmp_repo).raw() == constants.NOTHING


def test_repository_is_dirty_contains_raw_symbol():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)
        new_file = tempfile.NamedTemporaryFile(dir=tmp_repo)

        assert repository.IsDirty(tmp_repo).raw() == '*'

        new_file.close()


def test_repository_is_dirty_segment_contains_text_and_style():
    colors.load_theme()

    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)
        new_file = tempfile.NamedTemporaryFile(dir=tmp_repo)

        segment = repository.IsDirty(tmp_repo).segment()
        assert segment == {'text': '*', 'style': colors.style('mute')}

        new_file.close()


def test_repository_dirty_symbol_color_is_mute():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)
        new_file = tempfile.NamedTemporaryFile(dir=tmp_repo)

        segment = repository.IsDirty(tmp_repo).segment()

        assert fetch(segment) in colorful.mute('*').styled_string
        new_file.close()
