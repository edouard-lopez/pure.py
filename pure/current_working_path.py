import os

from pure import colors


def current_working_path():
    return colors.info(os.getcwd())
