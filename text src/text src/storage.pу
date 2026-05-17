# src/storage.py
"""Модуль для работы с JSON-файлом задач."""
import json
import os
from typing import List, Dict
from .exceptions import StorageError

DEFAULT_FILENAME = "tasks.json"

class TaskStorage:
    def __init__(self, filename: str = DEFAULT_FILENAME):
        self.filename = filename

    def load(self) -> List[Dict]:
        """Загружает задачи из файла. Возвращает пустой список, если файла нет."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            raise StorageError(f"Не удалось прочитать файл {self.filename}: {e}")

    def save(self, tasks: List[Dict]):
        """Сохраняет список задач в файл."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(tasks, f, ensure_ascii=False, indent=2)
        except IOError as e:
            raise StorageError(f"Не удалось записать в файл {self.filename}: {e}")
