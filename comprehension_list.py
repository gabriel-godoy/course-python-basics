#!python3

# List comprehension offers a shorter syntax when you want to create a new list
# based on the values of an existing list

numbers = [1, 3, 5]
doubled = [num * 2 for num in numbers]      # [2, 6, 10]
print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)
