# src/task_manager.py
"""Модуль управления задачами: CRUD и бизнес-правила."""
from typing import List, Dict, Optional
import uuid
from datetime import datetime
from .exceptions import TaskNotFoundError, ValidationError
from .storage import TaskStorage

class TaskManager:
    def __init__(self, storage: TaskStorage):
        self.storage = storage
        self.tasks = self.storage.load()

    def _save(self):
        self.storage.save(self.tasks)

    def _find_index(self, task_id: str) -> int:
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                return i
        raise TaskNotFoundError(task_id)

    def add(self, title: str, description: str = "") -> Dict:
        if not title.strip():
            raise ValidationError("Название задачи не может быть пустым.")
        task = {
            "id": str(uuid.uuid4()),
            "title": title.strip(),
            "description": description.strip(),
            "status": "todo",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        self.tasks.append(task)
        self._save()
        return task

    def list(self, status: Optional[str] = None) -> List[Dict]:
        if status and status not in ('todo', 'in-progress', 'done'):
            raise ValidationError(f"Недопустимый статус: {status}")
        if status:
            return [t for t in self.tasks if t['status'] == status]
        return self.tasks

    def update(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None) -> Dict:
        idx = self._find_index(task_id)
        if title is not None:
            if not title.strip():
                raise ValidationError("Название не может быть пустым.")
            self.tasks[idx]['title'] = title.strip()
        if description is not None:
            self.tasks[idx]['description'] = description.strip()
        self.tasks[idx]['updated_at'] = datetime.now().isoformat()
        self._save()
        return self.tasks[idx]

    def change_status(self, task_id: str, new_status: str) -> Dict:
        if new_status not in ('todo', 'in-progress', 'done'):
            raise ValidationError(f"Недопустимый статус: {new_status}")
        idx = self._find_index(task_id)
        self.tasks[idx]['status'] = new_status
        self.tasks[idx]['updated_at'] = datetime.now().isoformat()
        self._save()
        return self.tasks[idx]

    def delete(self, task_id: str) -> Dict:
        idx = self._find_index(task_id)
        deleted = self.tasks.pop(idx)
        self._save()
        return deleted
