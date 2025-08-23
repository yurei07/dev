import json

with open('books.json') as f:
    json_data = json.load(f)

# Мои книги 
class Book:
    # Обьект
    def __init__(self, title, author, isbn) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn 
        self.is_available = True # Проверка в наличии


# Моя библиотека
class Library:
    # Обьект
    def __init__(self) -> None:
        self.books = [] 
    # Добавляет книгу в массив обьект библиотеки
    def add_book(self, book):
        self.books.append(book)

    # получает книгу и изминяет наличия в false
    def check_out(self, book):
        if book.is_available:
            book.is_available = False
            print(f"Book {book.title} check out")
    # возращяет книгу и изминяет наличия на true
    def return_book(self, book):
        if book.is_available == False:
           book.is_available = True 
           print(f"Book {book.title} return")

    # Переберает книги и выдает книгу  
    def list_available_books(self):
        for book in self.books: 
            if book.is_available:
                print(f"We have book: {book.title}")
            else:
                print(f"We dont have book: {book.title}")

book1 = Book(json_data(f))
book2 =  Book("Мастер и Маргарита", "Михаил Булгаков", "978-5389076463")

library = Library()
library.add_book(book1)
library.add_book(book2)

# Пользователь берет книгу
library.check_out(book1)
print(library.list_available_books())
