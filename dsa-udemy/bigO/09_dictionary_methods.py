my_dict = {
    'name': 'Rose',
    'age': 28,
    'address': 'London',
    'education': 'master'
}

my_dict_copy = my_dict.copy()
print(my_dict_copy)


# fromkeys() method, default is None if values not provided
new_dict = {}.fromkeys([1,2,3],0)
new_dict2 = {}.fromkeys([1,2,3])
print(new_dict)
print(new_dict2)

# get() method
print(my_dict.get('name')) #key found then return value of the key
print(my_dict.get('name2')) #key not found and value not provided then return None
print(my_dict.get('name2','Tiger')) #key not found and valur provided then return value provided

# items() method (returns list of tuples)
print(my_dict.items())

# keys() method (returns list of all keys in dictionary)
print(my_dict.keys())

# values() method (returns list of all values in dictionary)
print(my_dict.values())

# popitem() method
print(my_dict.popitem())

# setdefault() method
print(my_dict.setdefault('name','added')) #sets default value if key present
print(my_dict.setdefault('name1','added')) #returns value if key not present, inserts the key value in the dictionary used
print(my_dict)

# pop() method, pops provided key, default value (if key not found, optional)
print(my_dict.pop('name1', 'val'))
print(my_dict.pop('name1', 'val'))

# update() method
new_dict3 = {'a': 1, 'b': 2, 'c': 3} # inserts the keys from the second dict if keys not present in the first dict
new_dict3 = {'name': 'Ava', 'b': 2, 'c': 3} # updates the value of key from the second dict if the key is present
my_dict.update(new_dict3)
print(my_dict )