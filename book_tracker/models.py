import datetime

class Book:
    def __init__(self, author: str, title: str, rating: int, date_read: str = None):
        self.author = author
        self.title = title
        if not (1 <= rating <= 5):
            raise ValueError("Оценка должна быть от 1 до 5")
        self.rating = rating
        # Если дата не указана, ставим сегодняшнюю
        self.date_read = date_read if date_read else datetime.date.today().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date_read": self.date_read
        }