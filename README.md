# Fishy Launcher 🐟

A lightweight Python-based launcher for managing and launching cracked Minecraft versions with an intuitive terminal interface.

**Created by:** Just Me

---

## 📋 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

---

## ✨ Features

- **Interactive Terminal UI** — User-friendly command-line interface using questionary
- **Version Management** — Easily manage and switch between different Minecraft versions
- **Lightweight Design** — Minimal dependencies, fast startup time
- **Settings Management** — Customize launcher preferences and game settings
- **Cross-Platform Support** — Works on Windows, macOS, and Linux
- **Color Output** — Enhanced terminal experience with colorized text

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** — [Download Python](https://www.python.org/downloads/)
- **Java (JRE/JDK)** — Required to run Minecraft
  - Windows: [Download Java](https://www.oracle.com/java/technologies/downloads/)
  - macOS: `brew install java`
  - Linux: `sudo apt install openjdk-17-jre` (Ubuntu/Debian) or equivalent for your distribution

---

## 🚀 Installation

### Step 1: Clone or Download the Repository

```bash
git clone https://github.com/hken768/Fishy-Launcher.git
cd Fishy-Launcher
```

Or download the ZIP file and extract it.

### Step 2: Install Required Dependencies

```bash
pip install -r requirements.txt
```

If you encounter permission issues, try:

```bash
pip install --user -r requirements.txt
```

### Step 3: Verify Installation

To ensure everything is set up correctly:

```bash
python main.py
```

---

## 💻 Quick Start

1. **Open a terminal/command prompt** in the Fishy-Launcher directory
2. **Run the launcher:**
   ```bash
   python main.py
   ```
3. **Follow the on-screen prompts** to:
   - Select "Play" to launch Minecraft
   - Adjust "Settings" for launcher preferences
   - Choose "Exit" to close the launcher

---

## 📖 Usage

### Main Menu

When you start the launcher, you'll see three options:

#### 1. **Play**
Launches your selected Minecraft version. The launcher will:
- Load your configured game settings
- Initialize Java
- Start the Minecraft client

#### 2. **Settings**
Allows you to customize:
- Username and player preferences
- Game properties and performance settings
- Launcher configurations
- Version selection

#### 3. **Exit**
Safely closes the launcher application

---

## 📁 Project Structure

```
Fishy-Launcher/
├── main.py                 # Entry point of the application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── game/                  # Game launching logic
│   └── launch_game.py    # Minecraft launch handler
├── tool/                  # Utility modules
│   ├── title.py          # Title display
│   ├── getjson.py        # JSON data handler
│   └── ...
├── setting.py            # Settings management
└── config/               # Configuration files
    └── ...
```

---

## ⚙️ Configuration

### Custom Settings

Settings are managed through the interactive menu in the launcher. Your preferences are saved automatically.

### Minecraft Versions

Versions are managed within the launcher's version management system. You can:
- Add new versions
- Remove unused versions
- Set default version for launching

---

## 🔧 Troubleshooting

### Issue: "Java not found"

**Solution:**
- Ensure Java is installed and accessible from terminal/command prompt
- Test by running: `java -version`
- If not recognized, add Java to your system PATH environment variable

### Issue: "ModuleNotFoundError: No module named 'colorama'"

**Solution:**
- Run the installation command again:
  ```bash
  pip install -r requirements.txt
  ```
- On macOS/Linux, you may need to use `pip3` instead of `pip`

### Issue: "Permission denied" on Linux/macOS

**Solution:**
- Make the script executable:
  ```bash
  chmod +x main.py
  ```
- Or run with explicit Python:
  ```bash
  python3 main.py
  ```

### Issue: Launcher freezes when launching game

**Solution:**
- Check if Java is properly installed
- Ensure sufficient system resources (RAM, disk space)
- Close other applications to free up memory
- Check launcher logs for error messages

---

## 📦 Dependencies

The launcher requires the following Python packages (listed in `requirements.txt`):

- **colorama** — Cross-platform colored terminal text
- **questionary** — Interactive terminal prompts
- Additional packages as needed for game launching

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** (GPL-3.0).

See the LICENSE file for more details.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Changelog

### Version 1.0.0 (Initial Release)
- Initial release of Fishy Launcher
- Interactive terminal UI
- Version management
- Settings management
- Cross-platform support

---

## ⚠️ Disclaimer

This launcher is designed for cracked Minecraft. Ensure you comply with all applicable laws and terms of service in your jurisdiction.

---

## 💬 Support & Contact

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/hken768/Fishy-Launcher/issues) on GitHub
- Ensure you provide detailed information about your problem

---

**Enjoy your gaming experience with Fishy Launcher! 🎮🐟**
