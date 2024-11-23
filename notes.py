import os

# Файл для хранения заметок
NOTES_FILE = "notes.txt"

def read_notes():
    """Читает заметки из файла."""
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        return file.readlines()

def write_notes(notes):
    """Сохраняет заметки в файл."""
    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        file.writelines(notes)

# New

def add_note():
    """Добавляет новую заметку."""
    note = input("Введите текст заметки: ") + "\n"
    notes = read_notes()
    notes.append(note)
    write_notes(notes)
    print("Заметка добавлена.")

def view_notes():
    """Выводит все заметки."""
    notes = read_notes()
    if not notes:
        print("Заметок нет.")
    else:
        print("Ваши заметки:")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note.strip()}")

def delete_note():
    """Удаляет заметку по номеру."""
    view_notes()
    try:
        number = int(input("Введите номер заметки для удаления: "))
        notes = read_notes()
        if 1 <= number <= len(notes):
            deleted = notes.pop(number - 1)
            write_notes(notes)
            print(f"Заметка удалена: {deleted.strip()}")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Пожалуйста, введите корректный номер.")

def main():
    """Главное меню."""
    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Просмотреть заметки")
        print("3. Удалить заметку")
        print("4. Выход")
        
        choice = input("Выберите действие: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
