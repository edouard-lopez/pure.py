import argparse
import os

import colorful


def prompt_symbol(last_command_status=0):
    print(colorful.red('last_command_status'), last_command_status)
    symbol = '❯' if last_command_status == 0 else 'x❯'
    return symbol


def current_working_path():
    return os.getcwd()


def virtual_env():
    if 'VIRTUAL_ENV' in os.environ:
        return os.path.basename(os.environ['VIRTUAL_ENV'])
    return ''


def prompt(args):
    colorful.use_true_colors()
    print("%s\n%s%s " % (current_working_path(), virtual_env(), prompt_symbol(args.last_command_status)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process shell variables.')
    parser.add_argument('last_command_status', type=int, help='last command\'s exit status')

    prompt(parser.parse_args())
