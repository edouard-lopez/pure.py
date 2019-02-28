import argparse
import os
def prompt(last_command_status=0):
    symbol = '❯' if last_command_status == 0 else 'x❯'
    return symbol


def current_working_path():
    return os.getcwd()


def virtual_env():
    if 'VIRTUAL_ENV' in os.environ:
        return os.path.basename(os.environ['VIRTUAL_ENV'])
    return ''


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process shell variables.')
    parser.add_argument('last_command_status', type=int, help='last command\'s exit status')
    args = parser.parse_args()

    print("%s\n%s%s " % (current_working_path(), virtual_env(), prompt(args.last_command_status)))
