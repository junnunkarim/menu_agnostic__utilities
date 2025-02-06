#!/usr/bin/env python

import sys
import os
import json

from sys import argv
from argparse import ArgumentParser
from pathlib import Path

# enables importing from parent directories
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from menus.dmenu import Dmenu
from menus.fuzzel import Fuzzel

from window_managers.dwm import Dwm
from window_managers.hyprland import Hyprland


def apply_colorscheme(menu: str, wm: str) -> None:
    with open(
        Path(f"~/.config/menu_agnostic__utilities/{wm}/wallpapers.json").expanduser()
    ) as file:
        wallpaper_dict = json.load(file)

    colorschemes: dict[str, str] = {
        "[cancel]": "[  Cancel ]",
        "catppuccin_macchiato": " Catppuccin (Macchiato)",
        "dracula": " Dracula",
        "everblush": " Everblush",
        "everforest": " Everforest",
        "gruvbox": " Gruvbox",
        "matugen": " Matugen (Material-You Color Generator)",
        "nord": " Nord",
        "rose_pine": " Rose Pine",
    }

    if menu == "dmenu":
        menu_obj = Dmenu(
            width=600,
            line=len(colorschemes),
        )
    elif menu == "fuzzel":
        menu_obj = Fuzzel(
            width=50,
            line=10,
        )
    else:
        sys.exit(f"Menu - '{menu}' is not recognized!\n")

    if wm == "dwm":
        wm_obj = Dwm(
            menu=menu_obj,
            wallpaper_dict=wallpaper_dict,
            colorscheme_dict=colorschemes,
        )
    elif wm == "hyprland":
        wm_obj = Hyprland(
            menu=menu_obj,
            wallpaper_dict=wallpaper_dict,
            colorscheme_dict=colorschemes,
        )

    else:
        sys.exit(f"Window manager - '{wm}' is not recognized!\n")

    wm_obj.apply(choose_wallpaper=True)


def main():
    wms = ["dwm", "hyprland"]
    menus = ["dmenu", "fuzzel"]

    arg_parser = ArgumentParser(description="change colorscheme")
    # define necessary cli arguments
    arg_parser.add_argument(
        "-m",
        "--menu",
        help="specify the menu launcher",
        choices=menus,
        required=True,
    )
    arg_parser.add_argument(
        "-w",
        "--window-manager",
        help="specify the window manager",
        choices=wms,
        required=True,
    )

    # if no cli arguments are provided, show the help message and exit
    if len(argv) <= 1:
        arg_parser.print_help()
        sys.exit()

    # parse all cli arguments
    args = arg_parser.parse_args()

    # 'window-manager' is accessed by 'window_manager'
    if args.menu and args.window_manager:
        apply_colorscheme(menu=args.menu, wm=args.window_manager)
    else:
        arg_parser.print_help()
        sys.exit()


if __name__ == "__main__":
    main()
