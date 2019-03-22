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


def is_dirty(directory):
    try:
        repo = git.Repo(directory)
        return colors.mute('*') if repo.is_dirty(untracked_files=True) else ''
    except Exception:
        return ''
