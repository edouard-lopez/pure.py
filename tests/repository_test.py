import tempfile

import git

from pure import colors, repository
from pure.prompt import fetch


def test_dummy_repository_has_no_branch_name():
    with tempfile.TemporaryDirectory() as tmp_repo:
        assert '' == repository.ActiveBranch(tmp_repo).raw()


def test_active_branch_contains_raw_git_branch_name():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)

        assert 'master' == repository.ActiveBranch(tmp_repo).raw()


def test_active_branch_segment_contains_text_and_style():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)

        segment = repository.ActiveBranch(tmp_repo).segment()

        assert segment == {'text': 'master', 'style': colors.mute}


def test_git_branch_name_color_is_mute():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)

        assert str(fetch(repository.ActiveBranch(tmp_repo).segment())) == str(colors.mute('master'))




def test_displays_when_repo_is_dirty():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)
        new_file = tempfile.NamedTemporaryFile(dir=tmp_repo)

        assert '*' in str(repository.is_dirty(tmp_repo))
        new_file.close()


def test_repo_is_dirty_color_is_mute():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)
        new_file = tempfile.NamedTemporaryFile(dir=tmp_repo)

        assert str(repository.is_dirty(tmp_repo)) == str(colors.mute('*'))

        new_file.close()
