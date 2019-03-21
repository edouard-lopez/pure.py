import git

from pure import colors


def active_branch(directory):
    try:
        repo = git.Repo(directory)
        return colors.mute(str(repo.active_branch))
    except Exception:
        return ''


def is_dirty(directory):
    try:
        repo = git.Repo(directory)
        return colors.mute('*') if repo.is_dirty(untracked_files=True) else ''
    except Exception:
        return ''
