#!python3

#  All methods within a class must have a parameter
class Student:
    # __init__ is the constructor
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (100, 100, 92, 78, 90))

print(student.name)
print(student.average_grade())
