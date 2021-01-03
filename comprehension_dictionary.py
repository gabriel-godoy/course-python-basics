users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

# Dictionary comprehension
# user[1]: user
username_mapping = {user[1]: user for user in users}
print(username_mapping)

# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")

# Get specific user
# _, username, password = username_mapping[username_input]

# if password_input == password:
#     print("Your details are correct!")
# else:
#     print("Your details are incorrect!")

# print(username)
