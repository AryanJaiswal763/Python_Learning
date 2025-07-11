#use of *args
# it is used when we do not know how many arguments will be passed to the function
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6,7,8,9,10))

print("__________________________________________")

#named arguments and positinal arguments
def print_info(val1, val2, name,city):
    print(val1-val2)
    print(name)
    print(city)
print_info(10, 5, name="Aryan", city="Delhi") #unamed arguments/positinal arguments
print_info(val2=10, val1=5, city="Mumbai", name="Suresh") #named arguments/keyword arguments

# Note: positional arguments must come before keyword arguments
print_info(10, 5, name="Aryan", city="Nagpur")  # This will run

# print_info(name="Aryan", city="Delhi", 10, 5)  # This will raise an error because positional arguments must come before keyword arguments

print("__________________________________________")

# use of **kawrgs
# it is used when we do not know how many keyword arguments will be passed to the function
def add_kwargs(**kwargs):
    sum=0
    for key, value in kwargs.items():
        sum+=value
    return sum
print(add_kwargs(a=1, b=2, c=3))
print(add_kwargs(a=1, b=2, c=3, d=4, e=5))

print("__________________________________________")
def print_inf(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)

print_inf(1, 2, 3, "Aryan", "Delhi")  
print_inf(name="Aryan", city="Delhi", age=20, country="India")
print_inf(20, "India", name="Aryan", city="Delhi")