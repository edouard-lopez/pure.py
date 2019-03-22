import os

from pure import colors
from pure.config import _NOTHING


def raw():
    if 'VIRTUAL_ENV' in os.environ:
        return os.path.basename(os.environ['VIRTUAL_ENV'])
    return _NOTHING


def segment():
    return {
        'text': raw(),
        'style': colors.mute
    }
