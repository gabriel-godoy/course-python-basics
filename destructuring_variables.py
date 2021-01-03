#!python3

x, y = 1, 2

print(x, y)


people = [
    ("Bob", 42, "Mechanic"),
    ("James", 24, "Artist"),
    ("Harry", 32, "Lecturer")
]

# destructuring a tuple
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")


# head and tail of a list
# tail gets every element except first
list_head, *list_tail = [1, 2, 3, 4, 5]

print(list_head)
print(list_tail)
