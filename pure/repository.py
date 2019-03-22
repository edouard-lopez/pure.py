import git

from pure import colors

_NOTHING = ''


class ActiveBranch:
    repo = None

    def __init__(self, directory):
        try:
            self.repo = git.Repo(directory)
        except Exception:
            self.repo = {}

    def raw(self):
        if hasattr(self.repo, 'active_branch'):
            return str(self.repo.active_branch)
        else:
            return _NOTHING

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
        if hasattr(self.repo, 'is_dirty'):
            return '*' if self.repo.is_dirty(untracked_files=True) else _NOTHING
        else:
            return _NOTHING

    def segment(self):
        return {
            'text': self.raw(),
            'style': colors.mute
        }
