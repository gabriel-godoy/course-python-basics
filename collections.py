from collections import Counter, namedtuple, OrderedDict, defaultdict, deque


"""
Counter
Is a container that stores the elements as dictionary keys
and their counts as dictionary values
"""
a = "aaaaabbbbccc"
my_counter = Counter(a)

print(my_counter)                 # Counter({'a': 5, 'b': 4, 'c': 3})
print(my_counter.items())         # dict_items([('a', 5), ('b', 4), ('c', 3)])
print(my_counter.keys())          # dict_keys(['a', 'b', 'c'])
print(my_counter.values())        # dict_values([5, 4, 3])
print(my_counter.most_common(1))  # [('a', 5)]
print(list(my_counter.elements()))
# ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']


"""
namedtuple
Is an easy to create an object type, similar to a struct
"""
Point = namedtuple('Point', 'x, y')     # Class with fields x and y

some_point = Point(1, -4)
print(some_point)


"""
OrderedDict
It is like a regular dictionary,
but can remember the order the items were inserted
It returns tuples
"""
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['d'] = 4
ordered_dict['b'] = 2
ordered_dict['c'] = 3

print(ordered_dict)     # OrderedDict([('a', 1), ('d', 4), ('b', 2), ('c', 3)])


"""
defaultdict
Is similir to the dictionary, the only difference is that it will have
a default value if the key has not been set yet
"""
some_default_dict = defaultdict(int)
some_default_dict['a'] = 1
some_default_dict['b'] = 2
print(some_default_dict)        # defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(some_default_dict['c'])   # It returns a default integer 0


"""
deque
Is a double-ended queue and it can be used to add,
or remove element from both ends.
It is implemented in a way that is very efficient
"""
some_deque = deque()

some_deque.append(1)
some_deque.append(2)

some_deque.appendleft(3)

some_deque.pop()                # Remove last element
some_deque.popleft()            # Remove first element

some_deque.extend([4, 5, 6])    # Insert elements at the end
some_deque.extendleft([4, 5])

some_deque.rotate(1)            # Rotate elements

print(some_deque)
