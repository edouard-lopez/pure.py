import os

from pure import colors


def name():
    if 'VIRTUAL_ENV' in os.environ:
        virtual_env_name = os.path.basename(os.environ['VIRTUAL_ENV'])
        return colors.mute('{} '.format(virtual_env_name))
    return ''
