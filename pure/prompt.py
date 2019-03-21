import argparse
import os

from pure import colors, repository

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




def layout():
    return "\n{current_working_path} {git_active_branch}{git_is_dirty}\n{virtual_env}{prompt_symbol} "


def prompt(args):
    data = {
        'current_working_path': current_working_path(), 
        'git_active_branch': repository.active_branch(os.getcwd()),
        'git_is_dirty': repository.is_dirty(os.getcwd()),
        'virtual_env': virtual_env(), 
        'prompt_symbol': prompt_symbol(args.last_command_status)
    }
    print(layout().format(**data), end='')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process shell variables.')
    parser.add_argument('--last-command-status', dest='last_command_status', type=int, help='last command\'s exit status')

    prompt(parser.parse_args())
