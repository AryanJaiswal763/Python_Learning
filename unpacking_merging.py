#unpacking
# List and tuple are unpacked in same sequence
# set and dictionary are unpacked in arbitrary sequence


info=[25, 10000, "Aryan", "Delhi"] #unpacked sequence same
info={25,10000, "Aryan", "Delhi"} #unpacked sequence would not necessorily be the same
age, salary, name, city = info 
print("Age:", age)
print("Salary:", salary)
print("Name:", name)
print("City:", city)

info2 = {"age": 25, "salary": 10000, "name": "Aryan", "city": "Delhi"} #packed dictionary
age, salary, name, city = info2  #unpacking dictionary values  , by deafult it will unpack in the order of keys not values
print(age)
print(salary)
print(name)
print(city)

print("__________________________________________")

num1=[1, 2, 3]
num2=[4, 5, 6]
#method 1
# nums=num1+num2 #merging two lists

#method 2
# nums=num1.copy()
# nums.extend(num2) #merging two lists using extend method
# print(num1,num2,nums)

#method 3
nums=[*num1, *num2] #merging two lists using unpacking
print(num1, num2, nums)

#using tuple
nums1=(1, 2, 3)
nums2=(4, 5, 6)
nums=(*nums1, *nums2) #merging two tuples using unpacking
print(nums1, nums2, nums)


# for dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict={**dict1, **dict2}  # merging two dictionaries using unpacking
print(dict1, dict2,dict)  # merging two dictionaries using unpacking

# for tuple and list single star is used while for dictionary double star is used