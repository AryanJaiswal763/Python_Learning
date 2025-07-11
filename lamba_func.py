# lambda function is a function that is defined without a name.
# It is used for creating small, one-time, anonymous functions, without the need to formally define a function using the `def` keyword.

def get_sum(a,b):
    return a+b
print(get_sum(2,3))

# Using lambda function to achieve the same result
sum_lambda = lambda a,b: a+b
print(sum_lambda(2,3))



# without naming the function
print((lambda a,b:a+b)(2,3))


# sorting with first value 
nums=[[10,100],[20,300],[15,400],[25,250],[6,200]]
nums.sort()
print(nums)


nums.sort(reverse=True)
print(nums)


#using lambda function to sort ascending based on second value
nums.sort(key=lambda x: x[1])
print(nums)



# using lambda function to sort in decending based on second  value
nums.sort(reverse=True, key=lambda x: x[1])
print(nums)


