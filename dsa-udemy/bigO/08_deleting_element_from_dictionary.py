my_dict = {
    'name': 'Rose',
    'age': 28,
    'address': 'London'
}

# 1. using del keyword
del my_dict['age']
print(my_dict)

# 2. using pop() method
removed_element = my_dict.pop('address', None) # If none is added then it won't return any error if the key is not found, returns ONLY VALUE, NOT KEY
print(removed_element)
print(my_dict)

# 3. using popitem() method
removed_element2 = my_dict.popitem() # deletes the last key, RETURNS BOTH KEY AND VALUE
print(removed_element2)
print(my_dict)

# 4. clear() method, deletes everything, Time complexity O(N) as deletes all the elements, Space complexity is O(1) as additional space is not needed for the operation
my_dict = {
    'name': 'Rose',
    'age': 28,
    'address': 'London'
}
my_dict.clear()
print(my_dict)