import tempfile

import git

from pure import colors, repository


def test_contains_git_branch_name():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)

        assert 'master' in str(repository.active_branch(tmp_repo))


def test_git_branch_name_color_is_mute():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)

        assert str(repository.active_branch(tmp_repo)) == str(colors.mute('master'))


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
