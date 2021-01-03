import functools

user = {"username": "jose", "access_level": "guest"}


# Example of decorator
def make_secure(some_function):
    # functools to keep the __name__ and documentation
    # of the original function get_admin_password
    @functools.wraps(some_function)
    def secure_function():
        if user["access_level"] == "admin":
            return some_function()
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


# People who are guest cannot get the value
@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password.__name__)
print(get_admin_password())
