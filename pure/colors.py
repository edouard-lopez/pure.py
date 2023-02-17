from genericpath import isfile
import os
import json
from pathlib import Path
import platformdirs
import colorful


class Theme(object):
    default_theme_name = "ayu-light"
    default_theme_scheme = {
        "primary": "#8959a8",
        "info": "#4271ae",
        "mute": "#969896",
        "success": "#718c00",
        "normal": "#e0e0e0",
        "danger": "#c82829",
        "light": "#1d1f21",
        "warning": "#eab700",
        "dark": "#d6d6d6",
    }
    file_extension = "json"
    name = None
    scheme = {}

    def __init__(self, autoload=True):
        if autoload == True:
            self.name, self.scheme = self.load_theme()

    def load_theme(self):
        if "PURE_THEME" in os.environ:
            self.name = os.environ["PURE_THEME"]
        else:
            os.environ["PURE_THEME"] = self.default_theme_name
            self.name = self.default_theme_name

        theme_filepath = self.get_theme_filepath(self.name)

        if not os.path.isfile(theme_filepath):
            theme_filepath.parent.mkdir(parents=True, exist_ok=True);
            with open(str(theme_filepath), "w", encoding="utf-8") as theme:
                json.dump(
                    self.default_theme_scheme, theme, ensure_ascii=False, indent=4
                )

        with open(str(theme_filepath), "r") as theme:
            self.scheme = json.load(theme)

        colorful.use_true_colors()
        colorful.use_palette(self.scheme)

        return self.name, self.scheme

    def get_default_theme(self, filepath=False):
        if filepath == True:
            return self.get_theme_filepath(self.default_theme_name)

        return self.default_theme_name

    def get_theme_filepath(self, theme_name=None):
        user_config_dir = platformdirs.user_config_dir(appname="pure")
        default_theme_path = Path(
            user_config_dir + "/theme/" + theme_name + ".json"
        )

        return default_theme_path

    def get_active_theme(self):
        self.load_theme()

        return os.environ["PURE_THEME"]

    def style(self, color):
        return getattr(colorful, color).style[0]
