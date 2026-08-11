import json

def get_username():
    try:
        with open("setting.json", "r") as f:
            settings = json.load(f)
        return settings.get("username")
    except FileNotFoundError:
        return "Player"
    
def get_ram_settings():
    try:
        with open("setting.json", "r") as f:
            settings = json.load(f)
        return settings.get("ram")
    except FileNotFoundError:
        return ["-Xmx2G", "-Xms2G"]