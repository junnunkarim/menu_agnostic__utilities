#!/usr/bin/env python

import os
import sys
import argparse
import pathlib

# enables importing from parent directories
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


from class__main.menus.dmenu import Dmenu
from class__main.menus.fuzzel import Fuzzel

from class__main.buku.base import BukuMenu


def buku(
    menu: str, online_status: str, database_path: pathlib.Path | None = None
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
            width=120,
            line=16,
        )
    else:
        sys.exit(f"Menu - '{menu}' is not recognized!")

    editor_cmd = "emacs"
    return_str = " Return"
    icon_menu: str = "󰍜"
    icon_tips: str = "󰔨"
    icon_enter: str = ""

    buku = BukuMenu(
        menu=menu_obj,
        database_path=database_path,
        editor_cmd=editor_cmd,
        attr_to_show=["id", "title", "tags"],
        max_str_len=max_str_len,
        online_status=online_status,
        return_str=return_str,
        icon_menu=icon_menu,
        icon_tips=icon_tips,
        icon_enter=icon_enter,
    )

    entry_new_bookmark = icon_menu + " add new bookmark "
    entry_edit_bookmark = icon_menu + " edit bookmark "
    entry_delete_bookmark = icon_menu + " delete bookmark "
    entry_all_tags = icon_menu + " show all tags "

    menu_entries = [
        entry_new_bookmark,
        entry_edit_bookmark,
        entry_delete_bookmark,
        entry_all_tags,
        "",  # for adding an empty line
    ]

    while True:
        selection = buku.get_selection(
            menu_entries=menu_entries,
            prompt_name="Bookmarks: ",
        )

        if selection in menu_entries:
            if selection == entry_new_bookmark:
                buku.add_edit_bookmark()
            elif selection == entry_edit_bookmark:
                buku.edit_bookmark()
            elif selection == entry_delete_bookmark:
                buku.delete_bookmark()
            elif selection == entry_all_tags:
                status = buku.show_tags()

                if status:
                    break
        elif not (selection in menu_entries):
            # get the id from the selected bookmark string
            bookmark_id = int(selection.split(" ")[0])

            buku.open_bookmark(id=bookmark_id)
            break


def main() -> None:
    menus = ["dmenu", "fuzzel"]
    modes = ["online", "offline"]

    arg_parser = argparse.ArgumentParser(description="buku bookmark manager")
    # define necessary cli arguments
    arg_parser.add_argument(
        "-m",
        "--menu",
        help="specify the menu launcher",
        choices=menus,
        required=True,
    )
    arg_parser.add_argument(
        "-os",
        "--online-status",
        help="specify if you want buku to fetch from online when adding new bookmarks",
        choices=modes,
        required=True,
    )
    arg_parser.add_argument(
        "-db",
        "--db-path",
        help="specify the sqlite3 database containing all buku bookmarks",
    )

    # if no cli arguments are provided, show the help message and exit
    if len(sys.argv) <= 1:
        arg_parser.print_help()
        sys.exit()

    # parse all cli arguments
    args = arg_parser.parse_args()

    # 'window-manager' is accessed by 'window_manager'
    if args.menu and args.online_status and args.db_path:
        buku(
            menu=args.menu,
            online_status=args.online_status,
            database_path=pathlib.Path(args.key_file).expanduser(),
        )
    elif args.menu and args.online_status:
        buku(
            menu=args.menu,
            online_status=args.online_status,
        )
    else:
        arg_parser.print_help()
        sys.exit()


if __name__ == "__main__":
    main()
