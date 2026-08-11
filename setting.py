import questionary
import json
import tool.getjson

def setting():
    print(f"Username: {tool.getjson.get_username()}")
    print(f"RAM Settings: MIN: {tool.getjson.get_ram_settings()[0]} MAX:{tool.getjson.get_ram_settings()[1]}\n")
    taken = questionary.select(
        "Choose a setting to change:",
        choices=[
            "Username",
            "RAM Settings",
            "Back"
        ]
    ).ask()
    
    if taken == "Username":
        new_username = questionary.text("Enter your new username:").ask()
        with open("setting.json", "r") as f:
            settings = json.load(f)
        settings["username"] = new_username
        with open("setting.json", "w") as f:
            json.dump(settings, f, indent=4)
        print(f"Username changed to {new_username}.")
    elif taken == "RAM Settings":
        min_ram_settings = questionary.text("Enter your min RAM settings:").ask()
        max_ram_settings = questionary.text("Enter your max RAM settings:").ask()
        with open("setting.json", "r") as f:
            settings = json.load(f)
        settings["ram"] = [f"-Xms{min_ram_settings.upper()}", f"-Xmx{max_ram_settings.upper()}"]
        with open("setting.json", "w") as f:
            json.dump(settings, f, indent=4)
        print(f"RAM settings changed to {settings['ram']}.")
    elif taken == "Back":
        return