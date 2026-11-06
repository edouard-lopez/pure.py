import git

from pure import colors, constants


class ActiveBranch:
    repo = None

    def __init__(self, directory):
        try:
            self.repo = git.Repo(directory, search_parent_directories=True)
        except (git.InvalidGitRepositoryError, git.NoSuchPathError):
            self.repo = None
        except Exception:
            self.repo = None

    def raw(self):
        if not self.repo:
            return constants.NOTHING
        try:
            return str(self.repo.active_branch)
        except TypeError:
            try:
                name = self.repo.git.name_rev('--name-only', 'HEAD')
                return str(name).strip()
            except Exception:
                return constants.NOTHING
        except Exception:
            return constants.NOTHING

    def segment(self):
        return {
            'text': self.raw(),
            'style': colors.Theme().style('mute')
        }


class IsDirty(object):
    repo = None

    def __init__(self, directory):
        try:
            self.repo = git.Repo(directory, search_parent_directories=True)
        except (git.InvalidGitRepositoryError, git.NoSuchPathError):
            self.repo = None
        except Exception:
            self.repo = None

    def raw(self):
        if self.repo and hasattr(self.repo, 'is_dirty'):
            try:
                return '*' if self.repo.is_dirty(untracked_files=True) else constants.NOTHING
            except Exception:
                return constants.NOTHING
        return constants.NOTHING

    def segment(self):
        return {
            'text': self.raw(),
            'style': colors.Theme().style('mute')
        }
