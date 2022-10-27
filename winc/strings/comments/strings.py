# Index selection
letter_grades = 'ABCDF'
letter_grades[0] # A
letter_grades[3] # D

# Slicing
waltz = 'onetwothree'
waltz[0:3]
# We don't need to specify the 0 if we start at the beginning
waltz[:3]
waltz[3:6]
waltz[6:11]
# Same goes for the end -- we can leave it empty
waltz[6:]
# We can specify a step size if we don't want a continuous slice
waltz[0:11:2]

# When we need the length of a string we have the len-function:
sentence = 'The length of this string is:'
print(sentence, len(sentence))
print('Wait.. You just made it longer!')

""" String interpolation 

If we want to insert a variable into a string we do it like this:

Write f in front of the string.
Use curly braces ({}) to insert the variable into the string. """

answer = 4
qa = f'The answer is... {answer}'
