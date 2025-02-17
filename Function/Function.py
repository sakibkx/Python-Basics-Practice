# 1. Def Keyword: Defining a simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!


# 2. Use of Pass Statement in Function
def placeholder_function():
    pass  # This function does nothing for now


# 3. Return Statement: Returning values from a function
def add(a, b):
    return a + b

print(add(3, 5))  # Output: 8


# 4. Global and Local Variables
x = 10  # Global variable

def modify_variable():
    global x  # Using global keyword
    x = 20  # Modifying global variable
    y = 5  # Local variable
    return y

print(modify_variable())  # Output: 5
print(x)  # Output: 20


# 5. Recursion in Python: Factorial Example
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# 6. *args and **kwargs in Function
def display_info(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

display_info(1, 2, 3, name="Alice", age=25)
# Output: Args: (1, 2, 3)
#         Kwargs: {'name': 'Alice', 'age': 25}


# 7. ‘Self’ as Default Argument in a Class
class Person:
    def __init__(self, name):
        self.name = name  # 'self' refers to the instance

    def introduce(self):
        return f"My name is {self.name}"

p = Person("Bob")
print(p.introduce())  # Output: My name is Bob


# 8. First-Class Functions: Passing function as an argument
def square(n):
    return n * n

def apply_func(func, value):
    return func(value)

print(apply_func(square, 4))  # Output: 16


# 9. Lambda Function: Anonymous function
double = lambda x: x * 2
print(double(5))  # Output: 10


# 10. Map, Reduce and Filter Functions
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map: Apply a function to each element
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Filter: Filter values based on a condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Reduce: Reduce values to a single result
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)  # Output: 15


# 11. Inner Function: Function inside a function
def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()

print(outer_function("hello"))  # Output: HELLO


# 12. Decorators: Modifying function behavior
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
