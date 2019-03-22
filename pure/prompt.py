import argparse
import os

from pure import current_working_path, repository, symbol, virtual_env


def layout():
    return "\n{current_working_path} {git_active_branch}{git_is_dirty}\n{virtual_env}{prompt_symbol} "


def prompt(args):
    data = {
        'current_working_path': fetch(current_working_path.segment()),
        'git_active_branch': fetch(repository.ActiveBranch(os.getcwd()).segment()),
        'git_is_dirty': fetch(repository.IsDirty(os.getcwd()).segment()),
        'virtual_env': fetch(virtual_env.segment()),
        'prompt_symbol': symbol.prompt(args.last_command_status)
    }
    print(layout().format(**data), end='')


def fetch(segment):
    return segment.get('style')(segment.get('text'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process shell variables.')
    parser.add_argument('--last-command-status', dest='last_command_status', type=int,
                        help='last command\'s exit status')

    prompt(parser.parse_args())
