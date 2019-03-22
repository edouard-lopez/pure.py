import os

from pure import colors
from pure import constants


def raw():
    if 'VIRTUAL_ENV' in os.environ:
        return os.path.basename(os.environ['VIRTUAL_ENV'])
    return constants.NOTHING


def segment():
    return {
        'text': raw(),
        'style': colors.mute
    }
