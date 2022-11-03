#list

names = ['Bob', 'Sarah', 'Shaun', 'Claire']

example_list = ['Bob', 3.14, 42]
example_list_of_lists = [['Bob', 3.14, 42], ['Preeti', 3.14, 42]]

# index and slicing

example_list = ['zeroth', 'first', 'second', 'third']
# Get the zeroth item.
example_list[0]
# Get the second item.
example_list[2]
# Get a slice of the list
example_list[0::2]

# Mutating



example_list = ['zeroth', 1, 2, 3]
example_list[0] = 0
print(example_list)
# Output: [0, 1, 2, 3]

example_list_a = [1, 2, 3]
example_list_b = [3, 2, 1]
print(example_list_a == example_list_b)

Casting
Some types of objects can be cast into lists using the built in list function, and vice versa. It doesn't come up often in practice for the types that we've discussed so far, but keep this one in your back pocket for later. One case you may find entertaining to look at now is list-to-string casting:

example_list = ['this', 'is', 'fun']
str(example_list)
list(str(example_list))
str(list(str(example_list)))
list(str(list(str(example_list))))
str(list(str(list(str(example_list)))))
# Et cetera :-)
Common operations
Some things that you will find yourself doing often with lists are:

Computing the length of a list with len

Finding the minimum or maximum within a list with min or max

Concatenating two or more lists with +

Checking if something is in a list with in

>>> example_list = [42.0, 3.50, 3.14, 42.0]
>>> len(example_list)
4

>>> min(example_list)
3.14

>>> max(example_list)
42.0

>>> example_list + ['another one']
[42.0, 3.5, 3.14, 42.0, 'another one']

>>> 42.0 in example_list
True
