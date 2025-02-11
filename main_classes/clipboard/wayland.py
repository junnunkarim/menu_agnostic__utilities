import os
import sys

from subprocess import run, check_output

# enables importing from parent directories
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from base_classes.clipboard.base import Clipboard


class ClipboardWayland(Clipboard):
    def __init__(self, menu: str, prompt_name: str = "Clipboard: ") -> None:
        super().__init__(menu, prompt_name)

    def run(self):
        # get clipboard history from cliphist
        raw_history = check_output(["cliphist", "list"]).decode().splitlines()

        # split and only get the text without the ID
        history_entries = [
            line.split(maxsplit=1)[1] if len(line.split(maxsplit=1)) > 1 else ""
            for line in raw_history
            if line.strip()
        ]
        # remove duplicates while preserving order
        history_entries = list(dict.fromkeys(history_entries))

        history_str = "\n".join(history_entries)

        # user selected history
        selection = self.menu_obj.get_selection(
            entries=history_str,
            prompt_name=self.prompt_name,
        )

        run(
            ["wl-copy", selection],
            text=True,
        )
