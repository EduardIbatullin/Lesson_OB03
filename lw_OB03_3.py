# Создайте класс Author и класс Book. Класс Book должен использовать композицию для включения автора в
# качестве объекта.

class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class Book:
    def __init__(self, title, author_book):
        self.title = title
        self.author_book = author_book

    def get_info_book(self):
        print(f"{self.title} - {self.author_book.name}")


author = Author("Лев Толстой", "русский")
book = Book("Война и мир", author)


book.get_info_book()
