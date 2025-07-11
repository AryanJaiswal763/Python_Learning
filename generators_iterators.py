#GENERATOR
# A generator is a special type of iterator that allows you to iterate over a sequence of values without storing them all in memory at once.
# It is defined using a function with the yield statement.

num=range(2, 1076887)
print(type(num),num)
for i in num:
    pass
print(num.__sizeof__())
print(" ")
# size of integer in bytes
n=100
print(n.__sizeof__())



# yeild function is used to create a generator function
# used to return values one by one
# Generally what happens, if return is used, then the function will return the value and exit the function
# but if yeild is used, then the function will return the value and pause the function
# now using next() function we can get the next value from the generator function
def my_generator(n):
    for i in range(n):
        # return i   -> this will not work as expected, it will return only the first value and exit the function
        yield i
fun=my_generator(3)
print(type(fun), fun)
print(next(fun))  # prints 0
print(next(fun))  # prints 1
print(next(fun))  # prints 2
# print(next(fun))  # raises StopIteration error because there are no more values to return


print("________________________________________________")
def infinite_generator():
    i = 0
    while True:
        yield i  # yeild is allowed only inside function
        i += 1
fun=infinite_generator()
print(next(fun))
print(next(fun))
print(next(fun))
print(next(fun))
for _ in range(10):
    print(next(fun),end=" ")

print("\n________________________________________________")
for i in range(1,11,2):
    print(i,end=" ")

# for i in range(0,2,0.1):             ->this will not work as range does not support float values
#     print(next(fun),end=" ")

print("\n________________________________________________")
#using yield 
def my_range(start, end, step=1):
    while start < end:
        yield start
        start += step
for i in my_range(0, 2, 0.1):
    print(i, end=" ")


print("\n____________________________________________________________________")
# ITERATOR:

# An iterator is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__().
# An iterator allows you to traverse through a collection (like a list or a tuple) without exposing the underlying structure.
from random import random
class MyIterator:
    def __init__(self, low,high,count):
        self.low=low
        self.high = high
        self.count=count
        self.current = 0


    def __iter__(self): # returns an object supporting the __next__() functionality
        return self

    def __next__(self):  #working of __next__()
        if self.current < self.count:
            self.current += 1
            
            return random()*(self.high - self.low) + self.low
        else:
            raise StopIteration
# Example usage of MyIterator
my_iter = MyIterator(50, 70, 10)
for value in my_iter:
    print(value, end=" ")



