# DECORATOR
# A decorator is a function that takes another function as an argument, extends its behavior, and returns a new function.
# it is used when we need to execute something after and before a function call without modifying the original function's code.

from datetime import datetime
def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before the function call {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After the function call {func.__name__}")
        return result
    return wrapper

@decorator
def say_hello(name):
    print(f"Hello, {name}!")

@decorator
def print_current_time():
    print(datetime.now())

@decorator
def add_numbers(a, b):
    print(f"The sum of {a} and {b} is {a + b}")
# Example usage
say_hello("Aryan")

print_current_time()

add_numbers(5, 10)

print("\n____________________________________________________________")
# function with parameter and return value
@decorator
def multiply_numbers(a, b):
    return a * b
# Example usage
print(multiply_numbers(3, 4))
