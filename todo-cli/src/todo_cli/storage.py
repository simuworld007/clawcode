import json
from pathlib import Path

DEFAULT_PATH = Path.home() / '.todo_cli' / 'tasks.json'


def load_tasks(path: Path = DEFAULT_PATH):
    if not path.exists():
        return []
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def save_tasks(tasks, path: Path = DEFAULT_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
