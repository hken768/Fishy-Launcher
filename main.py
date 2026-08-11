import os
from tool.title import print_title
from colorama import Fore, Style
import questionary
from game import launch_game
import sys
import setting
import tool.getjson

def main():
    print_title()
    print(Fore.GREEN + f"Welcome, {tool.getjson.get_username()}!" + Style.RESET_ALL)
    choice = questionary.select(
        "Choose an option:",
        choices=[
            "Play",
            "Settings",
            "Exit\n"
        ]
    ).ask()

    if choice == "Play":
        launch_game()
    elif choice == "Settings":
        setting.setting()
        main()
    elif choice == "Exit":
        print("Exiting the application...")
        sys.exit(0)

if __name__ == "__main__":
    if sys.platform == "win32":
        os.system("title Fishy Launcher")
    else:
        sys.stdout.write("\x1b]2;Fishy Launcher\x1c")
    main()