#!python3

# With list comprehension a new list is generated

numbers = [1, 3, 5]
doubled = [num * 2 for num in numbers]      # [2, 6, 10]
print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)
