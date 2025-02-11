import sys
import os

from subprocess import Popen
from pathlib import Path

# enables importing from parent directories
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from base_classes.window_manager.base import WindowManager
from base_classes.menu.base import Menu
from base_classes.program_color.base import ProgramColor

from helpers.colorscheme import matugen_gen_color
from helpers.reload_function import reload_dwm, reload_kitty, reload_konsole


class Hyprland(WindowManager):
    manage_programs: dict[str, ProgramColor]

    def __init__(
        self,
        menu: Menu,
        wallpaper_dict: dict,
        colorscheme_dict: dict,
    ) -> None:
        # programs with universally defined location
        # ------------------------------------------
        btop = ProgramColor(
            file="~/.config/btop/btop.conf",
            start_concat='color_theme = "',
            end_concat='"',
            colorscheme_map={
                "catppuccin_macchiato": "catppuccin_macchiato",
                "dracula": "dracula",
                "everblush": "everblush",
                "everforest": "everforest",
                "gruvbox": "gruvbox",
                "matugen": "Default",
                "nord": "nord",
                "rose_pine": "rose_pine",
            },
        )
        fuzzel = ProgramColor(
            file="~/.config/fuzzel/fuzzel.ini",
            start_concat="include=~/.config/fuzzel/colors/",
            end_concat=".ini",
        )
        gtk = ProgramColor(
            file="~/.config/gtk-3.0/settings.ini",
            start_concat="gtk-theme-name=",
            end_concat="",
            colorscheme_map={
                "catppuccin_macchiato": "catppuccin_macchiato",
                "dracula": "dracula",
                "everblush": "everblush",
                "everforest": "everforest",
                "gruvbox": "gruvbox",
                "matugen": "adw-gtk3",
                "nord": "nord",
                "rose_pine": "rose_pine",
            },
        )
        helix = ProgramColor(
            file="~/.config/helix/config.toml",
            start_concat='theme = "',
            end_concat='"',
        )
        kitty = ProgramColor(
            file="~/.config/kitty/kitty.conf",
            start_concat="include ~/.config/kitty/colorschemes/",
            end_concat=".conf",
        )
        konsole = ProgramColor(
            file="~/.local/share/konsole/main.profile",
            start_concat="ColorScheme=",
            end_concat="",
        )
        zathura = ProgramColor(
            file="~/.config/zathura/zathurarc",
            start_concat="include colorschemes/",
            end_concat="",
            colorscheme_map={
                "catppuccin_macchiato": "catppuccin_macchiato",
                "dracula": "dracula",
                "everblush": "everblush",
                "everforest": "everforest",
                "gruvbox": "gruvbox",
                "matugen": "matugen",
                "nord": "nord",
                "rose_pine": "rose_pine",
            },
        )

        # programs with user defined location
        # -----------------------------------
        hyprland = ProgramColor(
            file="~/.config/hypr/external_configs/ags/user_options.json",
            start_concat='  "colorscheme": "',
            end_concat='"',
        )
        nvim = ProgramColor(
            file="~/.config/nvim/lua/core/colorscheme.lua",
            start_concat='local color = "',
            end_concat='"',
            colorscheme_map={
                "catppuccin_macchiato": "base16-catppuccin-macchiato",
                "dracula": "base16-dracula",
                "everblush": "everblush",
                "everforest": "base16-everforest",
                "gruvbox": "base16-gruvbox-dark-medium",
                "matugen": "matugen",
                "nord": "base16-nord",
                "rose_pine": "base16-rose-pine",
            },
        )

        manage_programs = {
            "btop": btop,
            "fuzzel": fuzzel,
            "gtk": gtk,
            "helix": helix,
            "hyprland": hyprland,
            "kitty": kitty,
            "konsole": konsole,
            "nvim": nvim,
            "zathura": zathura,
        }

        self.manage_programs = manage_programs

        super().__init__(menu, wallpaper_dict, colorscheme_dict)

    # ------------------------------------
    # functions for hot reloading programs
    # ------------------------------------

    # -----------------------------------
    # functions for applying stuffs
    # -----------------------------------

    # for applying wallpaper
    # ----------------------
    def apply_desktop_wallpaper(
        self,
        wallpaper: str,
    ) -> None:
        command = [
            f"{Path('~/.config/hypr/scripts/change_wallpaper.py').expanduser()}",
            "--wallpaper",
            wallpaper,
        ]

        Popen(command, start_new_session=True)

    def apply_lockscreen_wallpaper(
        self,
        wallpaper: str,
    ) -> None:
        lock_wall = ProgramColor(
            file="~/.config/hypr/hyprlock.conf",
            start_concat="$lockscreen_wall = ",
            end_concat="",
        )
        wallpaper_path = "~/.config/wallpaper/" + wallpaper

        lock_wall.apply(wallpaper_path)

    # for applying colorscheme
    # ------------------------
    def apply_gtk_theme_wayland(self, colorscheme: str):
        gtk_colorscheme_map = {
            "catppuccin_macchiato": "catppuccin_macchiato",
            "dracula": "dracula",
            "everblush": "everblush",
            "everforest": "everforest",
            "gruvbox": "gruvbox",
            "matugen": "adw-gtk3",
            "nord": "nord",
            "rose_pine": "rose_pine",
        }

        command = [
            "gsettings",
            "set",
            "org.gnome.desktop.interface",
            "gtk-theme",
            gtk_colorscheme_map[colorscheme],
        ]

        Popen(command, start_new_session=True)

    def apply(
        self,
        choose_wallpaper=False,
    ):
        allowed_programs = {
            "matugen": [
                "btop",
                "fuzzel",
                "gtk",
                "hyprland",
                "luastatus",
                "kitty",
                "konsole",
                "nvim",
                "zathura",
            ],
        }

        apply_wallpaper_functions = [
            self.apply_desktop_wallpaper,
            self.apply_lockscreen_wallpaper,
        ]

        reload_programs = {
            self.apply_gtk_theme_wayland: {"replace": ["colorscheme"], "params": []},
            reload_dwm: {},
            reload_kitty: {},
            reload_konsole: {"replace": ["colorscheme"], "params": ["main"]},
        }

        self._apply(
            matugen_gen_color,
            self.manage_programs,
            reload_programs,
            choose_wallpaper,
            apply_wallpaper_functions,
            allowed_programs,
        )
