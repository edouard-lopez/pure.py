import tempfile

import git
import colorful

from pure import colors, repository, constants
from pure.prompt import fetch


def test_dummy_directory_has_no_pending_commits():
    with tempfile.TemporaryDirectory() as repo:
        assert repository.PendingCommit(repo).raw() == constants.NOTHING


def setup_repo(func):                                                                                            
    def wrapper():                                                                                            
        with tempfile.TemporaryDirectory() as remote_directory:
            remote_repo = git.Repo.init(remote_directory, bare=True)

            with tempfile.TemporaryDirectory() as repo_directory:
                repo = remote_repo.clone(repo_directory)
                with tempfile.NamedTemporaryFile(dir=repo.working_dir) as file:
                    repo.index.add([file.name])
                    repo.index.commit("init file")
                    repo.remotes.origin.push()
                    func(repo, remote_repo)
    return wrapper 

@setup_repo
def test_repository_pending_PUSH_commit_contains_raw_symbol(repo, remote_repo):
    with tempfile.NamedTemporaryFile(dir=repo.working_dir) as file_missing_upstream:
        repo.index.add([file_missing_upstream.name])
        repo.index.commit("file yet to be PUSHED")

    assert repository.PendingCommit(repo.working_dir).raw() == '⇡'


@setup_repo
def test_repository_pending_PULL_commit_contains_raw_symbol(repo, remote_repo):
    with tempfile.NamedTemporaryFile(dir=repo.working_dir) as file_missing_locally:
        repo.index.add([file_missing_locally.name])
        commit = repo.index.commit("file yet to be PULLED")

    repo.remotes.origin.push()
    branch = repo.active_branch
    repo.head.reset(commit='HEAD~1', index=True, working_tree=True)
    assert repository.PendingCommit(repo.working_dir).raw() == '⇣'
