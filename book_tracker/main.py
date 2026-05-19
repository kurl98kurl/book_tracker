from storage import load_books, add_book
from stats import get_statistics

def show_menu():
    print("\n=== ТРЕКЕР ПРОЧИТАННЫХ КНИГ ===")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку и статистику")
    print("4. Выход")

def main():
    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            author = input("Введите автора: ").strip()
            title = input("Введите название книги: ").strip()
            try:
                rating = int(input("Введите оценку (1-5): "))
                add_book(author, title, rating)
            except ValueError:
                print("Ошибка: Введите корректное число для оценки.")
                
        elif choice == "2":
            books = load_books()
            if not books:
                print("Вы еще не прочитали ни одной книги.")
            else:
                print("\nСписок прочитанных книг:")
                for idx, book in enumerate(books, 1):
                    print(f"{idx}. {book['author']} — «{book['title']}» | Оценка: {book['rating']} | Дата: {book['date_read']}")
                    
        elif choice == "3":
            get_statistics()
            
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню, попробуйте снова.")

if __name__ == "__main__":
    main()
