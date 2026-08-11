# Fishy-Launcher 🐟

A lightweight Python-based launcher for cracked Minecraft instances.

This project provides a simple, interactive terminal-based launcher that allows users to easily play Minecraft in offline/cracked mode.

## Badges 🚀

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0.html)

## Table of Contents 📜

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About ℹ️

Fishy Launcher is a Python application designed to simplify the process of launching cracked Minecraft versions. It offers an interactive command-line interface to manage game versions and launch the game with customizable settings.

> **Disclaimer**: This project is intended for educational purposes and personal use. Running or distributing cracked software may violate Minecraft's End User License Agreement and local laws. Use responsibly and ethically.

## Features ✨

- **Interactive Terminal UI**: User-friendly interface powered by `questionary` for easy navigation.
- **Version Management**: Allows selecting and installing specific Minecraft versions using `minecraft-launcher-lib`.
- **Customizable Settings**: Configure username, game directory, and RAM allocation.
- **Cross-Platform Compatibility**: Designed to work on Windows and Linux/macOS.
- **Lightweight**: Written purely in Python with minimal external dependencies.

## Tech Stack 💻

- **Language**: Python
- **Core Libraries**: `colorama`, `questionary`, `minecraft-launcher-lib`
- **Configuration**: JSON

## Installation 🛠️

### Prerequisites

- Python 3.8+ (recommended)
- pip package installer

### Steps

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/hken768/Fishy-Launcher.git
    cd Fishy-Launcher
    ```

2.  **(Optional) Create and activate a virtual environment**:
    *   **macOS / Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   **Windows**:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage 🎮

1.  **Prepare Configuration**:
    Copy the example configuration file to create your runtime configuration:
    *   **macOS / Linux**:
        ```bash
        cp config.example.json config.json
        ```
    *   **Windows PowerShell**:
        ```powershell
        Copy-Item config.example.json config.json
        ```

    Edit the `config.json` file to set your preferred `username`, `game_dir`, and `memory` settings.

2.  **Run the Launcher**:
    Execute the main script from the repository root:
    ```bash
    py main.py 
    ```
    or
    ```bash
    python main.py
    ```

3.  **Interact with the Menu**:
    The launcher will present an interactive menu. You can choose to:
    *   **Play**: Select or enter a Minecraft version to launch.
    *   **Settings**: Modify username and RAM settings.
    *   **Exit**: Close the launcher.

### How to Use 🚀

- **Playing Minecraft**: 
    When you select 'Play', the launcher will prompt you to either select a Minecraft version from a list (loading more if needed) or manually enter a version. If the version is not installed, it will be downloaded and installed using `minecraft-launcher-lib`. Once installed or if already present, the game will launch with the configured settings.

- **Configuring Settings**: 
    Navigate to 'Settings' to change your in-game username or adjust RAM allocation (minimum and maximum values for JVM arguments like `-Xms` and `-Xmx`). These settings are saved in `setting.json`.

## Configuration ⚙️

Use `config.example.json` as a template for your primary game launch settings. **Do not commit sensitive information or personal credentials to the repository.**

**Example `config.json`**: 

```json
{
  "username": "Player",
  "game_dir": "./.minecraft",
  "memory": "2G",
  "jvm_args": "-Xmx2G -Xms1G"
}
```

User-specific settings like username and RAM are managed via `setting.json` and configured through the in-app settings menu.

## Project Structure 📁

```
Fishy-Launcher/
├── .minecraft/         # Default directory for Minecraft installations (created on first run)
├── tool/
│   ├── __init__.py
│   ├── getjson.py      # Utility for reading settings from JSON files
│   └── title.py        # Displays the launcher's ASCII title
├── config.example.json # Example configuration file
├── config.json         # Runtime configuration file (user-specific)
├── game.py             # Handles Minecraft version selection, installation, and launching
├── LICENSE             # Project license file
├── main.py             # Entry point for the launcher application
├── README.md           # Project documentation
├── requirements.txt    # Project dependencies
├── setting.json        # User settings for username and RAM
├── setting.py          # Handles the settings menu logic
└── venv/               # Virtual environment (if created)
```

## Contributing 🤝

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request. Follow standard contribution workflows for clarity.

## License 📄

This project is licensed under the GNU General Public License v3.0.

See the `LICENSE` file for more details.

## Contact 📬

- **Repository**: [Fishy-Launcher on GitHub](https://github.com/hken768/Fishy-Launcher)

--- 

© 2023 [hken768](https://github.com/hken768). 
🚀 Boost your Minecraft experience! 
⭐ [Star the Repository](https://github.com/hken768/Fishy-Launcher/stargazers)
👀 [Watch the Repository](https://github.com/hken768/Fishy-Launcher/watchers)
🍴 [Fork the Repository](https://github.com/hken768/Fishy-Launcher/fork)
#️⃣ [Open an Issue](https://github.com/hken768/Fishy-Launcher/issues)


---
**<p align="center">Generated by [ReadmeCodeGen](https://www.readmecodegen.com/)</p>**
