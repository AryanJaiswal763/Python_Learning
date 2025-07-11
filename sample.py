def get_sum(a,b):
    return a+b
def get_product(a,b):
    return a*b
def print_name():
    print("__name__ in sample.py is", __name__  )

print(get_product(2, 3))

if __name__ == "__main__":
    print_name()
    print("Sum of 2 and 3 is", get_sum(2, 3))
    print("Product of 2 and 3 is", get_product(2, 3))