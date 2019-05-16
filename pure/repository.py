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
