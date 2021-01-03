#!python3

# Capture all arguments
def multiply(*args):
    total = 1

    for arg in args:
        total = total * arg

    return total


print(multiply(1, 3, 5))


#
def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))  # Unpack entire list as arguments


#
def add2(x, y):
    return x + y

nums = {'x': 15, 'y': 25} # x and y have the same names as the add function arguments
print(add2(**nums))  # Pass each key of the dict as a named argument


# pass a named argument called 'operator'
# *args gets all arguments, except the named arguments called operator
def apply(*args, operator): 
  if operator == "*":
    return multiply(args)
  elif operator == "+":
    return sum(args)
  else:
    return "No valid operator procided to apply()."

print('Apply: ', apply(1, 3, 6, 7, operator="*"))
