# src/exceptions.py
"""Кастомные исключения для Task Manager."""

class TaskManagerError(Exception):
    """Базовое исключение приложения."""
    pass

class TaskNotFoundError(TaskManagerError):
    """Задача с указанным ID не найдена."""
    def __init__(self, task_id):
        super().__init__(f"Задача с ID {task_id} не найдена.")
        self.task_id = task_id

class StorageError(TaskManagerError):
    """Ошибка при работе с файловым хранилищем."""
    pass

class ValidationError(TaskManagerError):
    """Ошибка валидации входных данных."""
    pass

def handle_errors(func):
    """Декоратор для перехвата исключений в CLI."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TaskManagerError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")
    return wrapper
