import git

from pure import colors, constants


class ActiveBranch:
    repo = None

    def __init__(self, directory):
        try:
            self.repo = git.Repo(directory)
        except Exception:
            self.repo = {}

    def raw(self):
        try:
            return str(self.repo.active_branch)
        except:
            return constants.NOTHING

    def segment(self):
        return {
            'text': self.raw(),
            'style': colors.style('mute')
        }


class IsDirty(object):
    repo = None

    def __init__(self, directory):
        try:
            self.repo = git.Repo(directory)
        except Exception:
            self.repo = {}

    def raw(self):
        if hasattr(self.repo, 'is_dirty'):
            return '*' if self.repo.is_dirty(untracked_files=True) else constants.NOTHING
        else:
            return constants.NOTHING

    def segment(self):
        return {
            'text': self.raw(),
            'style': colors.style('mute')
        }

class PendingCommit(object):
    repo = None

    def __init__(self, directory):
        try:
            self.repo = git.Repo(directory)
        except Exception:
            self.repo = {}

    def raw(self):
        if hasattr(self.repo, 'iter_commits'):
            branch = self.repo.active_branch
            unpushed_symbol = '⇡' if list(self.repo.iter_commits(f'{branch}@{{u}}..{branch}')) else constants.NOTHING
            unpulled_symbol = '⇣' if list(self.repo.iter_commits(f'{branch}..{branch}@{{u}}')) else constants.NOTHING
            return f'{unpulled_symbol}{unpushed_symbol}'
        else:
            return constants.NOTHING

