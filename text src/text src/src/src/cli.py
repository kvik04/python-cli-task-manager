# src/cli.py
"""Консольный интерфейс. Точка входа в приложение."""
import argparse
import sys
from .task_manager import TaskManager
from .storage import TaskStorage
from .exceptions import handle_errors

def main():
    parser = argparse.ArgumentParser(description="Task Manager - утилита для управления задачами")
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    # add
    parser_add = subparsers.add_parser("add", help="Добавить задачу")
    parser_add.add_argument("title", help="Название задачи")
    parser_add.add_argument("-d", "--description", default="", help="Описание задачи")

    # list
    parser_list = subparsers.add_parser("list", help="Показать задачи")
    parser_list.add_argument("-s", "--status", choices=["todo", "in-progress", "done"], help="Фильтр по статусу")

    # update
    parser_update = subparsers.add_parser("update", help="Обновить задачу")
    parser_update.add_argument("id", help="ID задачи")
    parser_update.add_argument("-t", "--title", help="Новый заголовок")
    parser_update.add_argument("-d", "--description", help="Новое описание")

    # status
    parser_status = subparsers.add_parser("status", help="Изменить статус задачи")
    parser_status.add_argument("id", help="ID задачи")
    parser_status.add_argument("new_status", choices=["todo", "in-progress", "done"], help="Новый статус")

    # delete
    parser_delete = subparsers.add_parser("delete", help="Удалить задачу")
    parser_delete.add_argument("id", help="ID задачи")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    manager = TaskManager(TaskStorage())
    handle_command(args, manager)

@handle_errors
def handle_command(args, manager: TaskManager):
    if args.command == "add":
        task = manager.add(args.title, args.description)
        print(f"✅ Задача создана: [{task['id']}] {task['title']}")
    elif args.command == "list":
        tasks = manager.list(status=args.status)
        if not tasks:
            print("📭 Список задач пуст.")
        for t in tasks:
            status_map = {"todo": "⏳", "in-progress": "🔄", "done": "✅"}
            print(f"{status_map.get(t['status'], '❓')} [{t['id'][:8]}] {t['title']}")
    elif args.command == "update":
        task = manager.update(args.id, title=args.title, description=args.description)
        print(f"✏️ Задача [{task['id']}] обновлена.")
    elif args.command == "status":
        task = manager.change_status(args.id, args.new_status)
        print(f"🔄 Статус задачи [{task['id']}] изменён на '{args.new_status}'.")
    elif args.command == "delete":
        task = manager.delete(args.id)
        print(f"🗑️ Задача [{task['id']}] '{task['title']}' удалена.")

if __name__ == "__main__":
    main()
