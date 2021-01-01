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
                repo = git.Repo.init(repo_directory)
                func(repo, remote_repo)
    return wrapper 

@setup_repo
def test_repository_pending_PUSH_commit_contains_raw_symbol(repo, remote_repo):
    origin = repo.create_remote('origin', url=remote_repo.working_dir)
    with tempfile.NamedTemporaryFile(dir=repo.working_dir) as file:
        repo.index.add([file.name])
        repo.index.commit("init file")
    origin.push()

    with tempfile.NamedTemporaryFile(dir=repo.working_dir) as file_missing_upstream:
        repo.index.add([file_missing_upstream.name])
        repo.index.commit("file yet to be pushed")

    assert repository.PendingCommit(repo.working_dir).raw() == '⇡'
