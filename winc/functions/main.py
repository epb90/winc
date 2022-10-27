# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
from re import X

# 1
def greet(name):
    return f"Hello, {name}!"

print(greet('Bob'))

# 2
def add(number1, number2, number3):
    return number1 + number2 + number3
     

print(add(5,3,2))

# 3
def positive(int):
    return int > 0

print(positive(50))
print(positive(-50))
print(positive(0))

# 4
def negative(int):
    return int < 0

print(negative(50))
print(negative(-50))
print(negative(0))
