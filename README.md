
# PyCraft IDE (Tkinter Desktop App)

This is a comprehensive, feature-rich **Python Integrated Development Environment (IDE)** built using **Tkinter**. It aims to provide a modern coding experience for Python developers directly on their desktop—no browser or internet required.


## Features

This IDE includes a wide range of functionalities designed to enhance productivity and streamline your development workflow:

- ✅ **Syntax Highlighting**  
  Colors keywords, strings, comments, and other elements for improved readability.

- 🔢 **Line Numbers**  
  Displays line numbers beside code for better navigation and debugging.

- 📂 **Tabbed File Editing**  
  Manage and edit multiple files in separate tabs.

- 🧠 **Auto-Indentation**  
  Automatically indents code based on Python syntax rules.

- ✨ **Auto-Completion**  
  Suggests keywords, variables, and functions while typing.

- ⚠️ **Real-Time Error Checking**  
  Highlights syntax and lint errors as you type using `flake8`.

- 💻 **Embedded Terminal**  
  Run shell commands and Python scripts inside the IDE.

- 🔁 **Git Integration (Basic)**  
  Perform Git operations (init, commit, push, pull, status) directly in the IDE.

- 🗂️ **Project Tree View**  
  Explore and manage project directories and files from a sidebar.

- 📋 **Right-click File Options**  
  Open, rename, delete, or create files/folders with context menus.

- 🧪 **Run with Input**  
  Provide stdin input to your Python scripts via an input dialog.

- 🌗 **Dark/Light Theme Toggle**  
  Switch between light and dark themes as per your comfort.

- 🔤 **Font & Color Settings**  
  Customize editor fonts and color schemes to your liking.

- 🧩 **Plugin Support**  
  Extend IDE functionality using user-created plugins.

- 💾 **Autosave & Recovery**  
  Automatically save open files periodically and recover unsaved work.

- 💼 **Session Restore**  
  Reopen previously edited files and restore scroll/cursor state.

- 🐞 **Debugger Integration (Basic)**  
  Step-by-step execution and breakpoints for Python scripts.

- 📑 **Output Panel Tabs**  
  Organized output for standard output, errors, and logs.

- 📖 **About & Help Section**  
  See usage instructions, shortcut keys, and app information.

- 🏗️ **Build Installer (External)**  
  Easily convert to `.exe` using `PyInstaller` or `cx_Freeze`.


## 📁 Project Structure
```

python-ide/
├── main.py                     # Main application entry point
├── modules/
│   ├── **init**.py             # Python package marker
│   ├── editor.py               # Code editor logic
│   ├── file\_explorer.py        # File manager and project tree
│   ├── terminal.py             # Embedded terminal
│   ├── git\_integration.py      # Git operations
│   ├── settings\_manager.py     # Themes, fonts, autosave, session
│   └── debugger.py             # Debugging system
├── assets/
│   ├── icon.ico                # App icon
│   └── themes/
│       ├── dark\_theme.json
│       └── light\_theme.json
├── plugins/
│   ├── **init**.py
│   └── example\_plugin.py       # Example plugin template
└── config.json                 # User settings and session data

````


## 🛠️ Setup and Installation

### 1. Clone the Repository

```bash
git clone <repository_url_here>
cd python-ide
````

### 2. Install Dependencies

Tkinter is included with most Python installations. For linting support:

```bash
pip install flake8
```

**Optional: To build as `.exe`:**

```bash
pip install pyinstaller
```

### 3. Ensure Git is Installed

Git operations require Git to be installed and available via system PATH.
[Download Git](https://git-scm.com)


## ▶️ How to Run

```bash
python main.py
```


## 🤝 Contributing

Contributions are welcome!
Please feel free to submit:

* Feature requests
* Bug reports
* Pull requests

Open an issue or fork the repo to start contributing!


## 📄 License

This project is open-source and available under the [MIT License](LICENSE.md).


## 📬 Contact

For questions, suggestions, or feedback, feel free to open an issue on GitHub.


