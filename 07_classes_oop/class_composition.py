#!python3

from typing import List
from classes_method_and_static import Book

# Class composition
# A class (BookShelf) that contains a lot of other class instances (Book)
# A BookShelf is composed of a lot of things, including books


class BookShelf:
    # *books means it receives a bunch of book objects
    def __init__(self, *books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."


class Book:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("Python 101")

shelf = BookShelf(book, book2)

print(shelf)
