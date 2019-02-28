import argparse
import os
def prompt(last_command_status=0):
    symbol = '❯' if last_command_status == 0 else 'x❯'
    return symbol


def current_working_path():
    return os.getcwd()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process shell variables.')
    parser.add_argument('last_command_status', type=int, help='last command\'s exit status')
    args = parser.parse_args()

    print("%s\n%s " % (current_working_path(), prompt(args.last_command_status)))
