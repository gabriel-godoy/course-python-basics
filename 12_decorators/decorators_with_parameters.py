import functools

user = {"username": "jose", "access_level": "guest"}


# make_secure now encapsulates the decorator,
# so we can pass arguments to the decorator
def make_secure(access_level):
    # Example of decorator
    def decorator(some_function):
        # functools to keep the __name__ and documentation
        # of the original function get_password
        @functools.wraps(some_function)
        def secure_function(*args, **kwargs):
            if user["access_level"] == "admin":
                return some_function(*args, **kwargs)
            else:
                return f"No admin permissions for {user['username']}"

        return secure_function

    return decorator


# People who are guest cannot get the value
@make_secure("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())


user = {"username": "anna", "access_level": "admin"}


print(get_admin_password())
print(get_dashboard_password())
