import argparse
import os

from pure import colors

SUCCESS = 0


def prompt_symbol(last_command_status=SUCCESS):
    symbol = colors.primary('❯') if last_command_status == SUCCESS else colors.danger('❯')
    return symbol


def current_working_path():
    return colors.mute(os.getcwd())


def virtual_env():
    if 'VIRTUAL_ENV' in os.environ:
        virtual_env_name = os.path.basename(os.environ['VIRTUAL_ENV'])
        return colors.mute('{} '.format(virtual_env_name))
    return ''


def layout():
    return "\n%s\n%s%s "


def prompt(args):
    print(layout() % (current_working_path(), virtual_env(), prompt_symbol(args.last_command_status)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process shell variables.')
    parser.add_argument('last_command_status', type=int, help='last command\'s exit status')

    prompt(parser.parse_args())
