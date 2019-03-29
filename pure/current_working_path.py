import os

from pure import colors


def raw():
    return os.getcwd()


def segment():
    return {
        'text': raw(),
        'style': colors.style('info')
    }
