import os

from pure import constants, colors


def raw():
    if 'VIRTUAL_ENV' in os.environ:
        return os.path.basename(os.environ['VIRTUAL_ENV'])
    return constants.NOTHING


def segment():
    return {
        'text': raw(),
        'style': colors.Theme().style('mute')
    }
