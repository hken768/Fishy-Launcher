import minecraft_launcher_lib
from colorama import Fore, Style
import subprocess
import sys
import json
import questionary
last_version = 0
def getTenVersions():
    global last_version
    version_list = minecraft_launcher_lib.utils.get_version_list()
    ten_versions = ["Release"]
    ten_versions.extend([v["id"] for v in version_list[last_version:last_version + 10]])
    last_version += 10
    ten_versions.append("Load More")
    return ten_versions

def launch_game():
    # Set the path to the Minecraft installation directory
    minecraft_directory = "./minecraft"
    version = None
    installed_versions = [v["id"] for v in minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)]
    wantSelect = questionary.confirm("Do you want to select a Minecraft version?").ask()
    if not wantSelect:
        version = input(Fore.GREEN + "Enter the Minecraft version to launch: " + Style.RESET_ALL)
        if version.lower() == "release":
                            version = next(v["id"] for v in minecraft_launcher_lib.utils.get_version_list() if v["type"] == "release")
    while wantSelect:
        version = questionary.select(
            "Select a Minecraft version to launch:",
            choices=getTenVersions()
        ).ask()
        if version.lower() == "release":
                    version = next(v["id"] for v in minecraft_launcher_lib.utils.get_version_list() if v["type"] == "release")
                    break
        elif version.lower() == "load more":
            continue
        if minecraft_launcher_lib.utils.is_version_valid(version, minecraft_directory):
            break
        
        
        print(Fore.RED + f"Version {version} is not available." + Style.RESET_ALL)

    if version not in installed_versions:
        print(Fore.YELLOW + "Installing Minecraft version: " + version + Style.RESET_ALL)
        minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory)
    else:
        print(f"{Fore.GREEN}Minecraft {version} is already installed. Launching game...{Style.RESET_ALL}")
    
    with open("setting.json", "r") as f:
        settings = json.load(f)
    options = {
        "username": settings.get("username"),
        "uuid": "00000000-0000-0000-0000-000000000000",
        "token": "token"
    }
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)
    subprocess.run(minecraft_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    launch_game()