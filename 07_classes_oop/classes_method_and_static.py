#!python3

class ClassTest:
    # self as first parameter are instance methods
    def instance_method(self):
        print(f"Called instance_method of {self}")

    # cls is the Class itself
    @classmethod
    def class_method(cls):
        print(f"Called class_method  of {cls}")

    # Methods that can't be used by instances, only the class itself
    @staticmethod
    def static_method():
        print("Called static_method.")


# ClassTest.class_method()
# ClassTest.static_method()

#
# Example below of usage of the class method


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    # Creates new objects, like factory method
    # cls is the Book class itself
    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover("Harry Potter", 1500)
book1 = Book.paperback("Python 101", 600)
print(book)
print(book1)
