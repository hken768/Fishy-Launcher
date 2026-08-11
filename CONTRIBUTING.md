# Contributing to Fishy Launcher

Thank you for your interest in contributing to Fishy Launcher! 🐟

We welcome contributions from everyone, whether it's bug reports, feature suggestions, or code improvements.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Submitting Code](#submitting-code)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Questions?](#questions)

---

## 💬 Code of Conduct

- **Be respectful** to all contributors and maintainers
- **No harassment, discrimination, or offensive behavior**
- **Be constructive** in your feedback and discussions
- **Help others learn** and grow
- **Report inappropriate behavior** to the maintainers

---

## 🤝 How to Contribute

### Reporting Bugs

Found a bug? We'd love to hear about it!

1. **Check existing issues** first:
   - Visit [Issues](https://github.com/hken768/Fishy-Launcher/issues)
   - Search for similar bug reports

2. **Create a new issue** with the following information:
   - **Clear title** — Briefly describe the bug
   - **Description** — Detailed explanation of the problem
   - **Steps to reproduce** — How to trigger the bug
   - **Expected behavior** — What should happen
   - **Actual behavior** — What actually happens
   - **System information**:
     - Operating System (Windows/macOS/Linux)
     - Python version (`python --version`)
     - Java version (`java -version`)
     - Minecraft version being used

**Example bug report:**
```
Title: Launcher crashes when launching Minecraft 1.16.5

Description: The launcher crashes with a Java error when I try to launch Minecraft version 1.16.5.

Steps to reproduce:
1. Open the launcher
2. Select "Play"
3. Choose Minecraft 1.16.5
4. Click launch

Expected: Game launches successfully
Actual: Launcher crashes with error

System: Windows 11, Python 3.9, Java 17
```

### Suggesting Features

Have an idea for an improvement? We'd love to hear it!

1. **Check existing issues** to avoid duplicates

2. **Open a new issue** with:
   - **Clear title** — Brief description of the feature
   - **Description** — Detailed explanation of what you want
   - **Use case** — Why this feature would be useful
   - **Examples** — Any relevant examples or mockups
   - **Additional context** — Any other relevant information

**Example feature request:**
```
Title: Add support for custom JVM arguments

Description: Allow users to specify custom Java arguments when launching Minecraft.

Use case: Some players need to allocate more RAM or use specific JVM flags for performance.

Example: --jvm-args "-Xmx4G -XX:+UseG1GC"
```

### Submitting Code

Ready to contribute code? Here's how:

#### Prerequisites
- **Python 3.8 or higher**
- **Git** installed
- **Basic Git workflow knowledge**
- **Your own GitHub account**

#### Step-by-Step Guide

##### 1. Fork the Repository
- Go to [Fishy-Launcher](https://github.com/hken768/Fishy-Launcher)
- Click the **"Fork"** button in the top-right corner
- This creates your own copy of the repo

##### 2. Clone Your Fork Locally
```bash
git clone https://github.com/YOUR-USERNAME/Fishy-Launcher.git
cd Fishy-Launcher
```
Replace `YOUR-USERNAME` with your GitHub username.

##### 3. Add Upstream Remote
```bash
git remote add upstream https://github.com/hken768/Fishy-Launcher.git
```
This lets you sync with the original repo.

##### 4. Create a New Branch
```bash
# For new features:
git checkout -b feature/your-feature-name

# For bug fixes:
git checkout -b bugfix/your-bug-fix-name

# For documentation:
git checkout -b docs/your-documentation-change
```

**Branch naming examples:**
- `feature/custom-java-args`
- `bugfix/launcher-crash-issue`
- `docs/improve-readme`

##### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

##### 6. Make Your Changes
- Keep code **clean and readable**
- Add **comments** for complex logic
- Follow the [Code Style Guidelines](#code-style-guidelines)
- Test your changes as you go

##### 7. Test Your Changes
```bash
python main.py
```
Make sure everything works as expected!

##### 8. Commit Your Changes
```bash
git commit -m "Brief description of what you changed"
```

**Good commit messages:**
- `Add support for custom JVM arguments`
- `Fix launcher crash when version not found`
- `Update documentation for setup`

**Avoid:**
- `fixed stuff`
- `update`
- `changes`

##### 9. Sync with Upstream (if needed)
```bash
git fetch upstream
git rebase upstream/main
```

##### 10. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

##### 11. Create a Pull Request
- Go to your forked repository on GitHub
- Click **"New Pull Request"** button
- Select your branch as the source
- Add a clear title and description
- Click **"Create Pull Request"**

**Pull Request description should include:**
- What changes you made
- Why you made them
- How to test the changes
- Related issues (e.g., "Fixes #123")

---

## 💻 Development Setup

### Quick Setup
```bash
# Clone the repo
git clone https://github.com/hken768/Fishy-Launcher.git
cd Fishy-Launcher

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the launcher
python main.py
```

### Project Structure
```
Fishy-Launcher/
├── main.py                 # Entry point
├── game.py                 # Game launching logic
├── setting.py              # Settings management
├── setting.json            # User settings file
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── CONTRIBUTING.md        # This file
├── LICENSE                # Project license
├── .gitignore            # Git ignore rules
└── tool/                  # Utility modules
    ├── __init__.py
    ├── title.py           # Launcher title display
    └── getjson.py         # JSON utilities
```

---

## 🎨 Code Style Guidelines

### Follow PEP 8
We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) — Python's official style guide.

### Key Points

**1. Naming Conventions**
```python
# Good
player_username = "Steve"
max_memory_mb = 4096
def launch_game():
    pass

# Bad
pun = "Steve"
maxMemory = 4096
def LaunchGame():
    pass
```

**2. Function Documentation**
```python
def launch_minecraft(version: str, username: str) -> bool:
    """
    Launch Minecraft with specified version and username.
    
    Args:
        version: The Minecraft version to launch (e.g., "1.20.1")
        username: Player username for authentication
        
    Returns:
        True if launch successful, False otherwise
        
    Raises:
        FileNotFoundError: If version directory not found
        ValueError: If username is empty
    """
    # Implementation here
    return True
```

**3. Comments**
```python
# Use comments for complex logic
def calculate_optimal_ram(system_ram_mb: int) -> int:
    """Calculate optimal RAM allocation for Minecraft."""
    # Reserve 20% of system RAM for OS
    available_ram = system_ram_mb * 0.8
    # Minecraft performs best with 2-4GB
    return min(int(available_ram), 4096)
```

**4. Line Length**
- Keep lines under 100 characters
- Break long lines logically

```python
# Good
result = launcher.launch_game(
    version="1.20.1",
    username=player_name,
    ram_mb=4096
)

# Avoid
result = launcher.launch_game(version="1.20.1", username=player_name, ram_mb=4096)
```

**5. Imports**
```python
# Good - organized imports
import os
import sys
from pathlib import Path

from colorama import Fore, Style
import questionary

# Avoid - random order
import questionary
from colorama import Fore
import os
```

**6. Type Hints**
```python
# Good - use type hints
def get_version_info(version: str) -> dict:
    """Get information about a Minecraft version."""
    pass

# Avoid - no type hints
def get_version_info(version):
    pass
```

---

## ✅ Pull Request Guidelines

Before submitting a PR, ensure:

- [ ] Your branch is up-to-date with `main`
  ```bash
  git fetch upstream
  git rebase upstream/main
  ```

- [ ] All your code follows the [Code Style Guidelines](#code-style-guidelines)

- [ ] You've tested your changes locally
  ```bash
  python main.py
  ```

- [ ] You've added comments for complex logic

- [ ] Your commit messages are clear and descriptive

- [ ] You've checked for any new dependencies added

### PR Title Format
- `[FEATURE] Add custom JVM arguments support`
- `[BUGFIX] Fix launcher crash on version not found`
- `[DOCS] Improve installation instructions`
- `[REFACTOR] Simplify game launching logic`

### PR Description Template
```markdown
## Description
Brief description of what this PR does.

## Related Issue
Fixes #123

## Changes Made
- Change 1
- Change 2
- Change 3

## How to Test
1. Step 1
2. Step 2
3. Expected result

## Screenshots (if applicable)
Add screenshots or GIFs of the changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Changes tested locally
- [ ] Documentation updated (if needed)
- [ ] No new warnings/errors
```

---

## ❓ Questions?

- **Have a question?** Open an [Issue](https://github.com/hken768/Fishy-Launcher/issues) with the `question` label
- **Need help with Git?** Check [GitHub's Git Guide](https://docs.github.com/en/get-started/using-git)
- **Want to discuss ideas?** Use [Discussions](https://github.com/hken768/Fishy-Launcher/discussions)

---

## 🙏 Thank You!

Every contribution helps make Fishy Launcher better. Whether it's code, bug reports, or documentation improvements — we appreciate your effort!

**Happy contributing! 🎮🐟**
