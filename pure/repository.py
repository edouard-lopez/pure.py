import git

from pure import colors


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
        except AttributeError:
            return ''

    def segment(self):
        return {
            'text': self.raw(),
            'style': colors.mute
        }


class IsDirty(object):
    repo = None

    def __init__(self, directory):
        try:
            self.repo = git.Repo(directory)
        except Exception:
            self.repo = {}

    def raw(self):
        return '*' if self.repo.is_dirty(untracked_files=True) else ''

    def segment(self):
        return {
            'text': self.raw(),
            'style': colors.mute
        }
