import tempfile

import git
import colorful

from pure import colors, repository, constants
from pure.prompt import fetch


def test_dummy_directory_has_no_branch_name():
    with tempfile.TemporaryDirectory() as tmp_repo:
        assert repository.ActiveBranch(tmp_repo).raw() == constants.NOTHING


def test_repository_active_branch_contains_raw_git_branch_name():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo, initial_branch='main')
        
        assert repository.ActiveBranch(tmp_repo).raw() == 'main'


def test_repository_active_branch_segment_contains_text_and_style():
    colors.Theme()

    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo, initial_branch='main')
        segment = repository.ActiveBranch(tmp_repo).segment()
        
        assert segment == {'text': 'main', 'style': colors.Theme().style('mute')}


def test_repository_active_branch_name_color_is_mute():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo, initial_branch='main')
        segment = repository.ActiveBranch(tmp_repo).segment()
        
        assert fetch(segment) in colorful.mute('main').styled_string


def test_dummy_directory_is_not_dirty():
    with tempfile.TemporaryDirectory() as tmp_repo:
        assert repository.IsDirty(tmp_repo).raw() == constants.NOTHING


def test_repository_is_dirty_contains_raw_symbol():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo, initial_branch='main')
        new_file = tempfile.NamedTemporaryFile(dir=tmp_repo)

        assert repository.IsDirty(tmp_repo).raw() == '*'

        new_file.close()


def test_repository_is_dirty_segment_contains_text_and_style():
    colors.Theme()

    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo, initial_branch='main')
        new_file = tempfile.NamedTemporaryFile(dir=tmp_repo)

        segment = repository.IsDirty(tmp_repo).segment()
        assert segment == {'text': '*', 'style': colors.Theme().style('mute')}

        new_file.close()


def test_repository_dirty_symbol_color_is_mute():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)
        new_file = tempfile.NamedTemporaryFile(dir=tmp_repo)

        segment = repository.IsDirty(tmp_repo).segment()

        assert fetch(segment) in colorful.mute('*').styled_string
        new_file.close()

import os


def test_repository_active_branch_in_subfolder():
    with tempfile.TemporaryDirectory() as tmp_repo:
        repo = git.Repo.init(tmp_repo, initial_branch="main")
        sub = os.path.join(tmp_repo, "sub", "folder")
        os.makedirs(sub)
        try:
            assert repository.ActiveBranch(sub).raw() == "main"
        finally:
            repo.close()


def test_repository_active_branch_detached_head():
    with tempfile.TemporaryDirectory() as tmp_repo:
        repo = git.Repo.init(tmp_repo, initial_branch="main")
        f = os.path.join(tmp_repo, "file.txt")
        with open(f, "w") as fh:
            fh.write("hello")
        repo.index.add(["file.txt"])
        commit = repo.index.commit("initial commit")
        repo.head.reference = commit
        repo.head.reset(index=True, working_tree=True)
        try:
            raw = repository.ActiveBranch(tmp_repo).raw()
            assert raw != constants.NOTHING
            assert len(raw) > 0
        finally:
            repo.close()


def test_repository_is_dirty_in_subfolder():
    with tempfile.TemporaryDirectory() as tmp_repo:
        repo = git.Repo.init(tmp_repo, initial_branch="main")
        sub = os.path.join(tmp_repo, "sub", "folder")
        os.makedirs(sub)
        new_file = os.path.join(tmp_repo, "untracked.txt")
        with open(new_file, "w") as fh:
            fh.write("dirty")
        try:
            assert repository.IsDirty(sub).raw() == "*"
        finally:
            repo.close()
