# Todo CLI

A small example Python project: a command-line todo app that stores tasks in a JSON file.

Directory layout
- src/: package code
- tests/: unit tests
- docs/: short usage guide
- env/: virtualenv instructions / requirements

Features
- Add, list, complete, and remove tasks
- Persistent storage in `~/.todo_cli/tasks.json`
- Simple tests with pytest

Quick start
1. Create a virtual environment and activate it:
   python -m venv .venv
   source .venv/bin/activate
2. Install dependencies:
   pip install -r env/requirements.txt
3. Install the package in editable mode (so changes take effect immediately):
   pip install -e .
4. Run the CLI:
   python -m todo_cli.main add "Buy milk"
   python -m todo_cli.main list

Commands
- add <description>   Add a new task
- list                List tasks
- complete <id>       Mark a task done
- remove <id>         Remove a task
- location            Show the absolute path of the storage file where tasks are saved

Notes
- Default storage file: `~/.todo_cli/tasks.json`
- To change the storage location programmatically, use the functions in `src/todo_cli/storage.py`.
- Tests: run `pytest -q` from the repository root to execute all tests under tests/.

Development
- The package uses a src/ layout. When developing locally, use `pip install -e .` from the project root to get an editable install.
