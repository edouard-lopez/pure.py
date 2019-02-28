def prompt():
    return '❯'
import os
def current_working_path():
    return os.getcwd()


if __name__ == "__main__":
    print("%s\n%s " % (current_working_path(), prompt()))
