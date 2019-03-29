import os
import json
from pathlib import Path

import colorful

def load_theme():
    try:
        theme_name = os.environ['PURE_THEME']
    except KeyError: 
        theme_name = 'tomorrow'
    finally:
        with open(Path('./pure/theme/' + theme_name + '.json'), 'r') as theme:
            scheme = json.load(theme)

    colorful.use_true_colors()
    colorful.use_palette(scheme)
    
    return theme_name, scheme

def style(color):
    return getattr(colorful, color).style[0]