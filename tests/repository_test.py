import os
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


def test_repository_active_branch_in_subfolder():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo, initial_branch="main")
        sub_directory = os.path.join(tmp_repo, "sub", "directory")
        os.makedirs(sub_directory)
        try:
            assert repository.ActiveBranch(sub_directory).raw() == "main"
        finally:
            empty_repo.close()


def test_repository_active_branch_detached_head():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo, initial_branch="main")
        new_file = os.path.join(tmp_repo, "file.txt")
        with open(new_file, "w") as file_handler:
            file_handler.write("hello")
        empty_repo.index.add(["file.txt"])
        commit = empty_repo.index.commit("initial commit")
        empty_repo.head.reference = commit
        empty_repo.head.reset(index=True, working_tree=True)
        try:
            raw = repository.ActiveBranch(tmp_repo).raw()
            assert raw != constants.NOTHING
            assert len(raw) > 0
        finally:
            empty_repo.close()


def test_repository_is_dirty_in_subfolder():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo, initial_branch="main")
        sub_directory = os.path.join(tmp_repo, "sub", "directory")
        os.makedirs(sub_directory)
        new_file = os.path.join(tmp_repo, "untracked.txt")
        with open(new_file, "w") as file_handler:
            file_handler.write("dirty")
        try:
            assert repository.IsDirty(sub_directory).raw() == "*"
        finally:
            empty_repo.close()
