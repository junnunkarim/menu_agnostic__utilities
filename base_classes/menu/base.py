import sys

from subprocess import run


class Menu:
    main_prompt: list = []
    prompt_flag: str = ""

    def __init__(
        self,
        main_prompt: list,
        prompt_flag: str = "-p",
    ) -> None:
        self.main_prompt = main_prompt
        self.prompt_flag = prompt_flag

    # -------------------
    # execution functions
    # -------------------

    def get_selection(
        self,
        entries: str,  # entries to populate the menu with
        prompt_name: str = "",
        extra_prompts: list = [],
        error_message: str = "Could not get user selection!",
    ) -> str:
        output = run(
            self.main_prompt + [self.prompt_flag, prompt_name] + extra_prompts,
            text=True,
            input=entries,
            capture_output=True,
            encoding="utf-8",
        )

        if output.returncode:
            sys.exit(
                f"return_code: {output.returncode}\n"
                + f"stderr: {output.stderr}\n"
                + f"error: {error_message}\n"
            )

        return output.stdout.strip()

    # -----------------
    # derived functions
    # -----------------

    def get_confirmation(
        self,
        question: str = "Are you sure? ",
        positive: str = " Yes",
        negative: str = " No",
    ) -> bool:
        entries: str = f"{positive}\n{negative}"

        output = self.get_selection(
            entries=entries,
            prompt_name=question,
            error_message="Could not get confirmation!",
        )

        if output == positive:
            return True
        else:
            return False

    def show(
        self,
        entries: str,
        prompt_name: str = "",
    ) -> None:
        self.get_selection(
            entries=entries,
            prompt_name=prompt_name,
            error_message="Could not display entries!",
        )

    def show_message(
        self,
        entries: str,
        prompt_name: str = "Error:",
    ) -> None:
        self.get_selection(
            entries=entries,
            prompt_name=prompt_name,
            error_message="Could not display message!",
        )
