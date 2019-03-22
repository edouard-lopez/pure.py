import argparse
import os

from pure import repository, virtual_env, current_working_path, symbol


def layout():
    return "\n{current_working_path} {git_active_branch}{git_is_dirty}\n{virtual_env}{prompt_symbol} "


def prompt(args):
    data = {
        'current_working_path': fetch(current_working_path.segment()),
        'git_active_branch': fetch(repository.ActiveBranch(os.getcwd()).segment()),
        'git_is_dirty': repository.is_dirty(os.getcwd()),
        'virtual_env': virtual_env.name(),
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
