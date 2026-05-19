import json
import os

FILE_NAME = "books.json"

def load_books():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_books(books_list):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(books_list, f, ensure_ascii=False, indent=4)

def add_book(author, title, rating):
    books = load_books()
    
    # Шаг 5 из ТЗ: Проверка на дубликаты (автор + название)
    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            print(f"Ошибка: Книга '{title}' автора {author} уже есть в списке!")
            return False
            
    from models import Book
    new_book = Book(author, title, rating)
    books.append(new_book.to_dict())
    save_books(books)
    print("Книга успешно добавлена!")
    return True