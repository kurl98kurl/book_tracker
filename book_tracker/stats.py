def get_statistics():
    from storage import load_books
    books = load_books()
    if not books:
        print("Список книг пуст. Нет данных для статистики.")
        return

    total_books = len(books)
    total_rating = sum(book["rating"] for book in books)
    avg_rating = total_rating / total_books

    # Статистика по авторам
    author_counts = {}
    for book in books:
        author = book["author"]
        author_counts[author] = author_counts.get(author, 0) + 1

    print("\n--- СТАТИСТИКА ---")
    print(f"Всего прочитано книг: {total_books}")
    print(f"Средняя оценка: {avg_rating:.2f}")
    print("Книг по авторам:")
    for author, count in author_counts.items():
        print(f" - {author}: {count}")
    print("------------------")