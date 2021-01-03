user = {"username": "jose", "access_level": "guest"}


# People who are guest cannot get the value
def get_admin_password():
    return "1234"


# Example of decorator
def make_secure(some_function):
    def secure_function():
        if user["access_level"] == "admin":
            return some_function()
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
