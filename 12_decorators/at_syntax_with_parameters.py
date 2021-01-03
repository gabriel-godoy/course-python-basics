import functools

user = {"username": "jose", "access_level": "guest"}


# Example of decorator
def make_secure(some_function):
    # functools to keep the __name__ and documentation
    # of the original function get_password
    @functools.wraps(some_function)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return some_function(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


# People who are guest cannot get the value
@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


print(get_password("billing"))
