import argparse
import os

import git

from pure import colors

SUCCESS = 0


def prompt_symbol(last_command_status=SUCCESS):
    symbol = colors.primary('❯') if last_command_status == SUCCESS else colors.danger('❯')
    return symbol


def current_working_path():
    return colors.info(os.getcwd()) 


def virtual_env():
    if 'VIRTUAL_ENV' in os.environ:
        virtual_env_name = os.path.basename(os.environ['VIRTUAL_ENV'])
        return colors.mute('{} '.format(virtual_env_name))
    return ''


def git_active_branch(directory):
    try:
        repo = git.Repo(directory)
        return colors.mute(str(repo.active_branch))
    except Exception:
        return ''


def git_is_dirty(directory):
    try:
        repo = git.Repo(directory)
        return colors.mute('*') if repo.is_dirty(untracked_files=True) else ''
    except Exception:
        return ''


def layout():
    return "\n{current_working_path} {git_active_branch}{git_is_dirty}\n{virtual_env}{prompt_symbol} "


def prompt(args):
    data = {
        'current_working_path': current_working_path(), 
        'git_active_branch': git_active_branch(os.getcwd()), 
        'git_is_dirty': git_is_dirty(os.getcwd()), 
        'virtual_env': virtual_env(), 
        'prompt_symbol': prompt_symbol(args.last_command_status)
    }
    print(layout().format(**data))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process shell variables.')
    parser.add_argument('last_command_status', type=int, help='last command\'s exit status', default=SUCCESS)

    prompt(parser.parse_args())
