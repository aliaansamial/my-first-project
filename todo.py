import json
import sys
from pathlib import Path

FILE = Path("todos.json")


def load():
    if FILE.exists():
        return json.loads(FILE.read_text())
    return []


def save(todos):
    FILE.write_text(json.dumps(todos, indent=2))


def add(text):
    todos = load()
    todos.append({"text": text, "done": False})
    save(todos)
    print(f"Added: {text}")


def list_todos():
    todos = load()
    if not todos:
        print("Nothing to do!")
        return
    for i, t in enumerate(todos, start=1):
        mark = "x" if t["done"] else " "
        print(f"{i}. [{mark}] {t['text']}")


def done(number):
    todos = load()
    if not 1 <= number <= len(todos):
        print("No such item.")
        return
    todos[number - 1]["done"] = True
    save(todos)
    print(f"Done: {todos[number - 1]['text']}")


def delete(number):
    todos = load()
    if not 1 <= number <= len(todos):
        print("No such item.")
        return
    removed = todos.pop(number - 1)
    save(todos)
    print(f"Deleted: {removed['text']}")


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 todo.py add <text> | list | done <n> | delete <n>")
        return
    command = args[0]
    if command == "add" and len(args) > 1:
        add(" ".join(args[1:]))
    elif command == "list":
        list_todos()
    elif command == "done" and len(args) == 2 and args[1].isdigit():
        done(int(args[1]))
    elif command == "delete" and len(args) == 2 and args[1].isdigit():
        delete(int(args[1]))
    else:
        print("Unknown command. Try: add, list, done, delete")


if __name__ == "__main__":
    main()
