import argparse
from .storage import load_tasks, save_tasks, get_storage_location


def add_task(description):
    tasks = load_tasks()
    tasks.append({'id': len(tasks) + 1, 'desc': description, 'done': False})
    save_tasks(tasks)
    print('Added:', description)


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks.')
        return
    for t in tasks:
        status = '✔' if t.get('done') else ' ' 
        print(f"[{status}] {t['id']}: {t['desc']}")


def complete_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t['id'] == task_id:
            t['done'] = True
            save_tasks(tasks)
            print('Completed:', t['desc'])
            return
    print('Task not found')


def remove_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]
    # reassign ids
    for i, t in enumerate(tasks, start=1):
        t['id'] = i
    save_tasks(tasks)
    print('Removed task', task_id)


def show_location():
    location = get_storage_location()
    print('Tasks are stored in:', location)


def parse_args():
    p = argparse.ArgumentParser(prog='todo')
    sub = p.add_subparsers(dest='cmd')
    sub.required = True

    a = sub.add_parser('add')
    a.add_argument('desc')

    sub.add_parser('list')

    c = sub.add_parser('complete')
    c.add_argument('id', type=int)

    r = sub.add_parser('remove')
    r.add_argument('id', type=int)

    sub.add_parser('location', help='Show storage file location')

    return p.parse_args()


def main():
    args = parse_args()
    if args.cmd == 'add':
        add_task(args.desc)
    elif args.cmd == 'list':
        list_tasks()
    elif args.cmd == 'complete':
        complete_task(args.id)
    elif args.cmd == 'remove':
        remove_task(args.id)
    elif args.cmd == 'location':
        show_location()


if __name__ == '__main__':
    main()
