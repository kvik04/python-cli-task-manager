# Task Manager CLI

Простой консольный менеджер задач. Учебный проект для практики модульной разработки и Git.

## 🚀 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/kvik04/python-cli-task-manager.git
   cd python-cli-task-manager
   ```
2. Установите пакет в режиме разработки:
   ```bash
   pip install -e .
   ```

## 📋 Использование

```bash
# Добавить задачу
task-cli add "Купить молоко" -d "В магазине у дома"

# Показать все задачи
task-cli list

# Фильтр по статусу
task-cli list -s in-progress

# Обновить описание
task-cli update <id> -d "Новое описание"

# Изменить статус
task-cli status <id> done

# Удалить задачу
task-cli delete <id>
```

## 🧪 Запуск тестов

```bash
pip install pytest
pytest tests/
```

## 🏗️ Архитектура проекта

- `src/cli.py` — интерфейс командной строки
- `src/task_manager.py` — бизнес-логика
- `src/storage.py` — работа с JSON-файлом
- `src/exceptions.py` — кастомные исключения# Task Manager CLI

Простой консольный менеджер задач. Учебный проект для практики модульной разработки и Git.

## 🚀 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/kvik04/python-cli-task-manager.git
   cd python-cli-task-manager
   ```
2. Установите пакет в режиме разработки:
   ```bash
   pip install -e .
   ```

## 📋 Использование

```bash
# Добавить задачу
task-cli add "Купить молоко" -d "В магазине у дома"

# Показать все задачи
task-cli list

# Фильтр по статусу
task-cli list -s in-progress

# Обновить описание
task-cli update <id> -d "Новое описание"

# Изменить статус
task-cli status <id> done

# Удалить задачу
task-cli delete <id>
```

## 🧪 Запуск тестов

```bash
pip install pytest
pytest tests/
```

## 🏗️ Архитектура проекта

- `src/cli.py` — интерфейс командной строки
- `src/task_manager.py` — бизнес-логика
- `src/storage.py` — работа с JSON-файлом
- `src/exceptions.py` — кастомные исключения# Task Manager CLI

Простой консольный менеджер задач. Учебный проект для практики модульной разработки и Git.

## 🚀 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/kvik04/python-cli-task-manager.git
   cd python-cli-task-manager
   ```
2. Установите пакет в режиме разработки:
   ```bash
   pip install -e .
   ```

## 📋 Использование

```bash
# Добавить задачу
task-cli add "Купить молоко" -d "В магазине у дома"

# Показать все задачи
task-cli list

# Фильтр по статусу
task-cli list -s in-progress

# Обновить описание
task-cli update <id> -d "Новое описание"

# Изменить статус
task-cli status <id> done

# Удалить задачу
task-cli delete <id>
```

## 🧪 Запуск тестов

```bash
pip install pytest
pytest tests/
```

## 🏗️ Архитектура проекта

- `src/cli.py` — интерфейс командной строки
- `src/task_manager.py` — бизнес-логика
- `src/storage.py` — работа с JSON-файлом
- `src/exceptions.py` — кастомные исключения
