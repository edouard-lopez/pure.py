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
        empty_repo = git.Repo.init(tmp_repo)
        
        assert repository.ActiveBranch(tmp_repo).raw() == 'master'


def test_repository_active_branch_segment_contains_text_and_style():
    colors.load_theme()

    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)
        segment = repository.ActiveBranch(tmp_repo).segment()
        
        assert segment == {'text': 'master', 'style': colors.style('mute')}


def test_repository_active_branch_name_color_is_mute():
    with tempfile.TemporaryDirectory() as tmp_repo:
        empty_repo = git.Repo.init(tmp_repo)
        segment = repository.ActiveBranch(tmp_repo).segment()
        
        assert fetch(segment) in colorful.mute('master').styled_string
