#!python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Turn object to a string
    # Usually the __str__ is used
    def __str__(self):
        return f"{self.name}, {self.age} years old."

    # To print out an unambiguious object
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"


bob = Person("Bob", 35)
print(bob)
