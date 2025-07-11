# MAP 
 
# -> it is used to apply a function to every item in an iterable (like a list) and return a new iterable with the results.
# It is often used for transforming data in a list.
nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#normal iteration
squared_nums = []
for num in nums:
    squared_nums.append(num ** 2)
print("Squared numbers using normal iteration:", squared_nums)

#using map function
squared_nums_map =list(map(lambda x: x ** 2, nums))
print("Squared numbers using map function:", squared_nums_map)

print("\n____________________________________________________________")

# FILTER -> it is like a conditional filter

#normal iteration
even_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
print("Even numbers using normal iteration:", even_nums)

#using filter function
even_nums_filter = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers using filter function:", even_nums_filter)

print("\n___________________________________________________________")

# if else in one line
result=list(map(lambda x: 0 if x % 2 == 0 else x**2, range(1, 11)))
print("Result using map with if-else:", result)
print("____________________________________________________________")

# REDUCE -> it is used to reduce a list to a single value, often used for aggregation like sum, product, etc.
from functools import reduce
#normal iteration
sum_of_nums = 0
for num in nums:
    sum_of_nums += num
print("Sum of numbers using normal iteration:", sum_of_nums)
#using reduce function
sum_of_nums_reduce = reduce(lambda x, y: x + y, nums)
print("Sum of numbers using reduce function:", sum_of_nums_reduce)

print("\n____________________________________________________________")  
# finding max and min using reduce

max_num = reduce(lambda x, y: max(x,y), nums)
min_num = reduce(lambda x, y: min(x,y), nums)
print("Maximum number using reduce function:", max_num)
print("Minimum number using reduce function:", min_num)  

print("\n____________________________________________________________")
# checking a list sorted or not using reduce
lists=[1, 2, 30, 4, 5]
is_sorted = reduce(lambda x,y: (x<y,y) if type(x) is not tuple else (x[0] and x[1]<y,y), lists)[0]
print("Is the list sorted using reduce function:", is_sorted)
