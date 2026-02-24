from todo_cli.storage import load_tasks, save_tasks
from pathlib import Path
import tempfile


def test_save_and_load(tmp_path):
    p = tmp_path / 'tasks.json'
    tasks = [{'id':1,'desc':'x','done':False}]
    save_tasks(tasks, path=p)
    loaded = load_tasks(path=p)
    assert loaded == tasks
