#!python3

# kwargs = keyword arguments
# **kargs is a dictionary
def named(**kwargs):
    # All named arguments gets collected in a dicionary
    print(kwargs)


named(name="Bob", age=25)       # {'name': 'Bob', 'age': 25}


details = {"name": "Gabriel", "age": 25}
named(**details)


# args gets all arguments
# kargs gets all named arguments
def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)
