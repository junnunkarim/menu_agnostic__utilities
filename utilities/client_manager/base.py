#!/usr/bin/env python

import os
import sys
import argparse
import pathlib

# enables importing from parent directories
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


from class__main.menus.dmenu import Dmenu
from class__main.menus.fuzzel import Fuzzel

from class__main.client_manager.hyprland import HyprClientManager


def client_manager(
    menu: str,
    wm: str,
) -> None:
    max_str_len = 150

    if menu == "dmenu":
        menu_obj = Dmenu(
            width=1400,
            line=15,
            fuzzy=False,
            # original_dmenu=True,
        )
    elif menu == "fuzzel":
        menu_obj = Fuzzel(
            width=80,
            line=12,
        )
    else:
        sys.exit(f"Menu - '{menu}' is not recognized!")

    client_manager = HyprClientManager(menu_obj)
    client_manager.run()


def main() -> None:
    menus = ["dmenu", "fuzzel"]
    wms = ["dwm", "hyprland"]

    arg_parser = argparse.ArgumentParser(description="client window manager")
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
    if len(sys.argv) <= 1:
        arg_parser.print_help()
        sys.exit()

    # parse all cli arguments
    args = arg_parser.parse_args()

    # 'window-manager' is accessed by 'window_manager'
    if args.menu and args.window_manager:
        client_manager(
            menu=args.menu,
            wm=args.window_manager,
        )
    else:
        arg_parser.print_help()
        sys.exit()


if __name__ == "__main__":
    main()
