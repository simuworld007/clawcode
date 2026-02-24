# Todo CLI

A small example Python project: a command-line todo app that stores tasks in a JSON file.

Structure:
- src/: package code
- tests/: unit tests
- docs/: short usage guide
- env/: virtualenv instructions / requirements

Features:
- Add, list, complete, and remove tasks
- Persistent storage in `~/.todo_cli/tasks.json`
- Simple tests with pytest

Run:

1. Create virtual environment:
   python -m venv .venv
   source .venv/bin/activate
2. Install dependencies:
   pip install -r env/requirements.txt
3. Run CLI:
   python -m todo_cli.main add "Buy milk"
   python -m todo_cli.main list

Commands:
- add <description>   Add a new task
- list                List tasks
- complete <id>       Mark a task done
- remove <id>         Remove a task
- location            Show the absolute path of the storage file where tasks are saved

Notes:
- Storage default: `~/.todo_cli/tasks.json`
- You can override storage path by editing `storage.py` or calling storage functions directly in code.
